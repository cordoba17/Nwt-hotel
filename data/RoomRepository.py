from domain.Room import Room
from data.ConexionMySQL import Conexion

class RoomRepository:

    def __init__(self):
        self.conexion = Conexion(None, None, None, None, None)

    def from_row(self, row):
        return Room(row[0], row[1], row[2], row[3])

    def create_room(self, db, room):
        query = "INSERT INTO room (room_number, type, price, status) VALUES (%s, %s, %s, %s)"
        values = (room.room_number, room.type, room.price, room.status)
        db.execute_query(query, values)

    def get_all_rooms(self, db):
        query = "SELECT * FROM room"
        result = db.execute_query(query)
        return [self.from_row(row) for row in result] if result else []

    def update_room(self, db, room):
        query = "UPDATE room SET type = %s, price = %s, status = %s WHERE room_number = %s"
        values = (room.type, room.price, room.status, room.room_number)
        db.execute_query(query, values)

    def delete_room(self, db, room_number):
        query = "DELETE FROM room WHERE room_number = %s"
        db.execute_query(query, (room_number,))
