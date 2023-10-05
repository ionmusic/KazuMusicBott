import os
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from KazuMusic import app, Ass, BOT_NAME, SUDO_USERS
from KazuMusic.Helpers.Database import get_active_chats


__MODULE__ = "Tᴏᴏʟs"
__HELP__ = """

**ɴᴏᴛᴇ :**
ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs


/joinassistant [ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ]
» ᴏʀᴅᴇʀ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ᴊᴏɪɴ ᴛʜᴀᴛ ᴄʜᴀᴛ.

/leaveassistant [ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ]
» ᴏʀᴅᴇʀ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ᴄʜᴀᴛ.

/leavebot [ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ]
» ᴏʀᴅᴇʀ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ᴄʜᴀᴛ.
"""


@app.on_message(filters.command(["vcs", "m"]) & filters.user(SUDO_USERS))
async def activevc(_, message: Message):
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ :** {e}")
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "ᴩʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴩ"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += (
                f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n\n"
            )
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n\n"
        j += 1
    if not text:
        await message.reply_text(f"**» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ᴏɴ {BOT_NAME} sᴇʀᴠᴇʀ.**")
    else:
        await message.reply_text(
            f"**» ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ᴏɴ {BOT_NAME} sᴇʀᴠᴇʀ :**\n\n{text}",
            disable_web_page_preview=True,
        )

@app.on_message(filters.command(["vcv", "v"]) & filters.user(SUDO_USERS))
async def activevi_(_, message: Message):
    mystic = await message.reply_text(
        "Getting active video chats.. Please hold"
    )
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "Private Group"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("No Active Voice Chats")
    else:
        await mystic.edit_text(
            f"**ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄᴀʟʟs:-**\n\n{text}",
            disable_web_page_preview=True,
        )

@app.on_message(filters.command(["joinassistant", "join", "ass", "assistant"]) & filters.user(SUDO_USERS))
async def assjoin(_, message):
    if len(message.command) != 2:
        await message.reply_text(
            "**ᴇxᴀᴍᴩʟᴇ :**\n/joinassistant [ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ ɪᴅ]"
        )
        return
    chat = message.text.split(None, 2)[1]
    try:
        await Ass.join_chat(chat)
    except Exception as e:
        await message.reply_text(f"ғᴀɪʟᴇᴅ.\n\n**ʀᴇᴀsᴏɴ :** {e}")
        return
    await message.reply_text("**» sᴜᴄᴄᴇssғᴜʟʟʏ ᴊᴏɪɴᴇᴅ ᴛʜᴀᴛ ᴄʜᴀᴛ.**")


@app.on_message(filters.command(["leavebot", "leave"]) & filters.user(SUDO_USERS))
async def botl(_, message):
    if len(message.command) != 2:
        await message.reply_text(
            "**ᴇxᴀᴍᴩʟᴇ :**\n/leavebot [ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ ɪᴅ]"
        )
        return
    chat = message.text.split(None, 2)[1]
    try:
        await app.leave_chat(chat)
    except Exception as e:
        await message.reply_text(f"ғᴀɪʟᴇᴅ\n**ʀᴇᴀsᴏɴ :** {e}")
        print(e)
        return
    await message.reply_text("**» sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴛʜᴀᴛ ᴄʜᴀᴛ.**")


@app.on_message(filters.command(["leaveassistant", "assleave", "userbotleave", "leaveass"]) & filters.user(SUDO_USERS))
async def assleave(_, message):
    if len(message.command) != 2:
        await message.reply_text(
            "**ᴇxᴀᴍᴩʟᴇ :**\n/assleave [ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ ɪᴅ]"
        )
        return
    chat = message.text.split(None, 2)[1]
    try:
        await Ass.leave_chat(chat)
    except Exception as e:
        await message.reply_text(f"ғᴀɪʟᴇᴅ\n**ʀᴇᴀsᴏɴ :** {e}")
        return
    await message.reply_text("**» ᴀssɪsᴛᴀɴᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴛʜᴀᴛ ᴄʜᴀᴛ.**")

@app.on_message(filters.command("aktif", [".", "^", "-", "!", "/"]) & filters.user(SUDO_USERS))
async def activecilik(_, message: Message):
    ms = len(await get_active_chats())
    vd = len(await get_active_video_chats())
    await app.send_message(message.chat.id, 
        f"💽 ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs:\n\n• ᴍᴜsɪᴄ: {ms}\n• ᴠɪᴅᴇᴏ:{vd}")