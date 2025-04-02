

from domain.Customer import Customer

class CustomerService:



    def createCustomer(self, customer: Customer):
        id = int(input("Ingrese su identificacion"))
        customer.id = id
        name = input("Ingrese su nombre:")
        customer.name = name
        last_name = input("Ingrese su apellido")
        customer.last_name = last_name
        email = input("Ingrese su correo")
        customer.email = email
        password = input("Ingrese su password")
        customer.password = password
        status = input("Ingrese True Si esta activo")
        customer.status = status
        origin = input("Ciudad de Origen ")
        customer.origin = origin
        occupation = input("Ocupación")
        customer.occupation = occupation