import requests
import json

APP_HOST = 'http://127.0.0.1'
APP_PORT = '5000'
APP_URL = '{}:{}'.format(APP_HOST,APP_PORT)


PRODUCT_API_END_POINT = '{}/{}'.format(APP_URL, 'product')


product_data = [
    {
    'product_id' : 15117729,
    'current_price' : {
        'value' : 13.99,
        'currency_code' : 'USD'
        }
    },
{
    'product_id' : 16483589,
    'current_price' : {
        'value' : 14.99,
        'currency_code' : 'USD'
        }
    },
{
    'product_id' : 16696652,
    'current_price' : {
        'value' : 15.99,
        'currency_code' : 'USD'
        }
    },
{
    'product_id' : 16752456,
    'current_price' : {
        'value' : 16.99,
        'currency_code' : 'USD'
        }
    },
{
    'product_id' : 15643793,
    'current_price' : {
        'value' : 17.99,
        'currency_code' : 'USD'
        }
    }

]

headers = {'Content-type': 'application/json'}
for product in product_data:
    import pdb ;pdb.set_trace()
    r = requests.post(PRODUCT_API_END_POINT, data=json.dumps({'product' : product}), headers=headers)
    if r.status_code != requests.status_codes.codes.OK:
        raise Exception("Product seeding failed")