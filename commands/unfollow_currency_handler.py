from aiogram import types
from db import Db
from response_formatters.me import me_formatter


async def handler(message: types.Message):
    await message.answer('unfollow_currency_handler')
