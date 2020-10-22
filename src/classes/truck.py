"""
Truck class that will represent the driver's of the packages.
"""
from classes.package import Package, Delivery_Status
from datetime import time, datetime, timedelta

class Truck:

    def __init__(self, time=datetime(2020, 10, 19, 8, 0)):
        self.total_miles: float = 0.0
        self.priority = set()
        self.packages = set()
        self.speed: int = 18
        self.time = time
        self.current_location: str = "HUB"

    # Time/Space Complexity: O(1)
    def deliver_package(self, distance: float, package: Package) -> None:
        self.time = self.time + timedelta(hours=(distance/self.speed))
        self.current_location = package.address
        self.total_miles = self.total_miles + distance
        package.deliver_package(self.time)
        self.packages.remove(package) if package.deadline == "EOD" else self.priority.remove(package)

    # Time/Space Complexity: O(1)
    def go_home(self, distance: float):
        self.time = self.time + timedelta(hours=(distance/self.speed))
        self.current_location = "HUB"
        self.total_miles = self.total_miles + distance

    # Time/Space Complexity: O(1)
    def add_package(self, package: Package) -> None:
        package.load_package(self.time)
        self.packages.add(package) if package.deadline == "EOD" else self.priority.add(package)

    # Time/Space Complexity: O(1)
    def current_packages(self) -> set():
        return self.priority if len(self.priority) != 0 else self.packages

    # Time/Space Complexity: O(1)
    def total_packages(self) -> int:
        return len(self.packages) + len(self.priority)
