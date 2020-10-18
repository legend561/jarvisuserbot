"""Emoji

Available Commands:

.ok"""

from telethon import events
import asyncio
from jarvis.utils import jarvis_cmd

@jarvis.on(jarvis_cmd("ok"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "ok":
    await event.edit("ok")
    animation_chars = [
            "OK",
            "BOSS",
            "OK MAN",
            "OK BITCH",
            "OK IDIOT",
            "OK MAM",
            "OK SIR",
            "GO AND SAY OK",
            "OK LOL",
            "YAA OK",
            "OK",
            "Boss",
            "Yeahhhhhh",
            "O",
            "K",
            "Ok Boss! 😇"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
