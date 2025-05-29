import logging
import os
from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from config.config import WELCOME_MESSAGE, WELCOME_VIDEO_PATH, WELCOME_IMAGE_PATH

logger = logging.getLogger(__name__)

def handle_private_start(update, context):
    """Handle /start command in private chats."""
    try:
        # First send the welcome message with photo
        try:
            with open(WELCOME_IMAGE_PATH, 'rb') as photo:
                update.message.reply_photo(
                    photo=photo,
                    caption="💫Мы ждали тебя…\n\n✨Добро пожаловать домой!\n\n🌌Нажми на ключ-слово, открой портал:",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(
                            "🔑KEY: NOVA",
                            callback_data="show_main_menu"
                        )]
                    ]),
                    parse_mode=ParseMode.HTML
                )
                logger.info(f"Sent initial welcome message to user {update.message.from_user.first_name}")
        except Exception as photo_error:
            logger.error(f"Could not send photo: {photo_error}")
            # Fallback to text-only initial message
            update.message.reply_text(
                "💫Мы ждали тебя…\n\n✨Добро пожаловать домой!\n\n🌌Нажми на ключ-слово, открой портал:",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(
                        "🔑KEY: NOVA",
                        callback_data="show_main_menu"
                    )]
                ])
            )
    except Exception as e:
        logger.error(f"Error in private start command: {e}")

def handle_button_callback(update, context):
    """Handle button callbacks in private chat."""
    try:
        query = update.callback_query
        if query.data == "show_main_menu":
            # Create keyboard with group link button and donation button
            main_menu_buttons = InlineKeyboardMarkup([
                [InlineKeyboardButton(
                    "🔮Вход в MV2",
                    url="https://t.me/+nyGyj8sb3RVlNzUy"
                )],
                [InlineKeyboardButton(
                    "💫 Поддержать проект",
                    url="http://donat24.ru/pay/10"
                )]
            ])
            
            try:
                with open(WELCOME_VIDEO_PATH, 'rb') as video:
                    # Delete the previous message
                    query.message.delete()
                    # Send the main welcome message with video
                    context.bot.send_video(
                        chat_id=query.message.chat_id,
                        video=video,
                        caption=WELCOME_MESSAGE,
                        parse_mode=ParseMode.HTML,
                        reply_markup=main_menu_buttons,
                        supports_streaming=True,
                        width=1280,
                        height=720
                    )
                    logger.info(f"Sent main welcome video to user {query.from_user.first_name}")
            except Exception as video_error:
                logger.error(f"Could not send video: {video_error}")
                # Fallback to text-only message
                query.message.edit_text(
                    WELCOME_MESSAGE,
                    parse_mode=ParseMode.HTML,
                    reply_markup=main_menu_buttons
                )
            
            # Answer the callback query to remove the loading state
            query.answer()
    except Exception as e:
        logger.error(f"Error in button callback: {e}")

def get_user_mention(user):
    """Create HTML-formatted user mention."""
    if user.username:
        return f'@{user.username}'
    else:
        return f'<a href="tg://user?id={user.id}">{user.first_name}</a>' 