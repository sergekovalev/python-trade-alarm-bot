from response_formatters.wallet import wallet_formatter


def notifications(notifications):
    if notifications is None:
        return 'Nothing here'
    
    message = '\n'
    for i in range(len(notifications)):
        n = notifications[i]

        message += f'    {i + 1} - {n["symbol"].upper()} when it\'s {n["human_readable_operator"]} {n["price"]} USD\n'
    
    return message


def me_formatter(data):
    return f'''
Name: {data['name']}
Wallet: {wallet_formatter(data['wallet'])}
Following: {', '.join(data['follow']) if 'follow' in data.keys() and len(data['follow']) else 'nothing'}
Notifications: {notifications(data['notifications'] if 'notifications' in data.keys() else None)}
    '''
