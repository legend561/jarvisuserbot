from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from jarvis.utils import admin_cmd,sudo_cmd,edit_or_reply


@jarvis.on(admin_cmd(pattern="ctg ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="ctg ?(.*)",allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event,"```Reply to a Link.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await edit_or_reply(event,"```Reply to a Link```")
        return
    chat = "@chotamreaderbot"
    reply_message.sender
    await edit_or_reply(event,```Processing```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`RIP Check Your Blacklist Boss`")
            return
        if response.text.startswith(""):
            await event.edit("Am I Dumb Or Am I Dumb?")
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)
