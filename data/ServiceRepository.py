# data/ServiceRepository.py

from domain.Service import Service

class ServiceRepository:
    def __init__(self):
        self.services = []

    def add_service(self, service: Service):
        self.services.append(service)

    def get_all_services(self):
        return self.services
