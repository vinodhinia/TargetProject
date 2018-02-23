from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_restful import Api
from mongokit import Document, Connection
from flask_mongokit import MongoKit
from datetime import datetime
from datetime import date
from models.products import Product
import json
from bson import ObjectId


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017


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
        #import pdb;pdb.set_trace()
        product = db.Product.find_one({'_id' : ObjectId(id)})
        return jsonify(product)
    elif request.method == 'PUT':
        req_data = request.get_json()
        product = db.Product.find_one({'_id' : ObjectId(id)})
        product.current_price = req_data
        #product = db.Product.update_one({'_id' : ObjectId(id)}, { '$set' : {'current_price' : {'value' : req_data['value'], 'currency_code' : req_data['currency_code']}}})
        product.save()
        return jsonify(product)



@app.route('/product', methods=['POST'])
def create_product():
    if request.method == 'POST':
        import pdb;pdb.set_trace()
        product = db.Product()
        req_data = request.get_json()
        product.product_id = req_data['product']['product_id']
        product.current_price = req_data['product']['current_price']

        product.save()

        return jsonify(product)

if __name__ == '__main__':
    app.run(port=5000, debug=True)









