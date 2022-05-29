from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler


async def handler(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="start"
    )