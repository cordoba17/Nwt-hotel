

from domain.Customer import Customer
from application.CustomerService import CustomerService
from data.CustomerRepository import CustomerRepository
from data.ConexionMySQL import Conexion


class Menu:
    db = Conexion(host='localhost', port=3307, user='root', password="", database='hotel_cesde')
    db.connect()
    def __init__(self):
        self.customer = Customer(None,None,None,None,None,None,None,None)
        self.customer_service = CustomerService()
        self.customer_repo = CustomerRepository()




    def app(self,):
        init = int(input("Presione 1 para iniciar"))
        while init != 0:
            option = int(input("1. login 2. registro 3. Salir"))

            if option == 1:
                print("1. Login")
                print(self.login())
            elif option == 2:
                print("2. registro")
                self.customer_service.createCustomer(self.customer, self.db)
            elif option == 3:
                option = 0
            else:
                print ("Seleccione una opción correcta")


    def login(self):
        email = input("Ingrese su correo")
        password = input("Ingrese su contraseña")
        self.customer_service.login(self.db, email, password)






