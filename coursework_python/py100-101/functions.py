collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1))
print(any(collection2))
print(any(collection3))
print(any([]))

print(all(collection1))
print(all(collection2))
print(all(collection3))
print(all([]))

numbers = [2, 5, 8, 10, 13]
print([number % 2 == 0 for number in numbers])


