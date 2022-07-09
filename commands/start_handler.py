from lib.db import Db
from lib.MessageEvent import MessageEvent
from entities.user import UserEntity


async def handler(event: MessageEvent):
    if Db().user_exists(event.message.chat.id):
        await event.message.answer("You're already with us :)")
        return
    
    new_user = UserEntity({
        'id': event.message.chat.id,
        'username': event.message.chat.username,
        'lang': event.message['from']['language_code'],
        'wallet': None
    })

    Db().add_user(new_user)

    await event.message.answer(f'Hey {event.message.chat.first_name} {event.message.chat.last_name}!')