import re

# Step 1: Open the file and read its content
with open("2~UML+LDyA'PfR$4ErF78PM^yWMrl!MkqH#.txt", "r") as file:
    content = file.read()

# Step 2: Use a regular expression to find the pattern
# The pattern is now: 2 vowels followed by 1 consonant
pattern = r"([aeiou]{2}[bcdfghjklmnpqrstvwxyz]{1})"
match = re.search(pattern, content, re.IGNORECASE)

# Step 3: Print the match
if match:
    print(match.group())
else:
    print("Pattern not found in the file.")