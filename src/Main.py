"""
Colby Allen, Student ID: 001355973
The main driver for this program where all of the magic will happen.
Fancy schmancy stuff will be abstracted out into separate classes and util files.
"""

from Classes.Package import Package
from Classes.PackageHashTable import PackageHashTable
import csv

# Globals
package_table = PackageHashTable()
package_csv_path = "./src/Assets/package.csv"
distance_csv_path = "./src/Assets/distance.csv"

# Populate all of the packages from csv file into the hashtable
# This block of code runs at O(n), where n is the number of packages in
# the .csv file. The putting of the packages into the hashmap is O(1)
with open(package_csv_path) as package_file:
    reader = csv.reader(package_file, delimiter=',')
    for row in reader:
        package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7] or "")
        package_table.put(package)

# Generate Mapping for Distances
# This block of code runs at O(n^2) as it has to go through each row of the 
# .csv distance file and then again through the list of different addresses
with open(distance_csv_path) as csvDataFile:
    # csvDistance = csv.reader(csvDataFile)
    distances = [row for row in csv.reader(csvDataFile)]
