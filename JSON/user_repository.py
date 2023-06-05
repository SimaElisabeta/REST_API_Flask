import json

from user_validator import UserValidator
from exceptions import UserNotFoundException


class UserRepository:
    def __init__(self, file_name):
        self.file_name = file_name
        self.validator = UserValidator()

    def get_current_users_data(self):
        with open(self.file_name, 'r') as f:
            try:
                data = json.load(f)
            except:
                data = []
            return data

    def write_all(self, data):
        with open(self.file_name, 'w') as f:
            json.dump(data, f, indent=2)

    # GET
    def find_by_name(self, username):
        users = self.get_current_users_data()
        for user in users:
            if user["username"] == username:
                return user
        raise UserNotFoundException(f'Username {username} not found!')

    # POST
    def add_user(self, user):
        self.validator.validate_user(user)
        data = self.get_current_users_data()
        with open(self.file_name, 'w') as f:
            data.append(user)
            json.dump(data, f, indent=2)

    # PUT
    def update_user_data(self, username, new_user):
        self.validator.validate_user_update(new_user)
        users = self.get_current_users_data()
        is_found = False
        for user in users:
            if user['username'] == username:
                is_found = True
                user.clear()
                user.update({"username": username})
                user.update(new_user)
        if not is_found:
            raise UserNotFoundException(f'Username {username} not found!')
        self.write_all(users)

    # DELETE
    def delete_by_username(self, username):
        users = self.get_current_users_data()
        is_found = False
        for user in users:
            if user['username'] == username:
                is_found = True
                users.remove(user)
        if not is_found:
            raise UserNotFoundException(f'Username {username} not found!')
        self.write_all(users)
