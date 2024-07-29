# program to check strength of password
# utilize dictionary for key value pairs per conditionals
while True:
    password = input("Enter new password: ")

    result = {}

    if len(password) >= 8:
        result["Length"] = True
    else:
        result["Length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result["Digit"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result["Upper-Case"] = uppercase

    print(result)

    if all(result.values()):
        print("Strong Password")
    else:
        print("Weak Password")






# my mvp attempt
# while True:
#     password = input("Enter new password: ")
#     if len(password) < 5:
#         print("Weak password entered")
#
#     elif len(password) >= 5 and len(password) <= 10:
#         print("Password is adequate")
#
#     else:
#         print("Password is strong!")