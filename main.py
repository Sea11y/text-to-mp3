from aiogram import executor
from src.utils.notify_admins import on_startup_notify
import src.handlers
from loader import dp



async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
