from customer import Customer

class Welcome:
    def __init__(self):
        self.welcome_message = "Welcome to Krystal's Doggy DayCare"

    
    
    def welcome_customer(self, customer):
        print(f"{self.welcome_message}, {customer.name}! We are happy to invite you and your dogs!, Your assigned Trainer of the Day is {customer.employee_assigned.name}")
                
        pickup_time = self.get_pickup_time(customer.session_duration)
        print(f"Today's session will last {customer.session_duration} hours, and you can pick up your dog at {pickup_time}.")
    
    
    
    
    def get_pickup_time(self, session_duration):
    # Calculate pickup time based on the chosen session duration
        pickup_times = {4: "2:00 PM", 6: "4:00 PM", 8: "6:00 PM"}
        return pickup_times.get(session_duration, "Unknown Pickup Time")


    def __str__(self):
        return f"{self.welcome_message}"
    
