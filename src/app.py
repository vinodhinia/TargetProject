from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_restful import Api
from mongokit import Document, Connection
from flask_mongokit import MongoKit
from datetime import datetime
from models.products import Product
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

app.config['MONGODB_SETTINGS'] = {
    'db': 'target',
    'host': 'localhost',
    'port': 27017
}


app.json_encoder = ProductEncoder

api = Api(app)


db = MongoKit(app)
db.register([Product])

# connection = Connection()
# db = connection['target']
#

#
# connection = Connection(app.config['MONGODB_HOST'],
#                         app.config['MONGODB_PORT'])



@app.route('/', methods=['GET'])
def get_all_products():

    products = db.Product.find()
    products_list = []
    for product in products:
        products_list.append(product)

    return jsonify(products_list)


@app.route('/products/<id>', methods=['GET', 'PUT'])
def get_product_by_id(id):

    if request.method == 'GET':
        import pdb;pdb.set_trace()
        product = db.Product.find_one({'product_id' : int(id)})
        return jsonify(product)

    elif request.method == 'PUT':
        req_data = request.get_json()
        product = db.Product.find_one({'_id' : ObjectId(id)})
        product.current_price = req_data
        #product = db.Product.update_one({'_id' : ObjectId(id)}, { '$set' : {'current_price' : {'value' : req_data['value'], 'currency_code' : req_data['currency_code']}}})
        product.save()
        return jsonify(product)

@app.route('/extproduct/<id>', methods=['GET'])
def get_data_from_external_api(id):
    url = EXTERNAL_API.format(id)

    product_data = requests.get(url).json()
    product_name = str(product_data['product']['item']['product_description']['title'])

    product = db.Product.find_one({'product_id' : int(id)})
    product['name'] = product_name
    #del product['_id']
    return jsonify(product)


@app.route('/product', methods=['POST'])
def create_product():
    if request.method == 'POST':
        product = db.Product()
        req_data = request.get_json()

        product.product_id = req_data['product']['product_id']
        product.current_price = req_data['product']['current_price']

        product.save()

        return jsonify(product)

if __name__ == '__main__':
    app.run(port=5000, debug=True)









