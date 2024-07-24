from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

from bot_config import database

dishes_router = Router()


@dishes_router.message(Command('menu'))
async def menu_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Салаты', callback_data='салаты'),
                types.InlineKeyboardButton(text='Первые блюда', callback_data='первое')
            ],
            [
                types.InlineKeyboardButton(text='Вторые блюда', callback_data='второе'),
                types.InlineKeyboardButton(text='Десерты', callback_data='десерты')
            ],
            [
                types.InlineKeyboardButton(text='Шашлык', callback_data='шашлык'),
                types.InlineKeyboardButton(text='Рыба', callback_data='рыба'),
                types.InlineKeyboardButton(text='Мясо',  callback_data='мясо')
            ]
        ]
    )

    await message.answer(
        text='Выберете меню',
        reply_markup=kb
    )

signal = ('салаты', 'первое', 'второе', 'десерты')


@dishes_router.callback_query(lambda call: call.data in signal)
async def dishes(call: types.CallbackQuery):
    query = """
    SELECT * FROM dishes JOIN categories ON dishes.category_id = categories.id
    WHERE categories.name = ?
    """
    data = database.fetch(
        query=query,
        params=(call.data,)
    )

    for i in data:
        photo = FSInputFile(i[5])
        await call.message.answer_photo(photo=photo, caption=f'Блюдо: {i[1]}\n'
                                                             f'Ингредиенты: {i[3]}. Вес: {i[2]}гр.\n'
                                                             f'Цена: {i[4]}')


@dishes_router.message(F.text.lower() == 'шашлык')
async def shashlyk_handler(message: types.Message):
    photo1 = types.FSInputFile('images/Шашлык.jpg')
    await message.answer_photo(photo=photo1, caption= 'Шашлык ассорти')


@dishes_router.message(F.text.lower() == 'мясо')
async def meat_handler(message: types.Message):
    photo2 = types.FSInputFile('images/мясное.jpg')
    await message.answer_photo(photo=photo2, caption='Мясное ассорти')


@dishes_router.message(F.text.lower() == 'рыба')
async def fish_handler(message: types.Message):
    photo3 = types.FSInputFile('images/рыба.jpg')
    await message.answer_photo(photo=photo3, caption='Рыбное ассорти')
