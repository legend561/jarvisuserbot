from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd


@jarvis.on(admin_cmd(pattern="purl ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="purl ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@FiletolinkTGbot"
    reply_message.sender
    await edit_or_reply(event, "**Making public url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1011636686)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await edit_or_reply(
                event, "```Please unblock me (@FiletolinkTGbot) u Nigga```"
            )
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@jarvis.on(admin_cmd(pattern="sang ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="sang ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "**Reply to an user message.**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("**Reply to a message.**")
        return
    chat = "@sangmatainfo_bot"
    reply_message.sender
    await event.edit("**Getting user's name history..**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock me (@SangMataInfo_bot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@jarvis.on(admin_cmd(pattern="reader ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="reader ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "**Reply to a URL.**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("**Reply to a url message.**")
        return
    chat = "@CorsaBot"
    reply_message.sender
    await event.edit("**Making instant view...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock me (@CorsaBot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )
