import asyncio
import logging

from bot_config import bot, dp
from handlers.start import start_router
from handlers.echo import echo_router
from handlers.myinfo import myinfo_router
from handlers.recipe import recipe_router
from handlers.dishes import shashlyk_router, meat_router, fish_router


async def main():
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(recipe_router)
    dp.include_router(shashlyk_router)
    dp.include_router(meat_router)
    dp.include_router(fish_router)
    dp.include_router(echo_router)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())