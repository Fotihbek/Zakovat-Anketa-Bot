from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

boshmenyu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard = [
    [KeyboardButton(text="➕ Ro'yhatdan o'tish")],
    [
        KeyboardButton(text="📄 Yo'riqnoma"),
        KeyboardButton(text="👨‍💻 Dasturchi")
    ]
])

back = ReplyKeyboardMarkup(resize_keyboard=True, keyboard = [
    [KeyboardButton(text="🔙 Bekor qilish")]])
