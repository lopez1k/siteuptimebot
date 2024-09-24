from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.database import DataBase as db

main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Додати сайт", callback_data="add_site")
        ],
        [
            InlineKeyboardButton(text = "Мої сайти", callback_data="mysites")
        ],
        [
            InlineKeyboardButton(text = "⚙️Налаштування", callback_data='settings')
        ]
    ]
)


def settings_kb(uid):
    silent, pause = db.get_setting_user(uid)
    if silent == 0:
        silent = 'Ввімкнути режим тиші'
    elif silent == 1:
        silent = 'Вимкнути режим тиші'
    
    if pause == 0:
        pause = "Ввімкнути паузу"
    elif pause == 1:
        pause = "Вимкнути паузу"

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=silent, callback_data=f"silent_switch")  
            ],
            [
                InlineKeyboardButton(text=pause, callback_data=f"pause_switch")  
            ],
            [
                InlineKeyboardButton(text = "⬅️Назад", callback_data='mainmenu')
            ]
        ]
    )
    return kb

backmain = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Видалити посилання", callback_data = "delete_site")
        ],
        [
            InlineKeyboardButton(text = "⬅️Назад", callback_data='mainmenu')
        ]
    ]
)