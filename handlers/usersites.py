from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command, CommandStart
from utils.database import DataBase as db
from utils.checksites import check_site_file
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


@router.callback_query(F.data == "file_stats")
async def mysites_callback(call: CallbackQuery):
    sites = db.get_user_links(call.from_user.id)
    if len(sites) == 0:
        await call.message.edit_text("Отакої... Ви ще не додали жодного сайту! Час зробити це саме зараз!", reply_markup=backmain)
    else:
        text = ""
        number = 1
        for link in sites:
            result = await check_site_file(link[0])
            text += f"{number}) {link[0]} - {result}\n\n"
            number = 1 + number
        with open(f"{call.from_user.id}.txt", "w", encoding= "utf_8") as file:
            file.write(text)
        print(text)
        await call.message.answer_document(FSInputFile(f"{call.from_user.id}.txt"))
        await call.message.edit_text(text, reply_markup=backmain)


        