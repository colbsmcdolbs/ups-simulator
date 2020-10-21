"""
Truck class that will represent the driver's of the packages.
"""
from classes.package import Package, Delivery_Status
from datetime import time, datetime, timedelta

class Truck:

    def __init__(self):
        self.package_limit = 16
        self.total_miles = 0
        self.priority = set()
        self.packages = set()
        self.speed = 18
        self.time = datetime(2020, 10, 19, 8, 0, 0)
        self.current_location = "HUB"

    def deliver_package(self, distance: float, location: str) -> None:
        self.set_location(location)
        self.add_time(distance)
        self.set_location(location)

    def add_time(self, distance: float) -> None:
        self.time = self.time + timedelta(hours=(distance/self.speed))

    def set_location(self, new_location: str) -> None:
        self.current_location = new_location

    def add_package(self, package: Package) -> None:
        package.delivery_status = Delivery_Status.IN_TRANSIT.value
        self.packages.add(package) if package.deadline == "EOD" else self.priority.add(package)

    def get_total_packages(self) -> int:
        return len(self.packages) + len(self.priority)
