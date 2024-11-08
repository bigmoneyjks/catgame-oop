from cat import *

name = input("What would you like your cat to be called? - ")
colour = input("What is your desired colour for your cat? - ")

cat = Cat(name, colour)

while True:
    opt = input(f"What would you like to do? 1.Feed Cat 2.Train Cat 3.Play with cat 4.Show {cat.name}'s stats - ")
    if opt == "1" and cat.energy <= 45:
        cat.eat()
    elif opt == "2" and cat.energy >= 5:
        cat.train()
    elif opt == "3" and cat.energy >= 2:
        cat.play()
    elif opt == "4":
        print(f"{cat.name}'s age is {cat.age}")
        print(f"{cat.name}'s weight is {cat.weight}kg")
        print(f"{cat.name}'s intelligence is {cat.intelligence} IQ")
        print(f"{cat.name}'s energy is {cat.energy}")
    cat.grow()
    if cat.weight <= 2:
        print(f"{cat.name} has died from being malnourished :(") 
        break
    elif cat.weight >= 7:
        print(f"{cat.name} has died from being too fat :(")
        break
    elif cat.age == 15:
        print(f"{cat.name} has died from old age :(")
        break
    
