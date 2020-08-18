""" by the @therrs 😎"""

from telethon import events
from uniborg.util import admin_cmd
import asyncio





@borg.on(admin_cmd(pattern="watt"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1
    

    animation_ttl = range(0, 15)

    

  

    await event.edit("watt!!!")

    animation_chars = [

            ".😎",
            ".😎🤏",
            ".😳🕶🤏",
            ".😎",
            ".😎🤏",
            ".😳🕶🤏",
            "wattt!!!"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])
