from jarvis.utils import admin_cmd


@jarvis.on(admin_cmd(pattern=r"lmoon"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        "🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕"
    )


@jarvis.on(admin_cmd(pattern=r"city"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        """☁☁🌞      ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖     l               \
   🌳/🚶           |   🚍         \ 🌴🚴🚴
🌴/                    |                     \🌲"""
    )


@jarvis.on(admin_cmd(pattern=r"hai"))
async def hai(event):
    if event.fwd_from:
        return
    await event.edit("🌺✨✨🌺✨🌺🌺🌺\n🌺✨✨🌺✨✨🌺✨\n🌺🌺🌺🌺✨✨🌺✨\n🌺✨✨🌺✨✨🌺✨\n🌺✨✨🌺✨🌺🌺🌺\n☁☁☁☁☁☁☁☁")

@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@jarvis.on(admin_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 ")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔❤️❤️")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💜💜𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💜💜")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💛💛𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💛💛")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓??𝒆𝒏𝒅𝒔💓💓")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💚💚𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💚💚")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("🧡🧡𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔🧡🧡")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💙💙")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💜💜𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💜💜")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💚💚𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💚💚")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💛💛𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💛💛")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("🖤🖤𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔🖤🖤")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💙💙")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💜💜𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💜💜")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💚💚𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💚💚")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💛💛𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💛💛")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💝💝𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💝💝")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💕💕𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💕💕")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💖💖𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💖💖")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💕💕𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💕💕")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💝💝𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💝💝")


@jarvis.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💕💕𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💕💕")


@jarvis.on(admin_cmd(pattern=r"cheer"))
async def cheer(event):
    if event.fwd_from:
        return
    await event.edit(
        "💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐"
    )


@jarvis.on(admin_cmd(pattern=r"getwell"))
async def getwell(event):
    if event.fwd_from:
        return
    await event.edit("🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹")


@jarvis.on(admin_cmd(pattern=r"sprinkle"))
async def sprinkle(event):
    if event.fwd_from:
        return
    await event.edit(
        "✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀"
    )


@jarvis.on(admin_cmd(pattern=r"kerala"))
async def kerala(event):
    if event.fwd_from:
        return
    await event.edit(
        "┈╱▔▔▔▔▔▔▔▔╲┈┈┈┈\n ╱▔▔▔▔▔▔▔▔╲╱┈┈┈┈\n▏┳╱╭╮┓┏┏┓▕╱▔▔╲┈\n▏┃╱┃┃┃┃┣▏▕▔▔╲╱▏\n▏┻┛╰╯╰╯┗┛▕▕▉▕╱╲\n▇▇▇▇▇▇▇▇▇▇▔▔▔╲▕\n▇▇╱▔╲▇▇▇▇▇╱▔╲▕╱\n┈┈╲▂╱┈┈┈┈┈╲▂╱▔┈"
    )


@jarvis.on(admin_cmd(pattern=r"ind"))
async def ind(event):
    if event.fwd_from:
        return
    await event.edit(
        "⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n⣇⣀ . ..INDIA🇮🇳INDIA .    .   . ⢷⣿⣿⣛⠐⣶⣿⣿\n⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿|n⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
    )


@jarvis.on(admin_cmd(pattern=r"like"))
async def like(event):
    if event.fwd_from:
        return
    await event.edit(
        "╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱\n╱╱┏╮╱╱╱╱╱╱╱╱╱╱╱\n╱╱┃┃╱╱╱┳╱┓┳╭┫┳┓\n▉━╯┗━╮╱┃╱┃┣┻╮┣╱\n▉┈┈┈┈┃╱┻┛┛┻╱┻┻┛\n▉╮┈┈┈┃╱╱╱╱╱╱╱╱╱\n╱╰━━━╯╱╱╱╱╱╱╱╱╱"
    )


