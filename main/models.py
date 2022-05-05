from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import UniqueConstraint


db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    images = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    # Ensure that the combination of user_id and product_id is unique.
    UniqueConstraint("user_id", "product_id", name="user_product_unique")
