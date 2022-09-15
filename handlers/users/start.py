from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Xush kelibsiz! Iltimos raqamingizni kiriting va sms kod yuborilishini kuting")
