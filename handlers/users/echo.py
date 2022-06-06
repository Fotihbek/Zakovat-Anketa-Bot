from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.Sts import MySt



@dp.message_handler(state=None)
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer("Matnning ikkinchi qismini kiriting:")
    await state.update_data({"id": "", "birinchi": message.text})
    await MySt.a.set()

@dp.message_handler(state=MySt.a)
async def bot_echo(message: types.Message, state: FSMContext):

    await state.update_data({"ikkinchi": message.text})
    data = await state.get_data()
    
    await message.answer(data)
    
    
    await state.reset_state(with_data=True)
