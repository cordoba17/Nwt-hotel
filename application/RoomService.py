from domain.Room import Room
from data.RoomRepository import RoomRepository

class RoomService:

    def __init__(self):
        self.room_repository = RoomRepository()

    def register_room(self, db):
        room_number = int(input("Número de habitación: "))
        type = input("Tipo (sencilla/doble/suite): ")
        price = float(input("Precio por noche: "))
        status = input("Estado (disponible/ocupada/mantenimiento): ")
        room = Room(room_number, type, price, status)
        self.room_repository.create_room(db, room)

    def show_rooms(self, db):
        rooms = self.room_repository.get_all_rooms(db)
        for room in rooms:
            print(f"Habitación {room.room_number} | Tipo: {room.type} | Precio: ${room.price} | Estado: {room.status}")
