feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {}
def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches*0.0254
    return f"{feet} feet and {inches} inches is equal to {meters} meters"

result = convert(feet_inches)



if result < 1 :
    print("You're too small")
else:
    print("You can use it")
