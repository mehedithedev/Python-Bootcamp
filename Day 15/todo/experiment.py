import glob

myfiles = glob.glob("*.txt")

for file_path in myfiles:
    with open(file_path, 'r') as file:
        print(file.read().upper())
print(myfiles)