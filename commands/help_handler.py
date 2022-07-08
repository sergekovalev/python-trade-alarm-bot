from lib.MessageEvent import MessageEvent


async def handler(event: MessageEvent):
    await event.message.answer('help')