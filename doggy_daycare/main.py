
from customer import Customer
from welcome import Welcome
from dog import Dog
from employee import Employee

employees = [Employee("Jessica"), Employee("Matt"), Employee("Chloe")]

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

print(f"\nCustomer Information:")
print(f"Name: {customer.name}")
print(f"Phone Number: {customer.contact_number}")

print(f"\nAssigned Employee Information:")
print(f"Name: {customer.employee_assigned.name}")


print(f"\nDog Information:")
print(f"Name: {dog.name}")
print(f"Breed: {dog.breed}")
print(f"Size: {dog.size}")
print(f"Age: {dog.age}")

welcoming = Welcome()
finished_welcoming = welcoming.welcome_customer(customer)
print(finished_welcoming)