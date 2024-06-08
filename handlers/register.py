from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.register import RegisterStates
from keyboards.keyboard import get_number

async def start_register(message: Message, state: FSMContext):
    await message.answer("Давайте начнем регистрацию. Как вас зовут?")
    await state.set_state(RegisterStates.regName)

async def register_name(message: Message, state: FSMContext):
    await state.update_data(regname=message.text)
    await message.answer(f"SALAM MALEKUM {message.text}. Введите ваш email.")
    await state.set_state(RegisterStates.regEmail)

async def register_email(message: Message, state: FSMContext):
    await state.update_data(regemail=message.text)
    await state.set_state(RegisterStates.regPhoneNumber)
    await message.answer('Отправьте ваш номер телефона', reply_markup=get_number)

async def register_number(message: Message, state: FSMContext):
    if message.contact is None:
        await message.answer("Используйте кнопку для отправки номера телефона.")
        return

    await state.update_data(regphone=message.contact.phone_number)
    reg_data = await state.get_data()
    reg_name = reg_data.get('regname')
    reg_phone = reg_data.get('regphone')
    reg_email = reg_data.get('regemail')

    msg = (f"Вы успешно зарегистрировались. Ваши данные:\n"
           f"Ваше имя: {reg_name}\n"
           f"Ваш номер телефона: {reg_phone}\n"
           f"Ваш email: {reg_email}")
    await message.answer(msg)
    await state.clear()

