"""
PackageHashTable that will hold all of the packages for the day
"""

from classes.Package import Package as pack

class PackageHashTable:
    
    # Constructor

    def __init__(self):
        self.hashTable = list(range(40))
        self.__table_size = 40
        self.__prime = 13
    

    # Methods

    def put(self, package: pack):
        i = 0
        print(package.id)
        notFound = True
        while notFound:
            index = self.__double_hash(package.id, i)
            if not self.hashTable[index]:
                self.hashTable[index] = package
                notFound = False
            i = i + 1

    def get(self, packageId):
        i = 0
        while True:
            index = self.__double_hash(packageId, i)
            package = self.hashTable[index]
            if not package: # If nothing found, return null
                return None
            elif packageId == package.id: # Package Found
                return package
            elif packageId != package.id: # Case of collisions
                i = i + 1

    def remove(self, package: pack):
        return ""

    def __double_hash(self, packageId: int, i: int):
        """Calculates the double hash of the packageId by combining the first and second hash functions

        Time Complexity
        ---------------
        O(1) - The hash functions that are called below are all O(1), so it remains constant

        """
        return (self.__hash1(packageId) + (i * self.__hash2(packageId))) % self.__table_size

    def __hash1(self, packageId):
        """Calculates the first hash of the packageId

        Time Complexity
        ---------------
        O(1) - The operations in this function are only a single time per call

        """
        return (int(packageId) % self.__table_size)

    def __hash2(self, packageId):
        """Calculates the second hash of the packageId

        Time Complexity
        ---------------
        O(1) - The operations in this function are only a single time per call

        """
        return (self.__prime - (int(packageId) % self.__prime))
