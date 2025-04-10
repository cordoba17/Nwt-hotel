


from domain.Employee import Employee

class EmployeeRepository:

    def __init__(self):
        self.employees = []

    def createEmployeeReposity(self, employee: Employee):
        employee_data = []
        id = employee.id
        employee_data.append(id)
        name = employee.name
        employee_data.append(name)
        last_name = employee.last_name
        employee_data.append(last_name)
        email = employee.email
        employee_data.append(email)
        password = employee.password
        employee_data.append(password)
        status = employee.status
        employee_data.append(status)
        origin = employee.origin
        employee_data.append(origin)
        occupation = employee.occupation
        employee_data.append(occupation)

        self.employees.append(employee_data)
        print(self.employees)



    