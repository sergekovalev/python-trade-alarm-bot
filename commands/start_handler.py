from aiogram import types
from db import Db


async def handler(message: types.Message):
    db = Db()

    if db.user_exists(message.chat.id):
        await message.answer("You're already with us :)")
        return

    db.add_user({
        'id': message.chat.id,
        'username': message.chat.username,
        'lang': message['from']['language_code'],
        'wallet': None
    })

    await message.answer(f'Hey {message.chat.first_name} {message.chat.last_name}!')