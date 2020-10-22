"""
Package class that will be the model for the data within the CSV file.
"""
from enum import Enum
from datetime import datetime

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
        self.in_transit_time: datetime = None
        self.delivery_time: datetime = None

    def deliver_package(self, time: datetime) -> None:
        self.delivery_status = Delivery_Status.DELIVERED.value
        self.delivery_time = time
    
    def load_package(self, time: datetime) -> None:
        self.delivery_status = Delivery_Status.IN_TRANSIT.value
        self.in_transit_time = time

    def get_status_at_time(self, hour: int, minute: int) -> str:
        time = datetime(2020, 10, 19, hour, minute)
        if self.in_transit_time > time:
            return Delivery_Status.HUB.value
        elif self.delivery_time <= time:
            return Delivery_Status.DELIVERED.value
        else:
            return Delivery_Status.IN_TRANSIT.value

    def print_package_status(self, hour: int, minute: int):
        status = self.get_status_at_time(hour, minute)
        print(f"Package {self.id}, {status}")

    def to_string(self) -> str:
        return f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.mass}, {self.special_notes}"


class Delivery_Status(Enum):
    HUB = "HUB"
    IN_TRANSIT = "IN TRANSIT"
    DELIVERED = "DELIVERED"
