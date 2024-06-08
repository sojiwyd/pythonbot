from aiogram.fsm.state import StatesGroup, State

class RegisterStates(StatesGroup):
    regName = State()
    regEmail = State()
    regPhoneNumber = State()