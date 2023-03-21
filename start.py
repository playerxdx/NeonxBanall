from pyrogram import filters
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
import asyncio
from .. import pbot


@pbot.on_message(filters.command('start'))
async def start_msg(bot, m):
    buttons = [
        [IKB("ꜱᴜᴍᴘᴘᴏʀᴛ☁️", url = "https://t.me/spotifyxlogs"), IKB("ᴜᴘᴅᴀᴛᴇꜱ📢", url = "https://t.me/spotifyxupdates")],
        [IKB("ᴅᴇᴠᴇʟᴏᴘᴇʀ🌙", user_id = 5666318586)]
]

    await m.reply_photo(
        photo = "https://telegra.ph/file/68d6d0c80c9bb02730e64.jpg",
        caption = f"ʜᴇʏᴀ {m.from_user.mention},ᴛʜɪꜱ ɪꜱ ᴍᴀꜱꜱ ᴀᴄᴛɪᴏɴꜱ ʙᴏᴛ ᴡɪᴛʜ ᴢᴇʀᴏ ᴅᴏᴡɴᴛɪᴍᴇ..!!\n\n **ᴄᴏᴍᴍᴀɴᴅꜱ**\n\n /ping - ᴄʜᴇᴄᴋ ʙᴏᴛꜱ ᴜᴘᴛɪᴍᴇ ! \n /banall - ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ ꜰʀᴏᴍ ɢʀᴏᴜᴘ \n /unbanall - ᴛᴏ ᴜɴʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ \n\ /kickall - ᴛᴏ ᴋɪᴄᴋ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ",
        reply_markup= IKM(buttons)
    )
