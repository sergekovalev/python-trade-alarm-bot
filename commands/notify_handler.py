from lib.MessageEvent import MessageEvent
import re
from lib.db import Db
from lib.math_operators import get_human_readable_operator


async def handler(event: MessageEvent):
    m = re.search('/?notify if (.+)$', event.message.text)
    
    condition = m.group(1).lower()
    
    symbols = [q["symbol"].lower() for q in Db().get_quotes()]
    
    if not re.match(rf'({"|".join(symbols)})\s*(>|<|>=|<=|==?)\s*(\d+(\.\d+)?)', condition):
        await event.message.answer(f'Cannot recognize a condition "{condition}". Please, fix it and try again.')
        return
    
    exp = [x for x in re.split(r'(\w+)\s*(>|<|>=|<=|==?)\s*(\d+.*)', condition) if x != '']
    
    symbol, operator, price = exp
    human_readable_operator = get_human_readable_operator(operator)
    
    await event.message.answer(f'Ok, now you\'re following {symbol} if it {human_readable_operator} {price} USD')

    notification = {
        'symbol': symbol,
        'operator': operator,
        'price': price,
        'human_readable_operator': human_readable_operator
    }
    
    Db().add_notification_to_user(user_id=event.user_id, notification=notification)