@jarvis.on(admin_cmd(pattern=r"sup"))
async def sup(event):
    if event.fwd_from:
        return
    await event.edit(
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⣠⣾⣿⡿⠋⠀⠀⠉⠻⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠃⠀⠀⣀⡀⠀⢹⣿⣿\n⣿⣿⣿⣿⣿⣿⡄⠀⠙⠻⠋⠀⠀⣸⣿⣿⠀⠀⣿⣿\n⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⣿⠟⠀⢠⣿⣿\n⣿⣿⣿⣿⣿⣿⡿⠛⠛⠒⠶⠾⢿⣿⣿⣷⣄⣾⣿⣿\n⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡀⠀⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n⣿⣿⠀⠀⠀⠉⠉⠛⠛⠛⠶⢶⣤⣼⣿⣿⣿⣿⣿⣿\n⣿⣿⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠁⠀⣾⣿⣷⡄⠀⢼⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⡿⠀⠈⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣇⠀⠀⠉⠋⠁⠀⢠⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠿⢷⣤⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠉⠉⠛⢻⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠹⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⠻⣀⣀⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠁⠀⣀⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣷⡀⠘⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡄⠈⢻⡇⠀⡿⠃⠀⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣷⣄⢸⡇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠉⠉⠑⠒⠲⠿⢿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢺⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⠉⠉⠙⠋⠀⠀⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣤⣤⣀⣀⡀⠀⠀⣰⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⢀⣤⡄⠀⡀⠀⢹⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣿⡄⠈⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡆⠀⢹⡇⠀⠟⠁⢀⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⣸⡇⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▀▀▄▄▀▀▀▄▄🟦\n🟦█▌▐██▌▄███🟦\n🟦█▌▐█▌▄████🟦\n🟦█▌▐▌▄█████🟦\n🟦█▌░▐██████🟦\n🟦█▌▐▌▀█████🟦\n🟦█▌▐█▌▀████🟦\n🟦█▌▐██▌▀███🟦\n🟦▀▄▄▀▀▄▄▄▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▀▀▄▄▄▄▄🟦\n🟦██████████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦███▌▐█████🟦\n🟦▀▀▀▄▄▀▀▀▀▀🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟦▄▄▄▄▄▄▄▄▄▄🟦\n🟦███▀▀▀▀███🟦\n🟦██▌░▐▄▄▐██🟦\n🟦██▌░▐█████🟦\n🟦██▌░▀▀▀▐██🟦\n🟦██▀▀█▌░▐██🟦\n🟦██▌▐█▌░▐██🟦\n🟦██▌▐▀▀░▐██🟦\n🟦███▄▄▄▄███🟦\n🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"kis"))
async def kis(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n🟪▄▀▀▄▄▀▀▀▄▄🟪\n🟪█▌▐██▌▄███🟪\n🟪█▌▐█▌▄████🟪\n🟪█▌▐▌▄█████🟪\n🟪█▌░▐██████🟪\n🟪█▌▐▌▀█████🟪\n🟪█▌▐█▌▀████🟪\n🟪█▌▐██▌▀███🟪\n🟪▀▄▄▀▀▄▄▄▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▀▀▄▄▄▄▄🟪\n🟪██████████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪███▌▐█████🟪\n🟪▀▀▀▄▄▀▀▀▀▀🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n🟪▄▄▄▄▄▄▄▄▄▄🟪\n🟪███▀▀▀▀███🟪\n🟪██▌░▐▄▄▐██🟪\n🟪██▌░▐█████🟪\n🟪██▌░▀▀▀▐██🟪\n🟪██▀▀█▌░▐██🟪\n🟪██▌▐█▌░▐██🟪\n🟪██▌▐▀▀░▐██🟪\n🟪███▄▄▄▄███🟪\n🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪\n\n Edit by ❤️@Munni_popz❤️"
    )


@jarvis.on(admin_cmd(pattern=r"hello"))
async def hello(event):
    if event.fwd_from:
        return
    await event.edit(
        "┏┓━┏┓━━━━┏┓━┏┓━━━━━\n┃┃━┃┃━━━━┃┃━┃┃━━━━━\n┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛"
    )


@jarvis.on(admin_cmd(pattern=r"welcome"))
async def getwell(event):
    if event.fwd_from:
        return
    await event.edit(
        """───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█"""
    )


@jarvis.on(admin_cmd(pattern=r"ooof"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(
        """╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ 
┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ 
┃┃╱┃┣━━┳━━┳━━┳╯╰╮ 
┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ 
┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ 
╰━━━┻━━┻━━┻━━╯╰╯"""
    )


@jarvis.on(admin_cmd(pattern=r"indiaflag"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(
        """🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧
⬜️⬜️⬜️⬜️⬜️🟦🟦🟦⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️🟦🟦🟦⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️🟦🟦🟦⬜️⬜️⬜️⬜️⬜️
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩

Made With Love 🧡🤍💚

Happy Independence Day !!!!!"""
    )
