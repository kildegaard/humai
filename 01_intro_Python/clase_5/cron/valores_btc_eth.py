"""
    La idea es armar un programa que consuma la API de Binance para obtener
    los valores de BTC y ETH, me guarde esa info en datasets y 
"""

import os
import requests
import pandas as pd
from datetime import datetime


def get_token_price(ticker: str) -> pd.DataFrame:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={ticker.upper()}USDT"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame([data])


import os
from datetime import datetime
import pandas as pd


def main():
    """
    Fetches token prices for Bitcoin and Ethereum, saves the data to a CSV file, and prints the export location.
    """
    # Fetch token prices
    btc = get_token_price("btc")
    eth = get_token_price("eth")

    # Combine token prices
    price = pd.concat([btc, eth])

    # Add timestamp to the data
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    price["timestamp"] = timestamp

    # Create directory if it doesn't exist
    path = "crypto_prices"
    os.makedirs(path, exist_ok=True)

    # Save data to a CSV file
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{path}/prices_{time}.csv"
    price.to_csv(filename)

    # Print export location
    print(f"Data exported to {filename}")


if __name__ == "__main__":
    main()
