# make a journal script
date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
journal_entry = input("Let your thoughts flow:\n")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(f"Mood Rating our of 10: {mood + 2 * "\n"}")
    file.write(f"Thought's of the day: {journal_entry}")