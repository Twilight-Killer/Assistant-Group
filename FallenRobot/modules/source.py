from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from FallenRobot import OWNER_USERNAME, dispatcher
from FallenRobot import pbot as client

ANON = "https://telegra.ph/file/1e52aeabec63b21b2b534.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**Hai​ {message.from_user.mention()},\n\nSaya [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

**» Developer​ :** [DarkiezZzz](tg://user?id=1128130156)
**» Python versi :** `{y()}`
**» Library versi :** `{o}` 
**» Telethon versi :** `{s}` 
**» Pyrogram versi :** `{z}`

**Saya dibuat khusus untuk mengelolah grup. jika berminat hubungi owner saya.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Owner •", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                    InlineKeyboardButton(
                        "• Source •",
                        url="t.me/DarkiezZzz",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
