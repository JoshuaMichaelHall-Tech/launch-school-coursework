numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = []

for value in numbers.values():
    half_numbers.append(value // 2)

print(half_numbers)

for key, value in numbers.items():
    print(f'A {key} number is {value}!')
