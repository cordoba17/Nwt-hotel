from data.ConexionMySQL import Conexion
from domain.Room import Room

class RoomRepository:
    def __init__(self, conexion):
        self.conexion = conexion

    def get_all_rooms(self):
        query = "SELECT room_number, type, price, status FROM rooms"
        results = self.conexion.execute_query(query)
        rooms = []
        if results:
            for row in results:
                rooms.append(Room(row[0], row[1], row[2], row[3]))
        return rooms

    def get_available_rooms(self):
        query = "SELECT room_number, type, price, status FROM rooms WHERE status = 'disponible'"
        results = self.conexion.execute_query(query)
        rooms = []
        if results:
            for row in results:
                rooms.append(Room(row[0], row[1], row[2], row[3]))
        return rooms

    def update_room_status(self, room_number, new_status):
        query = "UPDATE rooms SET status = %s WHERE room_number = %s"
        self.conexion.execute_query(query, (new_status, room_number))

