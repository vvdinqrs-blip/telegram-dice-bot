import os
import logging
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import requests

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def get_pyth_entropy() -> int:
    try:
        resp = requests.get("https://api.pyth.network/v1/price-feeds")
        resp.raise_for_status()
        data = resp.json()
        raw_hash = data["price_feeds"][0]["hash"]
        return int(raw_hash, 16)
    except Exception as e:
        logging.error(f"Failed to fetch Pyth entropy: {e}")
        raise


def roll_dice(entropy: int) -> int:
    return (entropy % 6) + 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🎲 Welcome to the Pyth Dice Bot!\n"
        "Type /roll to spin a dice powered by Pyth entropy."
    )

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        entropy = get_pyth_entropy()
        result = roll_dice(entropy)
        await update.message.reply_text(f"Your die shows: **{result}** 🎲")
    except Exception as e:
        await update.message.reply_text("⚠️ Something went wrong. Try again later.")
        logging.exception(e)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "/start - Start the bot\n"
        "/roll  - Roll a Pyth‑powered dice\n"
        "/help  - Show this message"
    )

def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("roll", roll))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if __name__ == "__main__":
    main()
