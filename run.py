from flask import Flask, send_file
from generate import generate_art
import io

app = Flask(__name__)

@app.route('/')
def index():
    return '<img src="./image.jpg" />'

@app.route('/image.jpg')
def render_image():
    image = generate_art()
    b = io.BytesIO()
    image.save(b, 'JPEG')
    b.seek(0)
    return send_file(
        b,
        mimetype='image/jpeg',
        as_attachment=True,
        attachment_filename='image.jpg')


app.run(debug=True)