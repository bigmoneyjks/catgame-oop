# Our cat entity
class cat:
    # The constructor creates a cat for us in the code
    # To create a cat, we need a given_name and a given_colour
    def __init__(self, given_name, given_colour):     # __init__ stands for initialise
        self.name = given_name     # self is the current cat we are creating
        self.colour = given_colour


# An instance of cat
# An instance is a specific occurance of a class
mimi = cat("Mimi", "Brown")

