# For @UniBorg
# (c) Shrimadhav U K

from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest

from jarvis.utils import j_cmd


@jarvis.on(j_cmd("listme"))
async def mine(event):
    """ For .reserved command, get a list of your reserved usernames. """
    result = await jarvis(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)
