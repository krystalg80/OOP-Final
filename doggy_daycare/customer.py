import random

class Customer:
    def __init__(self, name, contact_number):
        self.name = name
        self.contact_number = contact_number
        self.dogs = []
        self.employee_assigned = None
        self.session_duration = None  
        self.pickup_time = None

    def assign_employee(self, employees):
        # Randomly assign an employee to the customer
        self.employee_assigned = random.choice(employees)


    def add_dog(self,dog):
        self.dogs.append(dog)
    
     # Add a method for setting the pickup time
    def set_pickup_time(self, pickup_time):
        self.pickup_time = pickup_time