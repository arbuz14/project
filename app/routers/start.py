from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from app.keyboards.global_menu import global_menu_keyboard_builder

start_router = Router()

@start_router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    keyboard = global_menu_keyboard_builder()
    await message.answer(
        text=f"Вітаю у ветеринарній клініці '{message.from_user.full_name}'!",
        reply_markup=keyboard
    )
