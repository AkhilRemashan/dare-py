from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os   

# Init App
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__)) 

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init DB
db = SQLAlchemy(app)

# Init Marshmallow
marsh =  Marshmallow(app)

# Product Class/Modal
class Product(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(100), unique=True)
    description = db.Column (db.String(200))
    price = db.Column (db.Float)
    quantity = db.Column (db.Integer)

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

# Product Schema
class ProductSchema(marsh.Schema):
    class Mata:
        fields = ('id', 'name', 'description', 'price', 'quantity')

# Init Schema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)





# Run Server
if __name__ == '__main__':
    app.run(debug=True)