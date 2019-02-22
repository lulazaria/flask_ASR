from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os


ALLOWED_EXTENSIONS = set(['mp3', 'wav'])

app = Flask(__name__)

def transcribe(name):
    conv = "./preprocesser.sh %s" % name
    os.system(conv)
    os.system("pwd > pwd.txt")
    pwd = open("pwd.txt","r")
    path = pwd.read()
    path = path.replace("\n","")
    path = path.split("/egs/aspire/s5")
    
    shell = "./transcribe.sh %s temp.wav" % path[0]
    os.system(shell)
    os.system("./lat.sh")
    out = "./output.sh %s >transcription.txt" % path
    os.system("./output.sh >transcription.txt")
    os.system("rm temp.wav")
    with open('transcription.txt', 'r') as myfile:
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
	else:
		return "Not a valid format"

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
            file.truncate()
            transcription = "Transcription not available yet"

            return transcription
	else:
		return "Not a valid format"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
