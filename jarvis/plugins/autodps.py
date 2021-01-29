import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd

COLLECTION_STRING = [
    "avengers-logo-wallpaper",
    "avengers-hd-wallpapers-1080p",
    "avengers-iphone-wallpaper",
    "iron-man-wallpaper-1920x1080",
    "iron-man-wallpapers",
]


async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile("/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


@jarvis.on(j_cmd(pattern="avengersdp ?(.*)"))
@jarvis.on(sudo_cmd(pattern="avengersdp ?(.*)", allow_sudo=True))
async def main(event):
    await edit_or_reply(
        event,
        "**Starting Avengers Profile Pic...\n\nDone ! Check Your DP By @JarvisOt**",
    )
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(1000)  # Edit this to your required needs


import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd

COLLECTION_STRINGZ = [
    "star-wars-wallpaper-1080p",
    "4k-sci-fi-wallpaper",
    "star-wars-iphone-6-wallpaper",
    "kylo-ren-wallpaper",
    "darth-vader-wallpaper",
]


async def animepp():

    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)
    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile("/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


@jarvis.on(j_cmd(pattern="gamerdp ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="gamerdp ?(.*)", allow_sudo=True))
async def main(event):
    await edit_or_reply(
        event, "**Starting Gamer Profile Pic...\n\nDone !!! Check Your DP"
    )
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(3600)  # Edit this to your required needs


import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd

COLLECTION_STRINGZS = ["hacker-background"]


async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRINGZS) - 1)
    pack = COLLECTION_STRINGZS[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile("/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


@jarvis.on(j_cmd(pattern="hackerdp ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="hackerdp ?(.*)", allow_sudo=True))
async def main(event):
    await edit_or_reply(
        event, "**Starting Hacker Profile Pic...\n\nDone !!! Check Your DP"
    )  # Owner MarioDevs
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(60)  # Edit this to your required needs


import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from jarvis.utils import j_cmd

# Space lovers
COLLECTION_STRINGSZ = [
    "1920x1080-space-wallpapers",
    "4k-space-wallpaper",
    "cool-space-wallpapers-hd",
]


async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGSZ) - 1)

    pack = COLLECTION_STRINGSZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "jarvis.jpg")


@jarvis.on(j_cmd(pattern="spacedp ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting Space Profile Pic...\n\nDone !!! Check Your DP"
    )  # Owner MarioDevs

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(3600)  # Edit this to your required needs
