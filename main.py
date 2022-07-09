import logging
from dotenv import dotenv_values
from commands.main import parse_command
from workers.main import workers_process
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from entities.entity import Entity
from lib.db import Db

config = dotenv_values(".env")


logging.basicConfig(
    filename='.log',
    encoding='utf-8',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


bot = Bot(token=config['TELEGRAM_TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler()
async def start(message: types.Message):
    try:
        await parse_command(message)
    except Exception as err:
        print(err)

if __name__ == '__main__':
    Entity.set_db(Db())
    print('Bot is started')
    # asyncio.run(workers_process(bot))
    asyncio.ensure_future(workers_process(bot))
    executor.start_polling(dp, skip_updates=True)
