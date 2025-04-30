destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(destination, destinations):
    index = 0
    while index < len(destinations):
        if destinations[index] == destination:
            return True
        index += 1
    return False

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False
