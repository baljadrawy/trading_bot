from pymongo import MongoClient

class TradingBotDatabase:
    def __init__(self, db_name='trading_bot', collection_name='trades'):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_trade(self, trade):
        self.collection.insert_one(trade)

    def get_all_trades(self):
        return list(self.collection.find())

    def close(self):
        self.client.close()
