import patient

not_autenticate_message = "Nao autenticado"

class Screening:
    def createPatientScreening(self, cpf, weight=0, height=0, allergies='', blood_group='', authenticate=False): 
        if authenticate:
            patient_screening = patient.Patient(cpf, weight, height, allergies, blood_group)
            return patient_screening
        
        return not_autenticate_message


if __name__ == '__main__':
    patient = Screening("045.341.672-44", 70, 180, "abelha, leite, ovo, dipirona", "O+")
