## What are primitives?
Primitive types are the most fundamental data types in a language. Almost all 
data in a language is built up from these primitive types.

## What are collections?
Non-primitive types such as sequences, mappings, and sets that collect multiple
items in a single object.

## What is a literal?
Any syntactic notation that lets you directly represent an object in source code.
Includes: strings, floats, booleans, dictionaries, lists, tuples, and sets.

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
'single', ''double'', '''triple''', """triple double"""

## How do we escape quotes within a string?
- We can use a `\` just prior to the character to escape.
- We can use a different set of start/end quotes: 'start "problem" end'.
- We can use a raw literal.

## How can we access an individual character in a string?
Using [] indexing syntax. The value between the brackets must be an integer 
between 0 and the length of the string minus 1:
>>> my_str = 'abc'
>>> my_str[0]

## What are Raw Strings?
String literals with an r prefix. They don't recognize escapes `\` so they can 
be used freely.
print(r"C:\Users\File")  # raw string literal

## What are f-Strings?
Formatted string literals. They enable string interpolation. Created by prepend-
ing 'f' to the string:
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

## What does it look like to use multi-line formatting when creating a dictionary?
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
The literal syntax is a comma-separated list of objects between `{}`. Empty sets 
must be created with the set constructor to distinguish from an empty dictionary.
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
A shorthand notation for simultaneously operating on a value and reassigning it:
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
Use an `;` between the statements. This should generally only be done in the REPL.

## What is a REPL?
REPL stands for Read-Eval-Print-Loop. It's an interactive programming 
environment where Python reads your input, evaluates it, prints the result, 
and loops back for more input. Great for testing code snippets quickly.

## How can we get input from the terminal?
`input()`

## What are proceedures?
Blocks of code that run as separate units. In Python, these are called functions.

## What are common terms for using a function?
Calling, invoking, executing, or running it.

## What do we call the lines of code used to create a function?
The function definition or function declaration.

## What do min and max do?
Return the minimum and maximum values from a collection, respectively.

## What do ord and chr do?
ord returns representing the Unicode code point of the character. chr is the 
inverse and converts an integer to its corresponding Unicode character.

## What objects are falsy?
- False, None
- all numeric 0 values (integers, floats, complex)
- empty strings: ''
- empty collections: [], (), {}, set(), frozenset(), and range(0)
- Custom data types can also define additional falsy value(s).

## What do any and all do?
any returns true if there is any matching element in a collection. all returns 
true if every element in a collection matches.

## What are some functions only for the REPL?
id, dir, and help

## What are id, dir, and help used for?
- id: returns an object id integer
- dir: returns a list of all identifiers in the current local scope. When used
with an argument, returns a list of the objects attributes.
- help: use help() to get information.

## What is dunder?
AKA magic methods and magic variables. Names which begin and end with double 
underscores (double-under => dunder).

## How do we pretty print for readability?
```
from pprint import pp 
pp()
```

## What is a docstring?
a triple quoted string used to create a comment.

## Why do Python programmers often add a docstring at the beginning of functions?
Python can access these docstrings from its help function.

## What is scope?
Scope determines where an identifier can be used.

## What is function scope?
In Python, identifiers have function scope. Anything initialized within a function
is only available within that function and any nested functions.

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


