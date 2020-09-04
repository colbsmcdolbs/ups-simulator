"""
Package class that will be the model for the data within the CSV file.
"""

class Package:

    def __init__(self, id, address, city, zip, deadline, mass, specialNotes):
        self.id = id
        self.address = address
        self.city = city
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.specialNotes = specialNotes
