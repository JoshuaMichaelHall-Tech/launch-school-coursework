import random

highest = 10
while highest:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break


