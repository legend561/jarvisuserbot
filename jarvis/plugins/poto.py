"""Type `.poto` for get **All profile pics of that User**
\n Or type `.poto (number)` to get the **desired number of photo of a User** .
"""


import logging

from jarvis.utils import j_cmd, eor, sudo_cmd

logger = logging.getLogger(__name__)


if 1 == 1:

    name = "Profile Photos"

    client = jarvis

    @jarvis.on(j_cmd(pattern="poto(.*)", outgoing=True))
    @jarvis.on(sudo_cmd(pattern="poto(.*)", allow_sudo=True))
    async def potocmd(event):

        """Gets the profile photos of replied users, channels or chats"""

        id = "".join(event.raw_text.split(maxsplit=2)[1:])

        user = await event.get_reply_message()

        chat = event.input_chat

        if user:

            photos = await event.client.get_profile_photos(user.sender)

        else:

            photos = await event.client.get_profile_photos(chat)

        if id.strip() == "":

            try:

                await event.client.send_file(event.chat_id, photos)

            except a:

                photo = await event.client.download_profile_photo(chat)

                await jarvis.send_file(event.chat_id, photo)

        else:

            try:

                id = int(id)

                if id <= 0:

                    await eor(event, "`ID number you entered is invalid`")

                    return

            except:

                await eor(event, "`Are you Comedy Me ?`")

                return

            if int(id) <= (len(photos)):

                send_photos = await event.client.download_media(photos[id - 1])

                await jarvis.send_file(event.chat_id, send_photos)

            else:

                await eor(event, "`No photo found of that Nigga , now u Die`")

                return
