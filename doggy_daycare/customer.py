import random

class Customer:
    def __init__(self, name, contact_number):
        self.name = name
        self.contact_number = contact_number
        self.dogs = []
        self.employee_assigned = None

    def assign_employee(self, employees):
        # Randomly assign an employee to the customer
        self.employee_assigned = random.choice(employees)


    def add_dog(self,dog):
        self.dogs.append(dog)