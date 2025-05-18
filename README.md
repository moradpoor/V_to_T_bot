## 🎙️ Telegram Voice-to-Text Bot (via Premium Userbot)

This Telegram bot allows users to send voice messages and receive the transcribed text in return.
It works by forwarding the voice message to a **Telegram userbot** with an active **Premium subscription**, which uses Telegram’s internal voice-to-text feature. The result is then sent back to the user through the main bot.

---

### ⚙️ How It Works

1. A user sends a voice message to the bot.
2. The bot forwards the voice to a Premium-enabled userbot.
3. The userbot uses Telegram’s built-in transcription (voice-to-text).
4. The transcribed text is returned to the user through the main bot.

---

### ⚠️ Requirements

* A **Telegram Premium** account connected as a userbot.
* Python 3.8+
* Redis server (for task state management)

---

## 🎥 Setup Video Tutorial | آموزش ویدیویی راه‌اندازی

If you prefer a video guide, watch this tutorial on YouTube:  
اگر ترجیح می‌دهید به‌صورت ویدیویی آموزش ببینید، این آموزش را در یوتوب مشاهده کنید:

👉 [Watch on YouTube](https://youtu.be/pOJX022DEAk)


### 🛠️ Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/moradpoor/V_to_T_bot.git
   cd V_to_T_bot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   > Required libraries: `telethon`, `pyrogram`, `aiogram`, `python-dotenv`, `redis`

3. Create a `.env` file in the root directory and fill in your own credentials:

   ```env
   API_ID=your_api_id
   API_HASH=your_api_hash
   TOKEN=your_bot_token
   USERBOT_USERNAME=your_userbot_username
   DEV=your_telegram_id
   ```

4. Run the bot:

   ```bash
   python bot.py
   ```
5. Run the userbot

   ```bash
   python cli.py
   ```

---

## 🎙️ ربات تبدیل وویس به متن تلگرام (با استفاده از یوزربات پریمیوم)

این ربات به کاربران اجازه می‌دهد پیام صوتی (وویس) ارسال کنند و متن تبدیل‌شده آن را دریافت نمایند.
وویس کاربر برای یک **یوزربات دارای اشتراک پریمیوم** ارسال شده، و با استفاده از قابلیت داخلی تلگرام به متن تبدیل می‌شود. سپس متن نهایی از طریق ربات برای کاربر ارسال خواهد شد.

---

### ⚙️ نحوه عملکرد

1. کاربر یک پیام صوتی ارسال می‌کند.
2. رباط آن را برای یوزربات متصل به تلگرام پریمیوم فوروارد می‌کند.
3. یوزربات با استفاده از سرویس رسمی تلگرام وویس را به متن تبدیل می‌کند.
4. متن نهایی توسط رباط اصلی به کاربر بازگردانده می‌شود.

---

### ⚠️ پیش‌نیازها

* یک اکانت تلگرام پریمیوم به عنوان یوزربات
* پایتون 3.8 یا بالاتر
* Redis برای مدیریت وضعیت کاربران

---

### 📆 راه‌اندازی

1. ریپازیتوری را کلون کنید:

   ```bash
   git clone https://github.com/your-username/V_to_T_bot.git
   cd V_to_T_bot
   ```

2. کتابخانه‌های مورد نیاز را نصب کنید:

   ```bash
   pip install -r requirements.txt
   ```

   > کتابخانه‌های مورد نیاز: `telethon`, `pyrogram`, `aiogram`, `python-dotenv`, `redis`

3. فایل `.env` را در پوشه‌ی اصلی بسازید و مقادیر خود را وارد کنید:

   ```env
   API_ID=your_api_id
   API_HASH=your_api_hash
   TOKEN=your_bot_token
   USERBOT_USERNAME=your_userbot_username
   DEV=your_telegram_id
   ```

4. اجرای ربات:

   ```bash
   python bot.py
   ```

5. اجرای یوزربات
   ```bash
   python cli.py
   ```
---

🎉 حالا رباط آماده است!
