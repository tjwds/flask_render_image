from flask import Flask
from generate import generate_art
import os

app = Flask(__name__)

@app.route('/')
def index():
    print(os.path.abspath(os.curdir))
    image = generate_art()
    image.save('static/images/render.jpg')
    return '<img src="./static/images/render.jpg" />'

app.run(debug=True)