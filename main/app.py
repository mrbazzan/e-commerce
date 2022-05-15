from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Product


main = Flask(__name__)
main.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@db/user"
main.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(main)

db.init_app(main)
migrate = Migrate(main, db)


@main.route("/api/products/")
def index():
    products = Product.query.all()
    return jsonify(products)
