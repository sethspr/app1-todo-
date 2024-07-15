def todo_app():
    user_prompt = "Type 'add', 'show', 'edit', 'complete', or 'exit': "

    while True:
        user_action = input(user_prompt)
        user_action = user_action.strip()

        match user_action:
            case 'add':
                todo = input("Enter a to-do task: ") + "\n"

                file = open('todos.txt', 'r') # (second argument 'w' for write, 'r' read)
                todo_list = file.readlines()
                file.close()

                todo_list.append(todo.title())

                file = open('todos.txt', 'w')
                file.writelines(todo_list)
                file.close()
            #  Bitwise 'OR' operator
            case 'show':
                file = open('todos.txt', 'r')
                todo_list = file.readlines()
                for index, item in enumerate(todo_list):
                    index = index + 1
                    row = f"{index}-{item}"
                    print(row)
            case 'edit':
                task_number = int(input("Enter the number associated with your to-do task: "))
                task_number = task_number - 1
                new_task = input("Edit your to-do task: ")
                todo_list[task_number] = new_task.title()
            case 'complete':
                task_number = int(input("Enter the number associated with your completed task: "))
                todo_list.pop(task_number - 1)
            case 'exit':
                break
            #  common variable '_' for error handling - defined on the fly
            case _:
                print("Please type a valid command.")

    print("Goodbye!")
    return todo_list

if __name__ == "__main__":
    todo_app()
