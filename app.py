
from flask import Flask, jsonify, abort, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from DPR import DPR
from STT import STT

UPLOAD_FOLDER = '/home/fab/PycharmProjects/GLASpeechAPO'
ALLOWED_EXTENSIONS = {'wav'}



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "something"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/getSTT', methods=['POST'])
def getSTT():
    print(request.files)
    print(request)
    file = request.files['']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    print(filename)
    text = STT(filename)
    print(text)
    return text


@app.route('/getDPR', methods=['POST'])
def getDetailPhoneticResult():
    print(request.files)
    print(request)
    file = request.files['']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    print(filename)
    text = DPR(filename)
    print(text)
    return text

if __name__ == '__main__':
    app.run()
