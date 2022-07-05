from lib.db import Db
from response_formatters.wallet import wallet_formatter
from lib.MessageEvent import MessageEvent


async def handler(event: MessageEvent):
    wallet = Db().get_wallet(user_id=event.message.chat.id)

    await event.message.answer(wallet_formatter(wallet))