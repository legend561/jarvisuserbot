"""use command .ducduckgo"""

from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd


@jarvis.on(admin_cmd("ducduckgo (.*)", outgoing=True))
@jarvis.on(sudo_cmd("ducduckgo (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://duckduckgo.com/?q={}".format(input_str.replace(" ", "+"))
    if sample_url:
        link = sample_url.rstrip()
        await edit_or_reply(
            event,
            "Let me 🦆 DuckDuckGo that for you:\n🔎 [{}]({})".format(input_str, link),
        )
    else:
        await edit_or_reply(event, "something is wrong. please try again later.")
