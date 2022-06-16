# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there 
# are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
# "and" when writing out numbers is in compliance with British usage.

import re

pattern = re.compile(r'<td>(\D+)</td>')
letters = 0

with open("p17Number in Words.txt") as f:
    matches = pattern.findall(f.read())

    for match in matches:
        for character in match:
            if character.isalpha():
                letters += 1
        # solo dove si deve aggiungere 'and'
        add_and = re.search('hundred\s', match)
        if add_and:
            letters += 3
            # print(match)
    
    print(letters)