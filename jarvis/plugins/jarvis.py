from telethon.errors.rpcerrorlist import YouBlockedUserError

from jarvis import ALIVE_NAME
from jarvis.utils import admin_cmd

naam = str(ALIVE_NAME)

bot = "@jarvisotbot"


@jarvis.on(admin_cmd("jarvis ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)

    if sysarg == "hello":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("hello")
                audio = await conv.get_response()
                await borg.send_file(
                    event.chat_id,
                    audio,
                    caption="⚡Boss Listen To This Audio"
                    + naam
                    + "\n`Check out` [JARVIS](https://github.com/jarvis210904/JARVISuserbot)",
                )
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @jarvisotbot `and retry!")
    elif sysarg == "help":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("help me")
                audio = await conv.get_response()
                await borg.send_file(
                    event.chat_id,
                    audio,
                    caption="**Check Out Sir**\n`Check out` [JARVIS](https://github.com/jarvis210904/J.A.R.V.I.S-Userbot)",
                )
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @jarvisotbot `and retry!`")
    elif sysarg == "movies":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/movies")
                audio = await conv.get_response()
                await borg.send_file(
                    event.chat_id,
                    audio,
                    caption="**Here is Movie**\n`Check out` [JARVIS](https://github.com/jarvis210904/J.A.R.V.I.S-Userbot)",
                )
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @jarvisotbot `and retry!`")
    elif sysarg == "song":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/music")
                audio = await conv.get_response()
                await borg.send_file(
                    event.chat_id,
                    audio,
                    caption="**Hoi ! Here iz music**\n`Check out` [JARVIS](https://github.com/jarvis210904/J.A.R.V.I.S-Userbot)",
                )
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @jarvisotbot `and retry!`")
    elif sysarg == "meme":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/meme")
                audio = await conv.get_response()
                await borg.send_file(
                    event.chat_id,
                    audio,
                    caption="**Lol**\n`Check out` [JARVIS](https://github.com/jarvis210904/J.A.R.V.I.S-Userbot)",
                )
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @jarvisotbot `and retry!`")
    elif sysarg == "nord":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/nord")
                audio = await conv.get_response()
                await borg.send_file(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @jarvisotbot `and retry!`")
    elif sysarg == "cc":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/cc")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @jarvisotbot `and retry!`")
    else:
        await brog.send_message(
            event.chat_id, "**INVALID** -- FOR HELP COMMAND IS **hcc help**"
        )
        await event.delete()
