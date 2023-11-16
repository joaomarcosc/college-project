import user

class Auth:
  def __init__(self): 
    self.user = {}

  def login(self, cpf, password):
    self.user = user.User(cpf, password)
    return self.user


if __name__ == '__main__':
  auth = Auth()

  user = auth.login(123456, "oapasoakspoaks")