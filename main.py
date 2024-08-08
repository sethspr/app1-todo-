import functions
import time


def todo_app():

    now = time.strftime("%b %d, %Y %H:%H:%S")
    print("It is", now)

    while True:
        # get user input and strip space characters from input
        user_action = input("Type 'add', 'show', 'edit', 'complete', or 'exit': ")
        user_action = user_action.strip()

        if user_action.startswith('add'):
            # use list slicing - this will give us the part after 'add ', l
            todo = user_action[4:]

            todo_list = functions.get_todos()

            todo_list.append(todo.title() + "\n")

            functions.write_todos(todo_list)

        elif user_action.startswith('show'):

            todo_list = functions.get_todos()

            # new_todos = [item.strip('\n') for item in todo_list]

            for index, item in enumerate(todo_list):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        elif user_action.startswith('edit'):
            try:
                # task_number = int(input("Enter the number associated with your to-do task: "))
                task_number = int(user_action[5:])
                print(task_number)

                task_number = task_number - 1

                todo_list = functions.get_todos()

                new_task = input("Edit your to-do task: ")
                todo_list[task_number] = new_task.title() + '\n'

                functions.write_todos(todo_list)

            except ValueError:
                print("Your command is not valid.")
                # runs another cycle of the While loop
                continue


        elif user_action.startswith('complete'):
            # task_number = int(input("Enter the number associated with your completed task: "))
            try:
                task_number = int(user_action[9:])


                todo_list = functions.get_todos()
                index = task_number - 1
                todo_to_remove = todo_list[index].strip('\n')
                todo_list.pop(index)

                functions.write_todos(todo_list)

                message = f"Todo '{todo_to_remove}' was completed and removed from the list"
                print(message)
            except IndexError:
                print("No item with that number exists.")
                continue
            except ValueError:
                print("Your command is not valid.")
                continue

        elif user_action.startswith('exit'):
            break
        #  common variable '_' for error handling - defined on the fly
        else:
            print("Please type a valid command.")

    print("Goodbye!")
    return todo_list

if __name__ == "__main__":
    todo_app()
