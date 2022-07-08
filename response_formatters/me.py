from response_formatters.wallet import wallet_formatter
from entities.user import UserEntity


def notifications_formatter(notifications):
    if notifications is None:
        return 'Nothing here'
    
    message = '\n'
    for i in range(len(notifications)):
        n = notifications[i]

        message += f'    {i + 1} - {n["symbol"].upper()} when it\'s {n["human_readable_operator"]} {n["price"]} USD\n'
    
    return message


def me_formatter(user: UserEntity):
    return f'''
Name: {user.name}
Wallet: {wallet_formatter(user.wallet)}
Following: {', '.join(user.follow) if len(user.follow) else 'nothing'}
Notifications: {notifications_formatter(user.notifications)}
    '''
