import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import token
from api.get_current_date import get_date
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, WebAppInfo, InlineKeyboardButton, \
    InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ContentType

from database import add_user
from top_information import top

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

inline_button = InlineKeyboardButton(text="Перейти", callback_data='open_webapp')
inline_kb = InlineKeyboardMarkup(inline_keyboard=[[inline_button]])


class VacancyForm(StatesGroup):
    waiting_for_vacancy = State()


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
    user_data = (user_id, user_name, 'user', get_date())  # registration
    try:
        add_user(user_data)
        await message.answer("Здравствуйте!", reply_markup=builder.as_markup(resize_keyboard=True))
    except Exception as e:
        if e:
            await message.answer('Пользователь уже существует', reply_markup=builder.as_markup(resize_keyboard=True))


@dp.message(Command("checkvac"))
async def check_vacancy(message: types.Message, state: FSMContext):
    await message.answer('Чтобы отправить вакансию, пришлите её текст или фото')
    await state.set_state(VacancyForm.waiting_for_vacancy.state)


@dp.message(VacancyForm.waiting_for_vacancy)
async def process_vacancy(message: types.Message, state: FSMContext):
    if message.content_type == ContentType.TEXT:
        await message.answer('Вы отправили текстовую вакансию')
    elif message.content_type == ContentType.PHOTO:
        await message.answer('Вы отправили вакансию в виде фото')
    else:
        await message.answer('Пожалуйста, отправьте вакансию в виде текста или фото')

    await state.clear()

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


@dp.message(Command("quiz"))
async def send_quiz_link(message: types.Message):
    await message.answer('Вы можете пройти викторину по кнопке ниже', reply_markup=inline_kb)


@dp.callback_query(lambda callback_query: callback_query.data == 'open_webapp')
async def handle_button1(callback_query: types.CallbackQuery):
    webapp_button = InlineKeyboardButton(text="Пройти викторину",
                                         web_app=WebAppInfo(url='https://7861-85-174-195-151.ngrok-free.app/login'))
    webapp_kb = InlineKeyboardMarkup(inline_keyboard=[[webapp_button]])
    await bot.send_message(callback_query.from_user.id, 'Нажмите на кнопку ниже, чтобы пройти викторину',
                           reply_markup=webapp_kb)
    await callback_query.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
