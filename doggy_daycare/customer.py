class Customer:
    def __init__(self, name, contact_number):
        self.name = name
        self.contact_number = contact_number
        self.dogs = []
    def add_dog(self,dog):
        self.dogs.append(dog)