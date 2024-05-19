
while True:
    usIpu = input("add/ show/ edit/ exit: ").strip().lower()
    match usIpu:
        case "add":
            todo = input("Enter to do item: ") + "\n"
            file = open('todos.txt', 'r')
            todos = file.readlines()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
        case "show":
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

