from telethon import events
import asyncio
import os
import sys
from jarvis.utils import jarvis_cmd

@jarvis.on(jarvis_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit("Test Successfull. Boss !")
