from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

btn_start = KeyboardButton('start')
btn_help = KeyboardButton('help')
btn_text = KeyboardButton('convert')


keyboard_user = ReplyKeyboardMarkup(resize_keyboard=True)

keyboard_user.add(btn_text).row(btn_help, btn_start)