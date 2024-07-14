from aiogram import types, Router
from aiogram.filters.command import Command

myinfo_router = Router()

@myinfo_router.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}, {message.from_user.username}, {message.from_user.id}')
