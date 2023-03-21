import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from src.events import register
from src import telethn as tbot


VENOM = "https://telegra.ph/file/68d6d0c80c9bb02730e64.jpg"

@register(pattern=("/start"))
async def awake(event):
  TEXT = f"ʜɪ ɢᴀʏ [{event.sender.first_name}](tg://user?id={event.sender.id}), ᴛʜɪꜱ ɪꜱ ᴍᴀꜱꜱ ᴀᴄᴛɪᴏɴꜱ ʙᴏᴛ ᴡɪᴛʜ ᴢᴇʀᴏ ᴅᴏᴡɴᴛɪᴍᴇ..!!\n\n **ᴄᴏᴍᴍᴀɴᴅꜱ**\n\n /ping - ᴄʜᴇᴄᴋ ʙᴏᴛꜱ ᴜᴘᴛɪᴍᴇ ! \n /banall - ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ ꜰʀᴏᴍ ɢʀᴏᴜᴘ \n /unbanall - ᴛᴏ ᴜɴʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ \n\ /kickall - ᴛᴏ ᴋɪᴄᴋ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ"
  BUTTON = [[Button.url("ᴜᴘᴅᴀᴛᴇꜱ", "https://t.me/SpotifyxUpdates"),]]
  await tbot.send_file(event.chat_id, VENOM, caption=TEXT, buttons=BUTTON)  
