feet_inches = input("ENter feet and inches: ")
def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches*0.0254
    return f"{feet} feet and {inches} inches is equal to {meters} meters"

result = float(convert(feet_inches))

print((convert(feet_inches)))

if result < 1 :
    print("You're too small")
else:
    print("You can use it")
