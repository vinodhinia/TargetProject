import unittest
import requests
import random
import json



class TestProducts(unittest.TestCase):
    def setUp(self):
        self.APP_HOST = 'http://127.0.0.1'
        self.APP_PORT = '5000'
        self.APP_URL = '{}:{}'.format(self.APP_HOST, self.APP_PORT)

        self.PRODUCT_API_END_POINT = '{}/{}'.format(self.APP_URL, 'products')
        self.id = random.randint(10000,100000)


    def test_get_product_by_id(self):
        response = requests.get(self.PRODUCT_API_END_POINT)
        self.assertEqual(response.status_code, 200)

    def test_post_product_by_id(self):
        product ={
            'id' : self.id,
            'current_price' : {
                'value' : 13.99,
                'currency_code' : 'USD'
            }
        }
        headers = {'Content-type': 'application/json'}
        response = requests.post(self.PRODUCT_API_END_POINT, data=json.dumps({'product' : product}), headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_product_details_from_ext_api(self):
        GET_PRODUCTS_URL = '{}:{}/products/{}'.format(self.APP_HOST, self.APP_PORT, 13860428)
        response = requests.get(GET_PRODUCTS_URL)
        response_dict = json.loads(response.content)
        self.assert_(response_dict['name'])



if __name__ == "__main__":
    unittest.main()