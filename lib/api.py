import requests
from dotenv import dotenv_values


config = dotenv_values(".env")


class Api(object):
    @staticmethod
    def fetch_quotes():
        headers = {'X-CMC_PRO_API_KEY': config['COINMARKETCAP_TOKEN']}

        r = requests.get(config['FETCH_QUOTES_URL'], headers=headers)

        data = r.json()['data']
        
        return data

    @staticmethod
    def fetch_btc_balance(address: str, currency='usd') -> float:
        url = f'{config["FETCH_BTC_BALANCE_URL"]}/{address}'

        r = requests.get(url)

        btc_balance = float(r.json())
        
        if btc_balance > 0:
            btc_balance = btc_balance / 100000000
        
        return btc_balance
