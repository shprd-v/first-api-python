import random

names = ["James", "Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "Logan", "Isabella"]
ages = [10, 20, 15, 16, 83, 53, 21, 34, 51, 98]

class Person:
    def __init__(self):
        self.name = random.choice(names)
        self.age = random.choice(ages)

for i in range(5):
    p = Person()
    print(p.name, p.age)