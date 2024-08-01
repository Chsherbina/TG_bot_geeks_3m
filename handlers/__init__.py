from aiogram import Router, F

from .start import start_router
from .review_dialog import review_router
from .myinfo import myinfo_router
from .recipe import recipe_router
from .dishes import dishes_router
from .echo import echo_router
from .group import group_router
from .house_kgparser import house_router

private_router = Router()

private_router.include_router(start_router)
private_router.include_router(review_router)
private_router.include_router(myinfo_router)
private_router.include_router(recipe_router)
private_router.include_router(dishes_router)
private_router.include_router(house_router)
private_router.include_router(echo_router)

private_router.message.filter(F.chat.type == 'private')