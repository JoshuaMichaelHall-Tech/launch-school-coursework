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
