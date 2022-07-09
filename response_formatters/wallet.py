from lib.api import Api


def wallet_formatter(wallet):
    if wallet is None:
        return 'Your wallet is empty'
    
    res = ''
    
    for w in wallet:
        res += f'{w["symbol"]}: ${Api.fetch_btc_balance(address=w["address"])}\n'
        
    return res

