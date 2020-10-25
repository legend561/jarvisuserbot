"""Emoji

Available Commands:

.deploy"""


import asyncio

from jarvis import ALIVE_NAME
from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "jarvis"


@jarvis.on(admin_cmd(pattern=r"deploy", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"deploy", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 10

    animation_ttl = range(0, 12)

    # input_str = event.pattern_match.group(1)

    await edit_or_reply(event, "Deploying...")

    animation_chars = [
        "**Heroku Connecting To Latest Github Build (Jarvis-Works/JarvisUserbot)**",
        "**Build started by user** **{DEFAULTUSER}**",
        "**Deploy** `535a74f0` **by user** **{DEFAULTUSER}**",
        "**Restarting Heroku Server...**",
        "**State changed from up to starting**",
        "**Stopping all processes with SIGTERM**",
        "**Process exited with** `status 143`",
        "**Starting process with command** `python3 -m jarvis`",
        "**State changed from starting to up**",
        "__INFO:Jarvis:Logged in as 557667062__",
        "__INFO:Jarvis:Successfully loaded all plugins__",
        "**Build Succeeded**",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])
