"""
Package class that will be the model for the data within the CSV file.
"""
from enum import Enum

class Package:

    def __init__(self, id, address, city, state, zip, deadline, mass, special_notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.special_notes = special_notes
        self.delivery_status = Delivery_Status.HUB.value
        self.delivery_time = None

    def deliver_package(self, time: str) -> None:
        self.delivery_status = Delivery_Status.DELIVERED.value
        self.delivery_time = time

    def to_string(self) -> str:
        return f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.mass}, {self.special_notes}"


class Delivery_Status(Enum):
    HUB = "HUB"
    IN_TRANSIT = "IN TRANSIT"
    DELIVERED = "DELIVERED"
