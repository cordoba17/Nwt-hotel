import mysql.connector

class Conexion:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.connect()  # conectar automáticamente al crear instancia

    def connect(self):
        try:
            if self.connection is None or not self.connection.is_connected():
                self.connection = mysql.connector.connect(
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                )
                print("Conexión establecida")
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos:", err)

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.")

    def __del__(self):
        self.disconnect()

    def execute_query(self, query, params=None):
        """
        Ejecuta consultas INSERT, UPDATE, DELETE o SELECT.
        Para SELECT devuelve lista de tuplas (no diccionarios).
        """
        self.connect()  # asegurar conexión activa antes de ejecutar
        cursor = self.connection.cursor(buffered=True)
        try:
            cursor.execute(query, params)
            if query.strip().lower().startswith('select'):
                result = cursor.fetchall()
                return result  # lista de tuplas
            else:
                self.connection.commit()
                print("Consulta ejecutada exitosamente")
                return None
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta:", err)
            return None
        finally:
            cursor.close()

    def fetch_one(self, query, params=None):
        self.connect()
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            result = cursor.fetchone()
            print("Consulta fetch_one ejecutada exitosamente")
            return result
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta:", err)
            return None
        finally:
            cursor.close()

    def fetch_all(self, query, params=None):
        """
        Ejecuta una consulta SELECT y devuelve todos los resultados como lista de diccionarios.
        """
        self.connect()
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            print("Consulta fetch_all ejecutada exitosamente")
            return result
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta:", err)
            return None
        finally:
            cursor.close()
