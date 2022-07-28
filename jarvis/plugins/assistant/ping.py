# Copyright (C) Midhun KM
#
# Please Don't Kang Without Credits
# A Plugin For Assistant Bot
# x0x

import time
from datetime import datetime
from telethon import events
from jarvis import Lastupdate

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@assistant_cmd("ping", is_args=False)
@peru_only
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    await tgbot.send_message(
        event.chat_id,
        f"**╔═══╗╔══╗╔═╗─╔╗╔═══╗\n║╔═╗║╚╣─╝║║╚╗║║║╔═╗║\n║╚═╝║─║║─║╔╗╚╝║║║─╚╝\n║╔══╝─║║─║║╚╗║║║║╔═╗\n║║───╔╣─╗║║─║║║║╚╩═║\n╚╝───╚══╝╚╝─╚═╝╚═══╝**\n ➲ `{ms}` \n ➲ `{uptime}`",
    )
