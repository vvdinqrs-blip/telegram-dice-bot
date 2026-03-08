# Telegram Dice Bot powered by Pyth Network Entropy

This is a minimal Telegram bot that lets users roll a 6‑sided dice using entropy from the Pyth network.

## Prerequisites
- Python 3.10+ (recommended)
- `pip install -r requirements.txt`
- A **Telegram Bot Token** (obtainable via [@BotFather](https://t.me/BotFather)).
- The token should be stored as an environment variable named `TELEGRAM_BOT_TOKEN`.

## Running the bot locally
```bash
export TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
python bot.py
```

Once the bot is running, send `/roll` in any chat with the bot and you’ll get a dice result powered by Pyth entropy.

## Deployment
Feel free to deploy this on any platform that supports Python (Heroku, Fly.io, Railway, etc.). Just ensure the `TELEGRAM_BOT_TOKEN` environment variable is set.