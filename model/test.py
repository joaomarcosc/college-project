import unittest
import auth
import screening


class LoginTest(unittest.TestCase):
# Teste unitário para cpf
    def test_cpf(self):
        cpf = "066.341.672-94"
        auth_test = auth.Auth()
        userV = auth_test.login(cpf, "S@ud4vel")
        self.assertEqual(userV.cpf, cpf)

# Teste unitário para password
    def test_password(self):
        cpf = "066.341.672-94"
        password = "S@ud4vel"
        auth_test = auth.Auth()
        userV = auth_test.login(cpf, password)
        self.assertEqual(userV.password, password)

# Teste integracao login 
    def test_login_correct_data(self):
        cpf = "066.341.672-94"
        password = "S@ud4vel"
        auth_test = auth.Auth()
        userV = auth_test.login(cpf, password)
        self.assertTrue(type(userV) != str)
        
# Teste integracao login
    def test_login_incorrect_data(self):
        cpf = "066.341.672-93"
        password = "saudável"
        auth_test = auth.Auth()
        userV = auth_test.login(cpf, password)
        self.assertTrue(type(userV) is str)

# Teste de seguranca
    def test_password_validation_success(self):
        cpf = "066.341.672-94"
        password = "S@ud4vel"
        auth_test = auth.Auth()
        userV = auth_test.login(cpf, password)
        self.assertTrue(type(userV) != str)

# Teste de seguranca
    def test_password_validation_fail(self):
        cpf = "066.341.672-94"
        password = "saudável"
        auth_test = auth.Auth()
        userV = auth_test.login(cpf, password)
        self.assertTrue(userV == auth.error_password_message)

# Teste de seguranca
    def test_cpf_validation_success(self):
        cpf = "066.341.672-94"
        password = "S@ud4vel"
        auth_test = auth.Auth()
        userV = auth_test.login(cpf, password)
        self.assertTrue(type(userV) != str)

# Teste de seguranca
    def test_cpf_validation_error(self):
        cpf = "066.341.672-4"
        password = "S@ud4vel"
        auth_test = auth.Auth()
        userV = auth_test.login(cpf, password)
        self.assertTrue(userV == auth.error_cpf_message)  


class TestScreening(unittest.TestCase):
# Teste de seguranca
    def test_fail_authentication(self):
        screening_test = screening.Screening()
        patient_screening = screening_test.createPatientScreening("045.341.672-44", 70, 180, "abelha, leite, ovo, dipirona", "O+", False)
        self.assertTrue(patient_screening == screening.not_autenticate_message)

# Teste de seguranca
    def test_success_authentication(self):
        screening_test = screening.Screening()
        patient_screening = screening_test.createPatientScreening("045.341.672-44", 70, 180, "abelha, leite, ovo, dipirona", "O+", False)
        self.assertTrue(not patient_screening is str)

if __name__ == '__main__':
    unittest.main()