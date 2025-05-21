from domain.Reservation import Reservation

class ReservationService:
    def __init__(self, reservation_repository, customer_repository, room_repository, service_repository):
        self.reservation_repository = reservation_repository
        self.customer_repository = customer_repository
        self.room_repository = room_repository
        self.service_repository = service_repository  # Nuevo repositorio agregado

    def crear_reserva_interactivo(self, customer):
        try:
            # Obtener habitaciones disponibles
            available_rooms = self.room_repository.get_available_rooms()
            if not available_rooms:
                print("❌ No hay habitaciones disponibles.")
                return

            print("\n🔓 Habitaciones disponibles:")
            for room in available_rooms:
                print(f"Número: {room.room_number}, Tipo: {room.room_type}, Precio: {room.price}")

            room_number_input = input("Seleccione el número de habitación: ")
            if room_number_input not in [str(r.room_number) for r in available_rooms]:
                print("❌ Habitación no válida o no disponible.")
                return

            # Mostrar servicios disponibles
            available_services = self.service_repository.get_all()
            if not available_services:
                print("❌ No hay servicios disponibles.")
                return

            print("\n--- SERVICIOS DISPONIBLES ---")
            for svc in available_services:
                print(f"ID: {svc.service_id} - {svc.name} (${svc.price:.2f}): {svc.description}")

            service_id_input = input("Seleccione el ID del servicio deseado: ")
            if service_id_input not in [str(s.service_id) for s in available_services]:
                print("❌ Servicio no válido.")
                return

            service_id = int(service_id_input)

            date_reservation = input("Fecha de Reserva (YYYY-MM-DD): ")
            hour_reservation = input("Hora de Reserva (HH:MM): ")

            room_number = int(room_number_input)

            reservation = Reservation(
                customer.id,
                customer.name,
                customer.last_name,
                customer.email,
                customer.password,
                customer.status,
                date_reservation,
                hour_reservation,
                room_number
            )

            # Puedes añadir un atributo 'service_id' a Reservation si quieres guardar el servicio seleccionado
            reservation.service_id = service_id

            new_reservation_id = self.reservation_repository.create_reservation(reservation)
            self.room_repository.update_room_status(room_number, 'ocupada')

            selected_service = next((s for s in available_services if s.service_id == service_id), None)

            print(f"\n✅ Reserva creada exitosamente con ID {new_reservation_id} en la habitación {room_number}.")
            if selected_service:
                print(f"Servicio seleccionado: {selected_service.name} (${selected_service.price:.2f}) - {selected_service.description}")

            # Mostrar habitaciones disponibles restantes
            remaining_rooms = self.room_repository.get_available_rooms()
            if remaining_rooms:
                print("\n🔔 Habitaciones disponibles restantes:")
                for r in remaining_rooms:
                    print(f"Número: {r.room_number}, Tipo: {r.room_type}, Precio: {r.price}")
            else:
                print("\n❌ No hay más habitaciones disponibles.")

        except ValueError:
            print("❌ Entrada inválida. Por favor ingrese los datos correctamente.")
        except Exception as e:
            print(f"❌ Error al crear la reserva: {e}")

    def ver_reservas_por_cliente(self, id_cliente):
        try:
            reservas = self.reservation_repository.get_reservas_by_cliente(id_cliente)
            if not reservas:
                print("No tienes reservas registradas.")
                return

            print("\n--- TUS RESERVAS ---")
            for r in reservas:
                print(f"ID Reserva: {r.id_reservation}, Fecha: {r.date_reservation}, "
                      f"Hora: {r.hour_reservation}, Habitación: {r.room_number}")

        except Exception as e:
            print(f"❌ Error al obtener las reservas: {e}")
