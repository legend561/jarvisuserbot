""" by the @therrs 😎"""

import asyncio

from jarvis.utils import admin_cmd


@jarvis.on(admin_cmd(pattern="watt"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 15)

    await event.edit("watt!!!")

    animation_chars = [".😎", ".😎🤏", ".😳🕶🤏", ".😎", ".😎🤏", ".😳🕶🤏", "Whattt!!!"]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])
