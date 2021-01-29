"""Currency Converter Plugin for @UniBorg
Syntax: .currency number from to"""
from datetime import datetime

import requests

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd


@jarvis.on(j_cmd(pattern="currency (.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="currency (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split(" ")
    if len(input_sgra) == 3:
        try:
            number = float(input_sgra[0])
            currency_from = input_sgra[1].upper()
            currency_to = input_sgra[2].upper()
            request_url = "https://api.exchangeratesapi.io/latest?base={}".format(
                currency_from
            )
            current_response = requests.get(request_url).json()
            if currency_to in current_response["rates"]:
                current_rate = float(current_response["rates"][currency_to])
                rebmun = round(number * current_rate, 2)
                await edit_or_reply(
                    event,
                    "{} {} = {} {}".format(number, currency_from, rebmun, currency_to),
                )
            else:
                await event.edit("IDEKNOWTDWTT")
        except e:
            await event.edit(str(e))
    else:
        await event.edit("`.currency number from to`")
    end = datetime.now()
    (end - start).seconds
