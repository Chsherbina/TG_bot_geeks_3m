from aiogram import Router, types
from aiogram.filters.command import Command
from crawler.house_kg import HouseParser


house_router = Router()


@house_router.message(Command('show_house'))
async def show_house_links(message: types.Message):
    my_crawler = HouseParser()
    my_crawler.get_page()
    links = my_crawler.get_flat_links()
    for link in links:
        message.answer(link)



