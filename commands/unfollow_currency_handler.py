import re
from lib.MessageEvent import MessageEvent
from lib.db import Db


async def initial(event: MessageEvent):
    m = re.search('/?follow (.+)$', event.message.text)
    
    event.message.text = m.group(1)
    
    await final(event)


async def select_currency(event: MessageEvent):
    await event.message.answer('What currency would you like to unfollow?')


async def final(event: MessageEvent):
    tickers = Db().unfollow_ticker(user_id=event.user_id, ticker=event.message.text)
    
    await event.message.answer(f'Now you\'re following {"only " if len(tickers) == 1 else ""}{",    ".join(tickers) if len(tickers) > 0 else "nothing"}')
    
    event.context.clear_context()


contexts = {
    'initial': initial,
    'select_currency': select_currency
}


async def handler(event: MessageEvent):
    if event.contains_context():
        return await globals()[event.context.step['name']](event)
    
    if re.match(r'/?unfollow (.+)$', event.message.text):
        context = contexts['initial']
    else:
        event.context.set_context({
            'root': {
                'name': 'unfollow_currency_handler',
                'payload': {}
            },
            'step': {
                'name': 'final',
                'payload': {}
            }
        })
        
        context = contexts['select_currency']
    
    await context(event)
