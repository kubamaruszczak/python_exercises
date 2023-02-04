# External modules
import os
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
# My modules
import polly_client

UPLOAD_FOLDER = 'uploaded_files'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/convert', methods=["POST"])
def convert_file():
    if request.method == "POST":
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('home'))
        file = request.files['file']

        # Check if the file was selected
        if file.filename == '':
            flash('No file selected')
            return redirect(url_for('home'))

        # Check if file has allowed extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.mkdir(app.config['UPLOAD_FOLDER'])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Here file conversion should be executed
            # TO ADD

            return redirect(url_for('download', filename=filename))
        else:
            flash('This is not pdf file')

    return redirect(url_for('home'))


@app.route('/download/<path:filename>', methods=["GET"])
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, path=filename)


if __name__ == "__main__":
    app.run(debug=True)
