from domain.Customer import Customer
from data.ConexionMySQL import Conexion

class CustomerRepository:

    def __init__(self, conexion: Conexion):
        self.conexion = conexion

    @staticmethod
    def from_row(row):
        return Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

    def create_customer_repository(self, customer):
        self.insert_customer(customer)

    def insert_customer(self, customer):
        query = """
            INSERT INTO customer (customer_id, name, last_name, email, password, status, origin , occupation)
            VALUES (%s,%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            customer.id, customer.name, customer.last_name,
            customer.email, customer.password, customer.status,
            customer.origin, customer.occupation
        )
        try:
            self.conexion.execute_query(query, values)
        except Exception as e:
            print(f"Error al insertar cliente: {e}")

    def select_customer(self, customer_id):
        query = "SELECT * FROM customer WHERE customer_id = %s"
        try:
            result = self.conexion.execute_query(query, (customer_id,))
            if result:
                return self.from_row(result[0])
            else:
                print("Customer not found.")
                return None
        except Exception as e:
            print(f"Error al seleccionar cliente: {e}")
            return None

    def select_customer_by_email(self, email):
        query = "SELECT * FROM customer WHERE email = %s"
        try:
            result = self.conexion.execute_query(query, (email,))
            if result:
                return self.from_row(result[0])
            else:
                return None
        except Exception as e:
            print(f"Error al seleccionar cliente por email: {e}")
            return None

    def select_all_customers(self):
        query = "SELECT * FROM customer"
        try:
            result = self.conexion.execute_query(query)
            if result:
                return [self.from_row(row) for row in result]
            else:
                print("No customers found.")
                return []
        except Exception as e:
            print(f"Error al obtener todos los clientes: {e}")
            return []

    def update_customer(self, customer):
        query = """
            UPDATE customer
            SET name = %s, last_name = %s, email = %s, password = %s,
                status = %s, origin = %s, occupation = %s
            WHERE customer_id = %s
        """
        values = (
            customer.name, customer.last_name, customer.email, customer.password,
            customer.status, customer.origin, customer.occupation, customer.id
        )
        try:
            self.conexion.execute_query(query, values)
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")

    def delete_customer(self, customer_id):
        query = "DELETE FROM customer WHERE customer_id = %s"
        try:
            self.conexion.execute_query(query, (customer_id,))
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")

    def login(self, email, password):
        query = "SELECT * FROM customer WHERE email = %s AND password = %s"
        try:
            result = self.conexion.execute_query(query, (email, password))
            if result:
                return self.from_row(result[0])  # Devuelve el objeto Customer completo
            else:
                return None
        except Exception as e:
            print(f"Error en login: {e}")
            return None
