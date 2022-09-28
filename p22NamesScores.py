import csv
# import pandas
names = list()
with open('p022_names.txt') as file:
    reader = csv.reader(file)
    for row in reader:
        names = row

names.sort()

zeppa = ord('A') - 1

summation = 0
value = 0
count = 0
while True:
    count += 1
    # print(f'{count} {ord(names[count - 1][0]) - zeppa}')
    try:
        for letter in names[count - 1]:
            value += ord(letter) - zeppa
        summation += (count * value)
        value = 0
    except:
        break
    # if names[count - 1] == "COLIN":
    #     break

print(summation)
