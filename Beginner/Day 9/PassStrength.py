password = input("Enter  a password: ")
result = {}
if len(password) >= 8 :
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit


upper = False

for i in password:
    if i.isupper():
        upper = True

result["uppercase"] = upper

# Dictionaries, more like a list. m


if all(result.values()):
    print("Strong Password")
elif result["length"] == False:
    print("It needs to have more than 8 charcter")
elif result["digit"] == False:
    print("It requires to have at least one number")
elif result["uppercase"] == False:
    print("There should be at least one uppercase")
else:
    print("Weak Password! Choose another one: ")

