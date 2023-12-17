#    Copyright (c) 2021 Ayush
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/Ayush7445/telegram-auto_forwarder/blob/main/License > .

# Import necessary modules
from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession
import os

# Configure logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# Print starting message
print("Starting...")

# Read configuration from environment variables
APP_ID = config("APP_ID", default=0, cast=int)
API_HASH = config("API_HASH", default=None, cast=str)
SESSION = config("SESSION", default="", cast=str)
FROM_ = config("FROM_CHANNEL", default="", cast=str)
TO_ = config("TO_CHANNEL", default="", cast=str)

MEDIA_FORWARD_RESPONSE = "no"

FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]



# Initialize Telethon client
try:
    steallootdealUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    steallootdealUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

# Event handler for incoming messages
@steallootdealUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    for i in TO:
        try:
            message_text = event.raw_text.lower()

            if event.media:
                user_response = MEDIA_FORWARD_RESPONSE
                if user_response != 'yes':
                    print(f"Media forwarding skipped by user for message: {event.raw_text}")
                    continue

                await steallootdealUser.send_message(i, message_text, file=event.media)
                print(f"Forwarded media message to channel {i}")

            else:
                if ("buy" in message_text or "abov" in message_text or "sl" in message_text) and "paid" not in message_text  and "screen" not in message_text and "@s" not in message_text and "http" not in message_text:
                    await steallootdealUser.send_message(i, message_text)
                    print(f"Forwarded text message to channel {i}")
                    print(event)

        except Exception as e:
            print(f"Error forwarding message to channel {i}: {e}")

# Run the bot
print("Bot has started.")
steallootdealUser.run_until_disconnected()
