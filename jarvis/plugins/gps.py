# Credits :- Catuserjbot Made By @Sandy1709
from geopy.geocoders import Nominatim
from telethon.tl import types

from jarvis import CMD_HELP
from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd


@jarvis.on(admin_cmd(pattern="gps ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="gps ?(.*)", allow_sudo=True))
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await edit_or_reply(event, "Boss ! Give A Place To Search 😔 !.")

    await edit_or_reply(event, "Finding This Location In Maps Server.....")

    geolocator = Nominatim(user_agent="ios")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await event.delete()
    else:
        await edit_or_reply(event, "I Coudn't Find it")


CMD_HELP.update(
    {
        "gps": "`.gps` <location name> :\
      \nUSAGE: Sends you the given location name\
      "
    }
)
