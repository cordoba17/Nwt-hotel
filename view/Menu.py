from data.ConexionMySQL import Conexion
from application.CustomerService import CustomerService
from application.EmployeeService import EmployeeService
from data.CustomerRepository import CustomerRepository

class Menu:
    db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel_cesde')
    db.connect()

    def __init__(self):
        self.customer_service = CustomerService(CustomerRepository())
        self.employee_service = EmployeeService(self.db)  # Asegúrate que EmployeeService use la db si la necesitas

    def app(self):
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            option = int(input("1. Login Cliente\n2. Registro Cliente\n3. Login Empleado\n4. Registro Empleado\n5. Salir\nSeleccione opción: "))

            if option == 1:
                self.login_cliente()
            elif option == 2:
                self.customer_service.createCustomer(self.db)
            elif option == 3:
                self.employee_service.login_employee()
            elif option == 4:
                self.employee_service.createEmployee()  # Llamar al método correcto aquí
            elif option == 5:
                print("Saliendo...")
                self.db.disconnect()
                break
            else:
                print("Seleccione una opción válida.")

    def login_cliente(self):
        email = input("Ingrese su correo: ")
        password = input("Ingrese su contraseña: ")
        success = self.customer_service.login(self.db, email, password)
        if success:
            print("Login de cliente exitoso")
        else:
            print("Login de cliente fallido")
