from aiogram import types, Router


echo_router = Router()


@echo_router.message()
async def echo_handler(message: types.Message):
    await message.answer("Чтобы взаимодействовать с Ботом напиши команду")