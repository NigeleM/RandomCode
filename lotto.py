


# lotto

import random

def lotto():
    numbers = set()
    rangeWhite = 70
    rangeRed = 25
    count = 0
    while len(numbers) != 5:
        white = random.randrange(1,rangeWhite)
        numbers.add(white)
        rangeWhite -= 1


    while len(numbers) != 6:
        red = random.randrange(1,rangeRed)
        numbers.add(red)
        rangeRed -= 1
        power = red
    return numbers, power

lotto()

print(lotto())
print(lotto())
print(lotto())
print(lotto())
print(lotto())
print(lotto())
print(lotto())
                        
        
        
        
