class User:

    def __init__(self, username):
        self.username = username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    def get_name(self):
        return self.get_name()

    @staticmethod
    def validate_login(password_form, password):
        return password_form == password
