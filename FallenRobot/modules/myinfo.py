import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from FallenRobot import telethn as bot
from FallenRobot import telethn as tgbot
from FallenRobot.events import register

edit_time = 5
""" =======================HAOTOGEL OFFICIAL====================== """
file1 = "https://telegra.ph/file/35c7e093808029b04cc89.jpg"
file2 = "https://telegra.ph/file/a18854e60e366b849483d.jpg"
file3 = "https://telegra.ph/file/10ff969e26ab697dc0ada.jpg"
file4 = "https://telegra.ph/file/8023717fe0c53948a2e5a.jpg"
file5 = "https://telegra.ph/file/0e9f6b1968f7a81c7be93.jpg"
""" =======================HAOTOGEL OFFICIAL====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("Klik", data="informations")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"Hey {firstname},\nKlik tombol di bawah ini\nUntuk mendapatkan info tentang Kamu",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        LILIE = "POWERED BY : DarkiezZzz \n\n"
        LILIE += f"NAMA DEPAN : {PRO.first_name} \n"
        LILIE += f"NAMA BELAKANG : {PRO.last_name}\n"
        LILIE += f"KAMU BOT : {PRO.bot} \n"
        LILIE += f"DIBATASI : {PRO.restricted} \n"
        LILIE += f"USER ID : {boy}\n"
        LILIE += f"USERNAME : {PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__command_list__ = ["myinfo"]
