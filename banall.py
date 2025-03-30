#  Copyright (C) 2024-25 @SAIF_DICTATOR - DICTATOR
# TELEGRAM BAN ALL BOT
# CREATOR - SAIF PAPA

import logging
import re
import os
import sys, platform
import asyncio
from telethon import TelegramClient, events, Button
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon import __version__ as tel
from datetime import datetime
from var import Var
from SAIFBANALL import dad as gg, dady as g, SAISTART, SAIHELP, SSTART
from time import sleep
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl import functions
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


logging.basicConfig(level=logging.INFO)

print("Starting.....")

Saif = TelegramClient('Saif', Var.API_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)

SAIF= [
   "https://telegra.ph//file/507f06908daf43adf4bde.jpg",
]

repo = "https://github.com/djdjrjjrk"
Owner = "@Sanatani_Sujoy"

SUDO_USERS = []
for x in Var.SUDO: 
    SUDO_USERS.append(x)

@Saif.on(events.NewMessage(pattern="^/start"))
async def start(event):
    buttns = [Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/SuperToppers0"), Button.url("Oᴡɴᴇʀ", "https://t.me/SAIF_DICTATOR"), Button.url("Rᴇᴘᴏ", f'{repo}')]
    py = platform.python_version()
    if event.sender.id in SUDO_USERS:
        await Saif.send_file(
            event.chat.id,
            file="https://graph.org/file/507f06908daf43adf4bde.jpg",
            caption=SAISTART.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in SUDO_USERS:
        await Saif.send_file(
            event.chat.id,
            file="https://graph.org/file/507f06908daf43adf4bde.jpg",
            caption=SSTART.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )


@Saif.on(events.NewMessage(pattern="^/help"))
async def start(event):
    buttns = [Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/SuperToppers"), Button.url("Oᴡɴᴇʀ", "https://t.me/UncleChipssBot"),
    Button.url("Rᴇᴘᴏ", f'{repo}')]
    if event.sender.id in SUDO_USERS:
        await Saif.send_file(
            event.chat.id,
            file="https://graph.org/file/507f06908daf43adf4bde.jpg",
            caption=SAIHELP.format(event.sender.first_name, event.sender.id),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in SUDO_USERS:
        await event.reply(
            "ᴀᴘɴᴇ ᴀᴜᴋᴋᴀᴛ ᴍᴇ ʀʜᴀ ᴋᴀʀᴏ ʙᴇᴡᴀᴋᴜғ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ ғʀᴏᴍ ᴛʜɪs [ʀᴇᴘᴏsɪᴛᴏʀʏ](https://github.com/djudhejjr)",
            link_preview=False,
        )       

@Saif.on(events.NewMessage(pattern="^/ping"))
async def ping(event):
    if event.sender.id in SUDO_USERS:
        start = datetime.now()
        t = "Pinging..."
        txxt = await event.reply(t)
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await txxt.edit(f"ɪ ᴀᴍ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ ᴡɪᴛʜ sᴘᴇᴇᴅ ᴏꜰ \n➥ `{ms}` ms\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ || [ᴅɪᴄᴛᴀᴛᴏʀ](https://t.me/SuperToppers)||")

@Saif.on(events.NewMessage(pattern="^/kickall"))
async def kickall(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"ɴᴏ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ."
         await event.reply(Reply)
     else:
         await event.delete()
         SaiF = await event.get_chat()
         SaiFoP = await event.client.get_me()
         admin = SaiF.admin_rights
         creator = SaiF.creator
         if not admin and not creator:
              return await event.reply("sᴏʀʀʏ !! ɪ ᴅᴏɴ'ᴛ ʜᴀɪ sᴜғғɪᴄɪᴇɴᴛ ʀɪɢʜᴛ ")
         DeaD = await Saif.send_message(event.chat_id, "**ᴋɪʟʟɪɴɢ sᴛᴀʀᴛᴇᴅ !**")
         admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
         admins_id = [i.id for i in admins]
         all = 0
         kimk = 0
         async for user in event.client.iter_participants(event.chat_id):
             all += 1
             try:
                if user.id not in admins_id:
                    await event.client.kick_participant(event.chat_id, user.id)
                    kimk += 1
                    await asyncio.sleep(0.1)
             except Exception as e:
                    print(str(e))
                    await asyncio.sleep(0.1)
         await DeaD.edit(f"**ᴜsᴇʀ ᴋɪᴄᴋᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ! \n\n ᴋɪᴄᴋᴇᴅ:** `{kimk}` \n **ᴛᴏᴛᴀʟ:** `{all}`")
    

@Saif.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"ɴᴏ !! ᴜsᴇ ᴛʜɪs ᴄᴍᴅ ɪɴ ɢʀᴏᴜᴘ."
         await event.reply(Reply)
     else:
         await event.delete()
         SaiF = await event.get_chat()
         SaiFoP = await event.client.get_me()
         admin = SaiF.admin_rights
         creator = SaiF.creator
         if not admin and not creator:
              return await event.reply("ɪ ᴅᴏɴ'ᴛ ʜᴀɪ sᴜғғɪᴄɪᴇɴᴛ ʀɪɢʜᴛ !!")
         DeaD = await Saif.send_message(event.chat_id, "**ᴡᴀᴛᴄʜ ᴍᴀɢɪᴄ ᴍᴀsᴛᴇʀ**")
         admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
         admins_id = [i.id for i in admins]
         all = 0
         bann = 0
         async for user in event.client.iter_participants(event.chat_id):
             all += 1
             try:
               if user.id not in admins_id:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
                    await asyncio.sleep(0.1)
             except Exception as e:
                   print(str(e))
                   await asyncio.sleep(0.1)
         await Dead.edit(f"**ᴜsᴇʀ ʙᴀɴɴᴇᴅ sᴜᴄᴄᴇsғᴜʟʟʏ  ! \n\n ʙᴀɴɴᴇᴅ ᴜsᴇʀs:** `{bann}` \n **ᴛᴏᴛᴀʟ ᴜsᴇʀs:** `{all}`")

@Saif.on(events.NewMessage(pattern="^/unbanall"))
async def unban(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"ɴᴏ !! ᴜsᴇ ᴛʜɪs ᴄᴍᴅ ɪɴ ɢʀᴏᴜᴘ."
         await event.reply(Reply)
     else:
         msg = await event.reply("sᴇᴀʀᴄʜɪɴɢ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛ ʟɪsᴛs.")
         p = 0
         async for i in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
              rights = ChatBannedRights(until_date=0, view_messages=False)
              try:
                await event.client(functions.channels.EditBannedRequest(event.chat_id, i, rights))
              except FloodWaitError as ex:
                 print(f"sʟᴇᴇᴘɪɴɢ ғᴏʀ {ex.seconds} sᴇᴄᴏɴᴅs")
                 sleep(ex.seconds)
              except Exception as ex:
                 await msg.edit(str(ex))
              else:
                  p += 1
         await msg.edit("{}: {} ᴜɴʙᴀɴɴᴇᴅ".format(event.chat_id, p))


@Saif.on(events.NewMessage(pattern="^/leave"))
async def _(e):
    if e.sender_id in SUDO_USERS:
        DeaDop = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = DeaDop[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("sᴜᴄᴄᴇsғᴜʟʟʏ ʟᴇғᴛ")
            except Exception as e:
                await event.edit(str(e))   
        else:
            bc = e.chat_id
            text = "ʟᴇᴀᴠɪɴɢ....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("sᴜᴄᴄᴇsғᴜʟʟʏ ʟᴇғᴛ")
            except Exception as e:
                await event.edit(str(e))   
          

@Saif.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "__ʀᴇsᴛᴀʀᴛɪɴɢ__ !!!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await Saif.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


print("\n\n")
print("ʏᴏᴜʀ ʙᴀɴ ᴀʟʟ ʙᴏᴛ ᴅᴇᴘʟᴏʏᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅ ᴍᴀᴅᴇ ʙʏ sᴀɪғᴅᴇᴀᴅ ")

Saif.run_until_disconnected()
