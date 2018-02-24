from mongokit import Document, Connection
from db import db

#MONGODB_HOST = 'localhost'
#MONGODB_PORT = 27017
#
#connection = Connection(MONGODB_HOST,
#                        MONGODB_PORT)


@db.register
class Product(Document):
    __database__ = 'target'
    __collection__ = 'products'

    use_dot_notation = True

    structure = {
        'id': int,
        'current_price' : {
            'value' : float,
            'currency_code' : basestring
        }
    }



