# Create unit tests for product_service.py

import unittest
from product_service import ProductService

class TestProductService(unittest.TestCase):

    def test_get_products(self):
        product_service = ProductService()
        products = product_service.get_products()
        self.assertEqual(len(products), 10)

    def test_get_product(self):
        product_service = ProductService()
        product = product_service.get_product(1)
        self.assertEqual(product["id"], 1)
        self.assertEqual(product["name"], "Milk")
        self.assertEqual(product["description"], "Fresh milk from local cows")
        self.assertEqual(product["quantity"], 10)

if __name__ == '__main__':
    unittest.main()