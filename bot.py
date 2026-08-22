import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salam! 👋\n"
        "Mənə TikTok linki göndər."
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "tiktok.com" in text or "vm.tiktok.com" in text:
        await update.message.reply_text(
            "Link qəbul edildi. Videonu hazırlayıram..."
        )
    else:
        await update.message.reply_text(
            "Zəhmət olmasa TikTok linki göndər."
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

app.run_polling()
