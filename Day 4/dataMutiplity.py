filenames = ["1.Raw.Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-') # .replace will replace whatever is on the second argument
    
    print(filename)