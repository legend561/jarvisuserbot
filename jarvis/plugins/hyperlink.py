# For JARVIS
# By Priyam Kalra
# Ported To JARVIS By Spidy
# Syntax (.hl <link>)

from jarvis.utils import admin_cmd, sudo_cmd, edit_or_reply


@jarvis.on(admin_cmd(pattern="hl ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="hl ?(.*)",allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input = event.pattern_match.group(1)
    await edit_or_reply(event,"[ㅤㅤㅤㅤㅤㅤㅤ](" + input + ")")
