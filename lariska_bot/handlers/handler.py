from aiogram import types
from aiogram.dispatcher.filters import Text

from lariska_bot.dispatcher import dp
from lariska_bot.handlers.messages import *


@dp.message_handler(Text(contains=['с чего начать'], ignore_case=True))
async def where_to_begin(message: types.Message):
    await message.reply(get_start_here())


@dp.message_handler(commands=get_repo_list())
async def repo_answer(message: types.Message):
    await message.answer(get_repo())


@dp.message_handler(Text(contains=['наш репозиторий'], ignore_case=True))
async def our_repository_reply(message: types.Message):
    await message.reply(get_repo())


@dp.message_handler(Text(contains=['наша репа'], ignore_case=True))
async def our_repo_reply(message: types.Message):
    await message.reply(get_repo())


@dp.message_handler(Text(contains=['лариска', 'дура'], ignore_case=True))
async def call_names_reply(message: types.Message):
    await message.reply(dont_call_names())
