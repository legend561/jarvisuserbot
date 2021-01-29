from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd


@jarvis.on(j_cmd(pattern=r"hhi ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"hhi ?(.*)", allow_sudo=True))
async def hhi(event):
    giveVar = event.text
    cat = giveVar[5:6]
    if not cat:
        cat = "🌺"
    ct = giveVar[7:8]
    if not ct:
        ct = "✨"
    await edit_or_reply(
        event,
        f"{cat}{ct}{ct}{cat}{ct}{cat}{cat}{cat}\n{cat}{ct}{ct}{cat}{ct}{ct}{cat}{ct}\n{cat}{cat}{cat}{cat}{ct}{ct}{cat}{ct}\n{cat}{ct}{ct}{cat}{ct}{ct}{cat}{ct}\n{cat}{ct}{ct}{cat}{ct}{cat}{cat}{cat}\n☁☁☁☁☁☁☁☁",
    )


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern="dump ?(.*)"))
async def _(message):
    try:
        obj = message.pattern_match.group(1)
        if len(obj) != 3:
            raise IndexError
        inp = " ".join(obj)
    except IndexError:
        inp = "🥞 🎂 🍫"
    u, t, g, o, s, n = inp.split(), "🗑", "<(^_^ <)", "(> ^_^)>", "⠀ ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
        [
            y
            for y in (
                [
                    "".join(x)
                    for x in (
                        f + (s, g, s + s * f.count(""), t),
                        f + (g, s * 2 + s * f.count(""), t),
                        f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                        f[:i] + (s + s * f.count(""), o, f[i], s, t),
                        f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                        f[:i] + (s * 3 + s * f.count(""), o, t),
                        f[:i] + (s * 3 + s * f.count(""), g, t),
                    )
                ]
                for i, f in enumerate(reversed(h))
            )
        ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            try:
                await message.edit(something_else)
            except errors.MessageIdInvalidError:
                return


import random

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd


@jarvis.on(j_cmd(pattern=r"jainder(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"jainder(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "ex":
        emoticons = [
            "u is mard",
            "u is man",
            "u is aurat",
            "u is woman",
            "u is gey",
            "u is chakka",
        ]
    elif input_str in "thinking":
        emoticons = [
            "(҂⌣̀_⌣́)",
            "（；¬＿¬)",
            "(-｡-;",
            "┌[ O ʖ̯ O ]┐",
            "〳 ͡° Ĺ̯ ͡° 〵",
        ]
    elif input_str in "waving":
        emoticons = [
            "(ノ^∇^)",
            "(;-_-)/",
            "@(o・ェ・)@ノ",
            "ヾ(＾-＾)ノ",
            "ヾ(◍’౪◍)ﾉﾞ♡",
            "(ό‿ὸ)ﾉ",
            "(ヾ(´・ω・｀)",
        ]
    elif input_str in "wtf":
        emoticons = [
            "༎ຶ‿༎ຶ",
            "(‿ˠ‿)",
            "╰U╯☜(◉ɷ◉ )",
            "(;´༎ຶ益༎ຶ)♡",
            "╭∩╮(︶ε︶*)chu",
            "( ＾◡＾)っ (‿|‿)",
        ]
    elif input_str in "love":
        emoticons = [
            "乂❤‿❤乂",
            "(｡♥‿♥｡)",
            "( ͡~ ͜ʖ ͡°)",
            "໒( ♥ ◡ ♥ )७",
            "༼♥ل͜♥༽",
        ]
    elif input_str in "confused":
        emoticons = [
            "(・_・ヾ",
            "｢(ﾟﾍﾟ)",
            "﴾͡๏̯͡๏﴿",
            "(￣■￣;)!?",
            "▐ ˵ ͠° (oo) °͠ ˵ ▐",
            "(-_-)ゞ゛",
        ]
    elif input_str in "dead":
        emoticons = [
            "(✖╭╮✖)",
            "✖‿✖",
            "(+_+)",
            "(✖﹏✖)",
            "∑(✘Д✘๑)",
        ]
    elif input_str in "sad":
        emoticons = [
            "(＠´＿｀＠)",
            "⊙︿⊙",
            "(▰˘︹˘▰)",
            "●︿●",
            "(　´_ﾉ` )",
            "彡(-_-;)彡",
        ]
    elif input_str in "dog":
        emoticons = [
            "-ᄒᴥᄒ-",
            "◖⚆ᴥ⚆◗",
        ]
    else:
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "¯\_(ツ)_/¯",
            "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
            "ʕ•ᴥ•ʔ",
            "(▀ Ĺ̯▀   )",
            "(ง ͠° ͟ل͜ ͡°)ง",
            "༼ つ ◕_◕ ༽つ",
            "ಠ_ಠ",
            "(☞ ͡° ͜ʖ ͡°)☞",
            "¯\_༼ ି ~ ି ༽_/¯",
            "c༼ ͡° ͜ʖ ͡° ༽⊃",
        ]
    index = random.randint(0, len(emoticons))
    output_str = emoticons[index]
    await edit_or_reply(event, output_str)


import asyncio
import random

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd


@jarvis.on(j_cmd(pattern=r"lol", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"lol", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    await edit_or_reply(event, "Typing...")

    await asyncio.sleep(2)

    x = random.randrange(1, 28)
    if x == 1:
        await event.edit(";l;;o;;l;")
    if x == 2:
        await event.edit("lloll")
    if x == 3:
        await event.edit(";l;o;l;")
    if x == 4:
        await event.edit("lo/;l")
    if x == 5:
        await event.edit("/lol/*")
    if x == 6:
        await event.edit("\lol")
    if x == 7:
        await event.edit("lllolll")
    if x == 8:
        await event.edit("l-o-l")
    if x == 9:
        await event.edit("-l;o;l-")
    if x == 10:
        await event.edit("[lol]")
    if x == 11:
        await event.edit(";;loo;l")
    if x == 12:
        await event.edit("l.o.l")
    if x == 13:
        await event.edit(";l.o.l;")
    if x == 14:
        await event.edit("llooll")
    if x == 15:
        await event.edit("phuck.lol")
    if x == 16:
        await event.edit("/l:o;l.")
    if x == 17:
        await event.edit("ll;oo;lll")
    if x == 18:
        await event.edit("loooooooooooool")
    if x == 19:
        await event.edit("lollll.lll;lol")
    if x == 20:
        await event.edit(";;;llloo;oo;ollll;;")
    if x == 21:
        await event.edit("lol me laughed hehehe")
    if x == 22:
        await event.edit("tum haso ab lol")
    if x == 23:
        await event.edit(":l:o:l:")
    if x == 24:
        await event.edit("l-o+l")
    if x == 25:
        await event.edit("l+o=l")
    if x == 26:
        await event.edit("l|o|l")
    if x == 27:
        await event.edit("hola lol")
    if x == 28:
        await event.edit("llllllllllllllooooooooooollllllllll")


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd("ok"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "ok":
    await event.edit("ok")
    animation_chars = [
        "OK",
        "BOSS",
        "OK MAN",
        "OK BITCH",
        "OK IDIOT",
        "OK MAM",
        "OK SIR",
        "GO AND SAY OK",
        "OK LOL",
        "YAA OK",
        "OK",
        "Boss",
        "Yeahhhhhh",
        "O",
        "K",
        "Ok Boss! 😇",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


import asyncio

from telethon import events


@jarvis.on(j_cmd(pattern="plane", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("✈-------------")
    await event.edit("-✈------------")
    await event.edit("--✈-----------")
    await event.edit("---✈----------")
    await event.edit("----✈---------")
    await event.edit("-----✈--------")
    await event.edit("------✈-------")
    await event.edit("-------✈------")
    await event.edit("--------✈-----")
    await event.edit("---------✈----")
    await event.edit("----------✈---")
    await event.edit("-----------✈--")
    await event.edit("------------✈-")
    await event.edit("-------------✈")
    await asyncio.sleep(3)
    await event.delete()


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern=r"quickheal"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group("Scanning")

    await event.edit(input_str)

    animation_chars = [
        "`Downloading File..`",
        "`File Downloaded....`",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nReault: No Virus Found...`",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


"""
custom riddle questions...
Syntax: .rdl
  inspired by : conversationqt.py
  made by : @Hacker_The_Unknown | Noob
  edited by : @Hacker_The_Unknown | Noob
  
  # KANG wITH CREDIT
"""

import asyncio
import random

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern=r"rdl", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Selecting the best riddle for you...")
    await asyncio.sleep(2)
    x = random.randrange(1, 60)
    if x == 1:
        await event.edit('`"What has hands but can not clap?"`')
    if x == 2:
        await event.edit(
            '`"If an electric train is traveling south, which way is the smoke going?"`'
        )
    if x == 3:
        await event.edit(
            '`"A monkey, a squirrel, and a bird are racing to the top of a coconut tree. Who will get the banana first, the monkey, the squirrel, or the bird?"`'
        )
    if x == 4:
        await event.edit('`"What can you hear but not touch or see?"`')
    if x == 5:
        await event.edit(
            '`"Sheets of paper that tell new stories each day.What is it?"`'
        )
    if x == 6:
        await event.edit('`"I am milky white and scares people. What am I?"`')
    if x == 7:
        await event.edit('`"What is the only chain we can eat?"`')
    if x == 8:
        await event.edit(
            '`"I am beautiful, up in the sky. I am magical, yet I cannot fly. To people I bring luck, to some people, riches. The boy at my end does whatever he wishes. What am I?"`'
        )
    if x == 9:
        await event.edit(
            '`"I can whistle, I can howl, I can scream, And I can whisper, But I do not speak. What am I?"`'
        )
    if x == 10:
        await event.edit('`"What does someone else have to take before you can get?"`')
    if x == 11:
        await event.edit(
            '`"What number do you get when you multiply all of the numbers on a telephone’s number pad?"`'
        )
    if x == 12:
        await event.edit('`"What do you call a witch that lives in the sand?"`')
    if x == 13:
        await event.edit(
            '`"I come in many shapes, sizes, and colors. I stick to many surfaces but I am, in fact, not sticky at all. What am I?"`'
        )
    if x == 14:
        await event.edit('`"What kind of table has no legs?"`')
    if x == 15:
        await event.edit(
            '`"This type of food, which is a fungus, is often served on supreme pizza, in spaghetti and in a particular "cream of" style soup. What is it?"`'
        )
    if x == 16:
        await event.edit(
            '`"If you drop me I am sure to crack. But give me a smile and I will always smile back. What is it?"`'
        )
    if x == 17:
        await event.edit(
            '`"I weaken all men for hours each day. I show you strange visions while you are away. I take you by night, by day take you back. None suffer to have me, but do from my lack."`'
        )
    if x == 18:
        await event.edit('`"What is between heaven and earth?"`')
    if x == 19:
        await event.edit('`"A white horned symbol of purity and grace. What is it?"`')
    if x == 20:
        await event.edit(
            '`"It speaks without a tongue, and listens without ears. What is it?"`'
        )
    if x == 21:
        await event.edit(
            '`"I belong in the month of December, but not in any other month. What am I?"`'
        )
    if x == 22:
        await event.edit('`"What kind of men are always above board?"`')
    if x == 23:
        await event.edit(
            '`"Three men are on a boat. The boat sinks but only two people get their hair wet. Why?"`'
        )
    if x == 24:
        await event.edit('`"What has 13 hearts but no organs?"`')
    if x == 25:
        await event.edit('`"Where can you find success before work?"`')
    if x == 26:
        await event.edit('`"Live-in relation or marriage, what do you prefer?"`')
    if x == 27:
        await event.edit(
            '`"I am deaf, dumb and blind. But I am very shiny and always speak the truth. Who am I?"`'
        )
    if x == 28:
        await event.edit(
            '`"I am transparent. You can see and feel me, but you cannot hold me. I always take the shape of my container. Who am I?"`'
        )
    if x == 29:
        await event.edit(
            '`"Adam is 13 years old in 1980. In 1985 he is 8 years old. How?"`'
        )
    if x == 30:
        await event.edit(
            '`"I am a six letter word. Subtract one letter and twelve will remain. Who am I?"`'
        )
    if x == 31:
        await event.edit(
            '`"I am a part of your body. You can hold me in your left hand but not in your right hand. Who am I?"`'
        )
    if x == 32:
        await event.edit('`"I go around the world, but always stay in a corner."`')
    if x == 33:
        await event.edit(
            '`"When I am opened, I am U-shaped but when I am closed I am V-shaped. Who am I?"`'
        )
    if x == 34:
        await event.edit('`"Which room has no doors or windows?"`')
    if x == 35:
        await event.edit(
            '`"How many times is the alphabet "a" used while writing the spelling of each number from 1 to 500?"`'
        )
    if x == 36:
        await event.edit(
            '`"I have a mouth but I can’t speak, I can run but I can’t walk. Who am I?"`'
        )
    if x == 37:
        await event.edit(
            '`"6   15   18   20   ?   =   FORTY. What number relplaces the question mark?"`'
        )
    if x == 38:
        await event.edit(
            '`"We are 3 friends. Our product and our sum always give the same answer. Who are we?"`'
        )
    if x == 39:
        await event.edit(
            '`"When I get multiplied by any number the sum of the figures in the product is always me. Who I am?"`'
        )
    if x == 40:
        await event.edit('`"Find out the difference between 18°C and 64.4°F."`')
    if x == 41:
        await event.edit(
            '`"I have one letter but my name is spelled with eight. What am I?"`'
        )
    if x == 42:
        await event.edit(
            '`"Swap one letter from each of the words "Right" and "Blight" to make two related words."`'
        )
    if x == 43:
        await event.edit(
            '`"I am a four letter word. I am an animal. You use me to call your dear ones. Who am I?"`'
        )
    if x == 44:
        await event.edit(
            '`"You need to spend a night in a building where there is no power. There are three rooms in this building. On the door of each room there are three different signs. One says "Lions Inside - anyone goes inside becomes their supper", the second one says "Open the door and a machine gun starts firing" and the third one says "Electric Room - touch anything and you will die". Which room would you choose?"`'
        )
    if x == 45:
        await event.edit(
            '`"I am pronounced with only one letter but written with three letters. Two different letters are used to write me. My color varies from black, blue, green, brown, grey etc. Who am I?"`'
        )
    if x == 46:
        await event.edit(
            '`"I am in the beginning of sorrow and sadness. You will find me in happiness also. You will find me in sun and stars but not in moon. I am in summer and spring but not in fall or winter. Who am I?"`'
        )
    if x == 47:
        await event.edit('`"What can be imagine  but can’t be touched ??"`')
    if x == 48:
        await event.edit('`"What smells bad when living but smells good when dead ?"`')
    if x == 49:
        await event.edit(
            '`"Which time of a day when written in capital letters reads the same from all the four sides?"`'
        )
    if x == 50:
        await event.edit('`"You can catch me but cannot throw me. Who am I?"`')
    if x == 51:
        await event.edit(
            '`"When I get multiplied by any number, the sum of the figures in the product is always me. What am I?"`'
        )
    if x == 52:
        await event.edit(
            '`"I can fill up an entire room and still not take up any space. Who am I?"`'
        )
    if x == 53:
        await event.edit(
            '`"I help you in fixing your appointments and important schedules. You use me everyday several times. Still you keep on changing me every month. Who am I?"`'
        )
    if x == 54:
        await event.edit(
            '`"I look like a pearl. Clouds are my grandparents. I am very delicate. I die as soon as anybody touches me. Who am I?"`'
        )
    if x == 55:
        await event.edit(
            '`"I am an eight letter standard word used by almost everybody. If you take away two alphabets from me I will make a logical sequence. Who am I?"`'
        )
    if x == 56:
        await event.edit(
            '`"I am a two digit even number. I am a square of a number, and also a cube of another number. Who am I?"`'
        )
    if x == 57:
        await event.edit(
            '`"I am a seven letter word. I am very heavy. Take away two letters from me and you will get 8. Take away one letter from me and you will get 80. Who am I?"`'
        )

    if x == 58:
        await event.edit(
            '`"I am soft and transparent. I am so small that you can keep me on your fingers. I have no light but I help you to see the beautiful world. I improve your vision only when I come in contact with you. Who am I?"`'
        )
    if x == 59:
        await event.edit(
            '`"I have three wings. At times I have 4 wings but still I cannot fly. I can rotate but I can’t move from one place to other. People always relax in my company. Who am I?"`'
        )
    if x == 60:
        await event.edit('`"What can touch someone once and last them a lifetime?"`')


import random

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd


@jarvis.on(j_cmd(pattern="coin ?(.*)"))
@jarvis.on(sudo_cmd(pattern="coin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    r = random.randint(1, 100)
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r % 2 == 1:
        if input_str == "heads":
            await edit_or_reply(
                event, "The coin landed on: **Heads**. \n You were correct."
            )
        elif input_str == "tails":
            await event.edit(
                "The coin landed on: **Heads**. \n You weren't correct, try again ..."
            )
        else:
            await event.edit("The coin landed on: **Heads**.")
    elif r % 2 == 0:
        if input_str == "tails":
            await event.edit("The coin landed on: **Tails**. \n You were correct.")
        elif input_str == "heads":
            await event.edit(
                "The coin landed on: **Tails**. \n You weren't correct, try again ..."
            )
        else:
            await event.edit("The coin landed on: **Tails**.")
    else:
        await event.edit("¯\_(ツ)_/¯")


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern=r"fleave"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 17)

    # input_str = event.pattern_match.group(1)

    # if input_str == "fleave":

    await event.edit("fleave")

    animation_chars = [
        "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
        "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
        "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
        "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
        "**Chat Message Exported To** `./Inpu/`",
        "**Chat Message Exported To** `./Inpu/homework/`",
        "**Chat Message Exported To** `./Inpu/homework/groupchat.txt`",
        "__Legend is leaving this chat.....! ",
        "__Legend is leaving this chat.....!",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 17])


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern="cry"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 103)

    await event.edit("crying")

    animation_chars = [
        ";__",
        ";___",
        ";____",
        ";_____",
        ";______",
        ";_______",
        ";________",
        ";__________",
        ";____________",
        ";______________",
        ";________________",
        ";__________________",
        ";____________________",
        ";______________________",
        ";________________________",
        ";_________________________",
        ";_________________________",
        ";________________________",
        ";_______________________",
        ";______________________",
        ";_____________________",
        ";____________________",
        ";___________________",
        ";__________________",
        ";_________________",
        ";________________",
        ";_______________",
        ";_____________",
        ";___________",
        ";_________",
        ";_______",
        ";_____",
        ";____",
        ";___",
        ";__",
        ";You made me `CRY`",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd


@jarvis.on(j_cmd("scan ?(.*)"))
@jarvis.on(sudo_cmd("scan ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit_or_reply("```reply to a media message```")
        return
    chat = "@DrWebBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit(" `Sliding my tip, of fingers over it`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=161163358)
            )
            await jarvis.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            if response.text.startswith("Select"):
                await event.edit("`Please go to` @DrWebBot `and select your language.`")
            else:
                await event.edit(
                    f"**Antivirus scan was completed. I got dem final results.**\n {response.message.message}"
                )


"""COMMAND : .join , .pay , .work , .push , .aag , .climb"""
from telethon.tl.types import ChannelParticipantsAdmins

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern="join"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`━━━━━┓ \n┓┓┓┓┓┃\n┓┓┓┓┓┃　ヽ○ノ ⇦ Me When You Joined \n┓┓┓┓┓┃.     /　 \n┓┓┓┓┓┃ ノ) \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@jarvis.on(j_cmd(pattern="pay"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`█▀▀▀▀▀█░▀▀░░░█░░░░█▀▀▀▀▀█\n█░███░█░█▄░█▀▀░▄▄░█░███░█\n█░▀▀▀░█░▀█▀▀▄▀█▀▀░█░▀▀▀░█\n▀▀▀▀▀▀▀░▀▄▀▄▀▄█▄▀░▀▀▀▀▀▀▀\n█▀█▀▄▄▀░█▄░░░▀▀░▄█░▄▀█▀░▀\n░█▄▀░▄▀▀░░░▄▄▄█░▀▄▄▄▀▄▄▀▄\n░░▀█░▀▀▀▀▀▄█░▄░████ ██▀█▄\n▄▀█░░▄▀█▀█▀░█▄▀░▀█▄██▀░█▄\n░░▀▀▀░▀░█▄▀▀▄▄░▄█▀▀▀█░█▀▀\n█▀▀▀▀▀█░░██▀█░░▄█░▀░█▄░██\n█░███░█░▄▀█▀██▄▄▀▀█▀█▄░▄▄\n█░▀▀▀░█░█░░▀▀▀░█░▀▀▀▀▄█▀░\n▀▀▀▀▀▀▀░▀▀░░▀░▀░░░▀▀░▀▀▀▀`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@jarvis.on(j_cmd(pattern="climb"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`😏/\n/▌ \n/ \\n████\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\😦\n╬╬/▌\n╬╬/\`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@jarvis.on(j_cmd(pattern="aag"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`😲💨  🔥\n/|\     🔥🔥\n/ \   🔥🔥🔥`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@jarvis.on(j_cmd(pattern="push"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`.      😎\n          |\👐\n         / \\\n━━━━━┓ ＼＼ \n┓┓┓┓┓┃\n┓┓┓┓┓┃ ヽ😩ノ\n┓┓┓┓┓┃ 　 /　\n┓┓┓┓┓┃  ノ)　 \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@jarvis.on(j_cmd(pattern="work"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`📔📚             📚\n📓📚📖  😫  📚📚📓\n📕📚📚  📝  📗💻📘\n📖⁣📖📖📖📖📖📖📖📖`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern="watt"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 15)

    await event.edit("watt!!!")

    animation_chars = [".😎", ".😎🤏", ".😳🕶🤏", ".😎", ".😎🤏", ".😳🕶🤏", "Whattt!!!"]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd("think"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 288)

    # await event.edit(input_str)
    await event.edit("thinking")
    animation_chars = [
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING... 🤔",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 72])


import asyncio
from collections import deque

from telethon import events


@jarvis.on(j_cmd(pattern="rainl", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("☁️⛈Ř/~\İŇ🌬⚡🌪"))
    for _ in range(100):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


import asyncio

from jarvis import ALIVE_NAME
from jarvis.utils import j_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Jarvis Userbot"


@jarvis.on(j_cmd(pattern=r"police"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    await event.edit("Police")

    animation_chars = [
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "[JARVIS](https://www.github.com/jaris-works/jarvisuserbot) **Jarvis Police Service Here**",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])


import asyncio
import random

from jarvis.utils import j_cmd, edit_or_reply, sudo_cmd


@jarvis.on(j_cmd(pattern=f"tip", outgoing=True))
@jarvis.on(sudo_cmd(pattern=f"tip", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "Well, let me give you a life-pro tip... 😉")
    await asyncio.sleep(2)
    x = random.randrange(1, 87)
    if x == 1:
        await event.edit(
            "`\"Before telling your landlord you're moving, ask them to fix anything broken that you're worried you might get charged for. They often will, and then when you move out they won't be able to take it out of your security deposit.\"`"
        )
    if x == 2:
        await event.edit(
            '`"Walking before solving a problem improves your creativity by an average of 60%."`'
        )
    if x == 3:

        await event.edit(
            '`"Wake up a little earlier than your alarm? Don’t go back to bed and wait for your alarm. Waking up naturally instead of to some sort of stimuli will help you get off to a better and healthier start to your day."`'
        )

    if x == 4:

        await event.edit(
            '`"Act like your future self is a real person. So when you see a chore that needs to be done, you can say "I\'ll do this now to be nice to my future self". Helps motivate to get things done because you\'re doing work for someone you want to help."`'
        )

    if x == 5:

        await event.edit(
            '`"Think of purchases as a percentage of your budget/account balance rather than their actual cost."`'
        )

    if x == 6:

        await event.edit(
            '`"Counting on fingers is a vital part of learning math, and children that do it from an early age develop much better math skills than those who have been told not to."`'
        )

    if x == 7:

        await event.edit(
            '`"There are just some things in life you can’t control or you’ll never know the real reason why. The only thing you can do is accept it and move on. Part of happiness is accepting the past happened or being proud of it."`'
        )

    if x == 8:

        await event.edit(
            '`"Make a recording of your voice with a sweet message or telling a story. If anything happens to you, your loved ones will greatly appreciate being able to listen to your voice again."`'
        )

    if x == 9:

        await event.edit(
            "`\"If someone is treating you to a meal and you're wondering how much you should spend, ask them what they're ordering to get a better idea of the range.\"`"
        )

    if x == 10:

        await event.edit(
            '`"Never leave water bottles, reading glasses, or anything else that can focus light in a spot that could get direct sunlight. A significant number of house/vehicle fires happen every year because of this."`'
        )

    if x == 11:

        await event.edit(
            '`"If you reach out to someone for help on a technical issue and they spend their valuable time helping you but are unable to resolve it, always try and let them know how it got resolved so they can help the next person with the same issue."`'
        )

    if x == 12:

        await event.edit(
            '`"If you find information on the internet that you may need again in the future, print the page to a PDF digital file. There is no guarantee that the page will be available again in the future, and now you will have a digital copy for future reference."`'
        )

    if x == 13:

        await event.edit(
            '`"If you want to learn another language, watch children’s shows in that language to pick up on it quicker."`'
        )

    if x == 14:

        await event.edit(
            '`"If you want to separate some pdf pages without using any new software. you can open the pdf file in chrome then click on print then select custom pages option, and finally choose to save as pdf."`'
        )

    if x == 15:

        await event.edit(
            '`"If you’re ever in the heat of an argument, always act like you’re being recorded. This helps you from saying things you don’t mean and could regret later."`'
        )

    if x == 16:

        await event.edit(
            '`"Make music playlists during times in your life when good things are happening and you are experiencing good feelings. Then when you\'re down later in life listen to those playlists to instantly feel better, and feel those good emotions again."`'
        )

    if x == 17:

        await event.edit(
            '`"When going on a first date, think in terms of "will I like them?" instead of "will they like me?""`'
        )

    if x == 18:

        await event.edit(
            '`"When researching things to do for your next leisure travel. Include \<location\> tourism scam into your search. All tourist heavy areas will have their own scams. This should not dampen your excitement but heighten your knowledge so your vacation will be more enjoyable."`'
        )

    if x == 19:

        await event.edit(
            '`"Just because you’ve know that person for years doesn’t mean you should stay friends with them. A toxic friend need to be cut out of your life."`'
        )

    if x == 20:

        await event.edit(
            '`"Tired of all the ads in one of the free (offline) game apps you’re playing? Go to your settings and turn off the apps access to cellular data. Enjoy the ad free game play!"`'
        )

    if x == 21:

        await event.edit(
            '`"Treat your monthly savings goal like a bill. At the end of the month, hold yourself accountable to \“pay it off\” like you would your rent or your utilities. This will keep you on track for your savings goals."`'
        )

    if x == 22:

        await event.edit(
            '`"If you need to wait until your boss is in a good mood to ask for something as simple as time off, you\'re in a toxic work environment and you need to take steps to exit sooner than later."`'
        )

    if x == 23:

        await event.edit(
            '`"When debating someone on a heated issue, start by looking for something to agree with them on. The rest of the conversation will be a lot less hostile if you establish common ground."`'
        )

    if x == 24:

        await event.edit(
            '`"Record random conversations with your parents and grandparents. Someday hearing their voice may be priceless to you."`'
        )

    if x == 25:

        await event.edit(
            "`\"If you're a student planning on your career, look up postings of your dream job, find the skills and qualifications you'll need, then work backwards from there.\"`"
        )

    if x == 26:

        await event.edit(
            "`\"If someone asks how your weekend was, assume they're really wanting to tell you about theirs. Keep your answer short and enthusiastically ask about theirs. It'll make their day.\"`"
        )

    if x == 27:

        await event.edit(
            '`"When traveling with a friend or family member, don’t be afraid to suggest breaking off to each do your own things for a day. Going solo can be enjoyable (eat/go wherever want at your own pace), plus it reduces you being sick of each other by the end of the trip."`'
        )

    if x == 28:

        await event.edit(
            '`"If you’ve got some free time and you’re planning on spending it watching tv/playing video games, etc. make yourself go on a short walk or do some brief exercise beforehand. You’ll probably end up going longer than you planned and you’ll feel better about relaxing after."`'
        )

    if x == 29:

        await event.edit(
            '`"When you get a new notebook, leave the first page blank. When you finish using the notebook, you can number the pages and use the first page as a table of contents."`'
        )

    if x == 30:

        await event.edit(
            '`"Don’t delete old playlists if you can prevent it; years later you can listen and not only rediscover music you were into but also experience whatever emotion you had associated with your tunes at the time."`'
        )

    if x == 31:

        await event.edit(
            '`"No matter how small the job is, wear correct masks/respirators/eye or ear protection. Your future self will thank you."`'
        )

    if x == 32:

        await event.edit(
            '`"Getting angry with people for making mistakes doesn\'t teach them not to make mistakes, it just teaches them to hide them."`'
        )

    if x == 33:

        await event.edit(
            "`\"When making conversation with someone you've just met, ask them what they've been listening to lately, rather than what their favorite kind of music is - it's fresh in their mind and they won't have to pick favorites on the spot.\"`"
        )

    if x == 34:

        await event.edit(
            '`"Learn to do -- and enjoy -- things by yourself. You\'re going to miss out on a lot of fun if you keep waiting for someone else to accompany you."`'
        )

    if x == 35:

        await event.edit(
            '`"If you want someone to really listen to you, then start the conversation with "I shouldn\'t be telling you this, but...""`'
        )

    if x == 36:

        await event.edit(
            '`"Do you not like having bitter coffee but don\'t want to add sugar for dietary or other reasons? Add a pinch of salt instead, it removes the bitter taste while not making your coffee taste salty."`'
        )

    if x == 37:

        await event.edit(
            '`"Don\'t choose a common sound for your alarm clock to wake up. If you hear your alarm clock sound any other time, you will get anxiety."`'
        )

    if x == 38:

        await event.edit(
            '`"Keep your water bottle near you and your alarm far from you in the morning for a great start to the day!"`'
        )

    if x == 39:

        await event.edit(
            '`"If you borrow money from someone, don’t let it get to the point that he/she has to ask for it back. It sucks for both. If you can’t repay now, show intent by paying what you can and keeping the other person posted often"`'
        )

    if x == 40:

        await event.edit(
            '`"Don\'t brag about knowledge you just acquired, simply explain it. You will learn humility, plus people often like to learn new things."`'
        )

    if x == 41:

        await event.edit(
            '`"If you have a favorite movie you’ve seen several (or hundreds) of times, try watching it with subtitles/closed captioning on. You might be surprised just how many lines you heard wrong or missed entirely."`'
        )

    if x == 42:

        await event.edit(
            '`"Write down great ideas when you get them; do that right away. You think you will never forget them, but you almost always will."`'
        )

    if x == 43:

        await event.edit(
            '`"If you’re not sure whether someone is waving at you or someone behind you, just smile at them. \n(It’ll save you the very awkward feeling of receiving a greeting meant for someone else.)"`'
        )

    if x == 44:

        await event.edit(
            '`"If you want to offer a deep and memorable compliment, ask someone how they did something. It gives them the opportunity to tell their story, and shows your genuine interest."`'
        )

    if x == 45:

        await event.edit(
            '`"Don’t hide the things that make you unique. If you smile a certain way or have any thing about you that is not normal, be confident with it. People will find it cute or attractive because it makes you special."`'
        )

    if x == 46:

        await event.edit(
            '`"When someone only remove one ear pod to talk to you, they most probably don\'t want a lengthy conversation."`'
        )

    if x == 47:

        await event.edit(
            "`\"If you haven't used your voice in a while (sleeping, lonely, etc) and suddenly need to take a phone call, hum for a few seconds prior. Your vocal cords won't let you down.\"`"
        )

    if x == 48:

        await event.edit(
            '`"Open chip bags upside down. They\'ve been sitting upright most of their lives which makes the seasoning settle to the bottom of the bag."`'
        )

    if x == 49:

        await event.edit(
            '`"If you tell people there is an invisible man in the sky that created the entire universe, most will believe you; if you tell them the paint is wet, most will touch it to be sure."`'
        )

    if x == 50:

        await event.edit(
            '`"When asked online to confirm "I am not a robot", if you long press on the tick box and release, you will not be asked to complete the "click all store front" etc tests."`'
        )

    if x == 51:

        await event.edit(
            '`"Buy yourself a good pillow. You use it every night and the difference between a good pillow and a stack of cheap ones is almost immediately noticeable."`'
        )

    if x == 52:

        await event.edit(
            '`"If you want your man to win in this world, treat him as a king at home, the world by itself call you a queen!"`'
        )

    if x == 53:

        await event.edit(
            '`"Be mindful of poorer friends when suggesting splitting the bill equally in a restaurant. Some people will choose cheaper options because they\'re on a budget."`'
        )

    if x == 54:

        await event.edit(
            '`"When you are trying to resolve an issue where someone else made an error, put the focus on the error and not the person. Example of this: Instead of saying, \“You didn’t send the attachment,\” I say, \“The attachment didn’t come through, please try sending it again.\”"`'
        )

    if x == 55:

        await event.edit(
            '`"Buy a small bottle of perfume you have never tried on before going for a vacation and use it for while you\'re there. At any point after your vacation, you get a sniff of it, it brings back those memories instantly. Because scents are among the most powerful memory triggers."`'
        )

    if x == 56:

        await event.edit(
            "`\"If someone wishes you Merry Christmas and you don't celebrate Christmas, just say thank you. There's no need to tell them you don't celebrate. It just makes things awkward.\"`"
        )

    if x == 57:

        await event.edit(
            '`"When trying to focus on something (writing, revising, reading) listen to music with no words. This allows you to block out unwanted sound and having no lyrics can stop you from being distracted."`'
        )

    if x == 58:

        await event.edit(
            '`"If you are quitting a vice (smoking, drinking, etc.) treat yourself with the money you are saving. It makes quitting easier."`'
        )

    if x == 59:

        await event.edit(
            '`"Someone who likes you will often automatically look at you when they laugh or find something funny."`'
        )

    if x == 60:

        await event.edit(
            '`"Never shake spices over a hot pan. The steam will enter the bottle causing the spice to go hard."`'
        )

    if x == 61:

        await event.edit(
            '`"When starting a new change in your life such as going to the gym or quitting smoking, avoid telling friends or family. Their positive feedback can give you a false feeling of accomplishment tricking you into thinking you have already succeeded which can hinder your efforts to change."`'
        )

    if x == 62:

        await event.edit(
            '`"If you are composing an important message, do not enter the recipient until you have finished composing it so that you do not accidentally send an incomplete message."`'
        )

    if x == 63:

        await event.edit(
            '`"If you are nervous walking into a new place with a group of people, make sure you are the first to the building. You can hold the door for everyone else making yourself look kind, yet you will be the last one in and can follow everyone elses lead."`'
        )

    if x == 2:

        await event.edit(
            '`"If you\'re double checking a number or a sequence, read it backwards to avoid making the same mistake twice."`'
        )

    if x == 64:

        await event.edit(
            '`"Take photos of your parents doing things they do every day. When you get older, they will bring back memories more than any posed pic ever could."`'
        )

    if x == 65:

        await event.edit(
            "`\"If you're in a job interview and you're offered a glass of water, always accept. If you're asked a tough question, you can take a sip and get yourself some extra seconds to think of a response.\"`"
        )

    if x == 66:

        await event.edit(
            "`\"If you make a mistake, admit to the mistake, apologize, and explain what steps you'll take to prevent it from happening again in the future. It's very hard for people to yell at you if you've done that.\"`"
        )

    if x == 67:

        await event.edit(
            '`"Universities like MIT offer free online courses for subjects like Computer Science, Engineering, Psychology and more that include full lectures and exams."`'
        )

    if x == 68:

        await event.edit(
            "`\"Treat another persons phone or computer like you would their diary. Don't even touch it unless they allow you to. It's always for the best.\"`"
        )

    if x == 69:

        await event.edit(
            "`\"Don't undervalue yourself when deciding whether or not to apply for a new job. It's up to the person doing the hiring to determine if you are what they're looking for, and the only way to guarantee that you won't get the job is if you don't apply for it.\"`"
        )

    if x == 70:

        await event.edit(
            '`"When drying clothes in the sun, turn them inside out so the colours don’t fade in the sunlight."`'
        )

    if x == 71:

        await event.edit(
            '`"To listen to music on your phone via YouTube in the background, use the Chrome browser, go to the video, and request desktop site. This will allow you to listen anywhere on the phone."`'
        )

    if x == 72:

        await event.edit(
            '`"Whenever your smoke alarm goes off, give your dog a treat. They\'ll associate the alarm with the treat; so when the alarm goes off for real, your dog will come right to you."`'
        )

    if x == 73:

        await event.edit(
            '`"You never know what is taking place in a stranger\'s life. Try to be patient and passive if some seems to be "overreacting"."`'
        )

    if x == 74:

        await event.edit(
            '`"Everybody is genious of its own. But if you judge a fish by its ability to climb a tree rather than swimming, she will felt whole life like dumb. So master your field and recognise it very well rather than going after the blind suspections."`'
        )

    if x == 75:

        await event.edit(
            '`"Search a beautiful heart, not a beautiful face. Beautiful things are not always good, but good things are always beautiful."`'
        )

    if x == 76:

        await event.edit(
            '`"It\'s better to cross the line and suffer the consequences than to just stare at the line for the rest of your life."`'
        )

    if x == 77:

        await event.edit(
            '`"Rather than shushing someone who’s speaking too loudly, try just talking to them in a much quieter voice. They often pick up on the contrast in volume, and self-correct without feeling attacked."`'
        )

    if x == 78:

        await event.edit(
            '`"If there are no chances for job growth or improvement - it\'s time to move on. You are worth more the more you learn. Otherwise you are getting paid less the more you know."`'
        )

    if x == 79:

        await event.edit(
            '`"If you burn food to the bottom of a pot and can\'t scrub it out, put the pot back on the stove and boil water in it. It will loosen the burnt food and make it easier to clean."`'
        )

    if x == 80:

        await event.edit(
            '`"When filling out applications online, make sure you copy responses which typically take a long time to write, and paste them to a text file. You never know when you could get a server timeout."`'
        )

    if x == 81:

        await event.edit(
            '`"Being positive doesn’t mean we don’t get negative thoughts. It just means that we don’t allow those thoughts to control our life."`'
        )

    if x == 82:

        await event.edit(
            "`\"If you share an 'inside joke' with a friend around other people, just let them know what it is even if they won't get it. People don't appreciate being excluded.\"`"
        )

    if x == 83:

        await event.edit(
            '`"Never make fun of someone if they mispronounce a word. It means they learned it by reading."`'
        )

    if x == 84:
        await event.edit(
            '`"If a service dog without a person approaches you, it means that the person is in need of help."`'
        )
    if x == 85:
        await event.edit(
            '`"When taking a taxi ALWAYS get a receipt even if you don\'t need one. That way if you happen to accidentally leave a personal belonging behind you will have the company name and taxi number."`'
        )
    if x == 86:
        await event.edit(
            "`\"If you're buying a home printer for occasional use, get a laser printer; they're more expensive up front but way more economical in the long run.\"`"
        )
    if x == 87:
        await event.edit(
            '`"Go for that run, no one is looking at you, don\'t overthink it, do it!"`'
        )


import asyncio
import time
from collections import deque

from telethon.tl.functions.channels import LeaveChannelRequest

from jarvis import CMD_HELP
from jarvis.utils import j_cmd


@jarvis.on(j_cmd("leave"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I iz Leaving dis Lol Group kek!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await jarvis(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("`But Boss! This is Not A Chat`")


@jarvis.on(j_cmd(";__;"))
# @register(outgoing=True, pattern="^;__;$")
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)


@jarvis.on(j_cmd("yo"))
# @register(outgoing=True, pattern="^yo$")
async def Ooo(e):
    t = "yo"
    for j in range(15):
        t = t[:-1] + "oo"
        await e.edit(t)


@jarvis.on(j_cmd("oof"))
# @register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)


@jarvis.on(j_cmd("ccry"))
# @register(outgoing=True, pattern="^.cry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")


@jarvis.on(j_cmd("fp"))
# @register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")


@jarvis.on(j_cmd("moon"))
# @register(outgoing=True, pattern="^.mmoon$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@jarvis.on(j_cmd("source"))
# @register(outgoing=True, pattern="^.source$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://jarvisuserbot.gitbook.io/jarvisuserbot/")


@jarvis.on(j_cmd("readme"))
# @register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://jarvisuserbot.gitbook.io/jarvisuserbot/")


@jarvis.on(j_cmd("hheart"))
# @register(outgoing=True, pattern="^.heart$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern=r"macos"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    await event.edit("Mac")

    animation_chars = [
        "`Connecting To Hackintosh...`",
        "`Initiating Hackintosh Login.`",
        "`Loading Hackintosh... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Hackintosh... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Hackintosh... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Hackintosh... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Hackintosh... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Hackintosh... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Hackintosh... 89%\n█████████████████████▒▒▒▒ `",
        "`Loading Hackintosh... 100%\n█████████████████████████ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Hackintosh`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


@jarvis.on(j_cmd(pattern=r"windows"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    await event.edit("Windows")

    animation_chars = [
        "`Connecting To Windows 10...`",
        "`Initiating Windows 10 Login.`",
        "`Loading Windows 10... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 89%\n█████████████████████▒▒▒▒ `",
        "`Loading Windows 10... 100%\n█████████████████████████ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Windows 10`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


@jarvis.on(j_cmd(pattern=r"linux"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    await event.edit("Linux")

    animation_chars = [
        "`Connecting To Linux...`",
        "`Initiating Linux Login.`",
        "`Loading Linux... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Linux... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Linux... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Linux... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Linux... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Linux... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Linux... 89%\n█████████████████████▒▒▒▒ `",
        "`Loading Linux... 100%\n█████████████████████████ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Linux`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


@jarvis.on(j_cmd(pattern=r"stock"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    await event.edit("Stock")

    animation_chars = [
        "`Connecting To Symbian OS...`",
        "`Initiating Symbian OS Login.`",
        "`Loading Symbian OS... 0%\n█████████████████████████ `",
        "`Loading Symbian OS... 3%\n█████████████████████▒▒▒▒ `",
        "`Loading Symbian OS... 9%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Symbian OS... 23%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Symbian OS... 39%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Symbian OS... 69%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Symbian OS... 89%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Symbian OS... 100%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Symbian OS`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


@jarvis.on(j_cmd(pattern=r"os"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 7)

    await event.edit("OS")

    animation_chars = [
        "`Scanning OS...`",
        "`Scanning OS......`",
        "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\n☑️ `.macos`\n☑️ `.windows`\n☑️ `.linux`\n☑️ `.stock`",
        "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\n✅ `.macos`\n☑️ `.windows`\n☑️ `.linux`\n☑️ `.stock`",
        "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\n✅ `.macos`\n✅ `.windows`\n☑️ `.linux`\n☑️ `.stock`",
        "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\n✅ `.macos`\n✅ `.windows`\n✅ `.linux`\n☑️ `.stock`",
        "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\n✅ `.macos`\n✅ `.windows`\n✅ `.linux`\n✅ `.stock`\n\nDeveloped By: @JarvisOT",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 7])


from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern=r"shout"))
async def shout(args):
    if args.fwd_from:
        return
    else:
        msg = "```"
        messagestr = args.text
        messagestr = messagestr[7:]
        text = " ".join(messagestr)
        result = []
        result.append(" ".join([s for s in text]))
        for pos, symbol in enumerate(text[1:]):
            result.append(symbol + " " + "  " * pos + symbol)
        result = list("\n".join(result))
        result[0] = text[0]
        result = "".join(result)
        msg = "\n" + result
        await args.edit("`" + msg + "`")


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern=r"hypno"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.8

    animation_ttl = range(0, 15)

    # input_str = event.pattern_match.group(1)

    # if input_str == "hypno":

    # await event.edit(input_str)

    await event.edit("hypnotysing...")

    animation_chars = [
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬛⬜⬛⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛",
        "⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬛\n⬛⬜⬛⬜⬛\n⬛⬜⬜⬜⬛\n⬛⬛⬛⬛⬛",
        "⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜",
        "[👉🔴👈](https://t.me/JarvisOT)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 15])


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd("moody"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 288)

    # await event.edit(input_str)
    await event.edit("I am getting moody now")
    animation_chars = [
        "😆😆😆",
        "😋🤨🧐",
        "😛😒😣",
        "😝😖🤩",
        "😜😑😰",
        "🤪😳🥵",
        "😭🥺😩",
        "😫😠🤬",
        "😬😐😶",
        "😵😵😵",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 72])


import random

import requests

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern="quote ?(.*)"))
async def quote_search(event):
    if event.fwd_from:
        return
    await event.edit("Processing...")
    search_string = event.pattern_match.group(1)
    input_url = "https://bots.shrimadhavuk.me/Telegram/GoodReadsQuotesBot/?q={}".format(
        search_string
    )
    headers = {"USER-AGENT": "Jarvis"}
    try:
        response = requests.get(input_url, headers=headers).json()
    except:
        response = None
    if response is not None:
        result = (
            random.choice(response).get("input_message_content").get("message_text")
        )
    else:
        result = None
    if result:
        await event.edit(result.replace("<code>", "`").replace("</code>", "`"))
    else:
        await event.edit("Zero results found")


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern=r"smoon"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 32)
    # input_str = event.pattern_match.group(1)
    # if input_str == "smoon":
    await event.edit("moon")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 8])


@jarvis.on(j_cmd(pattern=r"tmoon"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 33)

    # input_str = event.pattern_match.group(1)

    # if input_str == "tmoon":

    await event.edit("moon")

    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 33])


import random

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern=r"react (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "happy":
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "(ʘ‿ʘ)",
            "(✿´‿`)",
            "=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾",
            "(*⌒▽⌒*)θ～♪",
            "°˖✧◝(⁰▿⁰)◜✧˖°",
            "✌(-‿-)✌",
            "⌒°(❛ᴗ❛)°⌒",
            "(ﾟ<|＼(･ω･)／|>ﾟ)",
            "ヾ(o✪‿✪o)ｼ",
        ]
    elif input_str in "thinking":
        emoticons = [
            "(҂⌣̀_⌣́)",
            "（；¬＿¬)",
            "(-｡-;",
            "┌[ O ʖ̯ O ]┐",
            "〳 ͡° Ĺ̯ ͡° 〵",
        ]
    elif input_str in "waving":
        emoticons = [
            "(ノ^∇^)",
            "(;-_-)/",
            "@(o・ェ・)@ノ",
            "ヾ(＾-＾)ノ",
            "ヾ(◍’౪`◍)ﾉﾞ♡",
            "(ό‿ὸ)ﾉ",
            "(ヾ(´・ω・｀)",
        ]
    elif input_str in "wtf":
        emoticons = [
            "༎ຶ‿༎ຶ",
            "(‿ˠ‿)",
            "╰U╯☜(◉ɷ◉ )",
            "(;´༎ຶ益༎ຶ`)♡",
            "╭∩╮(︶ε︶*)chu",
            "( ＾◡＾)っ (‿|‿)",
        ]
    elif input_str in "love":
        emoticons = [
            "乂❤‿❤乂",
            "(｡♥‿♥｡)",
            "( ͡~ ͜ʖ ͡°)",
            "໒( ♥ ◡ ♥ )७",
            "༼♥ل͜♥༽",
        ]
    elif input_str in "confused":
        emoticons = [
            "(・_・ヾ",
            "｢(ﾟﾍﾟ)",
            "﴾͡๏̯͡๏﴿",
            "(￣■￣;)!?",
            "▐ ˵ ͠° (oo) °͠ ˵ ▐",
            "(-_-)ゞ゛",
        ]
    elif input_str in "dead":
        emoticons = [
            "(✖╭╮✖)",
            "✖‿✖",
            "(+_+)",
            "(✖﹏✖)",
            "∑(✘Д✘๑)",
        ]
    elif input_str in "sad":
        emoticons = [
            "(＠´＿｀＠)",
            "⊙︿⊙",
            "(▰˘︹˘▰)",
            "●︿●",
            "(　´_ﾉ` )",
            "彡(-_-;)彡",
        ]
    elif input_str in "dog":
        emoticons = [
            "-ᄒᴥᄒ-",
            "◖⚆ᴥ⚆◗",
        ]
    else:
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "¯\_(ツ)_/¯",
            "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
            "ʕ•ᴥ•ʔ",
            "(▀̿Ĺ̯▀̿ ̿)",
            "(ง ͠° ͟ل͜ ͡°)ง",
            "༼ つ ◕_◕ ༽つ",
            "ಠ_ಠ",
            "(☞ ͡° ͜ʖ ͡°)☞",
            "¯\_༼ ି ~ ି ༽_/¯",
            "c༼ ͡° ͜ʖ ͡° ༽⊃",
        ]
    index = random.randint(0, len(emoticons))
    output_str = emoticons[index]
    await event.edit(output_str)


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern="lucky"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 17)
    # input_str = event.pattern_match.group(1)
    # if input_str == "lucky":
    await event.edit("Lucky..")
    animation_chars = [
        "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/jarvis-works/jarvisuserbot)⬜",
        "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/jarvis-works/jarvisuserbot)⬜",
        "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/jarvis-works/jarvisuserbot)⬜",
        "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/jarvis-works/jarvisuserbot)⬜",
        "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/jarvis-works/jarvisuserbot)⬜",
        "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/jarvis-works/jarvisuserbot)⬜",
        "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/jarvis-works/jarvisuserbot)⬜",
        "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/jarvis-works/jarvisuserbot/)⬜\n⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/jarvis-works/jarvisuserbot)⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜[🎁](https://github.com/jarvis-works/jarvisuserbot/)⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜[🎁](https://github.com/jarvis-works/jarvisuserbot)⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n[🎁](https://github.com/jarvis-works/jarvisuserbot)⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜",
        "⬜⬜⬜\n⬜⬜⬜\n⬜⬜⬜",
        "⬜⬜\n⬜⬜",
        "[🎁](https://github.com/jarvis-works/jarvisuserbot)",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])


import asyncio

from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 15)
    input_str = event.pattern_match.group(1)
    if input_str == "whatsapp":
        await event.edit("Trying to Break Protocols")
        animation_chars = [
            "Looking for WhatsApp databases in targeted person...",
            " User online: True\nTelegram access: True\nRead Storage: True ",
            "Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 20s",
            "Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 18s",
            "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 16s",
            "Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 14s",
            "Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases`\nETA: 0m, 12s",
            "Hacking... 55.30%\n[█████████░░░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s",
            "Hacking... 64.86%\n[███████████░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s",
            "Hacking... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 06s",
            "Hacking... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 04s",
            "Hacking... 93.50%\n[█████████████████░░░]\n`Decryption successful!`\nETA: 0m, 02s",
            "Hacking... 100%\n[████████████████████]\n`Scanning file...`\nETA: 0m, 00s",
            "Hacking complete!\nUploading file...",
            "Targeted Account Hacked...!\n\n ✅ File has been successfully uploaded to my server.\nWhatsApp Database:\n`./DOWNLOADS/msgstore.db.crypt12`",
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 15])


CMD_HELP.update({"leave": "Leave a Chat"})
CMD_HELP.update({";__;": "You try it!"})
CMD_HELP.update({"cry": "Cry"})
CMD_HELP.update({"fp": "Send face palm emoji."})
CMD_HELP.update({"moon": "Bot will send a cool moon animation."})
CMD_HELP.update({"clock": "Bot will send a cool clock animation."})
CMD_HELP.update({"readme": "Reedme."})
CMD_HELP.update({"source": "Gives the source of your userbot"})
CMD_HELP.update({"myusernames": "List of Usernames owned by you."})
CMD_HELP.update({"oof": "Same as ;__; but ooof"})
CMD_HELP.update({"earth": "Sends Kensar Earth animation"})
CMD_HELP.update({"heart": "Try and you'll get your emotions back"})
