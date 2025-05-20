from domain.Reservation import Reservation
from data.ConexionMySQL import Conexion

class ReservationRepository:
    def __init__(self, conexion: Conexion):
        self.conexion = conexion

    def create_reservation(self, reservation: Reservation):
        # Verificar si el usuario ya existe
        check_user = "SELECT * FROM users WHERE id = %s"
        existing_user = self.conexion.fetch_one(check_user, (reservation.id,))

        if not existing_user:
            insert_user = """
                INSERT INTO users (id, name, last_name, email, password, status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            user_data = (
                reservation.id,
                reservation.name,
                reservation.last_name,
                reservation.email,
                reservation.password,
                reservation.status
            )
            self.conexion.execute_query(insert_user, user_data)

        insert_reservation = """
            INSERT INTO reservations (user_id, date_reservation, hour_reservation, room_number)
            VALUES (%s, %s, %s, %s)
        """
        reservation_data = (
            reservation.id,
            reservation.date_reservation,
            reservation.hour_reservation,
            reservation.room_number
        )
        self.conexion.execute_query(insert_reservation, reservation_data)

        # Obtener el id_reservation generado automáticamente
        new_id_result = self.conexion.fetch_one("SELECT LAST_INSERT_ID() as last_id")
        if new_id_result:
            new_id = new_id_result.get('last_id')
            return new_id 
        else:
            raise Exception("No se pudo obtener el ID de la reserva.")

    def get_reservas_by_cliente(self, user_id):
        query = """
            SELECT r.id_reservation, r.date_reservation, r.hour_reservation,
                   r.room_number,
                   u.id as user_id, u.name, u.last_name, u.email, u.password, u.status
            FROM reservations r
            JOIN users u ON r.user_id = u.id
            WHERE u.id = %s
        """
        results = self.conexion.fetch_all(query, (user_id,))
        reservas = []

        if results:
            for row in results:
                reserva = Reservation(
                    id=row['user_id'],
                    name=row['name'],
                    last_name=row['last_name'],
                    email=row['email'],
                    password=row['password'],
                    status=row['status'],
                    date_reservation=row['date_reservation'],
                    hour_reservation=row['hour_reservation'],
                    room_number=row['room_number']
                )
                reserva.id_reservation = row['id_reservation']
                reservas.append(reserva)

        return reservas
