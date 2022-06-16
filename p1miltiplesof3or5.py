# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sumofmultiples = 0

### The following is not the solution cause it takes many numbers two times
# for i in range(0, 10, 3):
#     sumofmultiples += i
#     print(i)
# for j in range(0, 10, 5):
#     sumofmultiples += j
#     print(j)

for x in range(10):
    if x % 3 == 0 or x % 5 == 0:
        sumofmultiples += x
        print(x)

print(sumofmultiples)