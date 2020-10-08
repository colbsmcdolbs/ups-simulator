"""
Truck class that will represent the driver's of the packages.
"""
from classes.package import package

class truck:

    def __init__(self):
        self.package_limit = 16
        self.total_miles = 0
        self.packages = set()

    def add_package(self, package: package):
        self.packages.add(package)