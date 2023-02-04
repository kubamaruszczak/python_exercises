from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/pdfs'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/form-entry', methods=["POST"])
def receive_data():
    username = request.form['username']
    password = request.form['password']
    return render_template("login.html", u_name=username, u_pass=password)


if __name__ == "__main__":
    app.run(debug=True)
