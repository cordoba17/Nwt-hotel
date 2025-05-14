from domain.Service import Service
from data.ServiceRepository import ServiceRepository

class ServiceService:
    def __init__(self, repository: ServiceRepository):
        self.repository = repository

    def crear_servicio(self, service_id, name, description, price):
        nuevo_servicio = Service(service_id, name, description, price)
        self.repository.add_service(nuevo_servicio)

    def listar_servicios(self):
        return self.repository.get_all_services()

    def editar_servicio(self, service_id, name, description, price):
        for servicio in self.repository.services:
            if servicio.service_id == service_id:
                servicio.name = name
                servicio.description = description
                servicio.price = price
                return
        print("Servicio no encontrado.")
