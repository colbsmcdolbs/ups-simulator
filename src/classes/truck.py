"""
Truck class that will represent the driver's of the packages.
"""
from classes.package import Package

class Truck:

    def __init__(self):
        self.package_limit = 16
        self.total_miles = 0
        self.packages = set()
        self.speed = 18

    def add_package(self, package: Package) -> None:
        self.packages.add(package)

    def get_total_packages(self) -> int:
        return len(self.packages)
