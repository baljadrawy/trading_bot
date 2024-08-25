import pytest
from src.trading_bot_database import TradingBotDatabase

@pytest.fixture
def db():
    db = TradingBotDatabase(db_name="test_trading_bot")
    yield db
    db.collection.drop()
    db.close()

def test_insert_trade(db):
    trade = {"date": "2024-08-25", "symbol": "BTC", "action": "BUY", "price": 25000.0, "quantity": 0.1}
    db.insert_trade(trade)
    trades = db.get_all_trades()
    assert len(trades) == 1
    assert trades[0]["symbol"] == "BTC"
