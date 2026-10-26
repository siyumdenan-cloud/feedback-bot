import os
import asyncio
import logging
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler,
                          MessageHandler, filters, ContextTypes)

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ["8255651024:AAG7H8lHQnG9rU9mGXMb1dwi6yUiiEh3aqw"]
CHANNEL_ID = int(os.environ["-1003718644817"])


async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\nApna feedback photo ya video ke roop me bhejein.")


async def media(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    m = update.message
    status = await m.reply_text("⏳ Sending.")

    # sirf media bhejna, koi text/caption nahi
    if m.photo:
        await ctx.bot.send_photo(CHANNEL_ID, m.photo[-1].file_id)
    elif m.video:
        await ctx.bot.send_video(CHANNEL_ID, m.video.file_id)

    for dots in ["⏳ Sending..", "⏳ Sending..."]:
        await asyncio.sleep(0.6)
        await status.edit_text(dots)
    await asyncio.sleep(0.6)
    await status.edit_text("✅ Feedback successfully sent!\nThank you 🙏")


async def other(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Sirf photo ya video bhejein.")


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO, media))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, other))
    app.run_polling()


if __name__ == "__main__":
    main()
