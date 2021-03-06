import re
from lib.MessageEvent import MessageEvent
from lib.db import Db
from response_formatters.follow import select_currency_formatter, final_formatter


async def initial(event: MessageEvent):
    m = re.search('/?follow (.+)$', event.message.text)

    event.message.text = m.group(1)
    
    await final(event)


async def select_currency(event: MessageEvent):
    await event.message.answer(select_currency_formatter())


async def final(event: MessageEvent):
    Db().follow_ticker(user_id=event.user_id, ticker=event.message.text)
    
    await event.message.answer(final_formatter(event.message.text))
    
    event.context.clear_context()


contexts = {
    'initial': initial,
    'select_currency': select_currency
}


async def handler(event: MessageEvent):
    if event.contains_context():
        return await globals()[event.context.step['name']](event)

    if re.match(r'/?follow .+$', event.message.text):
        context = contexts['initial']
    else:
        event.context.set_context({
            'root': {
                'name': 'follow_currency_handler',
                'payload': {}
            },
            'step': {
                'name': 'final',
                'payload': {}
            }
        })

        context = contexts['select_currency']

    await context(event)
