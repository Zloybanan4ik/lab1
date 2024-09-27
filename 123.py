# Version 7
import random
from datetime import datetime

greetings = ["Hi", "Hello", "Hey", "Greetings", "Salutations"]

def get_time_based_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

for _ in range(3):
    name = input("Enter your name: ")
    random_greeting = random.choice(greetings)
    time_based_greeting = get_time_based_greeting()
    
    if len(name) > 5:
        print(f"{time_based_greeting}, {name}! {random_greeting}! You have a long name!")
    else:
        print(f"{time_based_greeting}, {name}! {random_greeting}!")
