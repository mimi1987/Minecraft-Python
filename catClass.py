# Creating a class
class Cat(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self, food):
        self.weight = self.weight + 0.05
        print(self.name + " is eating " + food)

    def eatAndSleep(self, food):
        self.eat(food)
        print(self.name + " is sleeping...")

        
# Creating an instance of cat class
fluff = Cat("Fluff", 4.5)

# Printing an anttribute of fluff
print(fluff.weight)

# Changing the weight of fluff
fluff.weight = 5
print(fluff.weight)

# Fluff is eating
fluff.eat("tuna")

# Fluff eats again and sleeps after it
fluff.eatAndSleep("tuna")

# Print the updated weight attribute
print(fluff.weight)

