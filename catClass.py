# Creating a class
class Cat(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

        
# Creating an instance of cat class
fluff = Cat("Fluff", 4.5)

# Printing an anttribute of fluff
print(fluff.weight)

# Changing the weight of fluff
fluff.weight = 5
print(fluff.weight)

