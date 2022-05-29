import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from dotenv import dotenv_values
from commands.main import Commands

config = dotenv_values(".env")


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    app = ApplicationBuilder().token(config['TELEGRAM_TOKEN']).build()

    for k, v in Commands.items():
        cmd = CommandHandler(k, v)
        app.add_handler(cmd)

    app.run_polling()
