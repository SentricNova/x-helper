# Copyrighted by Aresona & Sentric Nova 2024-2025
# Please do not modify any file if you don't sure what you doing.
# --------------------------------------Credits---------------------------------#
# Sentric Nova -> For his best ideas and making it shorts.
# Aresona -> For coding and making it short as much possible.
# Support channel --> social_bots.t.me
# Support Group --> Join social_bots's comment box
# Please gives credits if you fork or anything. also join our support channels too.

# Importing modules
import os, urllib.parse, asyncio
from pyrogram import filters
from core import userbot, app
from pyrogram.types import Message
from config import OWNER_ID, SUDO_USERS, LOGGER_GROUP
from pyrogram.errors import FloodWait
from pyrogram.enums import ChatType


async def valid_url(url):
    try:
        result = urllib.parse.urlparse(url)
        if not result.scheme or not result.netloc:
            return "No Hoster Found For This URL. You should given a valid URL."
        if not (result.scheme in ["http", "https"]):
            return "Invalid URL scheme. Only http and https are supported."
        return "valid"
    except ValueError:
        return "Invalid URL. Please try with a valid URL."
    except Exception as err:
        return f"While validating URL. The Following Issue Happened:\n{err}\n\n**HOW TO SOLVE :**\n- Check If you gave a wrong url.\n- A url looks like : https://t.me/social_bots"


async def channel_address_lookups(text):
    lower_text = text.lower()
    is_url = await valid_url(text)
    if is_url=="valid":
        split_url = text.split('/')
        if lower_text.startswith("https://t.me/c/"):
            try:
                return int(f"-100{split_url[-2]}"), "needlink", int(split_url[-1])
            except:
                return int(f"-100{split_url[-2]}"), "needlink", False
        
        elif lower_text.startswith("https://t.me/"):
            if len(split_url) > 2:
                return f"@{split_url[-2]}", "public", int(split_url[-1])
            else:
                return f"@{split_url[-2]}", "public", False
        elif lower_text.startswith("https://t.me/+"):
            entity = lower_text.replace("https://t.me/+", "https://t.me/joinchat/")
            return entity, "private", False
        elif lower_text.startswith("@"):
            return lower_text, "public", False
        else:
            return False, False, False
    elif lower_text.lstrip("-").isdigit() or lower_text.isdigit():
        return int(lower_text), "channel_id", False
    else:
        return False, False, False





# below are functions.
@app.on_message(filters.command("save") & filters.user(SUDO_USERS))
async def save(client, message, ub=userbot):
    saved = 0
    failed = 0
    msg_splited = message.text.split(" ")
    if len(msg_splited) == 3:
        msgs_ids = [] # do not delete this empty list
        pure_msgs = [] # same to this
        start_from = msg_splited[1]
        end_here = msg_splited[2]
        chat_id_1, chat_type_1, start_msg_id = await channel_address_lookups(start_from)
        chat_id_2, chat_type_2, end_msg_id = await channel_address_lookups(end_here)
        if chat_id_1 != chat_id_2:
            return await message.reply_text("LOL! You gave me two diff channels/groups's link. Check your given urls.")
        
        if chat_type_1=="private":
            try:
                await ub.join_chat(chat_type_2)
                return await message.reply_text("Chat joined! Now try again with message links.")
            except FloodWait as t:
                await asyncio.sleep(t.value)
            except Exception as err:
                return await message.reply_text(err)
        if not start_msg_id or not end_msg_id:
            return await message.reply_text("You didn't gave message link from where I'll start saving and from where I'll stop saving!\n\n**EXAMPLE:**\n/save https://t.me/msg_link/23432 https://t.me/msg_link/23440")

        try:
            info = await message.reply_text("⏳ **Loading message ids...**")
            async for messagex in ub.get_chat_history(chat_id=chat_id_1, min_id=start_msg_id, max_id=end_msg_id):
                if messagex.media:
                    pure_msgs.append(messagex)
                    msgs_ids.append(messagex.id)
            await info.edit_text(f"⌛ **{len(msgs_ids)} Media Messages are loaded! Trying to save...**")
            if chat_type_1 == "public":
                for save_msg_id in msgs_ids:
                    try:
                        await app.copy_message(message.chat.id, chat_id_1, save_msg_id)
                        saved += 1
                    except FloodWait as t:
                        await asyncio.sleep(t.value)
                        await app.copy_message(message.chat.id, chat_id_1, save_msg_id)
                        saved += 1
                    except Exception as err:
                        print(err)
                        failed += 1
                return await info.edit_text(f"{saved} every type of media files are saved {f'and {failed} failed' if failed else ''}.")
            else:
                for mmsg in pure_msgs:
                    try:
                        mediafile = await ub.download_media(mmsg)
                        await app.send_document(message.chat.id, mediafile)
                        saved += 1
                        try:
                            os.remove(mediafile)
                        except FloodWait as t:
                            await asyncio.sleep(t.value)
                        except Exception as err:
                            pass
                    except FloodWait as t:
                        await asyncio.sleep(t.value)
                        mediafile = await ub.download_media(mmsg)
                        await app.send_document(message.chat.id, mediafile)
                        saved += 1
                        try:
                            os.remove(mediafile)
                        except FloodWait as t:
                            await asyncio.sleep(t.value)
                        except Exception as err:
                            pass
                    except Exception as err:
                        print(err)
                        failed += 1
                        pass
                return await info.edit_text(f"{saved} every type of media files are saved {f'and {failed} failed' if failed else None}.")
        except FloodWait as t:
            await asyncio.sleep(t.value)
        except Exception as err:
            await message.reply_text(err)
            try:
                await info.delete()
            except:
                pass
            return
    elif len(msg_splited) == 2:
        chat_id_1, chat_type_1, start_msg_id = await channel_address_lookups(msg_splited[1])
        if not start_msg_id or not chat_id_1:
            return await message.reply_text("This is an invalid URL!")
        info = await message.reply_text("⏳ **Loading message ids...**")
        if chat_type_1 == "public":
            try:
                await app.copy_message(message.chat.id, chat_id_1, start_msg_id)
                saved += 1
            except FloodWait as t:
                await asyncio.sleep(t.value)
                await app.copy_message(message.chat.id, chat_id_1, start_msg_id)
                saved += 1
            except Exception as err:
                return await message.reply_text(err)
                failed += 1
            return await info.edit_text(f"{saved} every type of media files are saved {f'and {failed} failed' if failed else ''}.")
        else:
            try:
                lel = await ub.get_messages(chat_id_1, start_msg_id)
                if lel.text:
                    return await app.send_message(message.chat.id, lel.text)
                mediafile = await ub.download_media(lel)
                await app.send_document(message.chat.id, mediafile)
                saved += 1
                try:
                    os.remove(mediafile)
                except Exception as err:
                    pass
            except FloodWait as t:
                await asyncio.sleep(t.value)
                lel = await ub.get_messages(chat_id_1, start_msg_id)
                mediafile = await ub.download_media(lel)
                await app.send_document(message.chat.id, mediafile)
                saved += 1
                try:
                    os.remove(mediafile)
                except Exception as err:
                    pass
            except Exception as err:
                return await message.reply_text(err)
                failed += 1
                pass
            return await info.edit_text(f"{saved} every type of media files are saved {f'and {failed} failed' if failed else ''}.")
    else:
        return await message.reply_text("Wrong command! Use this command like:\n\n/save https://t.me/lol/234234 https://t.me/lol/2342387")
