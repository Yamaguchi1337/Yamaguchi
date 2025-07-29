# Photo OCR Telegram Bot

This repository contains a simple Telegram bot that transcribes text from photos using OCR.

## Features
- Receives a photo from a user.
- Recognizes text in the photo using the Tesseract OCR engine through `pytesseract`.
- Replies with the extracted text.

## Requirements
- Python 3.8+
- A Telegram bot token (from [BotFather](https://t.me/BotFather)).
- Tesseract OCR installed on the system.
- Python packages listed in `requirements.txt`.

## Setup
1. Install system package **Tesseract** (on Ubuntu: `sudo apt-get install tesseract-ocr`).
2. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the bot (the token is already included in `photo_ocr_bot.py`):
   ```bash
   python photo_ocr_bot.py
   ```

When you send a photo to the bot, it will reply with the recognized text.
