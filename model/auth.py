import user


class Auth:
    def __init__(self, cpf, password):
        self.user = {}

        self.user = user.User(cpf, password)


if __name__ == '__main__':
    auth = Auth(121343, "psapsapo")
