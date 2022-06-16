# the difference between the sum of the squares of the first ten 
# natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.

N = 100


def sum_of_squares(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i * i
    print(sum)
    return sum


def square_of_sum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print(sum * sum)
    return sum * sum


print(square_of_sum(N) - sum_of_squares(N))
