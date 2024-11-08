# Our cat entity
class cat:
    # The constructor creates a cat for us in the code
    # To create a cat, we need a given_name and a given_colour
    def __init__(self, given_name, given_colour):     # __init__ stands for initialise
        self.name = given_name     # self is the current cat we are creating
        self.colour = given_colour
        self.age = 1
        self.energy = 50
        self.intelligence = 5
        self.weight = 5
    
    def train(self):
        print(f"{self.name} is training..")
        self.intelligence += 1
        self.energy -= 5
    
    def eat(self):
        print(f"{self.name} eats a nice meal..")
        self.weight += 0.2
        self.energy += 5



# An instance of cat
# An instance is a specific occurance of a class
mimi = cat("Mimi", "Brown")
astha = cat("Astha", "Black")
astha.eat()
# mimi.train()
print(mimi.energy)
print(astha.energy)

