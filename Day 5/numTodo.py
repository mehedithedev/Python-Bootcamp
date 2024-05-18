todos = []
while True:
    userIn = input("Typd add, show, edit or exit").strip()

    match userIn:
        case "add":
            todo = input("Enter a todo item")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(index, '-', item)
        case "edit":
            todoIndex = int(input("Which option you want to choose? ")) - 1
            new_Todo = input("Enter new todo")
            todos[todoIndex] = new_Todo

        case "exit":
            break
print("Thanks for using :) ")
