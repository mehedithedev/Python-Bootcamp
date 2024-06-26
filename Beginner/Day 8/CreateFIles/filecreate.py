fileName = input("Enter your file name: \n")
extension = input("Enter your file extension, examples: py / docs/ txt/ java/ jpg/ html and so on....\n")
with open(f"{fileName}.{extension}", "w") as file:
    file.write(fileName)