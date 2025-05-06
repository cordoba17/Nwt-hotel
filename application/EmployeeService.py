
from domain.Employee import Employee
from data.EmployeeRepository import EmployeeRepository

class EmployeeService:

    def __init__(self):
        self.employee_repository = EmployeeRepository()
        self.employee = Employee()

    def createEmployee(self, employee):
        id = int(input("Ingrese su identificacion"))
        employee.id = id
        name = input("Ingrese su nombre:")
        employee.name = name
        last_name = input("Ingrese su apellido")
        employee.last_name = last_name
        email = input("Ingrese su correo")
        employee.email = email
        password = input("Ingrese su password")
        employee.password = password
        status = input("Ingrese True Si esta activo")
        employee.status = status
        origin = input("Ciudad de Origen ")
        employee.origin = origin
        occupation = input("Ocupación")
        employee.occupation = occupation
        rol = input("Rol")
        employee.rol = rol

        self.employee_repository.createEmployeeReposity(employee)
