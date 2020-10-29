import asyncio

from jarvis.utils import admin_cmd, sudo_cmd


@jarvis.on(admin_cmd(pattern=r"(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 101)
    input_str = event.pattern_match.group(1)
    if input_str == "repo":
        await event.edit(input_str)
        animation_chars = [
            "https://github.com/Jarvis-Works/jarvisuserbot",
            "https://github.com/Jarvis-Works/jarvisuserbot",
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 2])
