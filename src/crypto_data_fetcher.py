import datetime
import requests
from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def get_historical_data(self, symbol, interval='1d', start_str='1 Jan 2021', end_str=None):
        candles = self.client.get_historical_klines(symbol, interval, start_str, end_str)
        return candles


class CoinMarketCapClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/"

    def get_historical_data(self, symbol, start_date, end_date=None):
        if end_date is None:
            end_date = datetime.datetime.now()

        start_date_str = int(start_date.timestamp())
        end_date_str = int(end_date.timestamp())

        url = f"{self.base_url}quotes/historical"
        parameters = {
            'symbol': symbol,
            'time_start': start_date_str,
            'time_end': end_date_str,
            'interval': 'daily'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key,
        }

        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()

        return data


class TradingBot:
    def __init__(self, binance_client=None, cmc_client=None):
        self.binance_client = binance_client
        self.cmc_client = cmc_client

    def get_data(self, symbol, source='binance'):
        if source == 'binance':
            return self.binance_client.get_historical_data(symbol, interval='1d', start_str='1 Jan 2023')
        elif source == 'cmc':
            start_date = datetime.datetime(2023, 1, 1)
            return self.cmc_client.get_historical_data(symbol, start_date)
        else:
            raise ValueError("Unsupported data source")
