import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app

import re
import sys
from os import getenv

from dotenv import load_dotenv
#

load_dotenv()

OWNER_ID = getenv("OWNER_ID")

KIMMY = getenv("KIMMY")

OWNER = getenv("OWNER")


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

            
@app.on_message(
    command(["سورس سونك","سورس","السورس","سونك سورس", "source"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b5281f70c4dc630ee3e62.jpg",
        caption=f"""
╭──── • ◈ • ────╮ 

⌔︙معلومات السورس

⌔︙[سورس سونك](https://t.me/SONIC_source)

⌔︙[حسين مطور السورس](https://t.me/Huseenytiq)

⌔︙[مساعدة مطور السورس](https://t.me/MZ_864)

⌔︙[بوت تواصل السورس](https://t.me/Huseenytiq_bot)

⌔︙[مجموعة الدعم](https://t.me/SONIC_source_SUPPORT)

⌔︙[✲°• منتدى منارة القانتين •°✲](https://t.me/Manarat_Alqaniten)

╰──── • ◈ • ────╯ 
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطور السورس", url=f"https://t.me/Huseenytiq"), 
                ],[
                    InlineKeyboardButton(
                        "مساعدة مطور السورس", url=f"https://t.me/MZ_864"),
                ],[
                    InlineKeyboardButton(
                        "𝗦𝗢𝗡𝗜𝗖 𝗦𝗢𝗨𝗥𝗖𝗘 ⚡", url=f"https://t.me/SONIC_source"),
                ],[
                    InlineKeyboardButton(
                        "✲°• منتدى منارة القانتين •°✲", url=f"t.me/Manarat_Alqaniten"),
                ],

            ]

        ),

    )


@app.on_message(
    command(["حسين صلاح","مالك السورس","مبرمج","مطور السورس","المبرمج","المطور الاساسي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("Huseenytiq")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌔︙ معلومات مطور السورس\n\n⌔︙ الاسم :{name}\n⌔︙ المعرف :@{usr.username}\n⌔︙ الايدي :`{usr.id}`\n⌔︙ البايو :{usr.bio}**",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )





@app.on_message(
    command(["مطور","مطور البوت","المطور"])
    & filters.group
    & ~filters.edited
)
async def KIMMY(client: Client, message: Message):
    usr = await client.get_users(OWNER)
    name = usr.first_name
    async for photo in client.iter_profile_photos(OWNER, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**⌔︙ معلومات المطور**
                    
⌔︙ المطور :[{usr.first_name}](https://t.me/{OWNER})
⌔︙ المعرف :@{OWNER} 
⌔︙ الايدي :`{usr.id}`
⌔︙ البايو : {usr.bio}
** 𝗦𝗢𝗡𝗜𝗖 𝗦𝗢𝗨𝗥𝗖𝗘 ⚡** """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{OWNER}")
            ],                   
          ]              
       )                 
    )                    
                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    await app.send_message(OWNER, f"⌔︙  {message.from_user.mention} بحاجه اليك \n\n⌔︙ ايديه : {sender_id} \n\n⌔︙ اسمه : {sender_name}")
                    return await app.send_message(config.LOG_GROUP_ID, f"⌔︙  {message.from_user.mention} بحاجه اليك \n\n⌔︙ ايديه : {sender_id} \n\n⌔︙ اسمه : {sender_name}")


@app.on_message(command("تحويل لصوره"))
async def elkatifh(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("⌔︙ قم بالرد على ملصق")
    if not reply.sticker:
        return await message.reply("⌔︙ قم بالرد على ملصق.")
    m = await message.reply("⌔︙ يتم المعالجه..")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)



