from domain.Customer import Customer
from application.CustomerService import CustomerService
from data.CustomerRepository import CustomerRepository
from data.ConexionMySQL import Conexion

class Menu:
    db = Conexion(host='localhost', port=3306, user='root', password="Eukzchoto3856", database='hotel_cesde')
    db.connect()

    def __init__(self):
        self.customer = Customer(None, None, None, None, None, None, None, None)
        self.customer_service = CustomerService()
        self.customer_repo = CustomerRepository()

    def app(self):
        init = int(input("Presione 1 para iniciar: "))
        while init != 0:
            option = int(input("1. Login\n2. Registro\n3. Salir\nSeleccione una opción: "))

            if option == 1:
                self.login()
            elif option == 2:
                print("Registro de usuario:")
                self.customer_service.createCustomer(self.customer, self.db)
            elif option == 3:
                print("Saliendo del sistema...")
                break
            else:
                print("Seleccione una opción correcta.")

    def login(self):
        email = input("Ingrese su correo: ")
        password = input("Ingrese su contraseña: ")
        self.customer_service.login(self.db, email, password)




