import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions

START = "https://telegra.ph/file/68d6d0c80c9bb02730e64.jpg"

@register(pattern=("/start"))
async def awake(event):
  TEXT = f"ʜɪ ɢᴀʏ [{event.sender.first_name}](tg://user?id={event.sender.id}), ᴛʜɪꜱ ɪꜱ ᴍᴀꜱꜱ ᴀᴄᴛɪᴏɴꜱ ʙᴏᴛ ᴡɪᴛʜ ᴢᴇʀᴏ ᴅᴏᴡɴᴛɪᴍᴇ..!!\n\n **ᴄᴏᴍᴍᴀɴᴅꜱ**\n\n /ping - ᴄʜᴇᴄᴋ ʙᴏᴛꜱ ᴜᴘᴛɪᴍᴇ ! \n /banall - ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ ꜰʀᴏᴍ ɢʀᴏᴜᴘ \n /unbanall - ᴛᴏ ᴜɴʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ \n\ /kickall - ᴛᴏ ᴋɪᴄᴋ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ"
  BUTTON = [[Button.url("ᴜᴘᴅᴀᴛᴇꜱ", "https://t.me/SpotifyxUpdates"),]]
  await event.send_file(event.chat_id, START, caption=TEXT, buttons=BUTTON)  
