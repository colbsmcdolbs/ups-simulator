"""
The main driver for this program where all of the magic will happen.
Fancy schmancy stuff will be abstracted out into separate classes and util files.
"""

from classes.Package import Package
from classes.PackageHashTable import PackageHashTable
import csv

# Globals
package_table = PackageHashTable()

# Populate all of the packages from csv file into the hashtable
with open('assets/package.csv') as package_file:
    reader = csv.reader(package_file, delimiter=',')
    for row in reader:
        package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7] or "")
        package_table.put(package)
