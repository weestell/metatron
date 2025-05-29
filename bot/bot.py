import os
import sys
import logging

# Add utils directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'utils'))

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters

from config.config import BOT_TOKEN
from handlers.welcome import handle_private_start, handle_button_callback

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Start the bot."""
    try:
        # Create the Updater
        updater = Updater(BOT_TOKEN, use_context=True)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        # Add handlers for private chat only
        private_filter = Filters.private & Filters.command
        dp.add_handler(CommandHandler("start", handle_private_start, filters=private_filter))
        
        # Add callback query handler for buttons
        dp.add_handler(CallbackQueryHandler(handle_button_callback))

        # Start the Bot
        updater.start_polling()
        logger.info("Bot started successfully!")

        # Run the bot until you press Ctrl-C
        updater.idle()
    except Exception as e:
        logger.error(f"Error starting bot: {e}")

if __name__ == '__main__':
    main() 