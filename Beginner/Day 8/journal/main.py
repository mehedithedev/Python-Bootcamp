date = input("Enter today's data: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow: \n")

with open(f"{date}.txt", "w") as file:
    file.write(mood+ "\n"*2)
    file.write(thoughts)
