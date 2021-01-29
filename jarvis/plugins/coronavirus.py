"""CoronaVirus LookUp
Syntax: .covid <country>"""
from covid import Covid

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd


@jarvis.on(j_cmd(pattern="covid (.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="covid (.*)", allow_sudo=True))
async def _(event):
    covid = Covid()
    data = covid.get_data()
    country = event.pattern_match.group(1)
    country_data = get_country_data(country, data)
    output_text = ""
    for name, value in country_data.items():
        output_text += "`{}`: `{}`\n".format(str(name), str(value))
    await edit_or_reply(
        event,
        "**CoronaVirus Info in {}**:\n\n{}".format(country.capitalize(), output_text),
    )


def get_country_data(country, world):
    for country_data in world:
        if country_data["country"].lower() == country.lower():
            return country_data
    return {"Status": "No information yet about this country!"}
