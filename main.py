import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import load_dotenv
from utils.commands import set_commands
from handlers.register import start_register, register_name, register_email, register_number
from handlers.start import get_start
from state.register import RegisterStates

load_dotenv()
token = os.getenv("TOKEN")
db_name = os.getenv("DATABASE_NAME")

bot = Bot(token=token)
dp = Dispatcher()


async def start_bot(message: Message):
    await get_start(message, bot)

async def start():
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

dp.message.register(start_bot, CommandStart())
dp.message.register(start_register, F.text == "Зарегистрироваться")
dp.message.register(register_name, RegisterStates.regName)
dp.message.register(register_email, RegisterStates.regEmail)
dp.message.register(register_number, RegisterStates.regPhoneNumber, F.content_type == 'contact')

if __name__ == '__main__':
    asyncio.run(start())



