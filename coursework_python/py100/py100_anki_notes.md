## What are primitives?
Primitive types are the most fundamental data types in a language. Almost all 
data in a language is built up from these primitive types.

## What are collections?
Non-primitive types such as sequences, mappings, and sets that collect multiple
items in a single object.

## What is a literal?
Any syntactic notation that lets you directly represent an object in source 
code. Includes: strings, floats, booleans, dictionaries, lists, tuples, and 
sets.

## How do we create objects without literal forms?
We use the type constructor.
`range(10)`         # Range of numbers: 0-9
`range(1, 11)`      # Range of numbers: 1-10
`set()`             # Empty set
`frozenset([1, 2])` # Frozen set of values: 1 and 2
Note that you cannot use empty curly braces {} to create an empty set, as this 
syntax creates an empty dictionary instead.

## What are variables?
Names used to identify values, i.e. identifiers.

## How do we assign values to variables?
We initialize variables to create them:
`pi = 3.14 # Assignment`
We can then reassign variables:
`pi = 3.141592653589793 # Reassignment`

## What are booleans?
Values representing binary states such as true or false, on or off, yes or no,
one or zero, and so on. The only Boolean values are True and False.

## What are text sequences?
Strings of characters such as words, sentences, dates, and foreign texts.

## What is a string?
A text sequence of unicode characters.

## What is the difference between a text sequence and an ordinary sequence?
Ordinary sequences contain zero or more objects, but a text sequence simply
contains characters or bytes.

## How are string literals written?
With single, double, or triple quotes:
`'single'`, `''double''`, `'''triple'''`, `"""triple double"""`

## How do we escape quotes within a string?
- We can use a `\` just prior to the character to escape.
- We can use a different set of start/end quotes: `'start "problem" end'`.
- We can use a raw literal.

## How can we access an individual character in a string?
Using [] indexing syntax. The value between the brackets must be an integer 
between 0 and the length of the string minus 1:
```
>>> my_str = 'abc'
>>> my_str[0]
```

## What are Raw Strings?
String literals with an r prefix. They don't recognize escapes `\` so they can 
be used freely.
`print(r"C:\Users\File")  # raw string literal`

## What are f-Strings?
Formatted string literals. They enable string interpolation. Created by 
prepending 'f' to the string:
`>>> f'5 plus 5 equals {5 + 5}.'`
`'5 plus 5 equals 10.'`
Anything in the `{}` will be evaluated and the result passed to the string.
Doubling `{{}}` causes the inner `{}` to be used as literal characters.

## How can we print a number with '_' or ',' separators?
Using an f-String:
`print(f'{123456789:_}')       # 123_456_789`
`print(f'{123456789:,}')       # 123,456,789`
`print(f'{123456.7890123:_}')  # 123_456.7890123`
`print(f'{123456.7890123:,}')  # 123,456.7890123`

## What are functions?
Chunks of reusable code. They have a data type.

## What are sequences?
Ordered collection of objects. Includes lists, tuples, and ranges.

## What are lists and tuples?
Ordered lists. Lists use [], tuples use (). Access elements in either using [] 
indexing syntax. Lists are mutable, tuples are not.

## What does mutable and immutable mean?
Mutable means an object can be changed in memory. Immutable means that changes 
are reassignments to a new object at a different location in memory.

## What are ranges?
A sequence of integers between two endpoints. With 1 argument, starts at 0 and
ends just before the argument. With 2 arguments, starts at first argument and
ends just before the second argument. With 3 arguments, the third is the step
value.

## How can we create some ranges?
```
>>> tuple(range(5))
(0, 1, 2, 3, 4)

>>> tuple(range(5, 10))
(5, 6, 7, 8, 9)

>>> list(range(1, 10, 2))
[1, 3, 5, 7, 9]

>>> list(range(0, -5, -1))
[0, -1, -2, -3, -4]
```

## How do we get the integers from a range?
Since Python doesn't calculate the integers until it needs them, we may convert
them to use them. We can use the list or tuple functions, for example.

## How can we access specific numbers in a range?
We can use [] indexing syntax to access numbers in a range.

