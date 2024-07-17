import asyncio
import logging
import string
import re

from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from modules.get_date import get_date
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'vacansy_model'))
from vacansy_model.load import check_photo_vacancy, check_url_vacancy, check_text_vacancy
from aiogram.utils.keyboard import ReplyKeyboardBuilder, WebAppInfo, InlineKeyboardButton, \
    InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ContentType
from modules.text import hello, drop_vacancy, good_vacancy
from modules.database import add_user, select_from_base

allow_site = ['avito', 'hh', 'superjob', 'zarplata']
logging.basicConfig(level=logging.INFO)
token = '7131076437:AAF1yqCwAZRi3W5851NZ23CWNc4anULmj2g'
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


def top():
    data = select_from_base()
    uinf = []
    for user in data:
        uinf.append([user[1], int(user[3]), int(user[4])])
    sorted_data = sorted(uinf, key=lambda x: x[1], reverse=True)
    return sorted_data

def is_correct_name(name):
    alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" + string.ascii_lowercase
    if len(name) < 3:
        return False
    for i in range(len(name)):
        if name[i].lower() in alf:
            return True
    return False


def is_url(text):
    pattern = r'^(http|https):\/\/([\w.-]+)(\.[\w.-]+)+([\/\w\.-]*)*\/?$'
    return bool(re.match(pattern, text))


class NameForm(StatesGroup):
    waiting_for_name = State()


class VacancyForm(StatesGroup):
    waiting_for_vacancy = State()


@dp.message(Command("start"))
async def command_start(message: types.Message, state: FSMContext):
    await message.answer(hello, reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(NameForm.waiting_for_name.state)


@dp.message(NameForm.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    if not is_correct_name(message.text):
        await message.answer("Введите имя корректно!")
    else:
        user_id = message.from_user.id
        user_name = re.sub(r"\s+", "", message.text, flags=re.UNICODE)
        user_data = (user_id, user_name, 'user', get_date())
        try:
            add_user(user_data)
        except Exception as e:
            pass
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="Проверка вакансий"))
        builder.row(types.KeyboardButton(text="Викторина"))
        await message.answer('Выберите одну из функций', reply_markup=builder.as_markup(resize_keyboard=True))
        await state.clear()


@dp.message(F.text == "Проверка вакансий")
async def check_vacancy(message: types.Message, state: FSMContext):
    await message.answer('Чтобы отправить вакансию, пришлите её текст, фото или ссылку')
    await state.set_state(VacancyForm.waiting_for_vacancy.state)


@dp.message(VacancyForm.waiting_for_vacancy)
async def process_vacancy(message: types.Message, state: FSMContext):
    if message.content_type == ContentType.TEXT or message.content_type == ContentType.PHOTO or is_url(message.text):
        if message.content_type == ContentType.TEXT:
            if is_url(message.text):
                if message.text in allow_site:
                    if check_url_vacancy(message.text) == 0:
                        await message.answer(good_vacancy)
                    else:
                        await message.answer(drop_vacancy)
                else:
                    await message.answer(f'Пока принимаем вакансии тольно с сайтов {allow_site[0]}.ru, {allow_site[1]}.ru, {allow_site[2]}.ru, {allow_site[3]}.ru')
            else:
                if check_text_vacancy(message.text) == 0:
                    await message.answer(good_vacancy)
                else:
                    await message.answer(drop_vacancy)

        elif message.content_type == ContentType.PHOTO:
            await bot.download(
                message.photo[-1],
                destination=f"photo/{message.photo[-1].file_id}.jpg"
            )
            await message.answer('Подожди, идёт проверка вакансии...')
            current_dir = os.path.dirname(__file__)
            photo_dir = os.path.join(current_dir, 'photo')
            file_path = os.path.join(photo_dir, f"{message.photo[-1].file_id}.jpg")
            if check_photo_vacancy(file_path) == 0:
                await message.answer(good_vacancy)
            else:
                await message.answer(drop_vacancy)

            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
                print(f"Файл {file_path} успешно удален.")
            except FileNotFoundError:
                print(f"Файл {file_path} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при удалении файла {file_path}: {e}")

        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="Викторина"))
        builder.row(types.KeyboardButton(text="Полезная информация"))
    else:
        await message.answer('Пожалуйста, отправьте вакансию в виде текста, фото или ссылки')

    await state.clear()


@dp.message(F.text == "Викторина")
@dp.callback_query(lambda callback_query: callback_query.data == 'open_webapp')
async def handle_button1(callback_query: types.CallbackQuery):
    webapp_button = InlineKeyboardButton(text="Пройти викторину",
                                         web_app=WebAppInfo(url=''))
    webapp_kb = InlineKeyboardMarkup(inline_keyboard=[[webapp_button]])
    await bot.send_message(callback_query.from_user.id, 'Нажмите на кнопку ниже, чтобы пройти викторину',
                           reply_markup=webapp_kb)

    await callback_query.answer()
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Рейтинг"))
    builder.row(types.KeyboardButton(text="Полезная информация"))


@dp.message(Command("dk"))
async def delete_keyboard(message: types.Message):
    await message.answer('Ваша клавиатура удалена', reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text == "Рейтинг")
async def users_top(message: types.Message):
    await message.answer('Рейтинг пользователей, которые прошли викторину')
    top_information = top()
    top_text = ""
    c = 0

    for p in top_information:
        c += 1
        if c <= 3:
            top_text += f'{c} место занимает пользователь @{p[0]} с рейтингом {p[1]}\n'
        else:
            top_text += f"Вы занимаете {c} место с рейтингом {p[1]}"
            await message.answer(top_text)
            break


@dp.message(F.text == "Полезная информация")
@dp.callback_query(lambda callback_query: callback_query.data == 'open_webapp')
async def handle_button1(callback_query: types.CallbackQuery):
    webapp_button = InlineKeyboardButton(text="Перейти",
                                         web_app=WebAppInfo(url='https://antidropping.ru'))
    webapp_kb = InlineKeyboardMarkup(inline_keyboard=[[webapp_button]])
    await bot.send_message(callback_query.from_user.id,
                           'Нажмите на кнопку ниже, чтобы перейти на сайт с полезной информацией',
                           reply_markup=webapp_kb)
    await callback_query.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
