from aiogram import types
from db import Db


async def handler(message: types.Message):
    quotes = Db().get_quotes()

    quotes_list = [f'{q["symbol"]}: ${q["quote"]["USD"]["price"]}:' for q in quotes]

    quotes_list = '\n'.join(quotes_list)

    await message.answer(quotes_list)
