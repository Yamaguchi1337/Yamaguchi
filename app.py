from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import tempfile

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    photo = request.files.get('photo')
    if not photo:
        return render_template('index.html', text='No file provided')
    with tempfile.NamedTemporaryFile(suffix='.jpg') as f:
        photo.save(f.name)
        text = pytesseract.image_to_string(Image.open(f.name))
    if not text.strip():
        text = "Couldn't recognize any text."
    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
