# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
import os
import sys

from jarvis import CMD_HNDLR, SUDO_HNDLR
from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd


@jarvis.on(admin_cmd(pattern="restart", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("Restarting [██░] ...\n`.ping` me or `.helpme` to check if I am online")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [███]...\n`.ping` me or `.helpme` to check if I am online")
    # await asyncio.sleep(2)
    await edit_or_reply(
        event,
        f"Restarted. `{CMD_HNDLR}ping` or `{CMD_HNDLR}help` to check if I am online",
    )
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@jarvis.on(sudo_cmd(pattern="restart", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("Restarting [██░] ...\n`.ping` me or `.helpme` to check if I am online")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [███]...\n`.ping` me or `.helpme` to check if I am online")
    # await asyncio.sleep(2)
    await edit_or_reply(
        event,
        f"Restarted. `{SUDO_HNDLR}ping` or `{SUDO_HNDLR}help` to check if I am online",
    )
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@jarvis.on(admin_cmd(pattern="shutdown", outgoing=True))
@jarvis.on(sudo_cmd(pattern="shutdown", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "Turning off ...Manually turn me on later")
    await borg.disconnect()
