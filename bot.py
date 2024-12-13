from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# Function to handle /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Fetch the user's Telegram username
    user_username = update.message.from_user.username
    
    # Create a keyboard with the web app link
    keyboard = [
        [
            InlineKeyboardButton("Open App", web_app={"url": f"https://click-drink-front.netlify.app//?username={user_username}"})
        ]
    ]
    
    # Create the reply markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send a message with the username and the button
    await update.message.reply_text(f"Hello {user_username}, click below to open the app:", reply_markup=reply_markup)

# Set up the bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
