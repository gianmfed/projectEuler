def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

ntostring = str(fact(100))

sumofdig = 0
for l in ntostring:
    sumofdig += int(l)

print(sumofdig)