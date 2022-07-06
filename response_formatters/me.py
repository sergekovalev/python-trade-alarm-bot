from response_formatters.wallet import wallet_formatter


def me_formatter(data):
    return f'''
Name: {data['name']}
Wallet: {wallet_formatter(data['wallet'])}
Following: {', '.join(data['follow']) if len(data['follow']) else 'nothing'}
    '''
