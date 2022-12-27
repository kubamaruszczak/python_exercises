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
@app.route('/update-price/<int:cafe_id>', methods=["PATCH"])
def update_cafe(cafe_id):
    cafe_selected = db.session.query(Cafe).get(cafe_id)
    if cafe_selected is not None:
        cafe_selected.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(success="Successfully updated the price."), 200
    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>')
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe_selected = db.session.query(Cafe).get(cafe_id)
        if cafe_selected is None:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            db.session.delete(cafe_selected)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
