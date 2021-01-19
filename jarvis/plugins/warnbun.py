""".admin Plugin for Jarvis"""
from telethon.tl.types import ChannelParticipantsAdmins

from jarvis.utils import admin_cmd


@jarvis.on(admin_cmd("warn1"))
async def _(event):
    if event.fwd_from:
        return
    mentions = (
        "`You Have  1/3  warnings...\nWatch out!....\nReason for warn: Not given`"
    )
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


""".admin Plugin for jarvis"""
from telethon.tl.types import ChannelParticipantsAdmins

from jarvis.utils import admin_cmd


@jarvis.on(admin_cmd("warn2"))
async def _(event):
    if event.fwd_from:
        return
    mentions = (
        "`You Have  2/3  warnings...\nWatch out!....\nReason for last warn: Not given`"
    )
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


""".admin Plugin for @UniBorg"""
from telethon.tl.types import ChannelParticipantsAdmins

from jarvis.utils import admin_cmd


@jarvis.on(admin_cmd("warn3"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`You Have  3/3  warnings...\nBanned!!!....\nReason for ban: Not given`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


""".admin Plugin for jarvis"""
from telethon.tl.types import ChannelParticipantsAdmins

from jarvis.utils import admin_cmd


@jarvis.on(admin_cmd("warn0"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`Warning Resetted By Admin...\nYou Have  0/3  warnings`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
