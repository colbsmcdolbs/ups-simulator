"""

"""
import Package

class PackageHashTable:
    
    # Constructor

    def __init__(self):
        self.hashTable = []
        self.__table_size = 40
        self.__prime = 13
    

    # Methods

    def put(self, package):
        i = 0
        while True:
            index = self.__double_hash(package.id, i)
            if not self.hashTable[index]:
                self.hashTable[index] = package
                break
            i = i + 1

    def get(self, packageId):
        return ""

    def remove(self, package):
        return ""

    def __double_hash(self, packageId, i):
        """Calculates the double hash of the packageId by combining the first and second hash functions

        Time Complexity
        ---------------
        O(1) - The hash functions that are called below are all O(1), so it remains constant

        """
        return (self.__hash1(packageId) + i * self.__hash2(packageId)) % self.__table_size

    def __hash1(self, packageId):
        """Calculates the first hash of the packageId

        Time Complexity
        ---------------
        O(1) - The operations in this function are only a single time per call

        """
        return packageId % self.__table_size

    def __hash2(self, packageId):
        """Calculates the second hash of the packageId

        Time Complexity
        ---------------
        O(1) - The operations in this function are only a single time per call

        """
        return (self.__prime - (packageId % self.__prime))
