# Version 5
greetings = ["Hi", "Hello", "Hey", "Greetings", "Salutations"]

for _ in range(3):
    name = input("Enter your name: ")
    greeting = greetings[_ % len(greetings)]
    
    if len(name) > 5:
        print(f"{greeting}, {name}! You have a long name!")
    else:
        print(f"{greeting}, {name}!")
