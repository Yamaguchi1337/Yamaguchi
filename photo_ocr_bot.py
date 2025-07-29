import os
import tempfile
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from PIL import Image
import pytesseract


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Send me a photo and I will extract the text from it.")


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo = update.message.photo[-1]
    file = await photo.get_file()
    with tempfile.NamedTemporaryFile(suffix='.jpg') as f:
        await file.download_to_drive(f.name)
        text = pytesseract.image_to_string(Image.open(f.name))
    if text.strip():
        await update.message.reply_text(text)
    else:
        await update.message.reply_text("Couldn't recognize any text.")


def main() -> None:
    # Telegram bot token hardcoded as requested
    token = "7656359649:AAHN_0xwuSWlZuvUfqkZ6BqbSTKbnH6gdc4"
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    application.run_polling()


if __name__ == "__main__":
    main()
