from flask import Flask, jsonify, request, render_template, redirect, url_for

from datetime import datetime
from models.products import Product
from db import db
import json
from bson import ObjectId
import requests


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
EXTERNAL_API = 'http://redsky.target.com/v2/pdp/tcin/{}?excludes=taxonomy,price,promotion,bulk_ship,rating_and_review_reviews,rating_and_review_statistics,question_answer_statistics'

class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, datetime):
            return str(obj)



app = Flask(__name__)
app.config.from_object(__name__)
app.json_encoder = ProductEncoder

@app.route('/target/products/<id>', methods=['GET', 'PUT'])
def access_product_by_id(id):

    if request.method == 'GET':
        url = EXTERNAL_API.format(id)

        product_data = requests.get(url).json()
        product_name = str(product_data['product']['item']['product_description']['title'])

        product = db.Product.find_one({'id': int(id)}, {'_id': False})
        product['name'] = product_name
        return jsonify(product)

    elif request.method == 'PUT':

        req_data = request.get_json()
        product = db.Product.find_one({'id' : int(id)})
        product.current_price.value = req_data['current_price']['value']
        product.current_price.currency_code = req_data['current_price']['currency_code']
        #product = db.Product.update({'id' : int(req_data['id'])}, { '$set' : {'current_price' : {'value' : req_data['current_price']['value'], 'currency_code' : str(req_data['current_price']['currency_code'])}}})
        product.save()
        return jsonify(product)


@app.route('/target/products', methods=['GET', 'POST'])
def create_product():
    if request.method == 'GET':
        products = db.Product.find()
        products_list = []
        for product in products:
            products_list.append(product)

        return jsonify(products_list)

    elif request.method == 'POST':
        product = db.Product()
        req_data = request.get_json()
        product.id = req_data['product']['id']
        product.current_price = req_data['product']['current_price']
        product.save()
        return jsonify(product)

if __name__ == '__main__':
    app.run(port=5000, debug=True)