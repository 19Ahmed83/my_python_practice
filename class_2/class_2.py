class Vehicle:
    def move(self) -> str:
        return "Vehicle is moving"
    
class Bike(Vehicle):
    def move(self) -> str:
        return "Bike is riding"


v = Vehicle()
b = Bike()

print(v.move())
print(b.move())

