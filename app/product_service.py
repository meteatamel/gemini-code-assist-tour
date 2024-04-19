class ProductService:

    _products = [
        {
            "id": 1,
            "name": "Milk",
            "description": "Fresh milk from local cows",
            "quantity": 10
        },
        {
            "id": 2,
            "name": "Bread",
            "description": "Fresh bread from local bakery",
            "quantity": 10
        },
        {
            "id": 3,
            "name": "Eggs",
            "description": "Fresh eggs from local chickens",
            "quantity": 10
        },
        {
            "id": 4,
            "name": "Cheese",
            "description": "Fresh cheese from local cows",
            "quantity": 10
        },
        {
            "id": 5,
            "name": "Butter",
            "description": "Fresh butter from local cows",
            "quantity": 10
        },
        {
            "id": 6,
            "name": "Yogurt",
            "description": "Fresh yogurt from local cows",
            "quantity": 10
        },
        {
            "id": 7,
            "name": "Apples",
            "description": "Fresh apples from local orchard",
            "quantity": 10
        },
        {
            "id": 8,
            "name": "Oranges",
            "description": "Fresh oranges from local orchard",
            "quantity": 10
        },
        {
            "id": 9,
            "name": "Bananas",
            "description": "Fresh bananas from local orchard",
            "quantity": 10
        },
        {
            "id": 10,
            "name": "Grapes",
            "description": "Fresh grapes from local orchard",
            "quantity": 10
        }
    ]

    def get_products(self):
        return self._products

    def get_product(self, product_id):
        for product in self._products:
            if product["id"] == product_id:
                return product