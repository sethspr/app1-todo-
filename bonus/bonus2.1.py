# While loop to enter password until correct.

password = input("Enter password: ")

while password != "pass123":
    print("Incorrect password, please try again...")
    password = input("Enter password: ")

print("Password confirmed!")
