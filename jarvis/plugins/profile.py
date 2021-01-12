"""Profile Updation Commands
.pbio <Bio>
.pname <Name>
.ppic"""
import os

from telethon.tl import functions

from jarvis.utils import admin_cmd, eor, sudo_cmd


@jarvis.on(admin_cmd(pattern="pbio (.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="pbio (.*)", allow_sudo=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await borg(
            functions.account.UpdateProfileRequest(about=bio)  # pylint:disable=E0602
        )
        await eor(event, "Succesfully changed my profile bio")
    except Exception as e:  # pylint:disable=C0103,W0703
        await eor(event, str(e))


@jarvis.on(admin_cmd(pattern="pname ((.|\n)*)", outgoing=True))
@jarvis.on(
    sudo_cmd(pattern="pname ((.|\n)*)", allow_sudo=True)
)  # pylint:disable=E0602,W0703
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if "\\n" in names:
        first_name, last_name = names.split("\\n", 1)
    try:
        await borg(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=first_name, last_name=last_name
            )
        )
        await eor(event, "My name was changed successfully")
    except Exception as e:  # pylint:disable=C0103,W0703
        await eor(event, str(e))


@jarvis.on(admin_cmd(pattern="ppic", outgoing=True))  # pylint:disable=E0602
@jarvis.on(sudo_cmd(pattern="ppic", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    await eor(event, "Downloading Profile Picture to my local ...")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    photo = None
    try:
        photo = await borg.download_media(  # pylint:disable=E0602
            reply_message, Config.TMP_DOWNLOAD_DIRECTORY  # pylint:disable=E0602
        )
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))
    else:
        if photo:
            await event.edit("now, Uploading to @Telegram ...")
            file = await borg.upload_file(photo)  # pylint:disable=E0602
            try:
                await borg(
                    functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                        file
                    )
                )
            except Exception as e:  # pylint:disable=C0103,W0703
                await event.edit(str(e))
            else:
                await event.edit("My profile picture was succesfully changed")
    try:
        os.remove(photo)
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602

from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import InputPhoto

from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd


@jarvis.on(admin_cmd(pattern="delpfp ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="delpfp ?(.*)", allow_sudo=True))
async def remove_profilepic(delpfp):
    """ For .delpfp command, delete your current profile picture in Telegram. """
    group = delpfp.text[8:]
    if group == "all":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1

    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.from_id, offset=0, max_id=0, limit=lim)
    )
    input_photos = []
    for sep in pfplist.photos:
        input_photos.append(
            InputPhoto(
                id=sep.id,
                access_hash=sep.access_hash,
                file_reference=sep.file_reference,
            )
        )
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await edit_or_reply(
        delpfp, f"`Successfully deleted {len(input_photos)} profile picture(s).`"
    )
