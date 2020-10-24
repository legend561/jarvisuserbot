""" Spotify / Deezer downloader plugin by @anubisxx | Syntax: .sdd link"""
import asyncio

from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    YouBlockedUserError,
)
from telethon.tl.functions.messages import ImportChatInviteRequest

from jarvis.utils import admin_cmd


@jarvis.on(admin_cmd("sdd ?(.*)"))
@jarvis.on(admin_cmd(pattern="sdd ?(')", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.reply("` I need a link to download something pro.`**(._.)**")
    else:
        await event.reply("🎶**Initiating Download!**🎶")

    async with borg.conversation("@DeezLoadBot") as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            try:
                await borg(ImportChatInviteRequest("AAAAAFZPuYvdW1A8mrT8Pg"))
            except UserAlreadyParticipantError:
                await asyncio.sleep(0.00000069420)
            await conv.send_message(d_link)
            details = await conv.get_response()
            await borg.send_message(event.chat_id, details)
            await conv.get_response()
            songh = await conv.get_response()
            await borg.send_file(
                event.chat_id,
                songh,
                caption="🔆**Here's the requested song!**🔆\n`Check out` [JARVIS Userbot](https://github.com/Jarvis-Works/JarvisUserbot)",
            )
            await event.delete()
        except YouBlockedUserError:
            await event.reply("**Error:** `unblock` @DeezLoadBot `and retry!`")
