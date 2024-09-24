from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from utils.keyboard import main_kb, settings_kb
from utils.database import DataBase as db
from utils.checksites import check

router = Router()

@router.message(CommandStart())
async def start_cmd(msg: Message):
    db.create_user(msg.from_user.id)
    await msg.answer("Привіт! Я бот, який детектить WP-Content на сайтах вордпресу. Натисни на кнопку 'Додати сайт', аби додати сайт, який потрібно відслідковувати. Натисни на кнопку 'Мої сайти', аби переглянути список сайтів, які потрібно відслідковувати.", reply_markup = main_kb)

@router.message(Command("12"))
async def sdsd(msg: Message, bot: Bot):
    await check(bot)

@router.callback_query(F.data == "settings")
async def settings_callback(call: CallbackQuery):
    silent, pause = db.get_setting_user(call.from_user.id)
    kb = settings_kb(call.from_user.id)
    if silent == 0:
        silent = "🔉<b>Режим тиші:</b> <i>Вимкнуто🔉</i>"
    elif silent == 1:
        silent = "🔇<b>Режим тиші:</b> <i>Ввімкнено🔇</i>"

    if pause == 0:
        pause = "⏸<b>Пауза:</b> <i>Вимкнуто⏸</i>"
    elif pause == 1:
        pause = "⏸<b>Пауза:</b> <i>Ввімкнено⏸</i>"
    await call.message.edit_text(f"{silent}\n{pause}", reply_markup=kb)


@router.callback_query(F.data == "silent_switch")
async def settings_callback(call: CallbackQuery):
    db.switch_silent(call.from_user.id)
    silent, pause = db.get_setting_user(call.from_user.id)
    kb = settings_kb(call.from_user.id)
    if silent == 0:
        silent = "🔉<b>Режим тиші:</b> <i>Вимкнуто🔉</i>"
    elif silent == 1:
        silent = "🔇<b>Режим тиші:</b> <i>Ввімкнено🔇</i>"

    if pause == 0:
        pause = "⏸<b>Пауза:</b> <i>Вимкнуто⏸</i>"
    elif pause == 1:
        pause = "⏸<b>Пауза:</b> <i>Ввімкнено⏸</i>"
    await call.message.edit_text(f"{silent}\n{pause}", reply_markup=kb)

@router.callback_query(F.data == "pause_switch")
async def settings_callback(call: CallbackQuery):
    db.switch_pause(call.from_user.id)
    silent, pause = db.get_setting_user(call.from_user.id)
    kb = settings_kb(call.from_user.id)
    if silent == 0:
        silent = "🔉<b>Режим тиші:</b> <i>Вимкнуто🔉</i>"
    elif silent == 1:
        silent = "🔇<b>Режим тиші:</b> <i>Ввімкнено🔇</i>"

    if pause == 0:
        pause = "⏸<b>Пауза:</b> <i>Вимкнуто⏸</i>"
    elif pause == 1:
        pause = "⏸<b>Пауза:</b> <i>Ввімкнено⏸</i>"
    await call.message.edit_text(f"{silent}\n{pause}", reply_markup=kb)


@router.callback_query(F.data == "mainmenu")
async def back_main(call: CallbackQuery):
    await call.message.edit_text("Привіт! Я бот, який детектить WP-Content на сайтах вордпресу. Натисни на кнопку 'Додати сайт', аби додати сайт, який потрібно відслідковувати. Натисни на кнопку 'Мої сайти', аби переглянути список сайтів, які потрібно відслідковувати.", reply_markup = main_kb)