## What are mappings?
Unordered collections of objects stored as key/value pairs. Use keys to access 
the values. One example is the dictionary class.

## How can we create a dictionary?
```
>>> my_dict = {
...     'dog': 'barks',
...     'cat': 'meows',
...     'pig': 'oinks',
... }
{'dog': 'barks', 'cat': 'meows', 'pig': 'oinks'}
```

## How to use multi-line formatting when creating a dictionary?
```
my_dict = {
    'title': "Monty Python's Flying Circus",
    'cast': [
        'Eric Idle',
        'John Cleese',
        'Terry Gilliam',
        'Graham Chapman',
        'Michael Palin',
        'Terry Jones',
    ],
    'first_season': 1969,
    'last_season': 1974,
    'reboot_season': None,
}
```

## What is multi-line format?
Code that spans across multiple lines for better readability or to handle long 
content. Multi-line strings may use triple quotes (''' or """).
Breaking long statements using backslashes `\` or enclosing in parentheses `()`.

## What are the requirements for keys in dictionaries?
They must be immutable and hashable.

## What are sets?
Unordered collections of unique objects (sometimes called members of the sets).
The literal syntax is a comma-separated list of objects between `{}`. Empty 
sets must be created with the set constructor to distinguish from an empty 
dictionary.
`s1 = set()      # Empty sets`

## What are the requirements for set members?
They must be immutable and hashable.

## What are the two main set types?
Ordinary sets (class set) and frozen sets (class frozenset).

## How can we find the length of almost any collection object or text sequence?
`len()`

## What are the three main kinds of types?
- built-in: part of Python
- standard: available from importable modules that come with Python
- non-standard: additional custom modules

## What are the following 3 operations: //, %, ** ?
- `//` integer division: returns largest whole number less than or equal to float 
- `%` modulo: when both numbers are positive, returns remainder
- `**` exponentiation: raise left number to the power of right number

## What are the two equality comparators?
- `==` (equal?)
- `!=` (not equal?)

## What are the ordered comparitors?
- `<` (less than)
- `>` (greater than)
- `<=` (less than or equal to)
- `>=` (greater than or equal to)

## What does it mean that strings are compared lexicographically?
They are compared character-by-character from left to right.

## How are uppercase and lowercase letters compared?
All uppercase letters are lower than any lowercare letters.

## What is string contatenation?
Looks like numeric addition and multiplication, using `+` and `*` to join strings.
```
'foo' + 'bar'     # 'foobar'
'abc' * 3         # 'abcabcabc'
3 * 'abc'         # 'abcabcabc'
```

## What is coercion?
We cannot add the two strings '1' and '2' mathematically. We need to use type 
coercion. 
```
print(int('1') + int('2')    # 3
```
Numbers can also be converted to strings:
```
print(str(5))                 # '5'
```
These are examples of explicit conversion.

## What are examples of explicit and implicit conversion?
Explicit conversion:
```
print(str(3))    # 3 
```
Implicit conversion:
```
print(3)         # 3 
```
Implicit conversion is automatic when mixing different types of numbers in an 
expression.
Truthiness tests use implicit conversion.

## How can we determine the type of a given object?
```
print(type(1))   # <class 'int'>
```

## How can we just get the class name of a given object?
```
print(type('abc').__name__)   # str
```

## How can we find out if an object is a particular type?
```
# No regard to inheritance:
print(type('abc') is str)     # True
print(type('abc') is int)     # False
print(type(False) is bool)    # True
print(type([]) is list)       # True
print(type([]) is set)        # False 

# Includes inheritance:
print(isinstance('abc', str))    # True
print(isinstance([], set))       # False 
```

## How can we get a string representation of an object?
By using the str and repr functions:
```
my_str = 'abc'
print(my_str)       # abc
print(str(my_str))  # abc (same as print(my_str))
print(repr(my_str)) # 'abc' (note the quotes)
```

## What is the difference between the str and repr functions?
The repr function is a bit lower-level. It returns a string that you can, 
in theory, use to create a new instance of the object.

## What is the difference between statements and expressions in Python?
Expressions combine values, variables, operators, and function calls to produce
a new object. They must be evaluated to determine the expression's value.
Statements are instructions to Python to perform an action.
So, expressions return objects while statements perform actions.

## How does Python evaluate expressions?
- Generally from left to right.
- Follows order of operations.
- Nested parentheses are evaluated first.
- Use parentheses to control and document order of operations.

## What is the difference between output and return?
Outputs do something like print to the screen. Returns give a result, like 
evaluating 2 + 2 is 4. 

## What is a variable?
A label for information stored in memory. AKA identifiers.

## How do we create a function?
The def statement creates a function. 

## How do we call a function?
By appending `()` to the function name.

## How are different types of variables named in Python?
- CONSTANTS: SCREAMING_SNAKE_CASE
- Classes: PascalCase
- All Others: snake_case 
  
## Where are constants usually defined?
In the global scope.

## What happens when we assign an expression to a variable?
The expression is first evaluated and the return value is assigned to the 
variable.

## What is augmented assignment?
A shorthand notation for simultaneously operating on a value and reassigning 
it:
```
foo = 42            # foo is 42
foo -= 2            # foo is now 40
foo *= 3            # foo is now 120
foo += 5            # foo is now 125
foo //= 25          # foo is now 5
foo /= 2            # foo is now 2.5
foo **= 3           # foo is now 15.625
print(foo)          # prints 15.625
```
These operators are known as assignment operators.

## How does augmented assignment work with sets?
```
bar = {1, 2, 3}     # bar is {1, 2, 3}
bar |= {2, 3, 4, 5} # | performs set union
                    # bar is now {1, 2, 3, 4, 5}
bar -= {2, 4}       # - performs set difference
                    # bar is now {1, 3, 5}
print(bar)          # prints {1, 3, 5}
```

## What is the difference between reassignment and mutation?
- Reassignment changes the binding of a variable so it references a new object.
- Mutation changes the object itself.

## How to enter multiple statements on the same line?
Use an `;` between the statements. This should generally only be done in the 
REPL.

## What is a REPL?
REPL stands for Read-Eval-Print-Loop. It's an interactive programming 
environment where Python reads your input, evaluates it, prints the result, 
and loops back for more input. Great for testing code snippets quickly.

## How can we get input from the terminal?
`input()`
```
user_input = input("Enter something: ")
print(f"You entered: {user_input}")
```

## What are proceedures?
Blocks of code that run as separate units. In Python, these are called 
functions.

## What are common terms for using a function?
Calling, invoking, executing, or running it.

## What do we call the lines of code used to create a function?
The function definition or function declaration.

## What do `min` and `max` do?
Return the minimum and maximum values from a collection, respectively.

## What do `ord` and `chr` do?
`ord` returns an integer representing the Unicode code point of the character.
`chr` is the inverse and converts an integer to its corresponding Unicode 
character.

## What objects are falsy?
- `False`, `None`
- all numeric 0 values (integers, floats, complex)
- empty strings: `''`
- empty collections: `[]`, `()`, `{}`, `set()`, `frozenset()`, and `range(0)`.
- Custom data types can also define additional falsy value(s).

## What do `any` and `all` do?
`any` returns true if there is any matching element in a collection. `all` returns 
true if every element in a collection matches.

## What are some functions only for the REPL?
`id`, `dir`, and `help`

## What are id, dir, and help used for?
- `id`: returns an object id integer
- `dir`: returns a list of all identifiers in the current local scope. When used
with an argument, returns a list of the objects' attributes.
- `help`: use `help()` to get information.

## What is dunder?
AKA magic methods and magic variables. Names which begin and end with double 
underscores (double-under => dunder). EG `__name__`.

## How do we pretty print for readability?
```
from pprint import pp 
pp()
```

## What is a docstring?
A triple quoted string used to create a comment.

## Why Python programmers often add a docstring at the beginning of functions?
Python can access these docstrings from its help function.

## What is scope?
Scope determines where an identifier can be used.

## What is function scope?
In Python, identifiers have function scope. Anything initialized within a 
function is only available within that function and any nested functions.

## How to start and exit Python REPL?
- Start: `python` or `python3`
- Exit: `exit()`, `quit()`, or Control-D

## How to stop a running Python program?
Control-C

## Ways to continue lines?
- String literals in parentheses
- Triple-quoted strings
- Multi-value literals with line breaks
- Parentheses for expressions
- Backshash (`\`) at line end

## What are conditional statements?
Statements that control the path data takes through a program based on whether 
a condition evaluates to true or false.

## What are the basic conditional statement structures in Python?
- `if`: Executes a block of code if a condition is true
- `elif`: Checks another condition if the previous conditions were false
- `else`: Executes a block of code if all previous conditions were false

## How do we organize code blocks in conditional statements?
All statements in a block must be indented consistently using spaces. 
Indentation defines the block structure in Python.
Python uses 4 spaces for indentation.

## What does the equality operator (`==`) do?
Returns `True` when operands have equal values:
```python
print(5 == 5)                 # True
print('abc' == 'abc')         # True
print(5 == '5')               # False
```

## How can we perform case-insensitive string comparison?
By converting both strings to the same case before comparison:
```python
print('abc'.lower() == 'aBc'.lower())  # True
print('abc'.upper() == 'aBc'.upper())  # True
print('abc'.casefold() == 'aBc'.casefold())  # True
```

## What is the difference between `casefold()` and `lower()`?
`casefold()` is more aggressive and handles international text better than 
`lower()`, making it preferred for case-insensitive comparisons across 
languages.

## What does the inequality operator (`!=`) do?
Returns `True` when operands are not equal:
```python
print(5 != 5)             # False
print(5 != 4)             # True
```

## How do the less than (`<`) and less than or equal to (`<=`) operators work?
- `<` returns `True` when left operand is less than right
- `<=` returns `True` when left operand is less than or equal to right

## How do the greater than (`>`) and greater than or equal to (`>=`) operators work?
- `>` returns `True` when left operand is greater than right
- `>=` returns `True` when left operand is greater than or equal to right

## How does string comparison work with comparison operators?
Strings are compared character-by-character:
```python
print('42' < '402')       # False (because '4' == '4', but '2' > '0')
print('42' < '420')       # True
```

## What does the `not` operator do?
Negates a Boolean value:
```python
print(not True)           # False
print(not False)          # True
print(not(4 == 4))        # False
```

## What do the `and` and `or` operators do?
- `and`: Returns `True` if both operands are true
- `or`: Returns `True` if at least one operand is true

## What is short-circuit evaluation?
A performance optimization where the second part of a logical expression is 
only evaluated if necessary:
- In `A and B`, if `A` is `False`, `B` is not evaluated (result is always `False`)
- In `A or B`, if `A` is `True`, `B` is not evaluated (result is always `True`)

## What are the falsy values in Python?
- `False`, `None`
- Zero values: `0`, `0.0`
- Empty collections: `''`, `[]`, `()`, `{}`, `set()`, `range(0)`
- Everything else is truthy

## What do logical operators actually return in Python?
They return the last evaluated value, not just `True`/`False`:
```python
print(3 and 'foo')   # 'foo'
print(0 and 'foo')   # 0
print(3 or 'foo')    # 3
print(0 or 'foo')    # 'foo'
```

## What is the order of precedence for logical operators?
From highest to lowest:
- Comparison operators (`==`, `!=`, `<=`, `<`, `>`, `>=`)
- `not`
- `and`
- `or`

## What is the `match/case` statement?
Introduced in Python 3.10, it compares a single value against multiple 
patterns:
```python
match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _:  # default case
        print('value is neither 5 nor 6')
```

## How can we match multiple values in a single case?
Using the pipe (`|`) operator:
```python
match value:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _:
        print('value is something else')
```

## What is a ternary expression?
A concise way to choose between two values based on a condition:
```python
result = value1 if condition else value2
```

## How do functions help improve code?
- Reduce repetitive code
- Enable code reuse
- Improve readability and maintenance
- Organize code into logical blocks

## What are the terms for using a function?
Calling, invoking, executing, or running it.

## How are multiple arguments separated in a function call?
With commas:
```python
print('hello', 'good-bye', 'farewell')
```

## How can we format long argument lists?
By spreading them over multiple lines:
```python
print(
    'hello',
    'good-bye',
    'farewell',
    'adios',
)
```

## What are some examples of built-in functions in Python?
- Type conversion: `float`, `int`
- Constructors: `str`, `list`, `tuple`, `set`, `frozenset`
- I/O functions: `input`, `print`
- Information functions: `type`, `len`

## What are predicates?
Functions that return Boolean values:
```python
def is_digit(char):
    if char >= '0' and char <= '9':
        return True
    return False
```

## What is the default return value of a function without an explicit return?
`None` (implicit return)

## How do we provide default values for parameters?
Using the assignment operator in the parameter list:
```python
def say(text='hello'):
    print(text + '!')
```

## What's the rule for parameter defaults in functions?
After a default parameter, all subsequent parameters must have defaults.

## What's the difference between functions and methods?
- Functions are invoked as: `function_name(obj, ...)`
- Methods are invoked as: `obj.method_name(...)`
- Methods belong to a class and require an object of that class

## What does it mean to mutate the caller?
Some methods change the object used to call them:
```python
odd_numbers = [1, 3, 5, 7, 9]
odd_numbers.pop()      # Removes and returns 9
print(odd_numbers)     # [1, 3, 5, 7]
```

## What's a better practice than mutating arguments?
Return a new object instead:
```python
def add_new_number(my_list):
    return my_list + [9]  # Creates a new list
```

## What is variable shadowing?
When a local variable has the same name as a variable in an outer scope, hiding 
the outer variable:
```python
greeting = 'Salutations'

def well_howdy(who):
    greeting = 'Howdy'     # Local variable shadows outer greeting
    print(f'{greeting}, {who}')
```

## In what order does Python look for identifiers?
- Local namespace (local scope)
- Enclosing namespaces (outer scopes)
- Global namespace (global scope)
- Built-in namespace

## What is the difference between parameters and arguments?
- Parameters: Placeholders in function definition
- Arguments: Values passed when calling the function

## What is a collection?
A data structure that can contain multiple elements.

## What are the main collection types in Python?
- Sequences: ranges, tuples, lists, strings
- Mappings: dictionaries
- Sets: sets, frozen sets

## What's the difference between mutable and immutable collections?
- Mutable collections can be changed (lists, dictionaries, sets)
- Immutable collections cannot be changed (ranges, tuples, frozen sets, 
  strings)

## What defines a sequence collection?
- Ordered collections of objects
- Can be indexed by whole numbers (starting at 0)
- Examples: lists, tuples, ranges, strings

## What's the difference between homogeneous and heterogeneous collections?
- Homogeneous: All elements are of the same type (e.g., ranges)
- Heterogeneous: Can contain different types of objects (e.g., lists, tuples)

## How do strings differ from standard sequences?
- Homogenous (all characters)
- Characters aren't distinct objects until referenced
- Characters are strings of length 1
- Not a true collection (characters aren't objects)

## What defines a set collection?
- Unordered collections of unique objects
- Cannot be indexed
- No defined order for objects
- No duplicate members allowed

## What are the two types of sets?
- Sets (`set`): Mutable
- Frozen sets (`frozenset`): Immutable

## What defines a mapping collection?
- Unordered collections of key/value pairs
- Accessed by keys, not indices
- Keys must be unique and hashable
- Values can be any object

## What are the three forms of the range constructor?
- `range(start, stop, step)`: Generates sequence from `start` to `stop - 1` 
  with increment of `step`
- `range(start, stop)`: Same as `range(start, stop, 1)`
- `range(stop)`: Same as `range(0, stop, 1)`

## What is a lazy sequence?
A sequence that doesn't compute all its elements at once, but creates them only 
when needed. Ranges are lazy sequences.

## How can we create nested collections?
By including collections inside other collections:
```python
nested_list = [
    {'foo': 42, 'bar': [1, 2, 3]},
    {'Kim', ('Leslie', 'Les')},
    (4, 5, (1, 2, 3)),
    ['a', 'b', 'cde'],
]
```

## What are the limitations of nesting mutable collections?
- Can't nest mutable collections inside sets:
```python
# Error: TypeError: unhashable type: 'list'
my_set = {1, 2, 3, [4, 5]}
```

## How do we access elements in nested collections?
Using multiple indices:
```python
nested_seq = [[1, 2], [3, 4]]
print(nested_seq[1][0])  # 3
```

## When are two collections considered equal?
Equal collections must meet all criteria:
- Same type (list, tuple, set, etc.)
- Same number of elements
- For sequences, corresponding elements must be equal
- For sets, same members (order doesn't matter)
- For mappings, same key/value pairs (order doesn't matter)

## What is indexing?
The process of using a whole number to access and perhaps alter an element of 
a sequence.
```
seq = ('a', 'b', 'c')
print(seq[0])  # a (1st element)
print(seq[1])  # b (2nd element)
print(seq[2])  # c (3rd element)
print(seq[3])  # IndexError: tuple index out of range 
```

## What is slicing?
Slicing can extract or modify any number of consecutive elements in a 
collection simultaneously.
`seq[start:stop]`
`seq[start:stop:step]`

## Examples of slicing:
```
seq = 'abcdefghi'
print(seq[3:7])       # defg
print(seq[-6:-2])     # defg
print(seq[2:8:2])     # ceg
print(repr(seq[3:3])) # ''
print(seq[:])         # abcdefghi
print(seq[::-1])      # ihgfedcba
```

## What is key-based access?
The process of using keys to access values in mappings.
```
my_dict = {
    'a': 'abc',
    37: 'def',
    (5, 6, 7): 'ghi',
    frozenset([1, 2]): 'jkl',
}

print(my_dict['a'])                # abc
print(my_dict[37])                 # def
print(my_dict[(5, 6, 7)])          # ghi
print(my_dict[frozenset([1, 2])])  # jkl
print(my_dict['nothing'])     # KeyError: 'nothing'
```

## How can we verify that a key exists in a dictionary?
By using `dict.get`.
```
my_dict = {
    'a': 'abc',
    37: 'def',
    (5, 6, 7): 'ghi',
    frozenset([1, 2]): 'jkl',
}

print(my_dict.get('a'))                 # abc
print(my_dict.get('nothing'))           # None
print(my_dict.get('nothing', 'N/A'))    # N/A
print(my_dict.get('nothing', 100))      # 100
```

## What are some non-mutating operations for collections?
`in`: determines if the object to the left is in the collection on the right.
`not in`: reverse of in.
`min` and `max` return minimum and maximum members using `<` and `>`.
`sum`: computes and returns sum of collections numerals.
`index`: returns index of first matching object.
`count`: returns number of times a value occurs.
`zip`: merges members of multiple iterables into a single list of tuples.


## How does zip work?
```
iterable1 = [1, 2, 3]
iterable2 = ('Kim', 'Leslie', 'Bertie')
iterable3 = [None, True, False]

zipped_iterables = zip(iterable1, iterable2, iterable3)
print(list(zipped_iterables))
# Pretty printed for clarity
# [
#   (1, 'Kim', None),
#   (2, 'Leslie', True),
#   (3, 'Bertie', False)
# ]
```

## What is special about iterators?
They can only be consumed once:
```
result = zip(range(5, 10),    # length is 5
             range(1, 3),     # length is 2 (shortest)
             range(3, 7))     # length is 4
print(list(result)) # [(5, 1, 3), (6, 2, 4)]
print(list(result)) # []
```

## What are the three get operations for dictionaries?
`dict.keys`
`dict.values`
`dict.items`
They return their outputs in a wrapper: dict_keys(), dict_values(), or 
dict_items() to show that these aren't regular lists. They are actually 
dictionary view objects that are tied to the dictionary.

## What are some mutating operations for mutable sequences?
`seq.append` appends a single object to the end.
`seq.insert` inserts an object into a mutable sequence before the element at a 
given index.
`seq.extend` appends the contents of an iterable sequence to the calling 
iterable.
`seq.remove` searches and removes first occurance of an object.
`seq.pop` removes and returns indexed element or last element.
`seq.clear` removes all elements.

## What is the difference between `sorted` and `sort`?
`sorted` creates a new, sorted list from a collection.
```
names = ('Grace', 'Clare', 'Allison', 'Trevor')
print(sorted(names))
# ['Allison', 'Clare', 'Grace', 'Trevor']
```
`sort` mutates the list and is a little faster.
```
print(names.sort())   # None
print(names)
# ['Allison', 'Clare', 'Grace', 'Trevor']
```

## How can we sort in reverse?
By adding a reverse=True keyword argument.
```
names = ['Grace', 'Clare', 'Allison', 'Trevor']
print(sorted(names, reverse=True))
# ['Trevor', 'Grace', 'Clare', 'Allison']

names.sort(reverse=True)
print(names) # ['Trevor', 'Grace', 'Clare', 'Allison']
```

## How can we perform a case-insensitive sort?
```
words = ['abc', 'DEF', 'xyz', '123']
print(sorted(words))
# ['123', 'DEF', 'abc', 'xyz']

print(sorted(words, key=str.casefold))
# ['123', 'abc', 'DEF', 'xyz']
```

## How can we reverse sequences and dictionaries?
`reversed` # Non-mutating
`list.reverse` # Mutating
```
names = ('Grace', 'Clare', 'Allison', 'Trevor')
reversed_names = reversed(names)
print(reversed_names)
# <reversed object at 0x102848e50>
print(tuple(reversed(names))) # Requires extra memory
# ('Trevor', 'Allison', 'Clare', 'Grace')
print(names)
# ('Grace', 'Clare', 'Allison', 'Trevor')

names = list(names)
print(names.reverse())   # None
print(names)
# ['Trevor', 'Allison', 'Clare', 'Grace']

my_dict = {'abc': 1, 'xyz': 23, 'pqr': 0, 'jkl': 5}
reversed_dict = reversed(my_dict)
print(reversed_dict)
# <dict_reversekeyiterator object at 0x100d19f80>

print(list(reversed_dict))    # Requires extra memory
# ['jkl', 'pqr', 'xyz', 'abc']
```

## What are some basic string methods?
`str.lower` returns string all lowercased
`str.upper` returns string all uppercase
`str.capitalize` returns string with first letter only capitalized.
`str.title` returns string with first letter of every word capitalized. But 
uses some punctuation to mark new words.
`import string; string.capwords(str) capitalizes every word following white 
space.
`str.swapcase` generally swaps case of every letter.
Note that strings are immutable, so string methods are non-mutating!

## What are some character classification methods?
`str.isalpha` true if all characters are alphabetical.
`str.isdigit` true if all characters are digits.
`str.isalnum` true if all alphabetical or digits.
`str.islower` true if all letters are lowercase.
`str.isupper` true if all letters are uppercase.
`str.isspace` true if all characters are whitespace. False if empty.
`str.isascii` true if all characters are ascii.

## How to remove leading and trailing whitespace?
`str.strip` It can also remove other leading/trailing characters when provided
as a string arg.
```
text = ' \t  abc def    \n\r'
print(repr(text.strip('abc'))) # ' \t  abc def    \n\r'

text = 'aaabaacccabxyzabccba'
print(text.strip('a'))         # baacccabxyzabccb
print(text.strip('ab'))        # cccabxyzabcc
print(text.strip('ba'))        # cccabxyzabcc
print(text.strip('abc'))       # xyz
print(text.strip('bc'))        # aaabaacccabxyzabccba

print(repr(text.strip('abcxyz'))) # ''
```

## Why use `repr` when outputting strings?
`repr` formats strings with quotes and shows whitespace.

## How can we remove either leading or trailing whitespace or characters?
`str.lstrip` or `str.rstrip`

## How can we determine whether a string leads or trails with a substring?
`str.startswith`
`str.endswith`
May take index, or tuple as arguments.

## How can we split and join strings?
`str.split` defaults to split at whitespace but takes an argument to determine
alternative.
`str.join` same as `split` but joins.

## How can we split a string into its characters?
`list(str)` or `tuple(str)`
`for char in str:`

## How can we split a text into lines?
`text.splitlines`

## How can we join text?
```
words = ['You', 'were', 'lucky']
print(''.join(words))         # Youwerelucky
print(' '.join(words))        # You were lucky
print(','.join(words))        # You,were,lucky
print('\n  '.join(words))
# You
#   were
#   lucky
```

