# For JARVIS
# By Priyam Kalra
# Ported To JARVIS By Spidy
# Syntax (.hl <link>)

from jarvis.utils import admin_cmd


@jarvis.on(admin_cmd(pattern="hl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input = event.pattern_match.group(1)
    await event.edit("[ㅤㅤㅤㅤㅤㅤㅤ](" + input + ")")
