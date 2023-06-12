

import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, VoiceChatStarted, VoiceChatEnded
from AnonX import app

@app.on_message(filters.voice_chat_started)
async def brah(client, message):
       await message.reply("✦︙ تم بدأ محادثة صوتية جديدة.")

@app.on_message(filters.voice_chat_ended)
async def brah2(client, message):
    da = message.voice_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"**✦︙ تم انهاء المحادثة الصوتية مدتها {da} ثواني.**")        
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f"**✦︙ تم انهاء المحادثة الصوتية مدتها دقيقه.**")
        elif 2 <= ma[0] < 3:
            await message.reply(f"**✦︙ تم انهاء المحادثة الصوتية مدتها دقيقتين.**")
        elif 3 <= ma[0] < 11:
            await message.reply(f"**✦︙ تم انهاء المحادثة الصوتية مدتها {ma[0]} دقايق.**")  
        else:
            await message.reply(f"**✦︙ تم إنهاء المحادثة الصوتية مدتها {ma[0]} دقيقه.**") 
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"**✦︙ تم انهاء المحادثة الصوتية مدتها ساعه.**")
        elif 2 <= ho[0] < 3:
            await message.reply(f"**✦︙ تم انهاء المحادثة الصوتية مدتها ساعتين.**")
        elif 3 <= ho[0] < 11:
            await message.reply(f"**✦︙ تم انهاء المحادثة الصوتية مدتها {ho[0]} ساعات.**")  
        else:
            await message.reply(f"**✦︙ تم إنهاء المحادثة الصوتية مدتها {ho[0]} ساعة.**")
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"**✦︙ تم انهاء المحادثة الصوتية مدتها يوم.**")
        elif 2 <= day[0] < 3:
            await message.reply(f"**✦︙ تم انهاء المحادثة الصوتية مدتها يومين.**")
        elif 3 <= day[0] < 11:
            await message.reply(f"**✦︙ تم انهاء المحادثة الصوتية مدتها {day[0]} ايام.**")  
        else:
            await message.reply(f"**✦︙ تم إنهاء المحادثة الصوتية مدتها {day[0]} يوم.**")

async def send_invite(message):
   for x in message.voice_chat_members_invited.users:
       try:
        link = await app.export_chat_invite_link(message.chat.id)
       except:
        link = "البوت ليس ادمن لم استطع انشاء رابط"
       await app.send_message(x.id, f"قام هذا الشخص {message.from_user.mention} \n بدعوتك الي المحادثة الصوتية \nرابط المجموعة : {link}")
