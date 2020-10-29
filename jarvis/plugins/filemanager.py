"""Execute GNU/Linux commands inside Telegram
Syntax: .lsroot , .lslocal"""
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import asyncio
import io
import os
import time

from jarvis.utils import admin_cmd, sudo_cmd

if not os.path.isdir("./SAVED"):
    os.makedirs("./SAVED")
if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


@jarvis.on(admin_cmd(pattern="lslocal", outgoing=True))
@jarvis.on(sudo_cmd(pattern="lslocal", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "ls -lh ./DOWNLOADS/"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**Files in [JARVIS](https://t.me/JarvisOT) DOWNLOADS Folder:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.reply(f"**{stderr.decode()}**")
        return
    await event.reply(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@jarvis.on(admin_cmd(pattern=r"lsroot", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"lsroot", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    cmd = "ls -lh"

    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**Files in root directory:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.reply(f"**{stderr.decode()}**")
        return
    await event.reply(f"{OUTPUT}`{stdout.decode()}`")


@jarvis.on(admin_cmd(pattern=r"lssaved", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"lssaved", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    cmd = "ls ./SAVED/"

    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**Files in SAVED directory:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.reply(f"**{stderr.decode()}**")
        return
    await event.reply(f"{OUTPUT}`{stdout.decode()}`")


@jarvis.on(admin_cmd(pattern=r"rnsaved ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"rnsaved ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        src, dst = input_str.split("|")
        src = src.strip()
        dst = dst.strip()
    cmd = f"mv ./SAVED/{src} ./SAVED/{dst}"
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**Files in root directory:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.reply(f"**{stderr.decode()}**")
        return
    await event.reply(f"File renamed `{src}` to `{dst}`")


@jarvis.on(admin_cmd(pattern=r"rnlocal (.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"rnlocal (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        src, dst = input_str.split("|")
        src = src.strip()
        dst = dst.strip()
    cmd = f"mv ./DOWNLOADS/{src} ./DOWNLOADS/{dst}"
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**Files in root directory:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.reply(f"**{stderr.decode()}**")
        return
    await event.reply(f"File renamed `{src}` to `{dst}`")


@jarvis.on(admin_cmd(pattern=r"delsave (.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"delsave (.*)", allow_sudo=True))
async def handler(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    pathtofile = f"./SAVED/{input_str}"

    if os.path.isfile(pathtofile):
        os.remove(pathtofile)
        await event.reply("✅ File Deleted 🗑")

    else:
        await event.reply("⛔️ File Not Found 😬")


@jarvis.on(admin_cmd(pattern=r"delocal (.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"delocal (.*)", allow_sudo=True))
async def handler(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    pathtofile = f"./BotHub/{input_str}"

    if os.path.isfile(pathtofile):
        os.remove(pathtofile)
        await event.reply("✅ File Deleted 🗑")

    else:
        await event.reply("⛔️ File Not Found 😬")
