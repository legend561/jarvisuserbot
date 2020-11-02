"""IX.IO pastebin like site
Syntax: .npaste"""
import logging
import os
from datetime import datetime

import requests

from jarvis.utils import admin_cmd, sudo_cmd, edit_or_reply

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)


def progress(current, total):
    logger.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )

@jarvis.on(admin_cmd(pattern="paste( (.*)|$)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="paste( (.*)|$)", allow_sudo=True))
async def _(event):
    jevent = await edit_or_reply(event, "`Pasting .. 😅`")
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message,
                Config.TEMP_DIR,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            try:
                for m in m_list:
                    message += m.decode("UTF-8")
            except:
                message = "Usage : .paste <long text to include/reply to text file>"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "Usage : .paste <long text to include/reply to text file>"
    url = "https://del.dog/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://del.dog/{r['key']}"
    if r["isUrl"]:
        nurl = f"https://del.dog/v/{r['key']}"
        rawurl = f"https://del.dog/raw/{r['key']}"
        await jevent.edit(
            f"**Pasted Successfully 🤗**\n**~ Pasted to dogbin : **[dog]({nurl}).\n**~ Raw url :** [raw link]({rawurl})\n**~ GoTo Original URL: **[link]({url})"
        )
    else:
        await jevent.edit(
            f"**Pasted Successfully 🤗**\n**~ Pasted to dogbin : **[dog]({url})\n**~ Raw url :** [raw link](https://del.dog/raw/{r['key']})"
        )
    
@jarvis.on(admin_cmd(pattern="neko( (.*)|$)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="neko( (.*)|$)", allow_sudo=True))
async def _(event):
    jevent = await edit_or_reply(event, "`Pasting .. 😅`")
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    if input_str:
        message = input_str
        downloaded_file_name = None
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message,
                Config.TEMP_DIR,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            try:
                for m in m_list:
                    message += m.decode("UTF-8")
            except:
                message = (
                    "**Usage : **`.neko <long text to include/reply to text file>`"
                )
            os.remove(downloaded_file_name)
        else:
            downloaded_file_name = None
            message = previous_message.message
    else:
        downloaded_file_name = None
        message = "**Usage : **`.neko <long text to include/reply to text file>`"
    if downloaded_file_name and downloaded_file_name.endswith(".py"):
        py_file = ".py"
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}{py_file}"
    else:
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
    reply_text = f"**Pasted Successfully 🤗**\n**~ Pasted to Nekobin : **[neko]({url})\n**~ Raw url : **[Raw](https://nekobin.com/raw/{key})"
    await jevent.edit(reply_text)
