# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

class Number_String:
    def __init__(self):
        pass


with open('p8LargestProductInASeries.txt') as n:
    
    number_str = n.read()
    number = []

    for t in number_str:
        if t.isnumeric():
            number.append(int(t))

    product = 1
    result = 0

    number_length = len(number)
    for index in range(number_length - 13):
        for i in range(13):
            product *= number[index + i]
        if product > result:
            result = product
        product = 1

    print(result)

    