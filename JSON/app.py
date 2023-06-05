from flask import Flask, request, abort, jsonify
from user_repository import UserRepository
import exceptions

app = Flask(__name__)
repo = UserRepository('users.json')


@app.route("/")
def index():
    return 'Main page working OK!'


# GET
@app.route("/user/<username>", methods=['GET'])
def get_user(username):
    try:
        user = repo.find_by_name(username)
        return jsonify(user)
    except exceptions.UserNotFoundException as ex:
        abort(404, ex)


# POST
@app.route("/user", methods=['POST'])
def add_user():
    user = request.json
    try:
        repo.add_user(user)
        return "OK", 201
    except exceptions.InvalidUserException as ex:
        abort(400, ex)


# PUT
@app.route("/user/<username>", methods=['PUT'])
def update_all_user_data(username):
    user = request.json
    try:
        repo.update_user_data(username, user)
        return "OK", 201
    except exceptions.UserNotFoundException as ex:
        abort(404, ex)
    except exceptions.InvalidUserException as ex:
        abort(400, ex)


# DELETE
@app.route("/user/<username>", methods=['DELETE'])
def delete_user(username):
    try:
        repo.delete_by_username(username)
        return "", 204
    except exceptions.UserNotFoundException as ex:
        abort(404, ex)


if __name__ == '__main__':
    app.run(debug=True)
