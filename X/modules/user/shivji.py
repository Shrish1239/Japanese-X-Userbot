import asyncio
from random import choice
from pyrogram.types import Message
from pyrogram import filters, Client
from config import OWNER_ID
from config import CMD_HANDLER as cmd
from SANATANDB.sanatan import SHIVAJI
from .help import *

@Client.on_message(filters.command("shivji", cmd) & filters.me)
async def shivji(x: Client, e: Message):
      NOBI = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(NOBI) == 2:
          ok = await x.get_users(NOBI[1])
          counts = int(NOBI[0])
          for _ in range(counts):
                reply = choice(SHIVAJI)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await x.get_users(user_id)
          counts = int(NOBI[0])
          for _ in range(counts):
                reply = choice(SHIVAJI)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text(". shivji 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")  


add_command_help(
    "•─╼⃝𖠁 Sʜɪᴠᴀ ᴊɪ",
    [
        ["shivji", "Tᴏ ꜱᴇɴᴅ Sʜɪᴠᴀ ᴊɪ ᴊɪ Mᴇssᴀɢᴇs."],
    ],
  )
