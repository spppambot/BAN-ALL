#  Copyright (C) 2024-25 @SAIF_DICTATOR - DICTATOR
# TELEGRAM BAN ALL BOT
# CREATOR - SAIF PAPA

import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from var import Var
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
   "https://telegra.ph//file/93901ec36088ca936f133.jpg",
]

SUDO_USERS = []
for x in Var.SUDO: 
    SUDO_USERS.append(x)

@Saif.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
        start = datetime.now()
        t = "ᴀɪ ʙᴏᴛ ᴀʟɪᴠɪɴɢ..."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("ᴀɪ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ......")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(SAIF,
                             caption=f"ʜᴇʏ ʙᴀʙʏ!!\n**sᴀɪғʙᴏʀᴢ ʙᴀɴ-ᴀʟʟ ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ ᴡɪᴛʜ sᴘᴇᴇᴅ ᴏꜰ \n➥ `{ms}` ms\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ || [sᴀɪғ](https://t.me/SAIF_DICTATOR)||")

@Saif.on(events.NewMessage(pattern="^/kickall"))
async def kickall(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"𝙽𝚘𝚘𝚋 !! 𝚄𝚜𝚎 𝚃𝚑𝚒𝚜 𝙲𝚖𝚍 𝚒𝚗 𝙶𝚛𝚘𝚞𝚙."
         await event.reply(Reply)
     else:
         await event.delete()
         SaiF = await event.get_chat()
         SaiFoP = await event.client.get_me()
         admin = SaiF.admin_rights
         creator = SaiF.creator
         if not admin and not creator:
              return await event.reply("I Dɸƞ'τ հα⋎ε ៜυẜẜιϲιεƞτ Ɍιϑհτៜ !!")
         DeaD = await Saif.send_message(event.chat_id, "**Ηεℓℓ𝙾 !! I'ʍ Δℓι⋎ε**")
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
         await DeaD.edit(f"**Ʊៜεʀៜ ƘιϲΚεδ ⟆υϲϲεៜៜẜυℓℓψ ! \n\n ƘιϲΚεδ:** `{kimk}` \n **Total:** `{all}`")
    

@Saif.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"Noob !! Use This Cmd in Group."
         await event.reply(Reply)
     else:
         await event.delete()
         SaiF = await event.get_chat()
         SaiFoP = await event.client.get_me()
         admin = SaiF.admin_rights
         creator = SaiF.creator
         if not admin and not creator:
              return await event.reply("I Dɸƞ'τ հα⋎ε ៜυẜẜιϲιεƞτ Ɍιϑհτៜ !!")
         DeaD = await Saif.send_message(event.chat_id, "**Ηεℓℓɸ !! I'ʍ Δℓι⋎ε**")
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
         await Dead.edit(f"**Ʊៜεʀៜ Βαƞƞεδ ៜυϲϲεៜẜυℓℓ𝚢 ! \n\n Yzmmvw Users:** `{bann}` \n **Total Users:** `{all}`")

@Saif.on(events.NewMessage(pattern="^/unbanall"))
async def unban(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"𝙽𝚘𝚘𝚋 !! Ʊៜε Ƭнιƨ Ɔм∂ ιи Ǥяσʋρ."
         await event.reply(Reply)
     else:
         msg = await event.reply("sᴇᴀʀᴄʜɪɴɢ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛ ʟɪsᴛs.")
         p = 0
         async for i in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
              rights = ChatBannedRights(until_date=0, view_messages=False)
              try:
                await event.client(functions.channels.EditBannedRequest(event.chat_id, i, rights))
              except FloodWaitError as ex:
                 print(f"sleeping for {ex.seconds} seconds")
                 sleep(ex.seconds)
              except Exception as ex:
                 await msg.edit(str(ex))
              else:
                  p += 1
         await msg.edit("{}: {} unbanned".format(event.chat_id, p))


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
print("ʏᴏᴜʀ ʙᴀɴ ᴀʟʟ ʙᴏᴛ ᴅᴇᴘʟᴏʏᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅ ᴍᴀᴅᴇ ʙʏ sᴀɪғ ᴘᴀᴘᴀ")

Saif.run_until_disconnected()
