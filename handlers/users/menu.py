from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, message,ReplyKeyboardRemove
from data.config import ADMINS, CHANEL
from keyboards.default.bosh import boshmenyu, back
from loader import dp, bot
from states.login import Edit
from keyboards.inline.tuman import tumanlarkb, diff_callback, check
ADMIN = 170363208
@dp.message_handler(text="➕ Ro'yhatdan o'tish")
async def enter_test(message: types.Message):

    await message.answer("Tumaningizni tanlang!", reply_markup=tumanlarkb)
    await Edit.tuman.set()

@dp.callback_query_handler(diff_callback.filter(get='get'), state=Edit.tuman)
async def get_word(call: CallbackQuery, callback_data: dict, state: FSMContext):
    tuman = callback_data["tuman"]
    await call.message.delete()
    if tuman == "cancel":
        await call.message.answer("Bosh menyu", reply_markup=boshmenyu)
        await state.reset_state(with_data=False)

    else:
        await state.update_data(
            {
                "tuman": tuman
            }
        )
        await call.message.answer("Mahallangiz nomini kiriting!", reply_markup=ReplyKeyboardRemove())
        await Edit.next()


@dp.message_handler(state=Edit.mahalla)
async def enter_test(message: types.Message, state: FSMContext):
    await state.update_data(
        {
            "mahalla": message.text
        }
    )
    await message.answer("Jamoangiz nomini kiriting!")
    await Edit.next()

@dp.message_handler(state=Edit.jamoa)
async def enter_test(message: types.Message, state: FSMContext):
    await state.update_data(
        {
            "jamoa": message.text
        }
    )
    await message.answer("Jamoa sardorining ma'lumotlarini quyidagi namuna kabi kiriting!(1-ishtrokchi)", reply_markup=back)
    await message.answer("""Ism, familiya otasining ismi
Yashash manzili(Mahalla, ko'cha, uy)
Passport seriyasi va raqami
Tug'ilgan sana(kun.oy.yil)
Telefon raqam

!!! Diqqat, har bir ma'lumot, namunadagi kabi, yangi qatordan, bitta xabar ichida yuborilsin!""")
    await message.answer("""Ahadov Sardor Ikromjon o'g'li
Yuksalish mahallasi,Obod ko'cha, 2-uy
AC 2345678
20.02.2000
+998123456789""")
    await Edit.next()


@dp.message_handler(state=Edit.sardor)
async def answer_fulwlname(message: types.Message, state: FSMContext):
    mylist = message.text.split("\n")
    try:
        if len(mylist) == 5 and mylist[2][:2].isalpha() and mylist[2][3].isdigit() and 8 < len(mylist[4]) < 20:
            await state.update_data(
                {
                    "sardor": message.text
                }
            )
            await message.answer("2-ishtrokchining ma'lumotlarini ko'rsatilgan tartibda kiriting!")
            await Edit.next()
        elif message.text == "🔙 Bekor qilish":
            await message.answer("Bekor qilindi!", reply_markup=boshmenyu)
            await state.reset_state(with_data=False)

        else:
            await message.answer("Xatolik topildi, qaytadan namunadagidek kiriting!")
            await Edit.sardor.set()
    except:
        await message.answer("Xatolik topildi, qaytadan namunadagidek kiriting!")
        await Edit.sardor.set()



@dp.message_handler(state=Edit.person2)
async def answer_fwullname(message: types.Message, state: FSMContext):
    mylist = message.text.split("\n")
    try:
        if len(mylist) == 5 and mylist[2][:2].isalpha() and mylist[2][3].isdigit() and 8 < len(mylist[4]) < 20:
            await state.update_data(
                {
                    "person2": message.text
                }
            )
            await message.answer("3-ishtrokchining ma'lumotlarini ko'rsatilgan tartibda kiriting!")
            await Edit.next()

        elif message.text == "🔙 Bekor qilish":
            await message.answer("Bekor qilindi!", reply_markup=boshmenyu)
            await state.reset_state(with_data=False)

        else:
            await message.answer("Xatolik topildi, qaytadan namunadagidek kiriting!")
            await Edit.person2.set()

    except:
        await message.answer("Xatolik topildi, qaytadan namunadagidek kiriting!")
        await Edit.person2.set()

@dp.message_handler(state=Edit.person3)
async def answser_fullname(message: types.Message, state: FSMContext):
    mylist = message.text.split("\n")
    try:
        if len(mylist) == 5 and mylist[2][:2].isalpha() and mylist[2][3].isdigit() and 8 < len(mylist[4]) < 20:
            await state.update_data(
                {
                    "person3": message.text
                }
            )
            await message.answer("4-ishtrokchining ma'lumotlarini ko'rsatilgan tartibda kiriting!")
            await Edit.next()
        elif message.text == "🔙 Bekor qilish":
            await message.answer("Bekor qilindi!", reply_markup=boshmenyu)
            await state.reset_state(with_data=False)

        else:
            await message.answer("Xatolik topildi, qaytadan namunadagidek kiriting!")
            await Edit.person3.set()

    except:
        await message.answer("Xatolik topildi, qaytadan namunadagidek kiriting!")
        await Edit.person3.set()
