#  (c)2020 Jarvis-Works
#
# You may not use this plugin without proper authorship and consent from @JarvisSupportOt
#
# By @buddhhu, @Itzsjdude ,@xditya
#
import os

from jarvis.utils import admin_cmd, eor, sudo_cmd


@jarvis.on(admin_cmd(pattern=r"reveal", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"reveal", allow_sudo=True))
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    d = await eor(event, "**Reading file...**")
    await event.delete()
    if len(c) > 4095:
        await d.edit("`The Total words in this file is more than telegram limits.`")
    else:
        await event.client.send_message(event.chat_id, f"```{c}```")
    os.remove(b)
