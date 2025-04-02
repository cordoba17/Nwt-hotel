
from domain.Customer import Customer

class CustomerRepository:

    customers = []

    def createCustomerReposity(self, customer:Customer):
        customer_data = []
        id = customer.id
        customer_data.append(id)
        name = customer.name
        customer_data.append(name)
        last_name = customer.last_name
        customer_data.append(last_name)
        email = customer.email
        customer_data.append(email)
        password = customer.password
        customer_data.append(password)
        status = customer.status
        customer_data.append(status)
        origin = customer.origin
        customer_data.append(origin)
        occupation = customer.occupation
        customer_data.append(occupation)

        print(customer_data)