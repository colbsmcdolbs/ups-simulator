"""
Table that will hold all of the packages for the day
"""

from classes.package import Package

class Package_Table:

    def __init__(self):
        self.__table_size = 40
        self.__prime = 13
        self.hashTable = [None] * self.__table_size

    # Time Complexity: O(1), Space Complexity: O(1)
    def put(self, package: Package) -> None:
        i = 0
        found = False
        while not found:
            index = self.__double_hash(package.id, i)
            if self.hashTable[index] is None:
                self.hashTable[index] = package
                found = True
            else:
                i = i + 1

    # Time Complexity: O(1), Space Complexity: O(1)
    def get(self, packageId: int) -> Package:
        i = 0
        while True:
            index = self.__double_hash(packageId, i)
            package = self.hashTable[index]
            if not package: # If nothing found, return null
                return None
            elif packageId == int(package.id): # Package Found
                return package
            elif packageId != package.id: # Case of collisions
                i = i + 1

    # Time Complexity: O(1), Space Complexity: O(1)
    def __double_hash(self, packageId: int, i: int):\
        return (self.__hash1(packageId) + (i * self.__hash2(packageId))) % self.__table_size

    # Time Complexity: O(1), Space Complexity: O(1)
    def __hash1(self, packageId: int) -> int:
        return (int(packageId) % self.__table_size)

    # Time Complexity: O(1), Space Complexity: O(1)
    def __hash2(self, packageId: int) -> int:\
        return (self.__prime - (int(packageId) % self.__prime))

    # Time/Space Complexity: O(n)
    def print_packages(self) -> None:
        index = 1
        for pack in self.hashTable:
            print(f"{index} : {pack}")
            index = index + 1
        print(f"Total Packages: {len(self.hashTable)}")
