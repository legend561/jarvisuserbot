#  (c)2020 Jarvis-Works
#
# You may not use this plugin without proper authorship and consent from @JarvisSupportOt
#
# Creted by @buddhhu, @itzsjdude, @xditya
#
import asyncio
import os

from jarvis.utils import j_cmd, eor, sudo_cmd


@jarvis.on(j_cmd(pattern="repack ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="repack ?(.*)", allow_sudo=True))
async def _(event):
    jevent = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    b = open(input_str, "w")
    b.write(str(a.message))
    b.close()
    jevent = await eor(event, f"**Packing into** `{input_str}`")
    await asyncio.sleep(2)
    await jevent.edit(f"**Uploading** `{input_str}`")
    await asyncio.sleep(2)
    await jevent.client.send_file(event.chat_id, input_str)
    await event.delete()
    os.remove(input_str)
