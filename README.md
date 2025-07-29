# Photo OCR Web App

This repository provides a simple web interface to transcribe text from photos using OCR.

## Features
- Upload a photo through a browser.
- Recognize text in the photo using the Tesseract OCR engine via `pytesseract`.
- Display the extracted text on the page.

## Requirements
- Python 3.8+
- Tesseract OCR installed on the system.
- Python packages listed in `requirements.txt`.

## Setup
1. Install the **Tesseract** system package (on Ubuntu: `sudo apt-get install tesseract-ocr`).
2. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the web app:
   ```bash
   python app.py
   ```
4. Open `http://localhost:8000` in your browser and upload a photo to see the recognized text.
