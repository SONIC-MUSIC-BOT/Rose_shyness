from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="أضفني الى مجموعتك",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="الاوامر",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="الاعدادات", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="أضفني الى مجموعتك",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="الاوامر", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="مجموعة الدعم", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="المطور", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="✲°• منتدى منارة القانتين •°✲", url="https://t.me/Manarat_Alqaniten" 
            )
        ],
     ]
    return buttons
