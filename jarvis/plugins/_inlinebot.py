# Ported from Telebot for Jarvis
# Kangers, don't remove this line 
# @its_xditya

from math import ceil
import asyncio
import json
import random
import re
from telethon import events, errors, custom, Button
from jarvis import CMD_LIST
import io
from jarvis import ALIVE_NAME
from jarvis import bot

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "JARVIS User"
myid = bot.uid

if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @jarvisbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("`Userbot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© @JarvisOT",
                text="{}\nCurrently Loaded Plugins: {}".format(
                    query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False
            )
        elif event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**Jarvis Stats For [{DEFAULTUSER}](tg://user?id={myid})**\n\n__Bot is functioning normally, master!__\n\n(c) @JarvisOT",
                buttons=[
                    [custom.Button.inline("Stats", data="statcheck")],
                    [Button.url("Repo", "https://github.com/Jarvis-Works/JarvisUserbot")],
                    [Button.url("Deploy Now!",
                                "https://heroku.com/deploy?template=https://github.com/Jarvis-Works/jarvisuserbot/")],
                ]
            )
        else:
            result = builder.article(
                "Source Code",
                text="**Welcome to JARVIS**\n\n`Click below buttons for more`",
                buttons=[
                    [custom.Button.url("Creator👨‍🦱", "https://t.me/its_spidy")],
                    [custom.Button.url("👨‍💻Source Code‍💻", "https://github.com/Jarvis-Works/JarvisUserbot"), custom.Button.url(
                        "Deploy 🌀",
                        "https://heroku.com/deploy?template=https://github.com/Jarvis-Works/jarvisuserbot/")],
                    [custom.Button.url("Updates Channel↗️", "https://t.me/JarvisOT"), custom.Button.url("Support Group↗️", "https://t.me/JarvisSupportOT")]
                ],
                link_preview=False
            )
        await event.answer([result] if result else None)


    @jarvisbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own Userbot from @JarvisSupportOT , and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


    @jarvisbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit("Help Menu Closed.")
        else:
            reply_pop_up_alert = "Please get your own userbot from @JarvisSupportOT "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


    @jarvisbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1,
                CMD_LIST,  # pylint:disable=E0602
                "helpme"
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


    @jarvisbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"us_plugin_(.*)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            try:
                for i in CMD_LIST[plugin_name]:
                    help_string += i
                    help_string += "\n"
            except:
                pass
            if help_string == "":
                reply_pop_up_alert = "{} is useless".format(plugin_name)
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
                © Jarvis".format(
                plugin_name
            )
            try:
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            except:
                halps = "Do .help {} to get the list of commands.".format(plugin_name)
                await event.answer(halps, cache_time=0, alert=True)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"

def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = 5
    number_of_cols = 2
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [custom.Button.inline(
        "{} {}".format("❄️", x, "❄️"),
        data="us_plugin_{}".format(x))
        for x in helpable_plugins]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
                [
                    (custom.Button.inline("⏮️ Previous", data="{}_prev({})".format(prefix, modulo_page)),
                     custom.Button.inline("Close", data="close"),
                     custom.Button.inline("Next ⏭️", data="{}_next({})".format(prefix, modulo_page)))
                ]
    return pairs
