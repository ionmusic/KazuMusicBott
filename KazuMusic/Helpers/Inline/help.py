from KazuMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


help_panel = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴀᴅᴍɪɴs",
                    callback_data="help_callback ADMIN",
                ),
                InlineKeyboardButton(
                    text="ᴀᴜᴛʜ",
                    callback_data="help_callback AUTH",
                ),
                InlineKeyboardButton(
                    text="ᴩʟᴀʏ",
                    callback_data="help_callback PLAY",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴏᴡɴᴇʀ",
                    callback_data="help_callback OWNER",
                ),
                InlineKeyboardButton(
                    text="sᴜᴅᴏ",
                    callback_data="help_callback SUDO",
                ),
                InlineKeyboardButton(
                    text="ᴛᴏᴏʟs",
                    callback_data="help_callback TOOLS",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʙᴀᴄᴋ",
                    callback_data=f"fallen_home",
                ),
                InlineKeyboardButton(
                    text="ᴄʟᴏsᴇ",
                    callback_data=f"close"
                ),
            ]
        ]
    )


help_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ʙᴀᴄᴋ",
                    callback_data=f"fallen_help",
                ),
                InlineKeyboardButton(
                    text="ᴄʟᴏsᴇ",
                    callback_data=f"close"
                )
            ]
        ]
    )
