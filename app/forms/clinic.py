from aiogram.fsm.state import State, StatesGroup

class ReviewForm(StatesGroup):
    text = State()


class ClinicForm(StatesGroup):
    text = State()