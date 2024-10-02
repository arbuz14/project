from aiogram.fsm.state import State, StatesGroup

class ClinicServiceForm(StatesGroup):
    service_name = State()
    animal_name = State()
    appointment_date = State()
