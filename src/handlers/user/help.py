from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.dispatcher.filters import Text
from loader import dp

@dp.message_handler(Text(equals='help', ignore_case = True))
@dp.message_handler(CommandHelp(), state="*")
async def show_info(message: types.Message):
    await message.answer('📍Для того, чтобы начать пользоваться ботом:\n'
                         '📍Просто пришлите мне нужный вам текст/текстовый файл\n\n'
                         '📍 In order to start using the bot: \n'
                         '📍 Just send me the text/text file you need', disable_web_page_preview=True)