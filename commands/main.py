from commands.start_handler import handler as start_handler
from commands.help_handler import handler as help_handler
from commands.me_handler import handler as me_handler
from commands.get_quotes_handler import handler as get_quotes_handler
from commands.get_wallet_handler import handler as get_wallet_handler
from commands.add_wallet_handler import handler as add_wallet_handler
from commands.delete_wallet_handler import handler as delete_wallet_handler
from commands.follow_currency_handler import handler as follow_currency_handler
from aiogram import types
import re

cmds = {
    r'/start': start_handler,
    r'/help': help_handler,
    r'/me': me_handler,
    r'/wallet': get_wallet_handler,
    r'/add_wallet': add_wallet_handler,
    r'add .+ wallet': add_wallet_handler,
    r'/delete_wallet': delete_wallet_handler,
    r'delete .+ wallet': delete_wallet_handler,
    r'/quotes': get_quotes_handler,
    r'/follow': follow_currency_handler,
    r'/unfollow': follow_currency_handler
}


async def parse_command(message: types.Message):
    for p, handler in cmds.items():
        if re.match(p, message.text):
            await handler(message)
            return
