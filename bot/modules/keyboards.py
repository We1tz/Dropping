from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

builder = ReplyKeyboardBuilder()
builder.row(
        types.KeyboardButton(text="Запросить геолокацию", request_location=True),
        types.KeyboardButton(text="Запросить контакт", request_contact=True)
    )
builder.row(types.KeyboardButton(
        text="Создать викторину",
        request_poll=types.KeyboardButtonPollType(type="quiz"))
    )