from classes.truck import Truck
from classes.package_table import Package_Table

def generate_truck(truck_number: int, package_table: Package_Table) -> Truck:
    truck = Truck()
    
    if truck_number is 1:
        truck.add_package(package_table.get(13))
        truck.add_package(package_table.get(14))
        truck.add_package(package_table.get(15))
        truck.add_package(package_table.get(16))
        truck.add_package(package_table.get(19))
        truck.add_package(package_table.get(20))
        truck.add_package(package_table.get(1))
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
    elif truck_number is 2:
        truck.add_package(package_table.get(3))
        truck.add_package(package_table.get(18))
        truck.add_package(package_table.get(36))
        truck.add_package(package_table.get(38))
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
        truck.add_package(package_table.get())
    elif truck_number is 3:
        truck.add_package(package_table.get(6))
        truck.add_package(package_table.get(25))
        truck.add_package(package_table.get(28))
        truck.add_package(package_table.get(32))
        truck.add_package(package_table.get(9))
        truck.add_package(package_table.get())

    return truck