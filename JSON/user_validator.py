from exceptions import InvalidUserException


class UserValidator:
    def validate_user(self, user):
        if "username" not in user:
            raise InvalidUserException("No username provided!")
        if "first_name" not in user:
            raise InvalidUserException("No first_name provided!")
        if "last_name" not in user:
            raise InvalidUserException("No last_name provided!")

    def validate_user_update(self, user):
        if "username" in user:
            raise InvalidUserException("User already has a username")
        if "first_name" not in user:
            raise InvalidUserException("No first_name provided!")
        if "last_name" not in user:
            raise InvalidUserException("No last_name provided!")
