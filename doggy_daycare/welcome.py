from customer import Customer

class Welcome:
    def __init__(self):
        self.welcome_message = "Welcome to Krystal's Doggy DayCare!"

    def welcome_customer(self, customer):
        print(f"{self.welcome_message}, {customer.name}! We are happy to invite you and your dogs!")

    def __str__(self):
        return f"{self.welcome_message}"
    
