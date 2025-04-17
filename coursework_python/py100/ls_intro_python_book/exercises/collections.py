pi = 3.14
str_pi = str(pi)
str_pi = f'{pi}'

print(list(range(3, 17, 4)))
print(tuple(range(3, 17, 4)))

find_me = {
    'Alice': 'USA',
    'Francois': 'Canada',
    }

print(find_me['Alice'])

print(list(range(0, 25, 3))[6])
print(range(0, 25, 3)[6])

my_range = range(0, 25, 3)
print(my_range[6])

school = 'Launch School'
print(school[4:10])

start = school.find('c')
print(school[start:start + 6])

start = (1, 2, 3, 4, 5)
print(tuple(reversed(start[1:4])))

my_list = list(start)
my_list.reverse()
result = tuple(my_list[1:4])
print(result)

result = start[3:0:-1]
print(result)

result = start[-2:-5:-1]
print(result)

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])
print(pets['Lizard'] if 'Lizard' in pets else 'silence')

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info_list = '+'.join(info.split(':'))
print(info_list)

result = info.replace(':', '+')
print(result)

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3]=606

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

print(list(zip(my_str, my_list, my_tuple, my_range)))
