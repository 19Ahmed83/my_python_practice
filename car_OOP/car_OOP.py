class Car():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car_1 = Car("Toyota", "red")
car_2 = Car("BMW", "black")

print("Car_1 Brand: ", car_1.brand)
print("Car_1 Color: ", car_1.color)

print("Car_2 Brand: ", car_2.brand)
print("Car_2 Color: ", car_2.color)