import csv
# import pandas

with open('p22names.txt') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
