# For @UniBorg
# Courtesy @yasirsiddiqui

"""
.bye
"""
from telethon.tl.functions.channels import LeaveChannelRequest
from jarvis.utils import admin_cmd
import time

@jarvis.on(admin_cmd("bye", outgoing=True , allow_sudo=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I am leaving this chat.....!`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Sir This is Not A Chat`')
