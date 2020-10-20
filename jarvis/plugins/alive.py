"""Check if your userbot is working."""
import os
import requests
import time
from PIL import Image
from io import BytesIO
from jarvis import ALIVE_NAME
from jarvis.utils import admin_cmd
from datetime import datetime

sudousing = Config.SUDO_USERS
pmlogss = Config.PM_LOGGR_BOT_API_ID
isdbfine = Var.DB_URI
updaterok = Var.HEROKU_APP_NAME
gdriveisshit = Config.AUTH_TOKEN_DATA
currentversion = "3.2"

if sudousing:
    ssudo = "Enabled "
else:
    ssudo = "Disabled"

if pmlogss:
    pmllogs = "Enabled"
else:
    pmllogs = "Disabled"

if updaterok:
    updaterr = "Enabled"
else:
    updaterr = "Disabled"

if gdriveisshit:
    wearenoob = "Enabled"
else:
    wearenoob = "Disabled"

if isdbfine:
    dbstats = "All Fine 😉👍🏻"
else:
    dbstats = "Not Fine"

ALIVE_PIC = os.environ.get("ALIVE_PIC" , None)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

@jarvis.on(admin_cmd(outgoing=True, pattern="alive"))
@jarvis.on(admin_cmd(pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PIC:
        pm_caption = "**ᴊᴀʀᴠɪꜱ ɪꜱ ᴏɴʟɪɴᴇ**\n"
        pm_caption += f"**M̴y̴ ̴B̴o̴s̴s̴**            : {DEFAULTUSER}\n"
        pm_caption += "🔵 Pутнση Vєяѕιση           : 3.8.5\n"
        pm_caption += "🔵 Bσт Vєяѕιση              : 7.0.9\n"
        pm_caption += "🔵 ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ          : [ᴊᴏɪɴ](https://t.me/jarvisot)\n"
        pm_caption += "🔵 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ            : [ᴊᴏɪɴ](https://t.me/jarvissupportot)\n"
        pm_caption += "🔵 ʟɪᴄᴇɴꜱᴇ                  : [GPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jarvisuserbot.gitbook.io/jarvisuserbot/)\n"
        pm_caption += "🔵 ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ             : [𝙅𝘼𝙍𝙑𝙄𝙎](https://jarvisuserbot.gitbook.io/jarvisuserbot/)\n\n"
        pm_caption += " **✓ JARVIS STATS ✓** \n"
        pm_caption += f"  • ➣**VERSION**            : `{currentversion}` \n"
        pm_caption += f"  • ➣**DATABASE**           : `{dbstats}` \n"
        pm_caption += f"  • ➣**SUDO**               : `{ssudo}` \n"
        pm_caption += f"  • ➣**PM LOGS**            : `{pmllogs}` \n"
        pm_caption += f"  • ➣**HEROKU**             : `{updaterr}` \n"
        pm_caption += f"  • ➣**G-DRIVE**            : `{wearenoob}`\n\n"
        pm_caption += "[Git Repo](https://jarvisworks.ga/userbot)"
        chat = await alive.get_chat()
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        await jarvis.send_file(alive.chat_id, ALIVE_PIC,caption=pm_caption, link_preview = False)
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/c7b581aac71e7bda597f7.png")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await jarvis.send_file(alive.chat_id, file=sticker)
        await jarvis.send_message(alive.chat_id,"**ᴊᴀʀᴠɪꜱ ɪꜱ ᴏɴʟɪɴᴇ**\n"
                                  f"**M̴y̴ ̴B̴o̴s̴s̴**            : {DEFAULTUSER}\n"
                                  "🔵 Pутнση Vєяѕιση           : 3.8.5\n"
                                  "🔵 Bσт Vєяѕιση              : 7.0.9\n"
                                  "🔵 ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ          : [ᴊᴏɪɴ](https://t.me/jarvisot)\n"
                                  "🔵 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ            : [ᴊᴏɪɴ](https://t.me/jarvissupportot)\n"
                                  "🔵 ʟɪᴄᴇɴꜱᴇ                  : [GPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jarvisuserbot.gitbook.io/jarvisuserbot/)\n"
                                  "🔵 ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ             : [𝙅𝘼𝙍𝙑𝙄𝙎](https://jarvisuserbot.gitbook.io/jarvisuserbot/)\n\n"
                                  " **✓ JARVIS STATS ✓** \n"
                                  f"  • ➣**VERSION**            : `{currentversion}` \n"
                                  f"  • ➣**DATABASE**           : `{dbstats}` \n"
                                  f"  • ➣**SUDO**               : `{ssudo}` \n"
                                  f"  • ➣**PM LOGS**            : `{pmllogs}` \n"
                                  f"  • ➣**HEROKU**             : `{updaterr}` \n"
                                  f"  • ➣**G-DRIVE**            : `{wearenoob}`\n\n"
                                  "[Git Repo](https://jarvisworks.ga/userbot)" 
    await alive.delete()
