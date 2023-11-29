import random

class Customer:
    def __init__(self, name, contact_number):
        self.name = name
        self.contact_number = contact_number
        self.dogs = []
        self.employee_assigned = None
        self.session_duration = None  
        self.pickup_time = None
        self.payment_amount = None

    def assign_employee(self, employees):
        # Randomly assign an employee to the customer
        self.employee_assigned = random.choice(employees)


    def add_dog(self,dog):
        self.dogs.append(dog)

     # Add a method for setting the pickup time
    def set_pickup_time(self, pickup_time):
        self.pickup_time = pickup_time

    def calculate_payment_amount(self):
        if self.session_duration == 4:
            self.payment_amount = 50 # Adjust the payment amount as needed
        elif self.session_duration == 6:
            self.payment_amount = 70  # Adjust the payment amount as needed
        elif self.session_duration == 8:
            self.payment_amount = 90  
        else:
            self.payment_amount = None  # Handle unknown session durations

    def display_payment_information(self):
        print(f"Payment Amount: ${self.payment_amount}")