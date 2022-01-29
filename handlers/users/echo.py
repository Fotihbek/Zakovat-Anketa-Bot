from aiogram import types

from loader import dp

@dp.message_handler(text="👨‍💻 Dasturchi")
async def bot_echo(message: types.Message):
    await message.answer("Manfaatli taklif!\nHar xil telegram bot va veb-saytlar tuzib berish xizmatini tavsiya etamiz!\n👨‍💻 Dasturchi: @ProgerUzb (Fotihbek Komilov)")

@dp.message_handler(text="📄 Yo'riqnoma")
async def bot_echo(message: types.Message):
    await message.answer("https://telegra.ph/Zakovat-uchun-ro%CA%BByxatdan-o%CA%BBtish-01-29")

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
