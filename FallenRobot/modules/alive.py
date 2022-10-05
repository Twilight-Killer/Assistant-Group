import random

from pyrogram import __version__ as pyrover
from telegram import __version__ as telever
from telethon import Button
from telethon import __version__ as tlhver

from FallenRobot import OWNER_USERNAME, SUPPORT_CHAT, dispatcher
from FallenRobot import telethn as tbot
from FallenRobot.events import register

PHOTO = [
    "https://telegra.ph/file/b39e49873f77e4737d622.jpg",
    "https://telegra.ph/file/b39e49873f77e4737d622.jpg",
]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"`Hay​` [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n`Saya` {dispatcher.bot.first_name} \n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» `Developer`​ : [DarkiezZzz](https://t.me/{OWNER_USERNAME}) \n\n"
    TEXT += f"» `Library versi :` `{telever}` \n\n"
    TEXT += f"» `Telethon versi :` `{tlhver}` \n\n"
    TEXT += f"» `Pyrogram versi :` `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", f"https://t.me/{dispatcher.bot.username}?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


__mod_name__ = "Aʟɪᴠᴇ"
