class Coffee:
    def __init__(self, size, flavor):
        self.size = size
        self.flavor = flavor

    def brew(self):
        return f"Brewing a {self.size} cup with {self.flavor} flavor"

cup_1 = Coffee("large", "mocha")
cup_2 = Coffee("small", "caramel") 

print(cup_1.brew())
print(cup_2.brew())