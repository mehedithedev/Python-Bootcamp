def strength(password):
    upper = False
    number = False
    for i in password:
        if i.isupper():
            upper = True
        if i.isnumeric():
            number = True

    if len(password) >= 8 and upper and number:
        return "Strong Password"
    else:
        return "Weak Password"


print(strength("asdf45"))

