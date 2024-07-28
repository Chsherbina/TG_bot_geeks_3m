from aiogram import Router, types
from aiogram.filters.command import Command
from bot_config import bot
from datetime import timedelta


group_router = Router()

BAD_WORDS = ('идиот', 'бомж', 'тупой', 'дурак', 'дебил')


@group_router.message(Command('ban', prefix='!'))
async def ban_user(message: types.Message):
    reply = message.reply_to_message
    if reply:
        author = reply.from_user.id
        await bot.ban_chat_member(chat_id=message.chat.id, user_id=author, until_date=timedelta(seconds=90))


@group_router.message()
async def filter_bad_words(message: types.Message):
    for word in message.text.split():
        if word.lower() in BAD_WORDS:
            await message.delete()
            await bot.ban_chat_member(chat_id=message.chat.id, user_id=message.from_user.id, until_date=timedelta(hours=1))
            await message.answer(
                f'Не ругайся {message.from_user.first_name}')