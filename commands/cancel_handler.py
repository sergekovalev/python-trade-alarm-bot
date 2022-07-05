from lib.db import Db
from lib.MessageEvent import MessageEvent


async def handler(event: MessageEvent):
    Db().clear_user_context(user_id=event.message.chat.id)

    await event.message.answer('Request cancelled')