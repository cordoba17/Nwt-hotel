from domain.Customer import Customer
from application.CustomerService import CustomerService
from data.CustomerRepository import CustomerRepository



customer = Customer(None,None,None,None,None,None,None,None)
customer_repository =CustomerRepository()
customer_service = CustomerService()

customer_service.createCustomer(customer)
customer_service.createCustomer(customer)
customer_repository.createCustomerReposity(customer)
