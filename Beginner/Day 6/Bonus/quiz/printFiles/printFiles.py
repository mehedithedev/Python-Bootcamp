list = ['a', 'b', 'c']

for i in list:

    # The below part is to create 3 files first:
    # file = open(f"{i}.txt", 'w')
    # file.write(f"I'm {i}")


    file = open(f"{i}.txt", "r")
    print(file.read())
