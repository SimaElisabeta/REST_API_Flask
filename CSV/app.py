from flask import Flask, request, abort, jsonify
from product_repository import ProductRepository
import exceptions

app = Flask(__name__)
repo = ProductRepository('products.csv')


@app.route("/")
def index():
    return 'Main page working OK!'


@app.route("/product", methods=["POST"])
def add_product():
    product = request.json
    try:
        repo.add_product(product)
        return "OK", 201
    except exceptions.InvalidProductException as ex:
        abort(400, ex)


@app.route("/product/<name>", methods=["GET"])
def get_product(name):
    try:
        product = repo.find_by_name(name)
        return jsonify(product)
    except exceptions.ProductNotFoundException as ex:
        abort(404, ex)


@app.route("/product/<name>", methods=["PUT"])
def update_all_product_data(name):
    product = request.json
    try:
        repo.update_all_product_data(name, product)
        return "OK", 201
    except exceptions.ProductNotFoundException as ex:
        abort(404, ex)
    except exceptions.InvalidProductException as ex:
        abort(400, ex)


@app.route("/product/<name>", methods=["DELETE"])
def delete_product(name):
    try:
        repo.delete_by_name(name)
        return "", 204
    except exceptions.ProductNotFoundException as ex:
        abort(404, ex)


if __name__ == '__main__':
    app.run(debug=True)
