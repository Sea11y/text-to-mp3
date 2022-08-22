import time
import os, shutil
from aiogram.types import InputFile
from gtts import gTTS
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import dp, bot
from src.states.txt_conv import FSMText
from aiogram.dispatcher.filters import Text


async def del_mp3():
    folder = 'C:/Users/Admin/Desktop/swag/text-to-mp3/src/handlers/user/mp3files' #Deleting files from the specified folder
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


async def mp3_to_text(pages, language='ru'): #Translating text to audio format
    text = ''.join(pages)
    text = text.replace('\n', '')
    my_audio = gTTS(text=text, lang=language)
    time.sleep(10)
    my_audio.save("%s.mp3" % os.path.join('C:/Users/Admin/Desktop/swag/text-to-mp3/src/handlers/user/mp3files', f'{pages}'))


@dp.message_handler(Text(equals='convert', ignore_case = True))
@dp.message_handler(Command("convert"))
async def bot_start(message : types.Message):
    await message.answer("Привет 👋!\n\nОтправьте ваш текст и бот сконвертирует его в аудио файл😃")
    await FSMText.file.set()


@dp.message_handler(state=FSMText.file)
async def get_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['file'] = message.text
        await FSMText.next()
        await message.reply('Теперь введите язык который используется в тексте(ru/en)\n')


@dp.message_handler(state=FSMText.language)
async def sending_mp3(message: types.Message, state: FSMContext):
    try:
        await message.answer('[+] Processing...')
        async with state.proxy() as data:
            data['language'] = message.text
        file_lan = data['language']
        file_name = data['file']
        await mp3_to_text(file_name, file_lan)
        audio_bytes = InputFile(path_or_bytesio=f'src/handlers/user/mp3files/{file_name}.mp3')
        await dp.bot.send_audio(chat_id=message.from_user.id, audio=audio_bytes)
        await message.answer('Хорошего дня!')
        await del_mp3()
    except:
        await message.answer('Произошла ошибка')
    await state.finish()


@dp.message_handler(state='*', commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case = True), state='*')
async def cancel_header(message : types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return 'Ничего не происходит'
    await state.finish()
    await message.reply('Вы отменили конвертацию')