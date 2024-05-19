filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for i in filenames:
    file = open(f"{i}", "w")
    file.writelines("Hello")
