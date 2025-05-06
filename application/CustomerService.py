from domain.Customer import Customer
from data.CustomerRepository import CustomerRepository

class CustomerService:

    def __init__(self, customer_repository):
        self.customer_repository = customer_repository

    def createCustomer(self, db):
        id = int(input("Ingrese su identificación: "))
        name = input("Ingrese su nombre: ")
        last_name = input("Ingrese su apellido: ")
        email = input("Ingrese su correo: ")
        password = input("Ingrese su password: ")
        status = input("¿Está activo? (True/False): ")
        origin = input("Ciudad de Origen: ")
        occupation = input("Ocupación: ")

        customer = Customer(id, name, last_name, email, password, status, origin, occupation)
        self.customer_repository.create_customer_repository(db, customer)

    def login(self, db, email, password):
        if self.customer_repository.login(db, email, password):
            print("Login exitoso")
            return True
        else:
            print("Error en el login")
            return False
