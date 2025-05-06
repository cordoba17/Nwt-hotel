from domain.Customer import Customer
from data.ConexionMySQL import Conexion
from data.CustomerRepository import CustomerRepository
from application.CustomerService import CustomerService

class Menu:
    db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel_cesde')
    db.connect()

    def __init__(self):
        self.customer = Customer(None, None, None, None, None, None, None, None)
        self.customer_repo = CustomerRepository()
        self.customer_service = CustomerService(self.customer_repo)

    def app(self):
        init = int(input("Presione 1 para iniciar: "))
        while init != 0:
            option = int(input("1. Login\n2. Registro\n3. Salir\nSeleccione opción: "))

            if option == 1:
                print(self.login())
            elif option == 2:
                self.customer_service.createCustomer(self.db)
            elif option == 3:
                print("Saliendo...")
                break
            else:
                print("Seleccione una opción correcta")

    def login(self):
        email = input("Ingrese su correo: ")
        password = input("Ingrese su contraseña: ")
        success = self.customer_service.login(self.db, email, password)
        if success:
            return "Login exitoso"
        else:
            return "Login fallido"
