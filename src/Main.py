"""
The main driver for this program where all of the magic will happen.
Fancy schmancy stuff will be abstracted out into separate classes and util files.
"""

from Classes.Package import Package
from Classes.PackageHashTable import PackageHashTable
import csv

# Globals
package_table = PackageHashTable()
csv_path = "Assets/package.csv"

# Populate all of the packages from csv file into the hashtable
with open(csv_path) as package_file:
    reader = csv.reader(package_file, delimiter=',')
    for row in reader:
        package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7] or "")
        package_table.put(package)
