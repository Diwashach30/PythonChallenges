##Write a Python program to create a class Laptop with the properties id, name, and ram. Then,
##create three objects of this class and print all their details.

class Laptop:
    def __init__(self, id, name, ram):
        self.id = id
        self.name = name
        self.ram = ram
    
    def _get_details(self):
        return f"ID: {self.id}, Name: {self.name}, RAM: {self.ram}"
    
laptop1 = Laptop(1, "Dell", "8GB")
laptop2 = Laptop(2, "Asus", "16GB")
laptop3 = Laptop(3, "HP", "12GB")

print(laptop1._get_details())
print(laptop2._get_details())
print(laptop3._get_details())

print(laptop1.id, laptop1.name, laptop1.ram)
print(laptop2.id, laptop2.name, laptop2.ram)
print(laptop3.id, laptop3.name, laptop3.ram)