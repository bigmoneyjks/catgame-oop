class Cat:
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
        print(f"{self.name} curls dumbells whilst reading a big book...")
        self.intelligence += 3
        self.energy -= 5
        self.weight += 0.1
    
    def eat(self):
        print(f"{self.name} eats a delicious 3 course meal...")
        self.weight += 0.2
        self.energy += 5

    def play(self):
        print(f"You throw a ball to {self.name} and they play with it...")
        self.weight -= 0.1
        self.energy -= 2
    
    def grow(self):
        self.age += 0.25