# modified for FRIDAY by @WhySooSerious
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import asyncio
from jarvis.utils import admin_cmd


@jarvis.on(admin_cmd("smd (.*)"))
@jarvis.on(admin_cmd(pattern="smd (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    await event.reply("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
    await event.delete()
          await asyncio.sleep(2)
          await event.reply("`Downloading Music \nIt may take some time\n   So Stay Tuned.....`")
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=752979930))
              await bot.send_message(chat, name)
              respond = await response
          except YouBlockedUserError:
              await event.reply("```Please unblock @SpotifyMusicDownloaderBot and try again```")
              return
          await event.delete()
          await bot.forward_messages(event.chat_id, respond.message)
