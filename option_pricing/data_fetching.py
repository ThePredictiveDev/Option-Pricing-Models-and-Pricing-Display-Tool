import yfinance as yf
import pandas as pd
import time

class DataFetcher:
    def __init__(self, ticker: str, interval: str = '1m'):
        self.ticker = ticker
        self.interval = interval

    def fetch_live_data(self):
        data = yf.download(tickers=self.ticker, period='1d', interval=self.interval)
        return data

    def start_live_feed(self, update_interval=60):
        while True:
            data = self.fetch_live_data()
            yield data
            time.sleep(update_interval)
