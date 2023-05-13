from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import YAFA_CHANNEL, YAFA_NAME

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text= "‹ الاوامر العربية ›",
                    callback_data="help_callback hb13",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• المشرفين •",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="• المعتمدين •",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="• الحظر •",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• الاذاعة •",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="• مجموعه •",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="• كلمات •",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• السرعه •",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="• التشغيل •",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="قائمة التشغيل",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• المكالمات •",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="• اضافية •",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="• المطور •",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="• الاوامر •",
                callback_data="settings_back_helper",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{YAFA_NAME}", url=f"{YAFA_CHANNEL}",
            )
        ],
    ]
    return buttons
