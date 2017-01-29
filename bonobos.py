#!/usr/local/bin/env python

import flask
import flask_sqlalchemy
import hashlib
import os
import csv
from flask import request, json
from flask import render_template
from flask import abort
from flask import abort
from flask import render_template

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/bonobos.db'
db = flask_sqlalchemy.SQLAlchemy(app)

#Model
class Product(db.Model):
	__tablename__ = 'products_'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	product_id = db.Column(db.Integer)
	name = db.Column(db.String(100))
	image = db.Column(db.String(500))
	description = db.Column(db.String(1000))

	def __init__(self, product_id=None, name=None, image=None, description=None):
		self.product_id = product_id
		self.name = name
		self.image = image
		self.description = description

class Inventory(db.Model):
	__tablename__ = 'inventory'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	product_id = db.Column(db.Integer, db.ForeignKey("products_.product_id"))
	waist = db.Column(db.Integer)
	length = db.Column(db.Integer)
	style = db.Column(db.String(100))
	count = db.Column(db.Integer)

	def __init__(self, product_id=None, waist=None, length=None, style=None, count=None):
		self.product_id = product_id
		self.waist = waist
		self.length = length
		self.style = style
		self.count = count

#Util
def load_product_db():
	Product.query.delete()
	products_file = open("products.csv")
	csv_file = csv.reader(products_file, skipinitialspace=True)
	csv_file.next()
	for row in csv_file:
		product = Product(int(row[0]), row[1], row[2], row[3].replace("\xe2\x80\x99","'"))
		db.session.add(product)
		db.session.commit()

def load_json_from_product(product):
	return {"product_id":product.product_id,"product_name":product.name,"product_image":product.image,"product_description":product.description}

def load_inventory_db():
	Inventory.query.delete()
	inventory_file = open("inventory.csv")
	csv_file = csv.reader(inventory_file)
	csv_file.next()
	for row in csv_file:
		inventory_item = Inventory(int(row[0]), int(row[1]), int(row[2]), row[3], int(row[4]))
		db.session.add(inventory_item)
		db.session.commit()

def load_json_from_inventory(item):
	return {"product_id":item.product_id,"waist":item.waist,"length":item.length,"style":item.style,"count":item.count}

def build_product_inventory_json(product):
	product_json = load_json_from_product(product)
	inventory_json = []
	inventory = Inventory.query.filter(Inventory.product_id == product.product_id).all()
	for item in inventory:
		item = load_json_from_inventory(item)
		inventory_json.append(item)
	return {"product":product_json,"inventory":inventory_json}

#Routes
@app.route('/inventorybyproduct', methods = ['GET'])
def api_products():
	return get_inventory_by_product()

#Controller
def get_inventory_by_product():
	all_products = Product.query.all()
	all_products_json = []
	for product in all_products:
		all_products_json.append(build_product_inventory_json(product))
	return render_template('allinventory.html', products=all_products_json)

if __name__ == '__main__':
	db.create_all()
	port = int(os.environ.get("PORT", 5000))
	load_product_db()
	load_inventory_db()
	app.run(host='0.0.0.0', port=port)






