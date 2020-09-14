"""
Package class that will be the model for the data within the CSV file.
"""

class Package:

    def __init__(self, id, address, city, state, zip, deadline, mass, special_notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.special_notes = special_notes

    def to_string(self):
        return f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.mass}, {self.special_notes}"
