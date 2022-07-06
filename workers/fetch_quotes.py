import logging
from lib.db import Db
from lib.api import Api


def worker():
    print('WORKER::fetch_quotes')
    logging.info('WORKER::fetch_quotes')

    # quotes = Api.fetch_quotes()
    #
    # Db().set_quotes(quotes)

    check_users_stats()
    

def check_users_stats():
    print('WORKER::check_users_stats')
    logging.info('WORKER::check_users_stats')
    
    users = Db().get_users()
    
    for user in users:
        print(user)
