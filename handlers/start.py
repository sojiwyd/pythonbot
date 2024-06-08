from aiogram import Bot
from aiogram.types import Message
from keyboards.keyboard import register_keyboard


async def get_start(message: Message, bot: Bot):
    await message.answer(f"SALAM MALEKUM, {message.from_user.first_name}, your id: {message.from_user.id}", reply_markup=register_keyboard)
