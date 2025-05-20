from data.ConexionMySQL import Conexion
from application.CustomerService import CustomerService
from application.EmployeeService import EmployeeService
from data.CustomerRepository import CustomerRepository
from data.ReservationRepository import ReservationRepository
from data.RoomRepository import RoomRepository
from application.ReservationService import ReservationService
from application.RoomService import RoomService

class Menu:
    db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel_cesde')
    db.connect()

    def __init__(self):
        self.customer_repository = CustomerRepository(self.db)
        self.customer_service = CustomerService(self.customer_repository)
        self.employee_service = EmployeeService(self.db)
        self.reservation_repository = ReservationRepository(self.db)
        self.room_repository = RoomRepository(self.db)
        self.room_service = RoomService(self.room_repository)
        self.reservation_service = ReservationService(
            self.reservation_repository,
            self.customer_repository,
            self.room_repository
        )
        self.cliente_actual = None  # Importante: inicializar

    def app(self):
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            option = input("1. Login Cliente\n2. Registro Cliente\n3. Login Empleado\n4. Registro Empleado\n5. Salir\nSeleccione opción: ")
            
            if option == '1':
                self.login_cliente()
            elif option == '2':
                self.customer_service.createCustomer(self.db)
            elif option == '3':
                self.employee_service.login_employee()
            elif option == '4':
                self.employee_service.createEmployee()
            elif option == '5':
                print("Saliendo...")
                self.db.disconnect()
                break
            else:
                print("Seleccione una opción válida.")

    def login_cliente(self):
        customer = self.customer_service.login()
        if customer:
            print("✅ Login exitoso")
            self.cliente_actual = customer  # Guardar cliente logueado
            self.mostrar_menu_reservas()
        else:
            print("Login de cliente fallido")
        
    def mostrar_menu_reservas(self):
        while True:
            print("\n--- MENÚ DE RESERVAS ---")
            option = input("1. Crear reserva\n2. Ver todas las reservas\n3. Volver al menú principal\nSeleccione una opción: ")

            if option == '1':
                self.reservation_service.crear_reserva_interactivo(self.cliente_actual)
            elif option == '2':
                if self.cliente_actual:
                    self.reservation_service.ver_reservas_por_cliente(self.cliente_actual.id)
                else:
                    print("❌ No hay cliente logueado.")
            elif option == '3':
                break
            else:
                print("Seleccione una opción válida.")
