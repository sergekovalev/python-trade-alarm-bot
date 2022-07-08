from lib.math_operators import get_human_readable_operator


def new_notification_formatter(n):
    return f'Knock-Knock! {n["symbol"].upper()} {get_human_readable_operator(n["operator"])} {n["price"]} USD'
