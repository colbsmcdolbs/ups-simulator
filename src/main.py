"""
Colby Allen, Student ID: 001355973
The main driver for this program where all of the magic will happen.
Fancy schmancy stuff will be abstracted out into separate classes and util files.
"""

from classes.package import package as Package
from classes.package_table import package_table
import csv
from pathlib import Path

# Globals
package_table = package_table()
file_path = Path(__file__).parent.absolute()

print("Starting run...\n")

# Populate all of the packages from csv file into the hashtable
# This block of code runs at O(n), where n is the number of packages in
# the .csv file. The putting of the packages into the hashmap is O(1)
with open(f"{str(file_path)}/assets/package.csv") as package_file:
    reader = csv.reader(package_file, delimiter=',')
    for row in reader:
        package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7] or "")
        package_table.put(package)

# Generate Mapping for Distances
# This block of code runs at O(n^2) as it has to go through each row of the 
# .csv distance file and then again through the list of different addresses
with open(f"{str(file_path)}/assets/distance.csv") as csvDataFile:
    # csvDistance = csv.reader(csvDataFile)
    distances = [row for row in csv.reader(csvDataFile)]

print("End of Run.")