from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Зарегистрироваться")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Пройдите регистрацию"
)

get_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отправить номер телефона", request_contact=True)],
    ],
    resize_keyboard=True
)

other_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Актуальные мероприятия")],
        [KeyboardButton(text="Предыдущие эфиры")],
        [KeyboardButton(text="Забрать подарки")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт"
)
