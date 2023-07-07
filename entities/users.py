class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password
