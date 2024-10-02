from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.client.default import DefaultBotProperties
from app.routers.products import clinic_router
from app.routers.reviews import review_router
from app.routers.start import start_router

load_dotenv()

root_router = Router()

root_router.include_routers(clinic_router,review_router,start_router)


@root_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
    f"Вітаю в ветклініці, {hbold(message.from_user.full_name)}! "
    "Ми готові допомогти вашому улюбленцю. Ви можете записатися на прийом або отримати консультацію."
)



async def main() -> None:
    BOT_TOKEN = getenv("TOKEN")
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(root_router)
    await dp.start_polling(bot)





