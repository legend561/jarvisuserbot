import asyncio
import os
from datetime import datetime
from pathlib import Path

from jarvis import ALIVE_NAME
from jarvis.utils import j_cmd, eor, load_module, remove_plugin, sudo_cmd

DELETE_TIMEOUT = 5
thumb_image_path = "./resource/20201012_204728.png"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "JARVIS"


@jarvis.on(j_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    hmm = jarvisub.uid
    message_id = event.message.id
    thumb = thumb_image_path
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./jarvis/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await eor(
            pro,
            f"**==> Plugin name:** `{input_str}`\n**==> Uploaded in {time_taken_in_ms} seconds only.**\n**==> Uploaded by:** [{DEFAULTUSER}](tg://user?id={hmm})\n",
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.delete()
    else:
        await eor(event, "**404**: __File Not Found__")


@jarvis.on(j_cmd(pattern="install"))
@jarvis.on(sudo_cmd(pattern="install", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "jarvis/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await eor(
                    event,
                    "Plugin successfully installed\n `{}`".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                await eor(
                    event,
                    "**Error!**\nPlugin cannot be installed!\n Or may have been pre-installed.",
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await eor(event, str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@jarvis.on(j_cmd(pattern=r"unload (?P<shortname>\w+)$"))
@jarvis.on(sudo_cmd(pattern=r"unload (?P<shortname>\w+)$", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        qwe = await eor(event, f"Jarvis Has Successfully unloaded {shortname}")
    except Exception as e:
        await qwe.edit(
            "Jarvis has Successfully unloaded {shortname}\n{}".format(shortname, str(e))
        )


@jarvis.on(j_cmd(pattern=r"load (?P<shortname>\w+)$"))
@jarvis.on(sudo_cmd(pattern=r"load (?P<shortname>\w+)$", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        qwe = await eor(event, f"Successfully loaded {shortname}")
    except Exception as e:
        await qwe.edit(
            f"Jarvis could not load {shortname} because of the following error.\n{str(e)}"
        )
