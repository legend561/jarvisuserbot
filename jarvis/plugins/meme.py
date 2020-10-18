"""
Memes Plugin for Userbot
usage = .meme someCharacter //default delay will be 3
By : - @Zero_cool7870

"""
from telethon import events
import asyncio
import os
import sys
from jarvis.utils import jarvis_cmd

@jarvis.on(jarvis_cmd(pattern=r"meme"))
async def meme(event):
    if event.fwd_from:
        return
    memeVar = event.text
    sleepValue = 3
    memeVar = memeVar[6:]

    await event.edit("-------------"+memeVar)
    await asyncio.sleep(sleepValue)
    await event.edit("------------"+memeVar+"-")
    await asyncio.sleep(sleepValue)
    await event.edit("-----------"+memeVar+"--")
    await asyncio.sleep(sleepValue)
    await event.edit("----------"+memeVar+"---")
    await asyncio.sleep(sleepValue)
    await event.edit("---------"+memeVar+"----")
    await asyncio.sleep(sleepValue)
    await event.edit("--------"+memeVar+"-----")
    await asyncio.sleep(sleepValue)
    await event.edit("-------"+memeVar+"------")
    await asyncio.sleep(sleepValue)
    await event.edit("------"+memeVar+"-------")
    await asyncio.sleep(sleepValue)
    await event.edit("-----"+memeVar+"--------")
    await asyncio.sleep(sleepValue)
    await event.edit("----"+memeVar+"---------")
    await asyncio.sleep(sleepValue)
    await event.edit("---"+memeVar+"----------")
    await asyncio.sleep(sleepValue)
    await event.edit("--"+memeVar+"-----------")
    await asyncio.sleep(sleepValue)
    await event.edit("-"+memeVar+"------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeVar+"-------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeVar)
    await asyncio.sleep(sleepValue)

"""
Bonus : Flower Boquee Generater
usage:- .flower

"""
@jarvis.on(jarvis_cmd(pattern=r"flower"))
async def meme(event):
    if event.fwd_from:
        return
    flower =" 🌹"
    sleepValue = 5

    await event.edit(flower+"        ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+"       ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+"      ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+"     ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+"    ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+"   ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+"   ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+"  ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+" ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+flower)
    await asyncio.sleep(sleepValue)
