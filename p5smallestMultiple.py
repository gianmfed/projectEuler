# 2520 is the smallest number that can be
# divided by each of the numbers from 1 to 10 
# without any remainder.

# What is the smallest positive number that 
# is evenly divisible by all of the numbers 
# from 1 to 20?

number = 2520
sentinel = False

while True:
    # print(number)
    for divisor in range(2, 21):
        if number % divisor == 0:
            if divisor == 20:
                sentinel = True
            continue
        else:
            # print(divisor)
            number += 10 # deve essere divisibile per 10
            divisor = 1 #???
            break
    if sentinel == True:
        break

print(number)
    