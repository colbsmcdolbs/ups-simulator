from classes.truck import Truck
from classes.package_table import Package_Table

def generate_truck(truck_number: int, package_table: Package_Table) -> Truck:
    """
    Manually load ALL the trucks!
    """
    truck = Truck()
    if truck_number == 1:
        truck.add_package(package_table.get(13))
        truck.add_package(package_table.get(14))
        truck.add_package(package_table.get(15))
        truck.add_package(package_table.get(16))
        truck.add_package(package_table.get(19))
        truck.add_package(package_table.get(20))
        truck.add_package(package_table.get(1))
        truck.add_package(package_table.get(34))
        truck.add_package(package_table.get(21))
        truck.add_package(package_table.get(7))
        truck.add_package(package_table.get(29))
        truck.add_package(package_table.get(37))
        truck.add_package(package_table.get(30))
        truck.add_package(package_table.get(39))
        truck.add_package(package_table.get(27))
        truck.add_package(package_table.get(35))
    elif truck_number == 2:
        truck.add_package(package_table.get(25))
        truck.add_package(package_table.get(18))
        truck.add_package(package_table.get(36))
        truck.add_package(package_table.get(26))
        truck.add_package(package_table.get(6))
        truck.add_package(package_table.get(22))
        truck.add_package(package_table.get(24))
        truck.add_package(package_table.get(28))
        truck.add_package(package_table.get(4))
        truck.add_package(package_table.get(40))
        truck.add_package(package_table.get(31))
        truck.add_package(package_table.get(32))
        truck.add_package(package_table.get(17))
        truck.add_package(package_table.get(12))
        truck.add_package(package_table.get(23))
        truck.add_package(package_table.get(11))
    elif truck_number == 3:
        truck.add_package(package_table.get(2))
        truck.add_package(package_table.get(33))
        truck.add_package(package_table.get(10))
        truck.add_package(package_table.get(5))
        truck.add_package(package_table.get(38))
        truck.add_package(package_table.get(8))
        truck.add_package(package_table.get(9))
        truck.add_package(package_table.get(3))

    return truck

def clean_address(input: str) -> str:
    return input.replace('North', 'N').replace('South', 'S').replace('East', 'E').replace('West', 'W').replace('\n', '')
