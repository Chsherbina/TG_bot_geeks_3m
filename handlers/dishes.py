from aiogram import types, Router, F


dishes_router = Router()


@dishes_router.message(F.text=='шашлык')
async def shashlyk_handler(message: types.Message):
    photo1 = types.FSInputFile('images/Шашлык.jpg')
    await message.answer_photo(photo=photo1, caption= 'Шашлык ассорти')


@dishes_router.message(F.text=='мясо')
async def meat_handler(message: types.Message):
    photo2 = types.FSInputFile('images/мясное.jpg')
    await message.answer_photo(photo=photo2, caption='Мясное ассорти')


@dishes_router.message(F.text=='рыба')
async def fish_handler(message: types.Message):
    photo3 = types.FSInputFile('images/рыба.jpg')
    await message.answer_photo(photo=photo3, caption='Рыбное ассорти')
