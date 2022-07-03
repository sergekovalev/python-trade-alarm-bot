from aiogram import types
from db import Db
from response_formatters.me import me_formatter


async def handler(message: types.Message):
    me = Db().get_user(message.chat.id)
    me['name'] = f'{message.chat.first_name} {message.chat.last_name}'

    await message.answer(me_formatter(me))
