def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:  # (second argument 'w' for write, 'r' read)
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todo_parameter, filepath="todos.txt"):
    """ Write a to-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_parameter)
    # no return, we want the None value. This is just a procedure