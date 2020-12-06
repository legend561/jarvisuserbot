from telethon.events import ChatAction

from jarvis import sclient
from jarvis.jconfig import Config

'''Bans Spammers/Scammer At time Of Arrival 
If You Add Him The Bot Won't Restrict.'''

@jarvis.on(ChatAction)
async def ok(event):
    if Config.ANTISPAM_FEATURE != "ENABLE":
        return
    if event.user_joined:
        juser = await event.get_user()
        user = sclient.is_banned(juser.id)
        if user.banned == True:
            await event.reply(
                    f"**Jarvis Antispam System Powered By @AntiSpaminc** #ALERT \n**Detected Malicious User.** \n**User-ID :** `{juser.id}`  \n**Reason :** `{user.reason}`"
                )
            try:
                await borg.edit_permissions(
                    event.chat_id, juser.id, view_messages=False
                )
            except:
                pass
        else:
            pass
