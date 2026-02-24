import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8672114822:AAHUPS661kpqsNy-1yx4t8ZU-_PSy65xg-w"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Instagram link yubor 📥")

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if "instagram.com" not in url:
        return
    await update.message.reply_text("⏳ Yuklanmoqda...")
    try:
        api = f"https://api.sssinstagram.com/download?url={url}"
        r = requests.get(api)
        data = r.json()
        video_url = data["video"]
        await update.message.reply_video(video_url)
    except:
        await update.message.reply_text("❌ Xatolik")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download))
app.run_polling()
