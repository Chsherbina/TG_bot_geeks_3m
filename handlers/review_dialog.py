from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

review_router = Router()


class ReviewDialog(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()



@review_router.callback_query(F.data=='feedback')
async def start_review(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(ReviewDialog.name)
    await call.message.answer('Как вас зовут?')


@review_router.message(ReviewDialog.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ReviewDialog.phone_number)
    await message.answer('Ваш номер телефона?')


@review_router.message(ReviewDialog.phone_number)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await state.set_state(ReviewDialog.visit_date)
    await message.answer('Дата вашего посещения нашего заведения?')


@review_router.message(ReviewDialog.visit_date)
async def process_visit(message: types.Message, state: FSMContext):
    await state.update_data(visit_date=message.text)
    await state.set_state(ReviewDialog.food_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='1'), types.KeyboardButton(text='2'), types.KeyboardButton(text='3'), types.KeyboardButton(text='4'), types.KeyboardButton(text='5')],
        ],
        resize_keyboard=True,
    )
    await message.answer('Как оцениваете качество еды?', reply_markup=kb)


@review_router.message(ReviewDialog.food_rating)
async def process_food(message: types.Message, state: FSMContext):
    food_rating = message.text
    if not food_rating.isdigit():
        await message.answer('Вводи только цифры')
        return
    food_rating = int(food_rating)
    if food_rating < 1 or food_rating > 5:
        await message.answer('Оценка от 1 до 5')
        return
    await state.update_data(food_rating=message.text)
    await state.set_state(ReviewDialog.cleanliness_rating)
    await message.answer('Как оцениваете чистоту заведения?')


@review_router.message(ReviewDialog.cleanliness_rating)
async def process_cleanliness(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    cleanliness_rating = message.text
    if not cleanliness_rating.isdigit():
        await message.answer('Вводи только цифры')
        return
    cleanliness_rating = int(cleanliness_rating)
    if cleanliness_rating < 1 or cleanliness_rating > 5:
        await message.answer('Оценка от 1 до 5')
        return
    await state.update_data(cleanliness_rating=message.text)
    await state.set_state(ReviewDialog.extra_comments)
    await message.answer('Дополнительные комментарии', reply_markup=kb)


@review_router.message(ReviewDialog.extra_comments)
async def process_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)

    data = await state.get_data()
    print(data)
    await state.clear()
    await message.answer('Спасибо за обратную связь!!!')