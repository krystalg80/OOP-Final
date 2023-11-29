
from customer import Customer
from welcome import Welcome
from dog import Dog
from employee import Employee

employees = [
    Employee("Chloe", "123-456-789"),
    Employee("Matt", "345-567-890"),
    Employee("Jessica", "102-345-678")
]

name = input("Enter your name: ")
phone_number = input("Enter your phone number: ")


customer = Customer(name, phone_number)
customer.assign_employee(employees)

dog_name = input("Enter your dog's name: ")
dog_breed = input("Enter your dog's breed: ")
dog_size = input("Enter your dog's size: Small, Medium, or Large: ")
dog_age = input("Enter your dog's age: ")

dog = Dog(dog_name, dog_breed, dog_size, dog_age)

customer.add_dog(dog)

# Allow the customer to choose the session duration
session_duration = int(input("Choose the session duration (4, 6, or 8 hours): "))
customer.session_duration = session_duration

# Allow the customer to choose the pickup time
pickup_time = input("Choose the pickup time (e.g., 2:00 PM): ")
customer.set_pickup_time(pickup_time)

# Calculate the payment amount based on the chosen duration
customer.calculate_payment_amount()

# Display payment information
customer.display_payment_information()


print(f"\nCustomer Information:")
print(f"Name: {customer.name}")
print(f"Phone Number: {customer.contact_number}")

print(f"\nAssigned Employee Information:")
print(f"Name: {customer.employee_assigned.name}")

for employee in employees:
    print(f"\nEmployee Information for {employee.name}:")
    print(f"Phone Number: {employee.phone_number}")

print(f"\nDog Information:")
print(f"Name: {dog.name}")
print(f"Breed: {dog.breed}")
print(f"Size: {dog.size}")
print(f"Age: {dog.age}")

welcoming = Welcome()
finished_welcoming = welcoming.welcome_customer(customer)
