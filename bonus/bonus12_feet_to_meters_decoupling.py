# functions with decoupling
from bonus.bonus12_functions import parse, convert

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")

if result < 1:
    print("Child is too short to ride the attraction")
else:
    print("Child can ride the attraction!")

