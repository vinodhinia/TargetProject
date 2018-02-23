from mongokit import Document, Connection

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

connection = Connection(MONGODB_HOST,
                        MONGODB_PORT)


@connection.register
class Product(Document):
    __database__ = 'target'
    __collection__ = 'products'

    use_dot_notation = True

    structure = {
        'product_id': int,
        'current_price' : {
            'value' : float,
            'currency_code' : basestring
        }
    }



