# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two 
# abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the 
# sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that 
# the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

##################################################
##### usare piccole funzioni ############

# Importo sqrt per trovare con meno iterazioni i divisori
from math import sqrt
upper_limit = 28123

# Funzione per sapere se un numero è abbondate
def is_abundant(n):
    # Il numero 1 è divisore di tutti perciò già l'ho aggiunto
    sum_of_divisors = 1

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n//i:
                sum_of_divisors += n//i
            print(i)
            print(n//i)

    print(f"\n\nThe sum is {sum_of_divisors}")

    if sum_of_divisors > n:
        return True


# Trava i numeri abbondanti ed inserili in una struttura dati

for n in range(12, upper_limit +1):
    if is_abundant(n):

        print(f"{n} is abundant")
    input()

# Trova tutte le somme di numeri abbondanti

# Somma tutti i numeri abbondanti

# Somma tutti i numeri e sottrai la somma di quelli abbondanti

