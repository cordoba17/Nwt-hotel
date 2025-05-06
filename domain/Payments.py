from domain.User import User

class Payments(User)

    def __init__(self, id, name, last_name, email, password , status,id_payments)
        super().__init__(id,name, last_name, email, password, status)
        self._id_payments = id_payments

    @property
    def id_payments(self):
        return self._id_payments
    @id_payments.setter
    def id_payments(self, id_payments):
        self._id_payments=id_payments

