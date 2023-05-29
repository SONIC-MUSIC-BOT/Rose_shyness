from pyrogram.types import InlineKeyboardButton
import config
from config import YAFA_CHANNEL, YAFA_NAME

def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="مجموعة الدعم", url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{YAFA_NAME}", url=f"{YAFA_CHANNEL}",
            )
        ],
    ]
    return buttons
