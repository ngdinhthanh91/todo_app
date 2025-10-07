import csv

with open('files/weather.csv', mode='r') as file:
    data = list(csv.reader(file))

city = input("Enter the city name: ").strip().lower()

for row in data[1:]:  # Skip header row
    if row[0].lower() == city:
        print(f"City: {row[0]}, Temperature: {row[1]}°C")
        break