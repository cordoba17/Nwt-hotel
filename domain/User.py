class User:

    def __init__(self, id, name, last_name, email, password, status):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
