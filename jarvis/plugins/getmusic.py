# modified for jarvis by @sppidy
import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd


@jarvis.on(admin_cmd("smd (.*)", outgoing=True))
@jarvis.on(sudo_cmd("smd (.*)",allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    await edit_or_reply(event, "```Getting Your Music```")
    async with bot.conversation(chat) as conv:
        await event.delete()
        await asyncio.sleep(2)
        await event.edit(
            "`Downloading Music \nIt may take some time\n   So Stay Tuned.....`"
        )
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=752979930)
            )
            await bot.send_message(chat, name)
            respond = await response
        except YouBlockedUserError:
            await event.edit(
                "```Please unblock @SpotifyMusicDownloaderBot and try again```"
            )
            return
        await event.delete()
        await bot.forward_messages(event.chat_id, respond.message)
