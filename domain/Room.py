class Room:
    def __init__(self, room_number, room_type, price, status):
        self.room_number = room_number  # número de habitación
        self.room_type = room_type      # tipo (sencilla, doble, suite)
        self.price = price              # precio por noche
        self.status = status            # 'disponible', 'ocupada', 'mantenimiento'
    
    def is_available(self):
        return self.status == 'disponible'
