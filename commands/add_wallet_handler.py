from lib.MessageEvent import MessageEvent
import re
from lib.db import Db


async def handler(event: MessageEvent):
    m = re.search('/?wallet add (.+)$', event.message.text)
    
    condition = m.group(1)

    symbols = [q["symbol"].lower() for q in Db().get_quotes()]

    if not re.match(rf'({"|".join(symbols)}) (.+)', condition):
        await event.message.answer(f'Cannot recognize a condition "{condition}". Please, fix it and try again.')
        return

    exp = [x for x in re.split(r'(\w+) (\w+)', condition) if x != '']
    
    symbol, address = exp
    
    event.user.add_to_wallet(symbol, address)

    await event.message.answer(f'Successfully added your {symbol.upper()} address')