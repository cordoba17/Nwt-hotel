class Room:
    def __init__(self, room_number, type, price, status):
        self.room_number = room_number  # número de la habitación
        self.type = type                # tipo (ej: sencilla, doble, suite)
        self.price = price              # precio por noche
        self.status = status            # disponible, ocupada, mantenimiento
