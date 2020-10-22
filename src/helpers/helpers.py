from classes.truck import Truck
from classes.package_table import Package_Table
from classes.graph import Graph
import re

# Time/Space Complexity: O(n)
def generate_truck(truck_number: int, package_table: Package_Table, truck: Truck = None) -> Truck:
    """
    Manually load ALL the trucks!
    """
    if truck == None:
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

# Time/Space Complexity: O(1)
def clean_address(input: str) -> str:
    clean_string = input.replace('North', 'N').replace('South', 'S').replace('East', 'E').replace('West', 'W').replace('\n', '').strip()
    return re.sub(r'\([^()]*\)', '', clean_string)

def incorrect_format() -> None:
    print("Incorrect format. Goodbye.")
    exit()

"""
THE GREEDY ALGORITHM
Time Complexity: O(n^2)
Space Complexity: O(n)
"""
def greedy_delivery(truck: Truck, address_graph: Graph) -> None:
    while truck.total_packages() != 0:
        packages = truck.current_packages()
        smallest_dist = 9999.0
        shortest_package = None
        for pack in packages:
            dist = float(address_graph.get_address_distance(pack.address, truck.current_location))
            if dist < smallest_dist:
                smallest_dist = dist
                shortest_package = pack
        truck.deliver_package(smallest_dist, shortest_package)
    truck.go_home(float(address_graph.get_address_distance("HUB", truck.current_location)))
