from lib.db import Db
from lib.MessageEvent import MessageEvent


async def handler(event: MessageEvent):
    db = Db()

    if db.user_exists(event.message.chat.id):
        await event.message.answer("You're already with us :)")
        return

    db.add_user({
        'id': event.message.chat.id,
        'username': event.message.chat.username,
        'lang':event. message['from']['language_code'],
        'wallet': None
    })

    await event.message.answer(f'Hey {event.message.chat.first_name} {event.message.chat.last_name}!')