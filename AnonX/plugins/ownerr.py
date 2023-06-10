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
⌔︙معلومات السورس

⌔︙[سورس سونك](https://t.me/SONIC_source)

⌔︙[حسين مطور السورس](https://t.me/Huseenytiq)

⌔︙[مساعدة مطور السورس](https://t.me/MZ_864)

⌔︙[بوت تواصل السورس](https://t.me/Huseenytiq_bot)

⌔︙[مجموعة الدعم](https://t.me/SONIC_source_SUPPORT)

⌔︙[✲°• منتدى منارة القانتين •°✲](https://t.me/Manarat_Alqaniten)
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
    command(["حسين صلاح","مالك السورس","حسين مطور السورس","مبرمج","مطور السورس","المبرمج","المطور الاساسي"])
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("Huseenytiq")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌔︙معلومات مطور السورس\n\n⌔︙الاسم : {name}\n⌔︙المعرف : @{usr.username}\n⌔︙الايدي : `{usr.id}`\n⌔︙البايو : {usr.bio}**",  
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
    command(["المطورة","المطوره","أولسنا على الحق","العلوية","مساعده مطور السورس","مساعدة مطور السورس","العلويه","مساعدة المطور الاساسي"])
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("MZ_864")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌔︙معلومات مساعدة مطور السورس\n\n⌔︙الاسم : {name}\n⌔︙المعرف : @{usr.username}\n⌔︙الايدي : `{usr.id}`\n⌔︙البايو : {usr.bio}**", 
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
    command(["مناره القانتين","مناره","منارة القانتين","منارة","مطور","المطور "])
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("manaratalqanitin")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌔︙ معلومات المطور\n\n⌔︙الاسم : {name}\n⌔︙المعرف : @{usr.username}\n⌔︙الايدي : `{usr.id}`\n⌔︙البايو : {usr.bio}**",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )

