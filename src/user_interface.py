import tkinter as tk
from src.trading_bot_database import TradingBotDatabase
from src.crypto_data_fetcher import BinanceClient, CoinMarketCapClient, TradingBot

class TradingBotApp:
    def __init__(self, root, binance_client, cmc_client):
        self.db = TradingBotDatabase()
        self.bot = TradingBot(binance_client=binance_client, cmc_client=cmc_client)

        self.root = root
        self.root.title("Trading Bot")

        tk.Label(root, text="Symbol:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=10)

        self.symbol_entry = tk.Entry(root)
        self.quantity_entry = tk.Entry(root)

        self.symbol_entry.grid(row=0, column=1, padx=10, pady=10)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)

        self.source_var = tk.StringVar(value='binance')
        tk.Label(root, text="Source:").grid(row=2, column=0, padx=10, pady=10)
        tk.OptionMenu(root, self.source_var, "binance", "cmc").grid(row=2, column=1, padx=10, pady=10)

        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.grid(row=3, columnspan=2, padx=10, pady=10)

        tk.Button(root, text='Execute Trade', command=self.execute_trade).grid(row=4, columnspan=2, padx=10, pady=10)
        tk.Button(root, text='Show Trade History', command=self.show_trade_history).grid(row=5, columnspan=2, padx=10, pady=10)

        self.history_text = tk.Text(root, height=10, width=50)
        self.history_text.grid(row=6, columnspan=2, padx=10, pady=10)
        self.history_text.config(state=tk.DISABLED)

    def execute_trade(self):
        symbol = self.symbol_entry.get()
        quantity = float(self.quantity_entry.get())
        source = self.source_var.get()
        data = self.bot.get_data(symbol, source)
        decision = self.bot.analyze_market(data)
        self.bot.execute_trade(symbol, decision, quantity)
        self.result_label.config(text=f"Executed {decision} on {symbol} with quantity {quantity}")

    def show_trade_history(self):
        trades = self.db.get_all_trades()
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        if trades:
            for trade in trades:
                self.history_text.insert(tk.END, f"{trade['date']}: {trade['action']} {trade['quantity']} of {trade['symbol']} at ${trade['price']}\n")
        else:
            self.history_text.insert(tk.END, "No trades executed yet.")
        self.history_text.config(state=tk.DISABLED)

    def close(self):
        self.db.close()

if __name__ == "__main__":
    binance_api_key = "YOUR_BINANCE_API_KEY"
    binance_api_secret = "YOUR_BINANCE_API_SECRET"
    binance_client = BinanceClient(binance_api_key, binance_api_secret)

    cmc_api_key = "YOUR_COINMARKETCAP_API_KEY"
    cmc_client = CoinMarketCapClient(cmc_api_key)

    root = tk.Tk()
    app = TradingBotApp(root, binance_client, cmc_client)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()
