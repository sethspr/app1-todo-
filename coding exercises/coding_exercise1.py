import random


lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random_nr = random.randint(lower_bound, upper_bound)

print(random_nr)