from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from os import environ

app = Flask(__name__)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = environ.get("FLASK_SECRET_KEY")
db.init_app(app)

# Crete and initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Lines below only required once, when creating DB.
# with app.app_context():
#     db.create_all()

@login_manager.user_loader
def load_user(user):
    return User.query.get(int(user))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Secure password provided by the user
        secured_password = generate_password_hash(
            request.form.get('password'),
            method=environ.get('PASS_HASH'),
            salt_length=8
        )
        # Check if the user is already in the database
        provided_email = request.form.get('email')
        user_exists = db.session.query(User).filter_by(email=provided_email).first()
        if user_exists:
            flash("You've already registered with that email. Try logging in instead.")
            return redirect(url_for('login'))
        # Create new user
        new_user = User()
        new_user.email = provided_email
        new_user.name = request.form.get('name')
        new_user.password = secured_password
        # Save user in database
        db.session.add(new_user)
        db.session.commit()
        # Log in the new user
        login_user(new_user)
        return render_template("secrets.html", username=new_user.name)
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get user credentials
        provided_email = request.form.get("email")
        provided_password = request.form.get("password")
        # Query user from database
        user = db.session.query(User).filter_by(email=provided_email).first()
        if user is not None:
            if check_password_hash(user.password, provided_password):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash('Password incorrect, please try again.')
        else:
            flash("That email does not exist, please try again.")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files', 'cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
