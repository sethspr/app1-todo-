def todo_app():

    while True:
        # get user input and strip space characters from input
        user_action = input("Type 'add', 'show', 'edit', 'complete', or 'exit': ")
        user_action = user_action.strip()

        match user_action:
            case 'add':
                todo = input("Enter a to-do task: ") + "\n"

                # context-manager with - as
                with open('todos.txt', 'r') as file: # (second argument 'w' for write, 'r' read)
                    todo_list = file.readlines()

                todo_list.append(todo.title())

                with open('todos.txt', 'w') as file:
                    file.writelines(todo_list)

            case 'show':
                with open('todos.txt', 'r') as file:
                    todo_list = file.readlines()

                # new_todos = [item.strip('\n') for item in todo_list]

                for index, item in enumerate(todo_list):
                    item = item.strip('\n')
                    row = f"{index + 1}-{item}"
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
