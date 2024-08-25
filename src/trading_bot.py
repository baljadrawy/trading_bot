from src.crypto_data_fetcher import BinanceClient, CoinMarketCapClient, TradingBot
from src.trading_bot_database import TradingBotDatabase

if __name__ == "__main__":
    binance_api_key = "YOUR_BINANCE_API_KEY"
    binance_api_secret = "YOUR_BINANCE_API_SECRET"
    binance_client = BinanceClient(binance_api_key, binance_api_secret)

    cmc_api_key = "5851a35d-6b17-4d11-802d-f2a4d325fbbe"
    cmc_client = CoinMarketCapClient(cmc_api_key)

    db = TradingBotDatabase()

    bot = TradingBot(binance_client=binance_client, cmc_client=cmc_client)

    data_binance = bot.get_data("BTCUSDT", source='binance')
    print(f"Binance Data: {data_binance}")

    data_cmc = bot.get_data("BTC", source='cmc')
    print(f"CoinMarketCap Data: {data_cmc}")
