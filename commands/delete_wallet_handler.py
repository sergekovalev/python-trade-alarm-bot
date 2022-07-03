from aiogram import types
from db import Db
from response_formatters.wallet import wallet_formatter


async def handler(message: types.Message):
    await message.answer('delete wallet')