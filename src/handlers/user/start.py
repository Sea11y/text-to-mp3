from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from src.keybords import keyboard_user
from aiogram.dispatcher.filters import Text

from loader import dp

@dp.message_handler(Text(equals='start', ignore_case = True))
@dp.message_handler(CommandStart(), state="*")
async def start(message: types.Message):
    await message.answer(f"Hello 👋, {message.from_user.full_name}!\n\n"
                         f"Я бот для обработки текста в mp3-файлы 🤖\n"
                         f"Я помогу тебе.\n\n чтобы начать пропиши: /convert\n\n"
                         f"I'm a bot for processing text into mp3 files🤖\n"
                         f"I'll help you with that\n\n"
                         f"To get started: /convert 📍", reply_markup=keyboard_user)


