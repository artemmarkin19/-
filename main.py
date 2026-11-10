import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime

URL = "https://api.binance.com/api/v3/ticker/price"

# Монеты, которые будут показываться (символ на бирже, понятное имя)
COINS = [
    ("BTCUSDT", "Bitcoin"),
    ("ETHUSDT", "Ethereum"),
    ("BNBUSDT", "BNB"),
    ("SOLUSDT", "Solana"),
    ("XRPUSDT", "XRP"),
    ("ADAUSDT", "Cardano"),
    ("DOGEUSDT", "Dogecoin"),
    ("LTCUSDT", "Litecoin"),
    ("DOTUSDT", "Polkadot"),
    ("LINKUSDT", "Chainlink"),
    ("BCHUSDT", "Bitcoin Cash"),
    ("ETCUSDT", "Ethereum Classic"),
    ("XLMUSDT", "Stellar"),
    ("TRXUSDT", "TRON"),
    ("ATOMUSDT", "Cosmos"),
    ("NEOUSDT", "NEO"),
    ("VETUSDT", "VeChain"),
    ("FILUSDT", "Filecoin"),
    ("ICPUSDT", "Internet Computer"),
    ("HBARUSDT", "Hedera")
]

# Здесь будем хранить цены с прошлого обновления, чтобы сравнивать
previous_prices = {}


def load_data():
    # 1. Запрос к API
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        status_label.config(text="Ошибка сети. Проверьте интернет.")
        return

    # 2. Превращаем ответ в JSON или если пришел "сломанный" — выдаем ошибку
    try:
        data = response.json()
    except ValueError:
        status_label.config(text="Ошибка: сервер прислал не JSON.")
        return

    # 3. Из списка делаем словарь
    prices = {}
    for item in data:
        prices[item["symbol"]] = float(item["price"])

    # 4. Очищаем таблицу перед заполнением
    for row in tree.get_children():
        tree.delete(row)


    # 5. Проходим по нашим монетам
    for symbol, name in COINS:
        if symbol not in prices:
            continue

        price = prices[symbol]

        # Решаем цвет строки: сравнили с прошлой ценой.
        if symbol in previous_prices:
            if price > previous_prices[symbol]:
                tag = "green"
            elif price < previous_prices[symbol]:
                tag = "red"
            else:
                tag = "black"
        else:
            tag = "black"  # первый запуск — сравнивать не с чем

        # форматируем цену
        if price < 1:
            price_text = f"${price:.6f}"
        else:
            price_text = f"${price:,.2f}"

        tree.insert("", tk.END, values=(name, symbol, price_text), tags=(tag,))

    # 6. Запоминаем цены для следующего обновления
    previous_prices.clear()
    for symbol, _ in COINS:
        if symbol in prices:
            previous_prices[symbol] = prices[symbol]

    # Обновляем надпись со временем
    now = datetime.now().strftime("%H:%M:%S")
    status_label.config(text=f"Обновлено в {now}")

