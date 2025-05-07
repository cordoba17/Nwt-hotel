from domain.Employee import Employee
from data.EmployeeRepository import EmployeeRepository

class EmployeeService:
    def __init__(self, conexion):
        self.employee_repository = EmployeeRepository(conexion)

    def createEmployee(self):
        id = int(input("Ingrese su identificacion: "))
        name = input("Ingrese su nombre: ")
        last_name = input("Ingrese su apellido: ")
        email = input("Ingrese su correo: ")
        password = input("Ingrese su password: ")
        status = input("¿Está activo? (True/False): ").lower() == "true"
        rol = input("Rol: ")

        employee = Employee(id, name, last_name, email, password, status, rol)
        self.employee_repository.create_employee_repository(employee)

    def login_employee(self):
        email = input("Ingrese su correo: ")
        password = input("Ingrese su contraseña: ")

        if self.employee_repository.login(email, password):
            print("Login exitoso como empleado.")
        else:
            print("Correo o contraseña incorrectos.")
