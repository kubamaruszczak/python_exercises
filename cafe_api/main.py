from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

# Connect to Database
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

# HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    # Query all cafes from database
    all_cafes = db.session.query(Cafe).all()
    random_cafe = choice(all_cafes)

    # Return a json with cafe data
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route('/search')
def search_cafe():
    # Read passed parameter
    query_location = request.args.get("loc")
    # Query all cafes
    cafe_selected = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe_selected is None:
        error_message = {
            "Not Found": "Sorry, we don't have a cafe at that location."
        }
        return jsonify(error=error_message)
    return jsonify(cafe=cafe_selected.to_dict())


# HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add_cafe():
    # Create new Cafe object
    new_cafe = Cafe(
        can_take_calls=bool(request.form.get("can_take_calls").title),
        coffee_price=request.form.get("coffee_price"),
        has_sockets=bool(request.form.get("has_sockets").title()),
        has_toilet=bool(request.form.get("has_toilet").title()),
        has_wifi=bool(request.form.get("has_wifi")),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        map_url=request.form.get("map_url"),
        name=request.form.get("name"),
        seats=request.form.get("seats"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
