from domain.User import User

class Reservation(User):

    def __init__(self, id, name, last_name, email, password, status, id_reservation, date_reservation, hour_reservation):
        #llama al constructor de la clase padre (user)
        super().__init__(id,name, last_name, email, password, status)
        #atributos propios de reservation
        self._id_reservation = id_reservation
        self._date_reservation = date_reservation
        self._hour_reservation = hour_reservation

        #------Getters y setters------

    @property
    def id_reservation(self):
        return self._id_reservation

    @id_reservation.setter
    def id_reservation(self, id_reservation):
        self._id_reservation = id_reservation

    @property
    def date_reservation(self):
        return self._date_reservation

    @date_reservation.setter
    def date_reservation(self, date_reservation):
        self._date_reservation = date_reservation

    @property
    def hour_reservation(self):
        return self._hour_reservation

    @hour_reservation.setter
    def hour_reservation(self, hour_reservation):
        self._hour_reservation = hour_reservation

