from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMText(StatesGroup):
    file = State()
    language = State()