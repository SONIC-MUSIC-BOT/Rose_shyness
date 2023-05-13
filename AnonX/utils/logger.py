from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "⌔︙ المجموعة خاصه"
        logger_text = f"""
⌔︙ **{MUSIC_BOT_NAME} يعمل الان **

⌔︙ **المجموعة : ** {message.chat.title} [`{message.chat.id}`]
⌔︙ **الاسم : ** {message.from_user.mention}
⌔︙ **المعرف : ** @{message.from_user.username}
⌔︙ **الايدي : ** `{message.from_user.id}`
⌔︙ **رابط المجموعة : ** {chatusername}

⌔︙ **تم طلب : ** {message.text}

⌔︙ **المنصة : ** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
