while True:
    usIpu = input("add/ show/ edit/ exit: ").strip().lower()
    match usIpu:
        case "add":
            todo = input("Enter to do item: ") + "\n"

            # Reading the existing to do items from the file
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo) #always close


            # Writing new todo items into the TXT tile
            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close() #always close
        case "show":
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for i, item in enumerate(todos):
                print(f"{i+1} - {item}")
                print(f"Your todo has {todos.__len__()} items")


        case "edit":
            editTodoIndex = int(input("Enter the number of todo you want to edit? "))-1
            print(f"You selected: {todos[editTodoIndex]}")
            reason = input("What do you want to do: edit/delete? ")
            match reason:
                case "edit":
                    editedTodo = input("Now enter your new todo item: ")
                    todos[editTodoIndex] = editedTodo
                case "delete":
                    todos.remove(todos[editTodoIndex])
        case "complete":
            completeNum = int(input("Number of the todo to complete: "))
            todos.pop(completeNum-1)
        case "exit":
            break

