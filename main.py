import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import logging
import random


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


@dp.message(Command('start'))
async def start_handler(message):
    print(message.from_user.id)
    await message.answer(f'Привет {message.from_user.first_name}, ты в боте Щербина Аслана для Д/З')


@dp.message(Command('random_recipe'))
async def start_handler(message):
    recipe = (f'Омлет с томатами и зеленью:\n'
              f'Взбейте 3 яйца с солью и перцем.\n'
              f'На сковороде обжарьте нарезанные томаты и зелень.\n'
              f'Залейте яйца и готовьте до готовности.',
              f'Салат "Греческий":\n'
              f'Смешайте нарезанные помидоры, огурцы, болгарский перец, лук, маслины и фету.\n'
              f'Заправьте оливковым маслом и лимонным соком.',
              f'Куриные крылышки в медово-соевом соусе:\n'
              f'Замаринуйте крылышки в смеси меда, соевого соуса и чеснока.\n'
              f'Запеките в духовке при 180°C в течение 25 минут.',
              f'Паста с чесночным маслом:\n'
              f'Отварите пасту до готовности.\n'
              f'Обжарьте измельченный чеснок на оливковом масле.\n'
              f'Смешайте пасту с чесночным маслом и посыпьте пармезаном.',
              f'Рис с овощами:\n'
              f'Обжарьте нарезанные морковь, брокколи и перец на сковороде.\n'
              f'Добавьте вареный рис и соевый соус, перемешайте и тушите несколько минут.')
    rc = random.choice(recipe)
    await message.answer(f'Рецепт: {rc}')


@dp.message(Command('myinfo'))
async def myinfo_handler(message):
    await message.answer(f'Привет {message.from_user.first_name}, {message.from_user.username}, {message.from_user.id}')


@dp.message()
async def echo_handler(message):
    await message.answer("Чтобы взаимодействовать с Ботом напиши команду")


async def main():
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())