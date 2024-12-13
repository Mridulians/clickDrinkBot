from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Your Render app URL
WEBHOOK_URL = f"https://clickdrinkbot.onrender.com/webhook"

# Function to handle /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_username = update.message.from_user.username

    keyboard = [
        [
            InlineKeyboardButton("Open App", web_app={"url": f"https://click-drink-front.netlify.app//?username={user_username}"})
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"Hello {user_username}, click below to open the app:", reply_markup=reply_markup)

# Main function
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handler
    app.add_handler(CommandHandler("start", start))

    # Use webhooks instead of polling
    app.run_webhook(
        listen="0.0.0.0",  # Listen on all network interfaces
        port=int(os.environ.get("PORT", 8443)),  # Use Render's dynamic port
        url_path="/webhook",  # Path for Telegram updates
        webhook_url=WEBHOOK_URL  # Telegram's webhook URL
    )

    print("Bot is running via webhooks...")

if __name__ == "__main__":
    main()
