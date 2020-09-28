#  (c)2020 JARVIS
#
# You may not use this plugin without proper authorship and consent from @JarvisSupportOt
#
# Creted by @buddhhu, @itzsjdude, @xditya
#
import os, asyncio
from jarvis.utils import admin_cmd

@jarvis.on(admin_cmd(pattern="repack ?(.*)", outgoing=True))

async def _(event):
    a = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    b = open(input_str, 'w')
    b.write(str(a.message))
    b.close()
    a = await event.reply(f"**Packing into** `{input_str}`")
    await asyncio.sleep(2)
    await a.edit(f"**Uploading** `{input_str}`")
    await asyncio.sleep(2)
    await event.client.send_file(event.chat_id, input_str)
    await a.delete()
    os.remove(input_str)