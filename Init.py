from domain.Customer import Customer
from application.CustomerService import CustomerService
from data.CustomerRepository import CustomerRepository
from view.Menu import Menu
from data.ConexionMySQL import Conexion

conexion = Conexion("localhost", 3306, "root", "", "hotel_cesde")
conexion.connect()


"""
customer = Customer(None,None,None,None,None,None,None,None)
customer1 = Customer(None,None,None,None,None,None,None,None)
customer_repository = CustomerRepository()
customer_service = CustomerService()

customer_service.createCustomer(customer)
customer_service.createCustomer(customer1)
customer_repository.createCustomerReposity(customer)"""



menu = Menu()

menu.app()