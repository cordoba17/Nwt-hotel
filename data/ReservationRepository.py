from domain.Reservation import Reservation

class ReservaRepository:
    def __init__(self):
        self.reservations = [] #guarda las reservas que se vayan creando

    def createReservaRepository(self, reservation: Reservation):
        self.reservations.append(reservation)
        self.print_all_reservations() #metodo para imprimir todos los datos almacenados

    def print_all_reservations(self): #recorre las listas de reservas , imprime sus datos
        for e in self.reservations:
            print("id:", e.id)
            print("name:", e.name, e.last_name)
            print("email:", e.email)
            print("password:", e.password)
            print("status:", e.status)
            print("id_reservation:", e.id_reservation)
            print("date_reservation:", e.date_reservation)
            print("hour_reservation:", e.hour_reservation)