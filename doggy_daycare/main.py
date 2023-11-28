
from customer import Customer
from welcome import Welcome
from dog import Dog

name = input("Enter your name: ")
phone_number = input("Enter your phone number: ")


customer = Customer(name, phone_number)

dog_name = input("Enter your dog's name: ")
dog_breed = input("Enter your dog's breed: ")
dog_age = input("Enter your dog's age: ")

dog = Dog(dog_name, dog_breed, dog_age)

customer.add_dog(dog)

print(f"\nCustomer Information:")
print(f"Name: {customer.name}")
print(f"Phone Number: {customer.contact_number}")

print(f"\nDog Information:")
print(f"Name: {dog.name}")
print(f"Breed: {dog.breed}")
print(f"Age: {dog.age}")

welcoming = Welcome()
finished_welcoming = welcoming.welcome_customer(customer)
print(finished_welcoming)