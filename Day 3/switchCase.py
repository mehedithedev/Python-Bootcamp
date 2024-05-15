todos = []

while True:
    userInput = input("Say add, show or exit: ").strip() ## strip will make the string more simple and remove all the whitespaces

    match userInput:
        case "add":
            todo = input("Enter a todo item: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break

