import logging
import requests
from dotenv import dotenv_values
from db import Db
import asyncio
from time import sleep

config = dotenv_values(".env")

headers = {'X-CMC_PRO_API_KEY': config['COINMARKETCAP_TOKEN']}


def worker():
    print('WORKER::fetch_quotes')
    logging.info('WORKER::fetch_quotes')

    r = requests.get(config['FETCH_QUOTES_URL'], headers=headers)

    data = r.json()['data']

    Db().set_quotes(data)

    check_users_stats()
    

def check_users_stats():
    print('WORKER::check_users_stats')
    logging.info('WORKER::check_users_stats')
    
    users = Db().get_users()
    
    for user in users:
        print(user)
