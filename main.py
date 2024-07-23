def todo_app():

    while True:
        # get user input and strip space characters from input
        user_action = input("Type 'add', 'show', 'edit', 'complete', or 'exit': ")
        user_action = user_action.strip()

        if 'add' in user_action:
            # use list slicing - this will give us the part after 'add ', l
            todo = user_action[4:]

            # context-manager with - as
            with open('todos.txt', 'r') as file: # (second argument 'w' for write, 'r' read)
                todo_list = file.readlines()

            todo_list.append(todo.title())

            with open('todos.txt', 'w') as file:
                file.writelines(todo_list)

        elif 'show' in user_action:
            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

            # new_todos = [item.strip('\n') for item in todo_list]

            for index, item in enumerate(todo_list):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        elif 'edit' in user_action:
            task_number = int(input("Enter the number associated with your to-do task: "))
            # task_number = int(user_action[5:])
            task_number = task_number - 1

            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

            new_task = input("Edit your to-do task: ")
            todo_list[task_number] = new_task.title() + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todo_list)

        elif 'complete' in user_action:
            # task_number = int(input("Enter the number associated with your completed task: "))
            task_number = int(user_action[9:])


            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()
            index = task_number - 1
            todo_to_remove = todo_list[index].strip('\n')
            todo_list.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todo_list)

            message = f"Todo '{todo_to_remove}' was completed and removed from the list"
            print(message)

        elif 'exit' in user_action:
            break
        #  common variable '_' for error handling - defined on the fly
        else:
            print("Please type a valid command.")

    print("Goodbye!")
    return todo_list

if __name__ == "__main__":
    todo_app()
