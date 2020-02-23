#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from tobrot import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text(" Contact : https://t.me/iamomkarofficial", quote=True)
    channel_id = str(AUTH_CHANNEL)[4:]
    message_id = 99
    # display the /help message
    await message.reply_text(
        f"[Welcome !!](https://t.me/magnetdownloader/2339)\n\nPlease read the Pinned Message\n\nReply these commands to Magnet link: \n`/leech@Alpacino_The_bot` \n`/leech@Alpacino_The_bot archive`\n`/ytdl@Alpacino_The_bot`\n`/savethumbnail@Alpacino_The_bot`\n`/clearthumbnail@Alpacino_The_bot`\n\nTry To bold Link if bot giving error\nIf still getting some problems try checking chat or tag and ask admins in chat.\n\nCheck out our Channel for older uploads : @alpacinodump\nCheck Our New Magnet To Google Drive Group : [Here](https://t.me/joinchat/JZwGtRZur77dpMkufWFaZA)",
        quote=True
    )


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="read this?",
            url="https://t.me/keralagram/698909"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "$€D",
        quote=True,
        reply_markup=reply_markup
    )
