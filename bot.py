from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
import os
load_dotenv()
from redis import Redis
r = Redis()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
TOKEN = os.getenv("TOKEN")

DEV = int(os.getenv("DEV"))
USERBOT_USERNAME = os.getenv("USERBOT_USERNAME")  # بدون @

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

@app.on_message(filters.voice & filters.private & filters.incoming)
async def handle_voice(client, message: Message):
    user_id = message.chat.id
    key = f"processing:{user_id}"
    if r.exists(key):
        await message.reply("⏳ وویس قبلی هنوز در حال پردازشه لطفاً کمی صبر کن.")
        return

    if message.voice.duration > 60 * 5 :
        return await message.reply("در حال حاضر برای تبدیل باید وویس ارسالیتون زیر ۵ دقیقه باشه",quote=True)
    
    await app.send_voice(USERBOT_USERNAME,voice=message.voice.file_id, caption=f"user_id:{user_id}|message_id:{message.id}")
    r.set(key, "1", ex=600)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply("سلام لطفا وویست رو برای تبدیل به متن ارسال کن")


app.run()
