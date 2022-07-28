from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd


@jarvis.on(j_cmd("mask ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd("mask ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "```reply to text message```")
        return
    chat = "@hazmat_suit_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "```Reply to actual users message.```")
        return
    await edit_or_reply(event, "```Processing```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await jarvis.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await jarvis.send_file(event.chat_id, response.message.media)
