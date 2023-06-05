from exceptions import InvalidProductException


class ProductValidator:
    def validate_product(self, product):
        if "name" not in product:
            raise InvalidProductException("No name provided")
        if "price" not in product:
            raise InvalidProductException("No price provided")
        if "category" not in product:
            raise InvalidProductException("No category provided")
