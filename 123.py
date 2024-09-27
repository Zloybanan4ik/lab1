# Version 6
import random

greetings = ["Hi", "Hello", "Hey", "Greetings", "Salutations"]

for _ in range(3):
    name = input("Enter your name: ")
    greeting = random.choice(greetings)
    
    if len(name) > 5:
        print(f"{greeting}, {name}! You have a long name!")
    else:
        print(f"{greeting}, {name}!")
