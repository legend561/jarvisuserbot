from os import remove
from os import execl
import sys
import git
import asyncio
import random
import re
import time
from collections import deque
import requests
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon import events
from userbot.utils import admin_cmd
from contextlib import suppress
import os
import sys
import asyncio

@borg.on(admin_cmd("update", about={
    'header': "Check Updates or Update Userge",
    'flags': {
        '-pull': "pull updates",
        '-push': "push updates to heroku",
        '-master': "select master branch",
        '-beta': "select beta branch",
        '-alpha': "select alpha branch"},
    'usage': "{tr}update : check updates from default branch\n"
             "{tr}update -[branch_name] : check updates from any branch\n"
             "add -pull if you want to pull updates\n"
             "add -push if you want to push updates to heroku",
    'examples': "{tr}update -beta -pull -push"}, del_pre=True, allow_channels=False))
async def check_update(message: Message):
    """ check or do updates """
    await message.edit("`Checking for updates, please wait....`")
    repo = Repo()
    try:
        repo.remote(https://github.com/jarvis210904/jarvisuserbot).fetch()
    except GitCommandError as error:
        await message.err(error, del_in=5)
        return
    flags = list(message.flags)
    pull_from_repo = False
    push_to_heroku = False
    branch = "master"
    if "pull" in flags:
        pull_from_repo = True
        flags.remove("pull")
    if "push" in flags:
        push_to_heroku = True
        flags.remove("push")
    if len(flags) == 1:
        branch = flags[0]
    if branch not in repo.branches:
        await message.err(f'invalid branch name : {branch}')
        return
    out = ''
    try:
        for i in repo.iter_commits(f'HEAD..{https://github.com/jarvis210904/jarvisuserbot}/{branch}'):
            out += (f"🔨 **#{i.count()}** : "
                    f"[{i.summary}]({https://github.com/jarvis210904/jarvisuserbot.rstrip('/')}/commit/{i}) "
                    f"👷 __{i.author}__\n\n")
    except GitCommandError as error:
        await message.err(error, del_in=5)
        return
    if out:
        if pull_from_repo:
            await message.edit(f'`New update found for [{branch}], Now pulling...`')
            await asyncio.sleep(1)
            repo.git.reset('--hard', 'FETCH_HEAD')
            await CHANNEL.log(f"**PULLED update from [{branch}]:\n\n📄 CHANGELOG 📄**\n\n{out}")
        elif not push_to_heroku:
            changelog_str = f'**New UPDATE available for [{branch}]:\n\n📄 CHANGELOG 📄**\n\n'
            await message.edit_or_send_as_file(changelog_str + out, disable_web_page_preview=True)
            return
    elif not push_to_heroku:
        await message.edit(f'**Userge is up-to-date with [{branch}]**', del_in=5)
        return
    if not push_to_heroku:
        await message.edit(
            '**JARVIS Successfully Updated!**\n'
            '`Now restarting... Wait for a while!`', del_in=3)
        asyncio.get_event_loop().create_task(userge.restart(True))
        return
    if not Config.HEROKU_GIT_URL:
        await message.err("please set heroku things...")
        return
    await message.edit(
        f'`Now pushing updates from [{branch}] to heroku...\n'
        'this will take upto 5 min`\n\n'
        f'* **Restart** after 5 min using `.restart -h`\n\n'
        '* After restarted successfully, check updates again :)')
    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(Config.HEROKU_GIT_URL)
    else:
        remote = repo.create_remote("heroku", Config.HEROKU_GIT_URL)
    remote.push(refspec=f'{branch}:master', force=True)
    await message.edit(f"**HEROKU APP : {Config.HEROKU_APP.name} is up-to-date with [{branch}]**")
