"""Check if your userbot is working."""
import os
import requests
import time
from PIL import Image
from io import BytesIO
from jarvis import ALIVE_NAME
from jarvis.utils import admin_cmd
from datetime import datetime
from jarvis import Lastupdate

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
PM_IMG = "https://telegra.ph/file/d61452c69b961e794eedd.jpg"
pm_caption = "**Master JARVIS AT YOU SERVICE 🤗 **\n"
pm_caption += f"**••Mу Bσѕѕ••**           {DEFAULTUSER}\n"
pm_caption += " **✓ JARVIS STATS ✓** \n"
pm_caption += "  🔸 ➣**Pутнση Vєяѕιση**    `3.8.5`\n"
pm_caption += f"  🔸 ➣**Bσт Vєяѕιση**        `{currentversion}` \n"
pm_caption += f"  🔸 ➣**Dαтαвαѕє**    `{dbstats}` \n"
pm_caption += f"  🔸 ➣**Sυ∂σ**               `{ssudo}` \n"
pm_caption += f"  🔸 ➣**Pм Lσgѕ**        `{pmllogs}` \n"
pm_caption += f"  🔸 ➣**Hєяσкυ**          `{updaterr}` \n"
pm_caption += f"  🔸 ➣**G-Dяινє**           `{wearenoob}`\n\n"
pm_caption += f"  🔸 ➣**UρTιмє**           `{uptime}`\n\n"
pm_caption += " **✓ SUPPORT INFO ✓** \n"
pm_caption += "🔹 ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ    [ᴊᴏɪɴ](https://t.me/jarvisot)\n"
pm_caption += "🔹 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ        [ᴊᴏɪɴ](https://t.me/jarvissupportot)\n"
pm_caption += "🔹 ʟɪᴄᴇɴꜱᴇ                     [GPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jarvisuserbot.gitbook.io/jarvisuserbot/)\n"
pm_caption += "🔹 ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ          [𝙅𝘼𝙍𝙑𝙄𝙎](https://jarvisuserbot.gitbook.io/jarvisuserbot/)\n\n"
pm_caption += "[☆ Git Repo ☆](https://jarvisworks.ga/userbot)"


@jarvis.on(admin_cmd(pattern=r"alive"))
@jarvis.on(admin_cmd(pattern=r"alive", allow_sudo=True))
async def jarvis(alive):
    start = datetime.now()
    myid = bot.uid
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    if ALIVE_PIC :
        await alive.get_chat()
        await borg.send_file(alive.chat_id, ALIVE_PIC, caption=pm_caption, linkpreview=False)
        await alive.delete()
    else :
        await alive.get_chat()
        await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption, linkpreview=False)
        await alive.delete()
