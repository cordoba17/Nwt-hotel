from domain.Customer import Customer
from data.CustomerRepository import CustomerRepository

class CustomerService:

    def __init__(self):
        self.customer_repository = CustomerRepository()

    def createCustomer(self, customer, db):
        # Solicita todos los datos del cliente
        id = int(input("Ingrese su identificación: "))
        name = input("Ingrese su nombre: ")
        last_name = input("Ingrese su apellido: ")
        email = input("Ingrese su correo: ")
        password = input("Ingrese su contraseña: ")
        status = input("¿Está activo? (True/False): ")
        origin = input("Ciudad de origen: ")
        occupation = input("Ocupación: ")

        # Crea un objeto Customer con los datos
        customer = Customer(
            id=id,
            name=name,
            last_name=last_name,
            email=email,
            password=password,
            status=status,
            origin=origin,
            occupation=occupation
        )

        # Guarda el cliente en la base de datos
        self.customer_repository.createCustomerReposity(db, customer)

    def login(self, db, email, password):
        if self.customer_repository.login(db, email, password):
            print("✅ Login exitoso.")
        else:
            print("❌ Error en el login.")
