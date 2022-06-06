from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.Sts import MySt
import json


@dp.message_handler(state=None)
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer("Matnning ikkinchi qismini kiriting:")
    await state.update_data({"id": "", "text1": message.text})
    await MySt.a.set()

@dp.message_handler(state=MySt.a)
async def bot_echo(message: types.Message, state: FSMContext):

    await state.update_data({"text2": message.text})
    data = await state.get_data()
    matn = json.dumps(data)
    await message.answer(matn)
    
    await state.reset_state(with_data=True)
