from aiogram import types


async def handler(message: types.Message):
    await message.answer('help')