@dp.message_handler(state=Edit.person4)
async def ansswer_fullname(message: types.Message, state: FSMContext):
    mylist = message.text.split("\n")
    try:
        if len(mylist) == 5 and mylist[2][:2].isalpha() and mylist[2][3].isdigit() and 8 < len(mylist[4]) < 20:
            await state.update_data(
                {
                    "person4": message.text
                }
            )
            await message.answer("5-ishtrokchining ma'lumotlarini ko'rsatilgan tartibda kiriting!")
            await Edit.next()
        elif message.text == "🔙 Bekor qilish":
            await message.answer("Bekor qilindi!", reply_markup=boshmenyu)
            await state.reset_state(with_data=False)

        else:
            await message.answer("Xatolik topildi, qaytadan namunadagidek kiriting!")
            await Edit.person4.set()
    except:
        await message.answer("Xatolik topildi, qaytadan namunadagidek kiriting!")
        await Edit.person4.set()


@dp.message_handler(state=Edit.person5)
async def answefr_fullname(message: types.Message, state: FSMContext):
    mylist = message.text.split("\n")
    try:
        if len(mylist) == 5 and mylist[2][:2].isalpha() and mylist[2][3].isdigit() and 8 < len(mylist[4]) < 20:
            await state.update_data(
                {
                    "person5": message.text
                }
            )
            await message.answer("6-ishtrokchining ma'lumotlarini ko'rsatilgan tartibda kiriting!")
            await Edit.next()
        elif message.text == "🔙 Bekor qilish":
            await message.answer("Bekor qilindi!", reply_markup=boshmenyu)
            await state.reset_state(with_data=False)

        else:
            await message.answer("Xatolik topildi, qaytadan namunadagidek kiriting!")
            await Edit.person5.set()
    except:
        await message.answer("Xatolik topildi, qaytadan namunadagidek kiriting!")
        await Edit.person5.set()
@dp.message_handler(state=Edit.person6)
async def ansrwer_fullname(message: types.Message, state: FSMContext):
    mylist = message.text.split("\n")
    try:
        if len(mylist) == 5 and mylist[2][:2].isalpha() and mylist[2][3].isdigit() and 8 < len(mylist[4]) < 20:
            await state.update_data(
                {
                    "person6": message.text
                }
            )
            data = await state.get_data()
            await message.answer(f"Tuman: {data['tuman']}\nMahalla: {data['mahalla']}\nJamoa nomi: {data['jamoa']}\n\n👤Guruh sardori:\n{data['sardor']}\n\n👤2-ishtokchi:\n{data['person2']}\n\n👤3-ishtokchi:\n{data['person3']}\n\n👤4-ishtokchi:\n{data['person4']}\n\n👤5-ishtokchi:\n{data['person5']}\n\n👤6-ishtokchi:\n{data['person6']}\n")
            await message.answer("Ushbu ma'lumotlar qabul qilindi! Tekshirish uchun yuborishga ruxsat berasizmi?", reply_markup=check)
            await Edit.check.set()

        elif message.text == "🔙 Bekor qilish":
            await message.answer("Bekor qilindi!", reply_markup=boshmenyu)
            await state.reset_state(with_data=False)

        else:
            await message.answer("Xatolik topildi, qaytadan namunadagidek kiriting!")
            await Edit.person6.set()

    except:
        await message.answer("Xatolik topildi, qaytadan namunadagidek kiriting!")
        await Edit.person6.set()

@dp.callback_query_handler(diff_callback.filter(get='check'), state=Edit.check)
async def get_word(call: CallbackQuery, callback_data: dict, state: FSMContext):
    boo = callback_data["tuman"]
    data = await state.get_data()
    if boo == "true": 
        await bot.send_message(chat_id=ADMIN, text=f"Foydalanuvchi - {call.from_user.mention} ushbu ma'lumotlarni yubormoqda. Tasdiqlaysizmi?")
        await bot.send_message(chat_id=ADMIN,text=f"Tuman: {data['tuman']}\nMahalla: {data['mahalla']}\nJamoa nomi: {data['jamoa']}\n\n👤Guruh sardori:\n{data['sardor']}\n\n👤2-ishtokchi:\n{data['person2']}\n\n👤3-ishtokchi:\n{data['person3']}\n\n👤4-ishtokchi:\n{data['person4']}\n\n👤5-ishtokchi:\n{data['person5']}\n\n👤6-ishtokchi:\n{data['person6']}\n", reply_markup=check)
        await call.message.delete()
        await call.message.answer("Tekshirish uchun yuborildi")
        await state.reset_state(with_data=False)
    elif boo == "false":
        await call.message.delete()
        await call.message.answer("Ma'lumotlar bekor qilindi, qaytadan kiritishingiz mumkin")
        await state.reset_state(with_data=False)

@dp.callback_query_handler(diff_callback.filter(get='check'), chat_id=ADMIN)
async def get_word(call: CallbackQuery, callback_data: dict, state: FSMContext):
    boo = callback_data["tuman"]
    if boo == "true":
        message = await call.message.edit_reply_markup()
        await message.send_copy(chat_id=-1001571086713)
        #await bot.send_message(chat_id=CHANEL[0], text="hhh")
        await call.message.delete()
        await call.message.answer("Tasdiqladingiz")

    elif boo == "false":
        await call.message.delete()
        await call.message.answer("Ma'lumotlarni ra'd etdingiz")
















