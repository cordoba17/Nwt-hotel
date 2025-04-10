
from domain.Customer import Customer
from data.ConexionMySQL import Conexion

class CustomerRepository:

    def __init__(self):
        self.conexion = Conexion(None, None, None, None, None)
        self.customer = Customer(None, None, None, None, None, None, None, None)


    @staticmethod
    def from_row(row):
        return Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

    def createCustomerReposity(self,db, customer):
        self.insert_customer(db,customer)


    def insert_customer(self,db,customer):
        query = "INSERT INTO customer (customer_id, name, last_name, email, password, status, origin , occupation) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)"
        values = (customer.id, customer.name, customer.last_name, customer.email, customer.password, customer.status, customer.origin, customer.occupation)
        db.execute_query(query, values)


    def select_customer(self,  db, customer_id):
        query = "SELECT * FROM customer WHERE id = %s"
        result = db.execute_query(query, (customer_id,))
        if result:
            return self.from_row(result[0])
        else:
            print("Customer not found.")
            return None

    def select_all_customers(self,  db):
        query = "SELECT * FROM customer"
        result = db.execute_query(query)
        if result:
            customers = []
            for row in result:
                customer = self.from_row(row)
                customers.append(customer)
            return customers
        else:
            print("No customers found.")
            return []

    def update_customer(self,  db, customer):
        query = "UPDATE customer SET name = %s, last_name = %s, email = %s, password = %s, status = %s, origin = %s, occupation = %s WHERE id = %s"
        values = (customer.name, customer.last_name, customer.email, customer.password, customer.status, customer.origin, customer.occupation, customer.id)
        db.execute_query(query, values)

    def delete_customer(self,  db, customer_id):
        query = "DELETE FROM customer WHERE id = %s"
        db.execute_query(query, (customer_id,))



    def login(self, db, email, password):
        query = "SELECT * FROM customer WHERE email = %s AND password = %s"
        result = db.execute_query(query, (email, password))
        if result:
            return True
        else:
            return False






