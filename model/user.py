class User:
    def __init__(self, cpf, password):
        self.cpf = cpf
        self.password = password

    def getAuthenticateUser(self):
        return  "Usuario autenticado com sucesso!!!"
    

authenticate_user = User("066.341.672-94", "S@ud4vel")
