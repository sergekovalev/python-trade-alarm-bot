import logging
from lib.db import Db
from lib.math_operators import get_comparator
from lib.api import Api
from response_formatters.notification import new_notification_formatter


async def worker(bot):
    print('WORKER::fetch_quotes')
    logging.info('WORKER::fetch_quotes')

    # quotes = Api.fetch_quotes()
    #
    # Db().set_quotes(quotes)

    await check_users_notifications(bot)
    

async def check_users_notifications(bot):
    logging.info('WORKER::check_users_notifications')
    
    users = Db().get_users()
    users = [u for u in users if 'notifications' in u.keys()]

    prices = {}
    quotes = Db().get_quotes()
    
    for q in quotes:
        prices[q['symbol'].lower()] = q["quote"]["USD"]["price"]
    
    for user in users:
        for n in user['notifications']:
            comparator = get_comparator(n['operator'])
            symbol_price = float(prices[n['symbol']])
            compare_price = float(n['price'])

            if comparator(symbol_price, compare_price):
                message = new_notification_formatter(n)

                await bot.send_message(user['id'], message)
                logging.info(f'User {user["id"]} is notified')
