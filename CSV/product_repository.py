import csv
from product_validator import ProductValidator
from exceptions import ProductNotFoundException


class ProductRepository:
    def __init__(self, file_name):
        self.file_name = file_name
        self.validator = ProductValidator()

    def get_current_products_data(self):
        with open(self.file_name, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def write_all(self, products):
        with open(self.file_name, 'w', newline='\n') as f:
            writer = csv.writer(f)
            writer.writerow(["name", "price", "category"])
            if products:
                writer.writerows(products)

    # POST
    def add_product(self, product):
        self.validator.validate_product(product)
        with open(self.file_name, 'a', newline='\n') as f:
            writer = csv.writer(f)
            writer.writerow(product.values())

    # GET
    def find_by_name(self, name):
        products = self.get_current_products_data()
        for product in products:
            if product["name"] == name:
                return product
        raise ProductNotFoundException(f'Product: {name} not found')

    # PUT
    def update_all_product_data(self, name, new_product):
        found_products = []
        is_found = False
        products = self.get_current_products_data()
        self.validator.validate_product(new_product)
        for product in products:
            if product['name'] == name:
                is_found = True
                product.clear()
                product.update(new_product)
            found_products.append(product.values())
        if not is_found:
            raise ProductNotFoundException(f"Product: {name} not found")
        self.write_all(found_products)

    # DELETE
    def delete_by_name(self, name):
        found_products = []
        is_found = False
        products = self.get_current_products_data()
        for product in products:
            if product["name"] == name:
                is_found = True
                continue
            found_products.append(product.values())
        if not is_found:
            raise ProductNotFoundException(f"Product: {name} not found")
        self.write_all(found_products)
