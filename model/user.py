class User:
    def __init__(self, cpf, password):
        self.cpf = cpf
        self.password = password

    def user(self):
        print("User cpf:" + self.cpf)