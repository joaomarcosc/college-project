import re
import user



error_password_message = "A senha precisar ter no minimo 8 caracteres, no minimo 1 caractere especial, no minimo 1 numero e no minimo 1 letra maiúscula"

error_authenticate_message = "Usuario nao existe ou credenciais invalidas"

error_cpf_message = "Este CPF e invalido"

def validate_factory(value, pattern):
    match = re.match(pattern, value)
    return bool(match)


def validate_password(password):
    return validate_factory(password, r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$")

def validate_cpf(cpf):
    return validate_factory(cpf, r"^([0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2})$")

class Auth:
    def __init__(self):
        self.user = {}
    
    def login(self, cpf, password):
        authenticate_cpf =  user.authenticate_user.cpf
        authenticate_password = user.authenticate_user.password

        if not validate_password(password):
            return error_password_message

        if not validate_cpf(cpf):
            return error_cpf_message

        if cpf == authenticate_cpf and password == authenticate_password:
            return user.User(cpf, password)
        

        return error_authenticate_message

if __name__ == '__main__':
    auth = Auth(121343, "psapsapo")
