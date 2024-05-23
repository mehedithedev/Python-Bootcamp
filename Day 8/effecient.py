readFile = open("list.txt", 'r')
todos = readFile.readlines()

while True:

    # Get user input and strip space chars from it
    userChoice = input("Choose any of this: add, show, edit, complete, exit: \n")


    if "add" in userChoice or "new" in userChoice:
        addTodo = userChoice[4:]

        with open('list.txt', 'r') as readFile:
            todoItems = readFile.readlines()
        todoItems.append(addTodo)

        writeFile = open("list.txt", "w")
        writeFile.writelines(todoItems)
        writeFile.close()


        with open('list.txt', 'w') as readFile:
            readFile.writelines(todoItems)

    elif "show" in userChoice:
        updatedTodo = open("list.txt", "r")
        finalTodo = updatedTodo.readlines()
        updatedTodo.close()

        with open('list.txt', 'r') as readFile:
            finalTodo = readFile.readlines()
        # for item in finalTodo:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
        # Below is by using list comparhansion

        # new_todos = [item.strip('\n') for item in finalTodo]

        for index, item in enumerate(finalTodo):
            item = item.strip("\n")
            print(f"{index + 1} - {item}")


    elif "edit" in userChoice:
        todoEdit = int(userChoice[5:])
        todoEdit = todoEdit -1

        with open('list.txt', 'r') as file:
            todos = file.readlines()

        editedTodo = input("Choose your replace todo item: ")
        todos[todoEdit] = editedTodo + "\n"

        with open('list.txt', 'w') as file:
            file.writelines(todos)

    elif "complete" in userChoice:
        deleteTask = int(userChoice[9:])

        with open('list.txt', 'r') as file:
            todos = file.readlines()
        index = deleteTask-1

        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open('list.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was remove from the list"
        print(message)

    elif "exit" in userChoice:
        print("Closing the program -- ")
        break
    else:
        print("Command is not valid")

print("Bye !")