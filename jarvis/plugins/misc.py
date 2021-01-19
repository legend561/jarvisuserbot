""" Userjbot module for other small commands. """

from random import randint
from time import sleep

from telethon.tl.types import (
    ChannelParticipantAdmin,
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
)
from telethon.utils import pack_jbot_file_id

from jarvis.utils import admin_cmd, edit_or_reply, eor, sudo_cmd


@jarvis.on(admin_cmd(outgoing=True, pattern="random"))
@jarvis.on(sudo_cmd(allow_sudo=True, pattern="random"))
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    if not items.text[0].isalpha() and items.text[0] not in ("/", "#", "@", "!"):
        itemo = (items.text[8:]).split()
        index = randint(1, len(itemo) - 1)
        await edit_or_reply(
            items,
            "**Query: **\n`"
            + items.text[8:]
            + "`\n**Output: **\n`"
            + itemo[index]
            + "`",
        )


@jarvis.on(admin_cmd(outgoing=True, pattern="sleep( [0-9]+)?$"))
@jarvis.on(sudo_cmd(allow_sudo=True, pattern="sleep( [0-9]+)?$"))
async def sleepyjbot(time):
    """ For .sleep command, let the userjbot snooze for a few second. """
    message = time.text
    if not message[0].isalpha() and message[0] not in ("/", "#", "@", "!"):
        if " " not in time.pattern_match.group(1):
            await edit_or_reply(time, f"Syntax: `{CMD_HNDLR}sleep [seconds]`")
        else:
            counter = int(time.pattern_match.group(1))
            await edit_or_reply(time, "`I am sulking and snoozing....`")
            sleep(2)
            if LOGGER:
                await time.client.send_message(
                    LOGGER_GROUP,
                    "You put the jbot to sleep for " + str(counter) + " seconds",
                )
            sleep(counter)


@jarvis.on(admin_cmd("listjbots", outgoing=True))
@jarvis.on(sudo_cmd("listjbots", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Bots in this Channel**: \n"
    input_str = event.pattern_match.group(1)
    to_write_chat = await event.get_input_chat()
    chat = None
    if not input_str:
        chat = to_write_chat
    else:
        mentions = "Bots in {} channel: \n".format(input_str)
        try:
            chat = await jbot.get_entity(input_str)
        except Exception as e:
            await event.reply(str(e))
            return None
    try:
        async for x in jbot.iter_participants(chat, filter=ChannelParticipantsBots):
            if isinstance(x.participant, ChannelParticipantAdmin):
                mentions += "\n ⚜️ [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
            else:
                mentions += "\n [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
    except Exception as e:
        mentions += " " + str(e) + "\n"
    await event.reply(mentions)


@jarvis.on(admin_cmd("id", outgoing=True))
@jarvis.on(sudo_cmd("id", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            jbot_api_file_id = pack_jbot_file_id(r_msg.media)
            await eor(
                event,
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender.id), jbot_api_file_id
                ),
            )
        else:
            await eor(
                event,
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender.id)
                ),
            )
    else:
        await eor(event, "Current Chat ID: `{}`".format(str(event.chat_id)))


@jarvis.on(admin_cmd("listadmins", outgoing=True))
@jarvis.on(sudo_cmd("listadmins", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Admins in this Channel**: \n"
    should_mention_admins = False
    reply_message = None
    pattern_match_str = event.pattern_match.group(1)
    if "m" in pattern_match_str:
        should_mention_admins = True
        if event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
    input_str = event.pattern_match.group(2)
    to_write_chat = await event.get_input_chat()
    chat = None
    if not input_str:
        chat = to_write_chat
    else:
        mentions_heading = "Admins in {} channel: \n".format(input_str)
        mentions = mentions_heading
        try:
            chat = await jbot.get_entity(input_str)
        except Exception as e:
            await event.reply(str(e))
            return None
    try:
        async for x in jbot.iter_participants(chat, filter=ChannelParticipantsAdmins):
            if not x.deleted:
                if isinstance(x.participant, ChannelParticipantCreator):
                    mentions += "\n 🔱 [{}](tg://user?id={}) `{}`".format(
                        x.first_name, x.id, x.id
                    )
        mentions += "\n"
        async for x in jbot.iter_participants(chat, filter=ChannelParticipantsAdmins):
            if not x.deleted:
                if isinstance(x.participant, ChannelParticipantAdmin):
                    mentions += "\n 🥇 [{}](tg://user?id={}) `{}`".format(
                        x.first_name, x.id, x.id
                    )
            else:
                mentions += "\n `{}`".format(x.id)
    except Exception as e:
        mentions += " " + str(e) + "\n"
    if should_mention_admins:
        if reply_message:
            await reply_message.reply(mentions)
        else:
            await event.reply(mentions)
        await event.delete()
    else:
        await event.reply(mentions)
