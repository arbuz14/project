from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import files_actions, list_files
from app.keyboards.services import services_keyboard_builder, service_actions_keyboards
from app.forms.clinic import ClinicForm, ReviewForm

clinic_router = Router()

# Пацієнти
@clinic_router.message(F.text == "Показати всіх пацієнтів")
async def show_patients(message: Message, state: FSMContext):
    patients = files_actions.open_file()
    keyboard = services_keyboard_builder(patients)
    await message.answer(text="Виберіть пацієнта", reply_markup=keyboard)

@clinic_router.callback_query(F.data.startswith("patient_"))
async def patient_actions(callback: CallbackQuery, state: FSMContext):
    patient = callback.data.split("_")[-1]
    keyboard = service_actions_keyboards(patient)
    await callback.message.answer(text=patient, reply_markup=keyboard)

# Прийоми
@clinic_router.callback_query(F.data.startswith("cured_animal_"))
async def visit_patient(callback: CallbackQuery, state: FSMContext):
    patient = callback.data.split("_")[-1]
    msg = files_actions.sold_product(patient)
    await callback.message.answer(text=msg)

# Послуги
@clinic_router.callback_query(F.data.startswith("delete_animal_"))
async def service_actions(callback: CallbackQuery, state: FSMContext):
    service = callback.data.split("_")[-1]
    msg = files_actions.del_product(service)
    await callback.message.answer(text=f"Обрано послугу: {service}")

# Відгуки
@clinic_router.message(F.text == "Додати новий відгук")
async def leave_review(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ReviewForm.text)
    await message.answer(text="Введіть ваш відгук")

@clinic_router.message(ReviewForm.text)
async def save_review(message: Message, state: FSMContext):
    data = await state.update_data(text=message.text)
    await state.clear()
    msg = files_actions.add_review(data.get("text"))
    await message.answer(text=f"Ваш відгук збережено: {msg}")

# Показати візити
@clinic_router.message(F.text == "Показати записи про візити")
async def show_visits(message: Message, state: FSMContext):
    visits = files_actions.open_file(list_files.VISITS)
    msg = "\n".join([f"{i+1}. {visit}" for i, visit in enumerate(visits)])
    await message.answer(text=msg)
