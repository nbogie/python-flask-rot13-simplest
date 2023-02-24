# quickstart docs for flask
# https: // flask.palletsprojects.com/en/2.2.x/quickstart/

from flask import Flask, redirect, url_for, request, render_template, session
from rot13 import rot13

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def encrypt():
    print(request.form)
    text_to_encrypt = request.form['text']
    decrypted_text = rot13(text_to_encrypt)
    return render_template('index.html', decrypted_text=decrypted_text)
