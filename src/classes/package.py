"""
Package class that will be the model for the data within the CSV file.
"""
from enum import Enum

class Package:

    def __init__(self, id, address, city, state, zip, deadline, mass, special_notes):
        self.id: int = id
        self.address: str = address
        self.city: str = city
        self.state: str = state
        self.zip: str = zip
        self.deadline: str = deadline
        self.mass: str = mass
        self.special_notes: str = special_notes
        self.delivery_status: Delivery_Status = Delivery_Status.HUB.value
        self.delivery_time = None

    def deliver_package(self, time) -> None:
        self.delivery_status = Delivery_Status.DELIVERED.value
        self.delivery_time = time
    
    def load_package(self) -> None:
        self.delivery_status = Delivery_Status.IN_TRANSIT.value

    def to_string(self) -> str:
        return f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.mass}, {self.special_notes}"


class Delivery_Status(Enum):
    HUB = "HUB"
    IN_TRANSIT = "IN TRANSIT"
    DELIVERED = "DELIVERED"
