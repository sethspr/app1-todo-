add_members= input("Add a new member: ")

file = open("6.5_members.txt", "r")
existing_members = file.readlines()
file.close()

existing_members.append(add_members + "\n")

file = open("6.5_members.txt", "w")
file.writelines(existing_members)
file.close()


