# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

with open('p13LargeSum.txt') as n:
    sum = 0
    for line in n:
        sum += int(line)
    # print(sum)

    str_sum = str(sum)
    for i in range(10):
        print(str_sum[i], end='')
        
    