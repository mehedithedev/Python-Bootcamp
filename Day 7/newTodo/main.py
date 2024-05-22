readFile = open("list.txt", 'r')
todos = readFile.readlines()

while True:

    # Get user input and strip space chars from it
    userChoice = input("Choose any of this: a, s, e, d, x: \n")
    match userChoice:

        case "a":
            addTodo = input("Enter a ToDo item: ") + "\n"
            readFile = open("list.txt", "r")
            todoItems = readFile.readlines()
            readFile.close()
            todoItems.append(addTodo)

            writeFile = open("list.txt", "w")
            writeFile.writelines(todoItems)
            writeFile.close()
        case "e":
            todoEdit = int(input("Enter the index of todo you want to edit: "))
            editedTodo = input("Choose your replace todo item: ")
            todos[todoEdit] = editedTodo
        case "d":
            deleteTask = input("Delete All = a \n Delete one: i ")
            match deleteTask:
                case "a":
                    with open("list.txt", "w") as file:
                        print("You successfully deleted all the todos")
                case "i":
                    deleteIndex = int(input("Index of todo you want to delete: "))
                    todos.pop(deleteIndex-1)
        case "s":
            updatedTodo = open("list.txt", "r")
            finalTodo = updatedTodo.readlines()
            updatedTodo.close()

            # for item in finalTodo:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)
            # Below is by using list comparhansion

            # new_todos = [item.strip('\n') for item in finalTodo]

            for index, item in enumerate(finalTodo):
                item = item.strip("\n")
                print(f"{index + 1} - {item}")
                readFile.close()
        case "x":
            print("Bye !")
            break
