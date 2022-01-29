from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, inline_keyboard
from keyboards.inline.callback_data import diff_callback


mylist="""Andijon shahri
Asaka
Xo'jaobod
Jalaquduq
Qo'rg'ontepa
Honobod
Bo'ston
Ulug'nor
Paxtaobod
Oltinko'l
Baliqchi
Andijon tumani
Izboskan
Shahrixon
Marhamat
Buloqboshi""".split("\n")



tumanlarkb = InlineKeyboardMarkup(row_width=2)


for key in mylist:
    tumanlarkb.insert(InlineKeyboardButton(text=key, callback_data=diff_callback.new(tuman=key, get='get' )))


tumanlarkb.add(InlineKeyboardButton(text="🔙 Bekor qilish", callback_data=diff_callback.new(tuman="cancel",get='get')))


check = InlineKeyboardMarkup(row_width=2)

check.add(InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=diff_callback.new(tuman="true",get='check')))
check.add(InlineKeyboardButton(text="❌ Ra'd etish", callback_data=diff_callback.new(tuman="false",get='check')))

