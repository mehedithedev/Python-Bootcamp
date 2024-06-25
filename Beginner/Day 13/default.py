def get_todos(filepath = "todos.txt"):

    """ Read a text file and return the list of
     to-do items.
    """

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
# print(help(get_todos())) we can use this to show the reader what does it mean as this
def write_todos(todos_arg, filepath = "todos.txt"): ## args should be forward
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

text = """

priciples of productivity:
Managing your inflow.
Systemizing everything that repeats. 
Above is a multiline string which can show the line break in output

"""
print(text)

while True:
    user_action = input("Choose between add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)


        except ValueError:
            print("Your command is not valid. ")
            continue
    elif user_action.startswith('complete'):
        try:

            number = int(user_action[9:])
            todos = get_todos()

            index = number - 1

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos( todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print("This item doesn't exist! ")
        except ValueError:
            print("Enter the index of todo you want to delete in numbers ")

    elif user_action.startswith("exit"):
        exit("Exiting the program")

    else:
        print("Command is not valid")

