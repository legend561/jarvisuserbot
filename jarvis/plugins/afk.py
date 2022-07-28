"""AFK Plugin for JARVIS
Syntax: .afk REASON"""
import asyncio
import datetime

from telethon import events
from telethon.tl import functions, types

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd

global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global last_afk_message  # pylint:disable=E0602
USER_AFK = {}
afk_time = None
last_afk_message = {}


@jarvis.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afk(event):
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:  # pylint:disable=E0602
        try:
            await jarvis.send_message(  # pylint:disable=E0602
                Config.PLUGIN_CHANNEL,  # pylint:disable=E0602
                "#AfkLogger My Boss is Busy",
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await jarvis.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PLUGIN_CHANNEL` "
                + "for the proper functioning of afk functionality "
                + "in @JarvisSupportOT\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        USER_AFK = {}  # pylint:disable=E0602
        afk_time = None  # pylint:disable=E0602


@jarvis.on(j_cmd(pattern=r"afk ?(.*)"))
@jarvis.on(sudo_cmd(pattern=r"afk ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global reason
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    reason = event.pattern_match.group(1)
    if not USER_AFK:  # pylint:disable=E0602
        last_seen_status = await jarvis(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_AFK = f"yes: {reason}"  # pylint:disable=E0602
        if reason:
            await edit_or_reply(
                event, f"My Boss Is Going Away ! And The Reason is {reason}"
            )
        else:
            await edit_or_reply(event, f"My Boss is Going")
        await asyncio.sleep(5)
        await event.delete()
        try:
            await jarvis.send_message(  # pylint:disable=E0602
                Config.PLUGIN_CHANNEL,  # pylint:disable=E0602
                f"#AfkLogger Reason : {reason}",
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


@jarvis.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    afk_since = "**A While Ago**"
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFK and not (await event.get_sender()).bot:  # pylint:disable=E0602
        if afk_time:  # pylint:disable=E0602
            now = datetime.datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**Yesterday**"
            elif days > 1:
                if days > 6:
                    date = now + datetime.timedelta(
                        days=-days, hours=-hours, minutes=-minutes
                    )
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime("%A")
            elif hours > 1:
                afk_since = f"`{int(hours)}h{int(minutes)}m` **ago**"
            elif minutes > 0:
                afk_since = f"`{int(minutes)}m{int(seconds)}s` **ago**"
            else:
                afk_since = f"`{int(seconds)}s` **ago**"
        msg = None
        message_to_reply = (
            f"**My Boss is Away** ! \n\n**Reason** : `{reason}` \n\n**Away Since** : {afk_since}"
            + f"\n\n__Kindly Leave A Message__ ! \n`He Will Reply To You Soon !`"
            if reason
            else f"**Hello, Boss Is Away Right Now And May Be Forgot List Reason ! Any Way He Will Come Back Soon** !"
        )
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_afk_message:  # pylint:disable=E0602
            await last_afk_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afk_message[event.chat_id] = msg  # pylint:disable=E0602
