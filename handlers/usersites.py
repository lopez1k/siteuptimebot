from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from utils.database import DataBase as db
from utils.keyboard import backmain
router = Router()

@router.callback_query(F.data == "mysites")
async def mysites_callback(call: CallbackQuery):
    sites = db.get_user_links(call.from_user.id)
    if len(sites) == 0:
        await call.message.edit_text("Отакої... Ви ще не додали жодного сайту! Час зробити це саме зараз!", reply_markup=backmain)
    else:
        text = ""
        number = 1
        for link in sites:
            text += f"<b>{number})</b> <code>{link[0]}</code>\n\n"
            number = 1 + number
        await call.message.edit_text(text, reply_markup=backmain)