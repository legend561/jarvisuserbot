"""Color Plugin for @Jarvis
Syntax: .color <color_code>"""
import os

from PIL import Image, ImageColor

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd


@jarvis.on(j_cmd(pattern="color (.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="color (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    if input_str.startswith("#"):
        try:
            usercolor = ImageColor.getrgb(input_str)
        except Exception as e:
            await edit_or_reply(event, str(e))
            return False
        else:
            im = Image.new(mode="RGB", size=(1280, 720), color=usercolor)
            im.save("jarvis.png", "PNG")
            input_str = input_str.replace("#", "#COLOR_")
            await jarvis.send_file(
                event.chat_id,
                "jarvis.png",
                force_document=False,
                caption=input_str,
                reply_to=message_id,
            )
            os.remove("jarvis.png")
            await event.delete()
    else:
        await edit_or_reply(event, "Syntax: `.color <color_code>`")
