power = 2 ** 1000
num_to_str = str(power)

sum = 0
for num in num_to_str:
    sum += int(num)

print(sum)