def do_twice(f, v):
    f(v)
    f(v)

def print_twice(str):
    print(str)
    print(str)

do_twice(print_twice, 'spam')

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

line1 = '+ - - - - + - - - - +'
line2 = '|         |         |'

def top(line1, line2):
    print(line1)
    do_twice(print_twice, line2)

top(line1, line2)
top(line1, line2)
print(line1)
