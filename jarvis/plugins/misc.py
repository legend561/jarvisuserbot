# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD

""" Userbot module for other small commands. """

from random import randint
from time import sleep

from jarvis.utils import admin_cmd, sudo_cmd, edit_or_reply
from jarvis import CMD_HNDLR


@jarvis.on(admin_cmd(outgoing=True, pattern="random"))
@jarvis.on(sudo_cmd(allow_sudo=True, pattern="random"))
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    if not items.text[0].isalpha() and items.text[0] not in ("/", "#", "@", "!"):
        itemo = (items.text[8:]).split()
        index = randint(1, len(itemo) - 1)
        await edit_or_reply(items,
            "**Query: **\n`"
            + items.text[8:]
            + "`\n**Output: **\n`"
            + itemo[index]
            + "`"
        )


@jarvis.on(admin_cmd(outgoing=True, pattern="sleep( [0-9]+)?$"))
@jarvis.on(sudo_cmd(allow_sudo=True, pattern="sleep( [0-9]+)?$"))
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    message = time.text
    if not message[0].isalpha() and message[0] not in ("/", "#", "@", "!"):
        if " " not in time.pattern_match.group(1):
            await edit_or_reply(time,f"Syntax: `{CMD_HNDLR}sleep [seconds]`")
        else:
            counter = int(time.pattern_match.group(1))
            await edit_or_reply(time,"`I am sulking and snoozing....`")
            sleep(2)
            if LOGGER:
                await time.client.send_message(
                    LOGGER_GROUP,
                    "You put the bot to sleep for " + str(counter) + " seconds",
                )
            sleep(counter)
