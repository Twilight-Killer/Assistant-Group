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
file1 = "https://te.legra.ph/file/e99b18a59987bc94d8a00.jpg"
file2 = "https://te.legra.ph/file/e99b18a59987bc94d8a00.jpg"
file3 = "https://te.legra.ph/file/286ecf92083b9fbdee502.jpg"
file4 = "https://te.legra.ph/file/a9a7e32b03de74be666e1.jpg"
file5 = "https://te.legra.ph/file/eba78dc0cf93fd38a9313.jpg"
""" =======================HAOTOGEL OFFICIAL====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("informasi", data="informations")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"Hey {firstname}, \n Klik tombol di bawah ini \n untuk mendapatkan info tentang Kamu",
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
        LILIE = "POWERED BY DarkiezZzz \n\n"
        LILIE += f"FIRST NAME : {PRO.first_name} \n"
        LILIE += f"LAST NAME : {PRO.last_name}\n"
        LILIE += f"YOU BOT : {PRO.bot} \n"
        LILIE += f"RESTRICTED : {PRO.restricted} \n"
        LILIE += f"USER ID : {boy}\n"
        LILIE += f"USERNAME : {PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__command_list__ = ["myinfo"]
