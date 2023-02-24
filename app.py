from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def encrypt():
    print(request.form)
    text_to_encrypt = request.form['text']
    decrypted_text = text_to_encrypt[::-1]
    return render_template('index.html', decrypted_text=decrypted_text)
