filenames = ["1.doc", "1.report", "1.presentaion"]
filenames = [filename.replace('.', '-') + ',txt' for filename in filenames]

print(filenames)