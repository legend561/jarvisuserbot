import asyncio
import os
import time
import zipfile

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern="compress ?(.*)"))
@jarvis.on(j_cmd(pattern="compress ?(.*)", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    mone = await event.reply("Processing ...")

    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):

        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)

    if event.reply_to_msg_id:

        reply_message = await event.get_reply_message()

        try:

            time.time()

            downloaded_file_name = await jarvis.download_media(
                reply_message, Config.TMP_DOWNLOAD_DIRECTORY
            )

            directory_name = downloaded_file_name

            await event.reply("Finish downloading to my local")

            zipfile.ZipFile(directory_name + ".zip", "w", zipfile.ZIP_DEFLATED).write(
                directory_name
            )

            await jarvis.send_file(
                event.chat_id,
                directory_name + ".zip",
                caption="Zipped By [JARVIS](https://t.me/JarvisOT)",
                force_document=True,
                allow_cache=False,
                reply_to=event.message.id,
            )

            try:

                os.remove(directory_name + ".zip")

                os.remove(directory_name)

            except:

                pass

            await event.reply("task Completed")

            await asyncio.sleep(3)

            await event.delete()

        except Exception as e:  # pylint:disable=C0103,W0703

            await mone.reply(str(e))

    elif input_str:

        directory_name = input_str

        zipfile.ZipFile(directory_name + ".zip", "w", zipfile.ZIP_DEFLATED).write(
            directory_name
        )

        await event.reply(
            "Local file compressed to `{}`".format(directory_name + ".zip")
        )
