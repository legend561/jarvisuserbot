"""Check if your userbot is working."""
import os
import requests
import time
from PIL import Image
from io import BytesIO
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from datetime import datetime

ALV_PIC = os.environ.get("ALIVE_PIC" , None)

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

@borg.on(admin_cmd(outgoing=True, pattern="alive"))
async def amireallyalive(alive):
    start = datetime.now()
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    req = requests.get("https://telegra.ph/file/0670190de8e3bddea6d95.png")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_message(alive.chat_id,"**ᴊᴀʀᴠɪꜱ ɪꜱ ᴏɴʟɪɴᴇ**\n"
                                f"**M̴y̴ ̴B̴o̴s̴s̴**            : {DEFAULTUSER}\n"
                                "Telethon Version         : 4.8\n"
                                "Python Version           : 3.8.5\n"
                                "Bot Version              : 7.0.9\n"
                                "ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ          : [ᴊᴏɪɴ](https://t.me/jarvisot)\n"
                                "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ            : [ᴊᴏɪɴ](https://t.me/jarvissupportot)\n"
                                "ʟɪᴄᴇɴꜱᴇ                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jarvisuserbot.gitbook.io/jarvisuserbot/)\n"
                                "ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ             : [𝙅𝘼𝙍𝙑𝙄𝙎](https://jarvisuserbot.gitbook.io/jarvisuserbot/)\n"
                                "[╔┓┏╦━╦┓╔┓╔━━╗\n║┗┛║┗╣┃║┃║X X║\n║┏┓║┏╣┗╣┗╣╰╯║\n╚┛┗╩━╩━╩━╩━━╝](https://t.me/jarvisot)")        
        await borg.send_file(alive.chat_id, file=sticker) 
        await alive.delete()
