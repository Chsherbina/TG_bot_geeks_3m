from aiogram import types, Router, F
from aiogram.filters.command import Command

start_router = Router()


@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Наш сайт', url="https://www.ersag.com.tr/"),
                types.InlineKeyboardButton(text='Наш адрес', url="https://maps.app.goo.gl/XXWo9VhnYNFzQsu56"),
            ],
            [
                types.InlineKeyboardButton(text='Наш инстаграм', url="https://www.instagram.com/ersag_inc/"),
                # types.InlineKeyboardButton(text='Наш телефон', call='0555999008')
            ],
            [
                types.InlineKeyboardButton(text='О нас', callback_data='about_us')
            ],
            [
                types.InlineKeyboardButton(text='Оставить отзыв', callback_data='feedback')
            ]
        ]
    )
    await message.answer(f'Привет {message.from_user.first_name}, Вас приветствует ресторан Ассорти!!!', reply_markup=kb)


@start_router.callback_query(F.data == 'about_us')
async def about_us_handler(callback: types.CallbackQuery):
    await callback.message.answer('Ресторан Ассорти: вкусная, традиционная, очень дальневосточная кухня')
    # await callback.massage.answer('Кушай много, становись больше')
