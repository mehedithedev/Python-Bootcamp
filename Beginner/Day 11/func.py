def get_todos():
    with open('list.txt', 'r') as file:
        todos = file.readlines()
    return todos




    # Get user input and strip space chars from it
    userChoice = input("Choose any of this: add, show, edit, complete, exit: \n")


    if userChoice.startswith("add"):
        todo = userChoice[4:]

        todos = get_todos()
        todos.append(todo+'\n')


        writeFile = open("list.txt", "w")

        writeFile.writelines(todos)
        writeFile.close()


        with open('list.txt', 'w') as file:
            file.writelines(todos)

    elif userChoice.startswith("show"):
        updatedTodo = open("list.txt", "r")
        finalTodo = updatedTodo.readlines()
        updatedTodo.close()

        todos = get_todos()
        # for item in finalTodo:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
        # Below is by using list comparhansion

        # new_todos = [item.strip('\n') for item in finalTodo]

        for index, item in enumerate(finalTodo):
            item = item.strip("\n")
            print(f"{index + 1} - {item}")


    elif userChoice.startswith("edit"):
        try:
            todoEdit = int(userChoice[5:])
            todoEdit = todoEdit -1

            todos = get_todos()

            editedTodo = input("Choose your replace todo item: ")
            todos[todoEdit] = editedTodo + "\n"

            with open('list.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Command invalid, please use the index of todo you want to edit!")


    elif userChoice.startswith("complete"):
        try:

            deleteTask = int(userChoice[9:])

            todos = get_todos()
            index = deleteTask-1

            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open('list.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was remove from the list"
            print(message)

        except IndexError:
            print("This item doesn't exist! ")

        except ValueError:
            print("Enter the index of todo you want to delete in numbers: ")

    elif userChoice.startswith("exit"):

        exit("Exiting the program")
    else:
        print("Command is not valid")

print("Bye !")