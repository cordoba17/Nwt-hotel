from domain.User import User

class Reservation:
    def __init__(self, id, name, last_name, email, password, status, date_reservation, hour_reservation, room_number):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status
        self._date_reservation = date_reservation
        self._hour_reservation = hour_reservation
        self._room_number = room_number
        self._id_reservation = None  # Inicializado como None hasta que se cree en la BD
        self._service_id = None  # Si quieres agregar servicio

    @property
    def id_reservation(self):
        return self._id_reservation

    @id_reservation.setter
    def id_reservation(self, value):
        self._id_reservation = value

    @property
    def date_reservation(self):
        return self._date_reservation

    @date_reservation.setter
    def date_reservation(self, value):
        self._date_reservation = value

    @property
    def hour_reservation(self):
        return self._hour_reservation

    @hour_reservation.setter
    def hour_reservation(self, value):
        self._hour_reservation = value

    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, value):
        self._room_number = value

    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
