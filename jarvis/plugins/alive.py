"""Check if your userbot is working."""
import os
import time
from datetime import datetime

from jarvis import ALIVE_NAME, Lastupdate
from jarvis.utils import j_cmd, sudo_cmd

sudousing = Config.SUDO_USERS
pmlogss = Config.PM_LOGGR_BOT_API_ID
isdbfine = Var.DB_URI
updaterok = Var.HEROKU_APP_NAME
currentversion = "0.2"

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

if isdbfine:
    dbstats = "All Fine 😉👍🏻"
else:
    dbstats = "Not Fine"

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)


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


@jarvis.on(j_cmd(pattern=r"alive"))
@jarvis.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def jarvis(alive):
    if alive.fwd_from:
        return
    start = datetime.now()
    jarvisub.uid
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    if ALIVE_PIC:
        pm_caption = "**Jarvis Is Alive 🤗 **\n"
        pm_caption += f"**••Mу Bσѕѕ••**           {DEFAULTUSER}\n"
        pm_caption += " **✓ JARVIS STATS ✓** \n"
        pm_caption += "  🔸 ➣**Pутнση Vєяѕιση**    `3.8.5`\n"
        pm_caption += f"  🔸 ➣**Bσт Vєяѕιση**        `{currentversion}` \n"
        pm_caption += f"  🔸 ➣**Dαтαвαѕє**    `{dbstats}` \n"
        pm_caption += f"  🔸 ➣**Sυ∂σ**               `{ssudo}` \n"
        pm_caption += f"  🔸 ➣**Pм Lσgѕ**        `{pmllogs}` \n"
        pm_caption += f"  🔸 ➣**Hєяσкυ**          `{updaterr}` \n"
        pm_caption += f"  🔸 ➣**UρTιмє**           `{uptime}`\n\n"
        pm_caption += "[☆ Git Repo ☆](https://jarvisworks.ga/userbot)"
        await alive.get_chat()
        await jarvis.send_file(
            alive.chat_id, ALIVE_PIC, caption=pm_caption, linkpreview=False
        )
        await alive.delete()
    else:
        PM_IMG = "https://telegra.ph/file/d61452c69b961e794eedd.jpg"
        pm_captionn = "**Master JARVIS AT YOU SERVICE 🤗 **\n"
        pm_captionn += f"**••Mу Bσѕѕ••**           {DEFAULTUSER}\n"
        pm_captionn += " **✓ JARVIS STATS ✓** \n"
        pm_captionn += "  🔸 ➣**Pутнση Vєяѕιση**    `3.8.5`\n"
        pm_captionn += f"  🔸 ➣**Bσт Vєяѕιση**        `{currentversion}` \n"
        pm_captionn += f"  🔸 ➣**Dαтαвαѕє**    `{dbstats}` \n"
        pm_captionn += f"  🔸 ➣**Sυ∂σ**               `{ssudo}` \n"
        pm_captionn += f"  🔸 ➣**Pм Lσgѕ**        `{pmllogs}` \n"
        pm_captionn += f"  🔸 ➣**Hєяσкυ**          `{updaterr}` \n"
        pm_captionn += f"  🔸 ➣**UρTιмє**           `{uptime}`\n\n"
        pm_captionn += "[☆ Git Repo ☆](https://jarvisworks.ga/userbot)"
        await alive.get_chat()
        await jarvis.send_file(
            alive.chat_id, PM_IMG, caption=pm_captionn, linkpreview=False
        )
        await alive.delete()
