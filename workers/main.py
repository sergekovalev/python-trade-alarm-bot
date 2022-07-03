from workers.fetch_quotes import worker as fetch_quotes
from lib.set_interval import set_interval


def workers_process():
    fetch_quotes()
    set_interval(fetch_quotes, 60 * 60)
