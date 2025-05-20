from domain.Customer import Customer
from data.CustomerRepository import CustomerRepository
from application.ReservationService import ReservationService  # Asegúrate de tener esta clase creada

class CustomerService:

    def __init__(self, customer_repository):
        self.customer_repository = customer_repository

    def createCustomer(self, db):
        try:
            id = int(input("Ingrese su identificación: "))
        except ValueError:
            print("Identificación inválida. Debe ser un número entero.")
            return

        name = input("Ingrese su nombre: ")
        last_name = input("Ingrese su apellido: ")
        email = input("Ingrese su correo: ")
        password = input("Ingrese su password: ")
        
        status_input = input("¿Está activo? (True/False): ")
        status = status_input.strip().lower() == 'true'
        
        origin = input("Ciudad de Origen: ")
        occupation = input("Ocupación: ")

        customer = Customer(id, name, last_name, email, password, status, origin, occupation)
        self.customer_repository.create_customer_repository(db, customer)

    def login(self):
        email = input("Ingrese su correo: ")
        password = input("Ingrese su contraseña: ")

    # Obtener el usuario por email
        user = self.customer_repository.select_customer_by_email(email)

        if user and user.password == password:
            print("✅ Login exitoso")
            return user  # Retornamos el objeto usuario completo
        else:
            print("❌ Error en el login")
            return None


