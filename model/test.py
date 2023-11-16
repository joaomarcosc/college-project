import unittest
import auth

# Teste unitario para autenticacao do usuario
class LoginTest(unittest.TestCase):
    def test_cpf(self):
        cpf = 123456
        auth_test = auth.Auth()
        user = auth_test.login(cpf, "oapasoakspoaks")
        self.assertEqual(user.cpf, cpf)

    def test_password(self):
        cpf = 123456
        password = "oapasoakspoaks"
        auth_test = auth.Auth()
        user = auth_test.login(cpf, password)
        self.assertEqual(user.password, password)

if __name__ == '__main__':
    unittest.main()