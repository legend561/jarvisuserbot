"""Enable Seen Counter in any message, Fix by @pureindialover
to know how many users have seen your message
Syntax: .fwd as reply to any message"""
from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd


@jarvis.on(admin_cmd(pattern="frwd", outgoing=True))
@jarvis.on(sudo_cmd(pattern="frwd", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.PLUGIN_CHANNEL is None:
        await edit_or_reply(
            event,
            "Please set the required environment variable `PLUGIN_CHANNEL` for this plugin to work",
        )
        return
    try:
        e = await borg.get_entity(Config.PLUGIN_CHANNEL)
    except Exception as e:
        await event.edit(str(e))
    else:
        re_message = await event.get_reply_message()
        # https://t.me/telethonofftopic/78166
        fwd_message = await borg.forward_messages(e, re_message, silent=True)
        await borg.forward_messages(event.chat_id, fwd_message)
        await fwd_message.delete()
        await event.delete()
