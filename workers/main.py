from workers.fetch_quotes import worker as fetch_quotes
import asyncio


async def workers_process(bot):
    while True:
        await fetch_quotes(bot)

        await asyncio.sleep(60 * 60)
