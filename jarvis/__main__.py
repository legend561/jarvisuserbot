import os
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from jarvis import jbot
from jarvis.utils import load_module, start_assistant
from var import Var

LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)


async def add_jbot(jbot_token):
    await jbot.start(jbot_token)
    jbot.me = await jbot.get_me()
    jbot.uid = telethon.utils.get_peer_id(jbot.me)


if len(argv) not in (1, 3, 4):
    jbot.disconnect()
else:
    jbot.tgjbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        jbot.tgjbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(jbot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialised Sucessfully")
        print("Starting JARVIS AI")
        jbot.loop.run_until_complete(add_jbot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        jbot.start()


import glob

if LOAD_USERBOT == True:
    path = "jarvis/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
else:
    print("Userjbot is Not Loading As U Have Disabled")

if LOAD_ASSISTANT == True:
    path = "jarvis/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
else:
    print("Assitant is Not Loading As U Have Disabled")

print("JARVIS AI AND YOUR ASSISTANT is Active Enjoy Join @JarvisOT For Updates.")

if len(argv) not in (1, 3, 4):
    jbot.disconnect()
else:
    jbot.run_until_disconnected()
