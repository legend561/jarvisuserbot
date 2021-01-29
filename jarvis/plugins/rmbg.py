"""Remove.BG Plugin for Jarvis
Syntax: .rmbg https://link.to/image.extension
Syntax: .rmbg as reply to a media"""
import io
import os
from datetime import datetime

import requests

from jarvis.utils import j_cmd, eor, sudo_cmd


@jarvis.on(j_cmd("rmbg ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd("rmbg ?(.*)", allow_sudo=True))
async def _(event):
    HELP_STR = (
        "`.rmbg` as reply to a media, or give a link as an argument to this command"
    )
    if event.fwd_from:
        return
    if Config.REM_BG_API_KEY is None:
        await eor(event, "You need API token from remove.bg to use this plugin.")
        return False
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
        reply_message = await event.get_reply_message()
        # check if media message
        jevent = await eor(
            event, "Connecting to Official JARVIS Server and analysing that img ..."
        )
        try:
            downloaded_file_name = await jarvis.download_media(
                reply_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
        except Exception as e:
            await jevent.edit(str(e))
            return
        else:
            await jevent.edit("sending to ReMove.BG")
            output_file_name = ReTrieveFile(downloaded_file_name)
            os.remove(downloaded_file_name)
    elif input_str:
        await jevent.edit("sending to ReMove.BG")
        output_file_name = ReTrieveURL(input_str)
    else:
        await jevent.edit(HELP_STR)
        return
    contentType = output_file_name.headers.get("content-type")
    if "image" in contentType:
        with io.BytesIO(output_file_name.content) as remove_bg_image:
            remove_bg_image.name = "@jarvisot.png"
            await jarvis.send_file(
                event.chat_id,
                remove_bg_image,
                force_document=True,
                supports_streaming=False,
                allow_cache=False,
                reply_to=message_id,
            )
        end = datetime.now()
        ms = (end - start).seconds
        await jevent.edit(
            "Removed dat annoying Backgroup in {} seconds, powered by JARVIS Userbot".format(
                ms
            )
        )
    else:
        await jevent.edit(
            "ReMove.BG API returned Errors. Please report to @JarvisOt Support Group\n`{}".format(
                output_file_name.content.decode("UTF-8")
            )
        )


# this method will call the API, and return in the appropriate format
# with the name provided.
def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": Config.REM_BG_API_KEY,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True,
    )
    return r


def ReTrieveURL(input_url):
    headers = {
        "X-API-Key": Config.REM_BG_API_KEY,
    }
    data = {"image_url": input_url}
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        data=data,
        allow_redirects=True,
        stream=True,
    )
    return r
