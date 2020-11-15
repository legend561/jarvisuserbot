""" Powered by @Google
Available Commands:
.go <query> credits to owner of bot
"""


from search_engine_parser import GoogleSearch

from jarvis import BOTLOG_CHATID
from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd


def progress(current, total):
    logger.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )


@jarvis.on(admin_cmd(outgoing=True, pattern=r"go (.*)"))
@jarvis.on(sudo_cmd(allow_sudo=True, pattern=r"go (.*)"))
async def gsearch(q_event):
    jevent = await edit_or_reply(q_event, "`Processing........`")
    match = q_event.pattern_match.group(1)
    page = re.findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"👉[{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    await jevent.edit(
        "**Search Query:**\n`" + match + "`\n\n**Results:**\n" + msg, link_preview=False
    )
    if BOTLOG_CHATID:
        await q_event.client.send_message(
            BOTLOG_CHATID,
            "Google Search query `" + match + "` was executed successfully",
        )
