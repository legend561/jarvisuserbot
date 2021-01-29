import os
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from jarvis import jarvisub
from jarvis.utils import load_module, start_assistant
from var import Var

LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)


async def add_bot(bot_token):
    await jarvisub.start(bot_token)
    jarvisub.me = await jarvisub.get_me()
    jarvisub.uid = telethon.utils.get_peer_id(jarvisub.me)


if len(argv) not in (1, 3, 4):
    jarvisub.disconnect()
else:
    jarvisub.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        jarvisub.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialised Sucessfully")
        print("Starting JARVIS AI")
        jarvisub.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        jarvisub.start()


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
    print("Userbot is Not Loading As U Have Disabled")

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
    jarvisub.disconnect()
else:
    jarvisub.run_until_disconnected()
