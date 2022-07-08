from lib.db import Db
from response_formatters.me import me_formatter
from lib.MessageEvent import MessageEvent
from entities.user import UserEntity


async def handler(event: MessageEvent):
    user: UserEntity = Db().get_user(event.message.chat.id)
    user.name = f'{event.message.chat.first_name} {event.message.chat.last_name}'

    await event.message.answer(me_formatter(user))
