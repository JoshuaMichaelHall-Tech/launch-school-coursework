my_list = [6, 3, 0, 11, 20, 4, 17]

# Loops Problem 3
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

for num in my_list:
    print(num)

# Loops Problem 4
index = 0
while index < len(my_list):
    num = my_list[index]
    if num % 2 == 0:
        print(num)
    index += 1

for num in my_list:
    if num % 2 != 0:
        print(num)

# Problem 5
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for list in my_list:
    for num in list:
        if num % 2 == 0:
            print(num)

# Problem 6
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

evaluated = []
for num in my_list:
    evaluated.append('even' if num % 2 == 0 else 'odd')

print(evaluated)


