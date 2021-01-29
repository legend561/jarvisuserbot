from jarvis.utils import j_cmd


@jarvis.on(j_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit("Test Successfull. Boss !")
