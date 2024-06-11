import csv
with open("weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data:
    if row[1:]:
        if row[0]== city:
            print(row[1])