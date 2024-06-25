myFiles = ("1.Raw.Data.txt", "2.Reports.txt", "3.Presentations.txt")
for file in myFiles:
    print(file)

    # Can't modify anything inside of a Tuple
    # It is advised to use lists instead of tuple as it's more flexible and mutable
    # Tuples can be used in more specialized cases
    