# Generate tests

It's always a good practice to have unit tests for our services. Let's see if
Gemini can help us to write some unit tests for the product service.

Create a `product_service_test.py` file and add the following comment for
Gemini:

```python
# Create unit tests for product_service.py
```

Gemini should fill the rest:

```python
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
```

You can run and see the test results:

```sh
python product_service_test.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s
```
