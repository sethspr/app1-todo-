user_prompt = "Type 'add', 'show', 'edit' or 'exit': "

todo_list = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a to-do task: ")
            todo_list.append(todo.title())
        #  Bitwise 'OR' operator
        case 'show' | 'display':
            for item in todo_list:
                print(item)
        case 'edit':
            task_number = int(input("Enter the number associated with your to-do task: "))
            task_number = task_number - 1
            new_task = input("Edit your to-do task: ")
            todo_list[task_number] = new_task.title()
        case 'exit':
            break
        #  common variable '_' for error handling - defined on the fly
        case _:
            print("Please type a valid command.")

print("Goodbye!")
