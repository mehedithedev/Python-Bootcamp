contents = ["content "
            "1",
            "content "
            "2",
            "content "
            "3"]
filenames = ["content 1.txt", "content 2.txt", "content 3.txt"]

# our task is to create 3 files with associated contents above:

# Enumarate always generates tuples so we can't use that here :(
for content , filename in zip(contents, filenames):  # we have to use zip instead
    file = open(f"files/{filename}", "w")
    file.write(content)

