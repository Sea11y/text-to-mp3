import logging

from aiogram import Dispatcher

from src.data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "the bot is running")

        except Exception as err:
            logging.exception(err)
