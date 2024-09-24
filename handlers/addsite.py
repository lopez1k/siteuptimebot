from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from utils.keyboard import main_kb
from utils.database import DataBase as db
from utils.checksites import check_site


router = Router()

class AddSite(StatesGroup):
    wait_for_site = State()

@router.callback_query(F.data == "add_site")
async def add_site_1step(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Відправте посилання на веб-сайт, який потрібно відслідковувати")
    await state.set_state(AddSite.wait_for_site)


@router.message(AddSite.wait_for_site)
async def add_site_2step(msg: Message, state: FSMContext):
    text = await check_site(msg.text)
    await msg.answer(text = text, reply_markup = main_kb)
    db.add_site(msg.from_user.id, msg.text)
    await state.clear()



class DelSite(StatesGroup):
    wait_for_site = State()

@router.callback_query(F.data == "delete_site")
async def add_site_1step(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Відправте посилання на веб-сайт, який потрібно видалити")
    await state.set_state(DelSite.wait_for_site)


@router.message(DelSite.wait_for_site)
async def add_site_2step(msg: Message, state: FSMContext):
    await msg.answer(text = "Чудово!", reply_markup = main_kb)
    db.del_site(msg.from_user.id, msg.text)
    await state.clear()