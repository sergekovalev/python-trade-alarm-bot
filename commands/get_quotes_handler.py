from lib.db import Db
from lib.MessageEvent import MessageEvent


async def handler(event: MessageEvent):
    quotes = Db().get_quotes()

    quotes_list = [f'{q["symbol"]}: ${q["quote"]["USD"]["price"]}:' for q in quotes]

    quotes_list = '\n'.join(quotes_list)

    await event.message.answer(quotes_list)
