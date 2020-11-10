"""
StartPage Search Plugin for Userbot . //Alternative to Google Search
cmd : .sch search_query 
By: @Zero_cool7870

"""

import json
import os

from jarvis.utils import admin_cmd, sudo_cmd, eor


@jarvis.on(admin_cmd(pattern="sch ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="sch ?(.*)", allow_sudo=True))
async def sp_search(event):
    search_str = event.pattern_match.group(1)

    jevent = await eor(event,"**Searching for " + search_str + " ...**")

    command = "sp --json " + search_str + " > out.json"

    os.system(command)

    f = open("out.json", "r").read()

    data = json.loads(str(f))

    msg = "**Search Query** \n`" + search_str + "`\n**Results**\n"

    for element in data:
        msg = msg + "⁍ [" + element["title"] + "](" + element["link"] + ")\n\n"

    await jevent.edit(msg)
