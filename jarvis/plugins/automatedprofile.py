import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions

from jarvis.utils import j_cmd, eor, sudo_cmd

DEL_TIME_OUT = 60


@jarvis.on(j_cmd(pattern="bio"))  # pylint:disable=E0602
@jarvis.on(sudo_cmd(pattern="bio", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | User Of JarvisUserbot 😎 | ⌚️ {HM}"
        logger.info(bio)
        try:
            await jarvis(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    about=bio
                )
            )
            await eor(event, "Autobio Enabled !!")
            await asyncio.sleep(2)
            await event.delete()
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
        # logger.info(r.stringify())
        # await jarvis.send_message(  # pylint:disable=E0602
        # Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
        # "Successfully Changed Profile Bio"
        # )
        await asyncio.sleep(DEL_TIME_OUT)


import asyncio
import os
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

from jarvis.utils import j_cmd, sudo_cmd

FONT_FILE_TO_USE = "fonts/digital.ttf"


@jarvis.on(j_cmd(pattern=r"autopic"))
@jarvis.on(sudo_cmd(pattern=r"autopic", allow_sudo=True))
async def autopic(event):
    if event.fwd_from:
        return
    downloaded_file_name = "jarvis/original_pic.png"
    downloader = SmartDL(
        Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False
    )
    downloader.start(blocking=False)
    photo = "jarvis/photo_pfp.png"
    while not downloader.isFinished():
        pass
    counter = -30
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime("%H:%M")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 50)
        drawn_text.text((95, 250), current_time, font=fnt, fill=(124, 252, 0))
        img.save(photo)
        file = await jarvis.upload_file(photo)  # pylint:disable=E0602
        try:
            await jarvis(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)
            counter -= 30
            await asyncio.sleep(60)
        except:
            return


"""Auto Profile Updation Commands
.autoname"""
import asyncio
import time
from telethon.errors import FloodWaitError
from telethon.tl import functions
import logging
from jarvis import ALIVE_NAME
from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd

DEL_TIME_OUT = 60
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"


@jarvis.on(j_cmd(pattern="autoname"))  # pylint:disable=E0602
@jarvis.on(sudo_cmd(pattern="autoname", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    while True:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"🕒{HM} ⚡{DEFAULTUSER}⚡ 📅{DM}"
        logger.info(name)
        try:
            await jarvis(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    first_name=name
                )
            )
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)

        #if PRIVATE_GROUP_BOT_API_ID :
         #   logger.info(r.stringify())
          #  await jarvis.send_message( # pylint:disable=E0602
           #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #    "Successfully Changed Profile Name"
            #)
        await asyncio.sleep(DEL_TIME_OUT)
    await edit_or_reply(event, f"Auto Name has been started Master")
