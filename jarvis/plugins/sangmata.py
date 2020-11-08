from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from jarvis.utils import admin_cmd, eor, sudo_cmd


@jarvis.on(admin_cmd("sg ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd("sg ?(.*)", allow_sudo=True))
async def _(event):

    if event.fwd_from:
        
        if not event.reply_to_msg_id:
            jevent = await eor(event, "```Reply to any user message.```")
            reply_message = await event.get_reply_message()
        if not reply_message.text:
            await jevent.edit("```reply to text message```")
        chat = "@SangMataInfo_bot"
        reply_message.sender
        if reply_message.sender.bot:
            await jevent.edit("```Reply to actual users message.```")
            await jevent.edit("```Processing```")
            async with borg.conversation(chat) as conv:
                try:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=461843263))
                    await borg.forward_messages(chat, reply_message)
                    response = await response
                except YouBlockedUserError:
                    await jevent.edit("```Please unblock @sangmatainfo_bot and try again```")
                    return
        if response.text.startswith("Forward"):
            await jevent.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await jevent.edit(f"{response.message.message}")
