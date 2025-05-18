from telethon import TelegramClient, events
from telethon.tl.functions.messages import TranscribeAudioRequest
from aiogram import Bot
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from redis import Redis
r = Redis()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
TOKEN = os.getenv("TOKEN")
bot_username = "@V_to_T_bot"
bot = Bot(token=TOKEN)
SESSION_NAME = dir_path = os.path.dirname(os.path.realpath(__file__)) + '/' + "user_session"

#راه اندازی اولیه یوزربات و دادن شماره و کد ورورد
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
if not os.path.exists(SESSION_NAME + '.session'):
    with client:
        print('session Created.')

@client.on(events.NewMessage(from_users=[bot_username]))
async def transcribe(event):
    if event.voice:
        parts = event.raw_text.split("|")
        user_id = int(parts[0].split(":")[1])
        message_id = int(parts[1].split(":")[1])

        process = await bot.send_message(chat_id=user_id, text="🔁 در حال تبدیل صدا به متن...",reply_to_message_id=message_id)
        await bot.send_chat_action(chat_id=user_id,action="typing")
        # منتظر آماده شدن متن ترجمه
        while True:
            res = await client(TranscribeAudioRequest(
                peer=event.chat_id,
                msg_id=event.message.id
            ))
            if res.text :
                # ارسال متن به کاربر از طریق ربات اصلی
                try:
                    await process.edit_text(text=res.text)
                except Exception as e:
                    print("❌ خطا در ارسال پیام:", e)
                break
            await asyncio.sleep(1)
        
        key = f"processing:{user_id}"
        r.delete(key)



async def main():
    await client.start()
    print("✅ یوزربات فعال شد.")
    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
