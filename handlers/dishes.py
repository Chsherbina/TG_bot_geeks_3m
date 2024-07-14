from aiogram import types, Router
from aiogram.filters.command import Command


shashlyk_router = Router()

@shashlyk_router.message(Command('shashlyk'))
async def shashlyk_handler(message: types.Message):
    photo1 = types.FSInputFile('images/Шашлык.jpg')
    await message.answer_photo(photo=photo1, caption= 'Шашлык ассорти')


meat_router = Router()

@meat_router.message(Command('meat'))
async def meat_handler(message: types.Message):
    photo2 = types.FSInputFile('images/мясное.jpg')
    await message.answer_photo(photo=photo2, caption='Мясное ассорти')


fish_router = Router()

@fish_router.message(Command('fish'))
async def fish_handler(message: types.Message):
    photo3 = types.FSInputFile('images/рыба.jpg')
    await message.answer_photo(photo=photo3, caption='Рыбное ассорти')


