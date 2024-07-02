user_prompt = "Type 'add', 'show', or 'exit': "

todo_list = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todo_list.append(todo.title())
        #  Bitwise 'OR' operator
        case 'show' | 'display':
            for item in todo_list:
                print(item)
        case 'exit':
            break
        #  common variable '_' for error handling - defined on the fly
        case _:
            print("Please type a valid command.")

print("Goodbye!")
