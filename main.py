import logging
from dotenv import dotenv_values
from commands.main import parse_command
from multiprocessing import Process
from workers.main import workers_process
from aiogram import Bot, Dispatcher, executor, types

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
    wp = Process(target=workers_process)
    wp.start()
    
    print('Bot is started')
    executor.start_polling(dp, skip_updates=True)

