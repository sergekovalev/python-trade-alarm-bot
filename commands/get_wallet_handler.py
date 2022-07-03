from aiogram import types
from db import Db
from response_formatters.wallet import wallet_formatter


async def handler(message: types.Message):
    wallet = Db().get_wallet(user_id=message.chat.id)

    await message.answer(wallet_formatter(wallet))