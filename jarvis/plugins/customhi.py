from jarvis.utils import admin_cmd, sudo_cmd, edit_or_reply


@jarvis.on(admin_cmd(pattern=r"hhi ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"hhi ?(.*)", allow_sudo=True))
async def hhi(event):
    giveVar = event.text
    cat = giveVar[5:6]
    if not cat:
        cat = "🌺"
    ct = giveVar[7:8]
    if not ct:
        ct = "✨"
    await edit_or_reply(event,
        f"{cat}{ct}{ct}{cat}{ct}{cat}{cat}{cat}\n{cat}{ct}{ct}{cat}{ct}{ct}{cat}{ct}\n{cat}{cat}{cat}{cat}{ct}{ct}{cat}{ct}\n{cat}{ct}{ct}{cat}{ct}{ct}{cat}{ct}\n{cat}{ct}{ct}{cat}{ct}{cat}{cat}{cat}\n☁☁☁☁☁☁☁☁"
    )
