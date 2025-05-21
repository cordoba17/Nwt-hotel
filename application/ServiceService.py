# services/ServiceService.py
from data.ServiceRepository import ServiceRepository
from domain.Service import Service

class ServiceService:
    def __init__(self, repository: ServiceRepository):
        self.repository = repository

    def create_service(self, service_id, name, description, price):
        service = Service(service_id, name, description, price)
        self.repository.add(service)
        return service

    def list_services(self):
        return self.repository.get_all()

    def find_service(self, service_id):
        return self.repository.get_by_id(service_id)

    def remove_service(self, service_id):
        self.repository.delete(service_id)
