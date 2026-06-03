class Car():
    def start(self):
        return "I start all cars"
    
class BMW(Car):
    def start(self):
        return "I start all BMW cars"

class X6(BMW):
    def start(self):
        return "I start the BMW X6 model"

car = X6()
print(car.start()) 

# output "I start the BMW X6 model"