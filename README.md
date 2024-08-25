# Trading Bot

A Python-based cryptocurrency trading bot that fetches historical data from Binance and CoinMarketCap, analyzes the market, and executes trades.

## Requirements

- Python 3.8+
- MongoDB
- Libraries listed in `requirements.txt`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/trading-bot.git
    cd trading-bot
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Start MongoDB (if not already running):
    ```bash
    sudo systemctl start mongodb
    ```

5. Run the bot:
    ```bash
    python3 src/trading_bot.py
    ```

## Usage

1. Edit `trading_bot.py` to include your Binance and CoinMarketCap API keys.
2. Run the script:
    ```bash
    python3 src/trading_bot.py
    ```
3. To use the graphical interface:
    ```bash
    python3 src/user_interface.py
    ```

## API Setup

- **Binance**: Create an API key from the [Binance account](https://www.binance.com/en/my/settings/api-management).
- **CoinMarketCap**: Create an API key from [CoinMarketCap Developer Portal](https://pro.coinmarketcap.com/signup/).

Once you have the keys, add them to `trading_bot.py` and `user_interface.py`:
```python
binance_api_key = "YOUR_BINANCE_API_KEY"
binance_api_secret = "YOUR_BINANCE_API_SECRET"
cmc_api_key = "YOUR_COINMARKETCAP_API_KEY"
