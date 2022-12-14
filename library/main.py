from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a books database
db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)


# Create a table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form['title'],
                        author=request.form['author'],
                        rating=request.form['rating'])
        # Add new book to the database
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html")


@app.route('/edit', methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        book_id = request.form["book_id"]
        book_details = db.get_or_404(Book, book_id)
        book_details.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for("home"))

    book_id = request.args.get("book_id")
    book_details = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_details)


@app.route('/delete', methods=["POST", "GET"])
def delete():
    book_id = request.args.get("book_id")
    book_selected = db.get_or_404(Book, book_id)
    db.session.delete(book_selected)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

