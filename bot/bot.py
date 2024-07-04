import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import token
from get_current_date import get_date
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from database import add_user, select_from_base
from top_information import top

#from keyboards import start_keyboard

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def command_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text='Узнать больше'),
        types.KeyboardButton(text="Викторина")
    )
    builder.row(types.KeyboardButton(text="Рейтинг игроков"))

    user_id = message.from_user.id
    user_name = message.from_user.username
    user_data = (user_id, user_name, get_date(), 'NaN', 'NaN')  # registration
    try:
        add_user(user_data)

        await message.answer("Здравствуйте!", reply_markup=builder.as_markup(resize_keyboard=True))
    except Exception as e:
        if e:
            await message.answer('Пользователь уже существует', reply_markup=builder.as_markup(resize_keyboard=True))


#
@dp.message(Command("dk"))
async def delete_keyboard(message: types.Message):
    await message.answer('Ваша клавиатура удалена', reply_markup=types.ReplyKeyboardRemove())


@dp.message(Command("top"))
async def delete_keyboard(message: types.Message):
    await message.answer('Рейтинг пользователей, которые прошли викторину')
    top_information = top()
    c = 0

    for p in top_information:
        c += 1
        if c <= 3:
            await message.answer(f'На данный момент {c} место занимает пользователь @{p[0]} с рейтингом {p[1]}')
        else:
            break


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
