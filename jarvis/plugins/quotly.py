"""QuotLy: Avaible commands: .qbot
"""
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from jarvis import jarvisub
from jarvis.utils import j_cmd, eor, sudo_cmd


# @register(outgoing=True, pattern="^.q(?: |$)(.*)")
@jarvis.on(j_cmd(pattern=r"qbot(?: |$)(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"qbot(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        wartime = await eor(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        wartime = await eor(event, "```Reply to text message```")
        return
    chat = "@QuotLyBot"
    reply_message.sender
    wartime = await eor(
        event, "```Making a Quote```"
    )  # J.A.R.V.I.S play "Its HAPPENS only in India" Xd
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await jarvis.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await wartime.edit("```Please unblock @QuotLyBot and try again```")
            return
        if response.text.startswith("Hi!"):
            await wartime.edit(
                "```Can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await wartime.delete()
            await jarvis.forward_messages(event.chat_id, response.message)
