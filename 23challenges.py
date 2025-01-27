##Write a Python program to create a class Vehicle with properties make and model. Then,
##create a derived class Car with an additional property year. Create objects of both classes and
##print all their details.


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_details(self):
        return f"Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def get_details(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

vehicle = Vehicle("Toyota", "Camry")
car = Car("Honda", "Civic", 2022)

print(vehicle.get_details())
print(car.get_details())