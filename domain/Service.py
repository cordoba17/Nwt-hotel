# domain/Service.py

class Service:
    def __init__(self, service_id, name, description, price):
        self.service_id = service_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price}): {self.description}"
