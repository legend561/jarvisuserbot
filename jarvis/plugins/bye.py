# For @UniBorg
# Courtesy @yasirsiddiqui

"""
.bye
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd


@jarvis.on(j_cmd("bye", outgoing=True))
@jarvis.on(sudo_cmd("bye", allow_sudo=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(e, "`I am leaving this chat.....!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await jarvis.LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("`Sir This is Not A Chat`")
