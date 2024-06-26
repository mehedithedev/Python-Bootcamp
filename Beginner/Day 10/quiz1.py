try:
    total_value = float(input("Enter total value: "))

    if total_value == 0:
        raise ZeroDivisionError("Total value cannot be zero")

    value = float(input("Enter value: "))
    result = str((value / total_value)*100)
    print(f"This is {result}%")
except ZeroDivisionError as e:
    print(e)
except ValueError:

    print("You need to enter a number. Run the program again.")
