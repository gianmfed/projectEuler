# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

sum_of_amicable_numbers = 0

def sum_of_divisors(n):
    sum = 0
    for d in range(1, n):
        if (n % d == 0):
            sum += d
    
    return sum



for number in range(1, 10000):
    d_a = sum_of_divisors(number)

    if sum_of_divisors(d_a) == number and number != d_a:
        sum_of_amicable_numbers += number
    
print(sum_of_amicable_numbers)