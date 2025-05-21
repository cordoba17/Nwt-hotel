from domain.Service import Service

class ServiceRepository:
    def __init__(self, db):
        self.db = db

    def add(self, service: Service):
        query = """
            INSERT INTO services (service_id, name, description, price)
            VALUES (%s, %s, %s, %s)
        """
        params = (service.service_id, service.name, service.description, service.price)
        self.db.execute_query(query, params)

    def get_all(self):
        query = "SELECT service_id, name, description, price FROM services"
        results = self.db.fetch_all(query)
        return [
            Service(
                row['service_id'],
                row['name'],
                row['description'],
                row['price']
            ) for row in results
        ]

    def get_by_id(self, service_id):
        query = "SELECT service_id, name, description, price FROM services WHERE service_id = %s"
        result = self.db.fetch_one(query, (service_id,))
        if result:
            return Service(
                result['service_id'],
                result['name'],
                result['description'],
                result['price']
            )
        return None

    def delete(self, service_id):
        query = "DELETE FROM services WHERE service_id = %s"
        self.db.execute_query(query, (service_id,))
