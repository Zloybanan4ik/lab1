# Version 4
greetings = ["Hi", "Hello", "Hey", "Greetings", "Salutations"]

for _ in range(3):
    name = input("Enter your name: ")
    greeting = greetings[_ % len(greetings)]
    print(f"{greeting}, {name}!")
