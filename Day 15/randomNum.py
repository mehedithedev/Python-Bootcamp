import random
lowBound = int(input("Enter the lower bound: "))
uppBound = int(input("Enter the upper bound: "))

randNum = random.randint(lowBound, uppBound+1)
print(randNum)
