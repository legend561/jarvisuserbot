"""DA.GD helpers in @UniBorg
Available Commands:
.isup URL
.dns google.com
.url <long url>
.unshort <short url>"""
import requests

from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd


@jarvis.on(admin_cmd("dns (.*)", outgoing=True))
@jarvis.on(sudo_cmd("dns (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/dns/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(
            event, "DNS records of {} are \n{}".format(input_str, response_api)
        )
    else:
        await event.edit("i can't seem to find {} on the internet".format(input_str))


@jarvis.on(admin_cmd("url (.*)", outgoing=True))
@jarvis.on(sudo_cmd("url (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(
            event, "Generated {} for {}.".format(response_api, input_str)
        )
    else:
        await event.edit("something is wrong. please try again later.")


@jarvis.on(admin_cmd("unshort (.*)", outgoing=True))
@jarvis.on(sudo_cmd("unshort (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith("3"):
        await edit_or_reply(
            event,
            "Input URL: {}\nReDirected URL: {}".format(
                input_str, r.headers["Location"]
            ),
        )
    else:
        await event.edit(
            "Input URL {} returned status_code {}".format(input_str, r.status_code)
        )
