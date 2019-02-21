from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './am'
ALLOWED_EXTENSIONS = set(['mp3', 'wav'])

app = Flask(__name__)

def transcribe(name):
    conv = "ffmpeg -i ./eng/%s -acodec pcm_s16le -ac 1 -ar 8000 temp.wav " % name
    os.system(conv)
    shell = "./test.sh x.wav"
    os.system(shell)
    os.system("./lat.sh")
    os.system("./final.sh >test.txt")
    os.system("rm temp.wav")
    with open('test.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')

    return data


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/am")
def am():

    return render_template("am.html")


@app.route("/eng")
def eng():
    return render_template("eng.html")


@app.route("/eng/trans", methods=['GET', 'POST'])
def eng_trans():
    if request.method == 'POST':

        if 'file' not in request.files:
            return "No file"
        file = request.files['file']

        if file.filename == '':
            return "no selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            UPLOAD_FOLDER = './eng'
            transcription = ""
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            transcription = transcribe(file.filename)

            return transcription


@app.route("/am/trans", methods=['GET', 'POST'])
def am_trans():
    if request.method == 'POST':

        if 'file' not in request.files:
            return "No file"
        file = request.files['file']
        if file.filename == '':
            return "no selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            UPLOAD_FOLDER = './am'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            transcription = "Transcription not available yet"

            return transcription


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
