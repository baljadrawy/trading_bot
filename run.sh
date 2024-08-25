#!/bin/bash

# Start MongoDB
sudo systemctl start mongodb

# Activate virtual environment
source ~/trading_bot/venv/bin/activate

# Run the bot
python3 ~/trading_bot/src/trading_bot.py
