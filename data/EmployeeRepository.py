from domain.Employee import Employee

class EmployeeRepository:
    def __init__(self, conexion):
        self.conexion = conexion

    def create_employee_repository(self, employee):
        # Inserta primero en la tabla users
        insert_user = """
            INSERT INTO users (id, name, last_name, email, password, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        user_data = (
            employee.id,
            employee.name,
            employee.last_name,
            employee.email,
            employee.password,
            employee.status
        )

        # Inserta en la tabla employees
        insert_employee = """
            INSERT INTO employees (user_id, rol)
            VALUES (%s, %s)
        """
        employee_data = (
            employee.id,
            employee.rol
        )

        # Ejecuta las consultas
        self.conexion.execute_query(insert_user, user_data)
        self.conexion.execute_query(insert_employee, employee_data)

    def login(self, email, password):
        query = """
            SELECT * FROM users u
            JOIN employees e ON u.id = e.user_id
            WHERE u.email = %s AND u.password = %s
        """
        result = self.conexion.fetch_one(query, (email, password))
        return result is not None
