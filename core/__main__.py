# Copyrighted by Aresona & Sentric Nova 2024-2025
# Please do not modify any file if you don't sure what you doing.
# --------------------------------------Credits---------------------------------#
# Sentric Nova -> For his best ideas and making it shorts.
# Aresona -> For coding and making it short as much possible.
# Support channel --> social_bots.t.me
# Support Group --> Join social_bots's comment box
# Please gives credits if you fork or anything. also join our support channels too.

import asyncio, config
from config import LOGGER_GROUP
from pyrogram import idle
from core import app, userbot

async def init():
    await app.start()
    try:
        print("ASSISTANT STARTING")
        with await userbot.start():
            print("ASSISTANT STARTED")
            try:
                await userbot.join_chat("Social_bots")
                await userbot.join_chat("Life_codes")
                await userbot.send_message(LOGGER_GROUP, "Assistant is started!")
            except:
                pass
    except Exception as err:
        print(err)
    await idle()
    await app.stop()
    try:
        await userbot.stop()
    except:
        pass
    print("Bot has been stopped!")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())