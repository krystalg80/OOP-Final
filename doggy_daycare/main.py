
from customer import Customer
from welcome import Welcome


name = input("Enter your name: ")
phone_number = input("Enter your phone number: ")


customer = Customer(name, phone_number)

print(f"Customer Name: {customer.name}")
print(f"Phone Number: {customer.contact_number}")

welcoming = Welcome()
finished_welcoming = welcoming.welcome_customer(customer)
print(finished_welcoming)