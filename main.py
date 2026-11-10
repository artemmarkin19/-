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
