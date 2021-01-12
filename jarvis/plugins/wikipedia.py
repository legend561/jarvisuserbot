import wikipedia

from jarvis.utils import admin_cmd


@jarvis.on(admin_cmd(pattern="wikipedia (.*)"))
@jarvis.on(sudo_cmd(pattern="wikipedia (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await eor(event, "Processing ...")
    input_str = event.pattern_match.group(1)
    result = ""
    results = wikipedia.search(input_str)
    for s in results:
        page = wikipedia.page(s)
        url = page.url
        result += f"> [{s}]({url}) \n"
    await event.edit(
        "Wikipedia **Search**: {} \n\n **Result**: \n\n{}".format(input_str, result)
    )
