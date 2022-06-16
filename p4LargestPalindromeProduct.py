# A palindromic number reads the same both ways. The largest palindrome made from 
# the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

number1 = 999
number2 = number1
result = 9009


def palindrome(num):
    snum = str(num)
    nlen = len(snum) // 2
    for i in range(nlen):
        if snum[i] != snum[-1-i]:
            return False
    return True

largest_palindrome = 0

while number1 > 99:
    number2 = 999
    while number2 > 99:
        result = number1 * number2 
        if palindrome(result):
            largest_palindrome = max(largest_palindrome, result)
        number2 -= 1
    number1 -= 1

print(largest_palindrome)