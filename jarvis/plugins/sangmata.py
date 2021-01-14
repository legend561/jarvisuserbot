from telethon.errors.rpcerrorlist import YouBlockedUserError

from jarvis.utils import admin_cmd, eor, sudo_cmd


@jarvis.on(admin_cmd("sg ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd("sg ?(.*)", allow_sudo=True))
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("Reply to any user message.")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.edit("Reply to actual users message.")
        return
    lol = await eor(steal, "Processingg !!!!!")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await lol.edit("Please unblock @sangmatainfo_bot and try again")
                return
            if response.text.startswith("No records found"):
                await lol.edit("No records found for this user")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await lol.edit(f"{response.message}")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await lol.edit("Error: @SangMataInfo_bot is not responding!.")
