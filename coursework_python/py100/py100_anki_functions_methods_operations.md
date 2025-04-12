# Python Programming Reference for Anki

## List the arithmetic operators
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division (returns float)
- `//` Integer division (rounds down to the nearest whole number)
- `%` Modulo (remainder)
- `**` Exponentiation (no spaces around this operator in Python)

## List the assignment operators
- `=` Assignment
- `+=` Add and assign (can mutate mutable objects)
- `-=` Subtract and assign
- `*=` Multiply and assign
- `/=` Divide and assign
- `//=` Integer divide and assign
- `%=` Modulo and assign
- `**=` Exponentiate and assign

## List the comparison operators
- `==` Equal to (compares values)
- `!=` Not equal to
- `<` Less than (strings compare lexicographically)
- `<=` Less than or equal to
- `>` Greater than
- `>=` Greater than or equal to
- `is` Identity comparison (compares memory addresses)
- `is not` Negated identity comparison

## List the logical operators
- `and` Logical AND (short-circuits if first operand is falsy)
- `or` Logical OR (short-circuits if first operand is truthy)
- `not` Logical NOT (unary operator)

## List the membership operators
- `in` Membership test (returns Boolean)
- `not in` Negated membership test (returns Boolean)

## List the type conversion functions
- `int()` Convert to integer
- `float()` Convert to float
- `str()` Convert to string
- `bool()` Convert to boolean
- `list()` Convert to list
- `tuple()` Convert to tuple
- `set()` Convert to set
- `dict()` Convert to dictionary
- `frozenset()` Convert to frozenset

## List the I/O functions
- `print()` Print objects to console
- `input()` Read input from user

## List the collection/sequence functions
- `len()` Return length of object
- `range()` Create sequence of numbers
- `sorted()` Return sorted list
- `reversed()` Return reversed iterator
- `enumerate()` Return index, value pairs
- `zip()` Combine multiple iterables
- `min()` Return minimum value
- `max()` Return maximum value
- `sum()` Sum of all elements
- `any()` True if any element is truthy
- `all()` True if all elements are truthy

## List the type inspection functions
- `type()` Return the type of an object
- `isinstance()` Check if object is of a type
- `id()` Return identity of an object
- `dir()` List attributes of object
- `help()` Interactive help

## List the string character functions
- `ord()` Unicode code point for character
- `chr()` Character from Unicode code point
- `repr()` Return string representation

## List the string methods for case conversion
- `upper()` Convert to uppercase
- `lower()` Convert to lowercase
- `casefold()` More aggressive lowercase
- `capitalize()` Capitalize first letter
- `title()` Capitalize all words
- `swapcase()` Swap case of all characters

## List the string methods for whitespace handling
- `strip()` Remove leading/trailing whitespace
- `lstrip()` Remove leading whitespace
- `rstrip()` Remove trailing whitespace

## List the string methods for splitting and combining
- `split()` Split string into list
- `splitlines()` Split by line breaks
- `join()` Join items with string

## List the string methods for searching
- `find()` Find substring (return index)
- `rfind()` Find substring from right
- `replace()` Replace substring
- `startswith()` Check if starts with
- `endswith()` Check if ends with

## List the string methods for character classification
- `isalpha()` Check if all alphabetic
- `isdigit()` Check if all digits
- `isalnum()` Check if alphanumeric
- `isspace()` Check if all whitespace
- `islower()` Check if all lowercase
- `isupper()` Check if all uppercase

## List the list methods that modify the list
- `append()` Add item to end
- `extend()` Add multiple items
- `insert()` Insert at position
- `remove()` Remove first occurrence
- `pop()` Remove and return item
- `clear()` Remove all items
- `sort()` Sort in place
- `reverse()` Reverse in place

## List the list methods that don't modify the list
- `index()` Return first index of value
- `count()` Count occurrences
- `copy()` Create shallow copy

## List the dictionary methods
- `keys()` Return view of keys
- `values()` Return view of values
- `items()` Return view of key-value pairs
- `get()` Get value with default
- `pop()` Remove and return item
- `popitem()` Remove and return last item
- `clear()` Remove all items
- `update()` Update with another dict
- `copy()` Create shallow copy

## List the set methods that modify the set
- `add()` Add element
- `remove()` Remove element (error if missing)
- `discard()` Remove if present
- `pop()` Remove and return arbitrary element
- `clear()` Remove all elements
- `update()` Update with union
- `intersection_update()` Update with intersection
- `difference_update()` Update with difference
- `symmetric_difference_update()` Update with symmetric difference

## List the set methods that don't modify the set
- `union()` Return union
- `intersection()` Return intersection
- `difference()` Return difference
- `symmetric_difference()` Return symmetric difference
- `issubset()` Test if subset
- `issuperset()` Test if superset
- `isdisjoint()` Test if no common elements
- `copy()` Create shallow copy

## List the control flow statements
- `if`/`elif`/`else` Conditional execution
- `while` Loop while condition is true
- `for` Loop over iterable
- `break` Exit loop
- `continue` Skip to next iteration
- `pass` Do nothing
- `match`/`case` Pattern matching (Python 3.10+)

## List the comprehension types
- List comprehension Create list from iterable
- Dictionary comprehension Create dict from iterable
- Set comprehension Create set from iterable

## List the module import statements
- `import` Import a module
- `from ... import` Import specific items
- `import ... as` Import with alias

## List the special statements
- `global` Access global variable
- `nonlocal` Access variable in outer function

## What is the purpose of the print() function?
- Displays output to the console
- Arguments: Any number of objects to print
- Optional arguments:
  - `sep`: Separator between values (default: space)
  - `end`: String appended after the last value (default: newline)
- Return value: None
- Not mutating

## What is the purpose of the input() function?
- Reads a line from standard input
- Arguments: Optional prompt string to display
- Return value: The input string (without trailing newline)
- Not mutating
- Example: `name = input("What's your name? ")`

## What is the purpose of the int() function?
- Converts a value to an integer
- Arguments: 
  - Value to convert (string or number)
  - Optional base for string conversion (default: 10)
- Return value: The integer value
- Raises ValueError if the conversion fails
- Not mutating

## What is the purpose of the float() function?
- Converts a value to a floating-point number
- Arguments: Value to convert (string or number)
- Return value: The floating-point value
- Raises ValueError if the conversion fails
- Not mutating

## What is the purpose of the str() function?
- Converts a value to a string
- Arguments: Value to convert (any object)
- Return value: String representation of the value
- Not mutating
- Always succeeds (never raises exceptions)

## What is the purpose of the bool() function?
- Converts a value to a Boolean
- Arguments: Value to convert (any object)
- Return value: True or False (based on truthiness)
- Not mutating
- Falsy values: False, None, 0, empty collections, empty strings

## What is the purpose of the list() function?
- Creates a list from an iterable
- Arguments: Optional iterable to convert
- Return value: A new list
- Not mutating (but creates a shallow copy)
- Example: `list('abc')` → `['a', 'b', 'c']`

## What is the purpose of the tuple() function?
- Creates a tuple from an iterable
- Arguments: Optional iterable to convert
- Return value: A new tuple
- Not mutating (creates a shallow copy)
- Example: `tuple([1, 2, 3])` → `(1, 2, 3)`

## What is the purpose of the set() function?
- Creates a set from an iterable
- Arguments: Optional iterable to convert
- Return value: A new set with unique elements
- Not mutating (creates a shallow copy)
- Example: `set([1, 2, 2, 3])` → `{1, 2, 3}`

## What is the purpose of the dict() function?
- Creates a dictionary from an iterable of key-value pairs
- Arguments: Optional iterable of pairs or keyword arguments
- Return value: A new dictionary
- Not mutating (creates a shallow copy)
- Example: `dict([('a', 1), ('b', 2)])` → `{'a': 1, 'b': 2}`

## What is the purpose of the len() function?
- Returns the number of items in a collection
- Arguments: Collection object (string, list, tuple, dict, set, etc.)
- Return value: Integer length
- Not mutating
- Example: `len('hello')` → `5`

## What is the purpose of the range() function?
- Creates a sequence of integers
- Arguments: 
  - stop (if only one argument)
  - start, stop (if two arguments)
  - start, stop, step (if three arguments)
- Return value: A range object (lazy sequence)
- Not mutating
- Examples: 
  - `range(5)` → `0, 1, 2, 3, 4`
  - `range(2, 7)` → `2, 3, 4, 5, 6`
  - `range(1, 10, 2)` → `1, 3, 5, 7, 9`

## What is the purpose of the sorted() function?
- Returns a new sorted list from an iterable
- Arguments: 
  - Iterable to sort
  - Optional keyword arguments:
    - `key`: Function to determine sort key
    - `reverse`: Whether to sort in descending order
- Return value: A new sorted list
- Not mutating
- Example: `sorted([3, 1, 2])` → `[1, 2, 3]`

## What is the purpose of the min() function?
- Returns the smallest item in an iterable
- Arguments:
  - Either an iterable or multiple arguments
  - Optional keyword argument `key` (function to compute comparison key)
- Return value: The smallest item
- Not mutating
- Examples: 
  - `min([3, 1, 4])` → `1`
  - `min(3, 1, 4)` → `1`

## What is the purpose of the max() function?
- Returns the largest item in an iterable
- Arguments:
  - Either an iterable or multiple arguments
  - Optional keyword argument `key` (function to compute comparison key)
- Return value: The largest item
- Not mutating
- Examples: 
  - `max([3, 1, 4])` → `4`
  - `max(3, 1, 4)` → `4`

## What is the purpose of the any() function?
- Returns True if any element in iterable is truthy
- Arguments: Iterable
- Return value: Boolean
- Not mutating
- Example: `any([False, True, False])` → `True`

## What is the purpose of the all() function?
- Returns True if all elements in iterable are truthy
- Arguments: Iterable
- Return value: Boolean
- Not mutating
- Example: `all([True, True, True])` → `True`

## What is the purpose of the sum() function?
- Returns the sum of elements in an iterable
- Arguments: 
  - Iterable of numbers
  - Optional start value (default: 0)
- Return value: Sum of elements
- Not mutating
- Example: `sum([1, 2, 3])` → `6`

## What is the purpose of the zip() function?
- Creates an iterator of tuples from multiple iterables
- Arguments: Two or more iterables
- Return value: A zip object (iterator of tuples)
- Not mutating
- Example: `list(zip([1, 2], ['a', 'b']))` → `[(1, 'a'), (2, 'b')]`
- Stops when the shortest iterable is exhausted

## What is the purpose of the enumerate() function?
- Creates an iterator of (index, value) pairs
- Arguments: 
  - Iterable
  - Optional start index (default: 0)
- Return value: An enumerate object
- Not mutating
- Example: `list(enumerate(['a', 'b']))` → `[(0, 'a'), (1, 'b')]`

## What is the purpose of the type() function?
- Returns the type of an object
- Arguments: Object to check
- Return value: The type object
- Not mutating
- Example: `type(42)` → `<class 'int'>`

## What is the purpose of the id() function?
- Returns the identity (memory address) of an object
- Arguments: Object
- Return value: Unique integer identifier
- Not mutating
- Used to check if two variables reference the same object

## What is the purpose of the ord() function?
- Returns the Unicode code point for a character
- Arguments: Single character string
- Return value: Integer code point
- Not mutating
- Example: `ord('A')` → `65`

## What is the purpose of the chr() function?
- Returns the character for a Unicode code point
- Arguments: Integer code point
- Return value: String of one character
- Not mutating
- Example: `chr(65)` → `'A'`

## What is the purpose of the str.upper() method?
- Converts a string to uppercase
- Arguments: None
- Return value: New string in uppercase
- Not mutating (strings are immutable)
- Example: `'hello'.upper()` → `'HELLO'`

## What is the purpose of the str.lower() method?
- Converts a string to lowercase
- Arguments: None
- Return value: New string in lowercase
- Not mutating (strings are immutable)
- Example: `'HELLO'.lower()` → `'hello'`

## What is the purpose of the str.casefold() method?
- More aggressive form of lowercase, for caseless matching
- Arguments: None
- Return value: New "casefolded" string
- Not mutating (strings are immutable)
- Example: `'ß'.casefold()` → `'ss'` (German)

## What is the purpose of the str.strip() method?
- Removes leading and trailing whitespace or specified characters
- Arguments: Optional characters to remove (default: whitespace)
- Return value: New string with characters removed
- Not mutating (strings are immutable)
- Example: `'  hello  '.strip()` → `'hello'`

## What is the purpose of the str.split() method?
- Splits a string into a list of substrings
- Arguments: 
  - Optional separator (default: whitespace)
  - Optional maximum number of splits
- Return value: List of substrings
- Not mutating (strings are immutable)
- Example: `'a,b,c'.split(',')` → `['a', 'b', 'c']`

## What is the purpose of the str.join() method?
- Joins an iterable of strings with the string as separator
- Arguments: Iterable of strings
- Return value: Single concatenated string
- Not mutating (strings are immutable)
- Example: `','.join(['a', 'b', 'c'])` → `'a,b,c'`

## What is the purpose of the str.find() method?
- Finds the first occurrence of a substring
- Arguments:
  - Substring to find
  - Optional start position
  - Optional end position
- Return value: Index of substring or -1 if not found
- Not mutating (strings are immutable)
- Example: `'hello'.find('e')` → `1`

## What is the purpose of the str.rfind() method?
- Finds the last occurrence of a substring (searches right to left)
- Arguments:
  - Substring to find
  - Optional start position
  - Optional end position
- Return value: Index of substring or -1 if not found
- Not mutating (strings are immutable)
- Example: `'hello'.rfind('l')` → `3`

## What is the purpose of the str.replace() method?
- Replaces occurrences of a substring
- Arguments:
  - Old substring
  - New substring
  - Optional maximum replacements
- Return value: New string with replacements
- Not mutating (strings are immutable)
- Example: `'hello'.replace('l', 'x')` → `'hexxo'`

## What is the purpose of the str.startswith() method?
- Checks if string starts with a prefix
- Arguments:
  - Prefix string or tuple of strings
  - Optional start position
  - Optional end position
- Return value: Boolean
- Not mutating (strings are immutable)
- Example: `'hello'.startswith('he')` → `True`

## What is the purpose of the str.endswith() method?
- Checks if string ends with a suffix
- Arguments:
  - Suffix string or tuple of strings
  - Optional start position
  - Optional end position
- Return value: Boolean
- Not mutating (strings are immutable)
- Example: `'hello'.endswith('lo')` → `True`

## What is the purpose of the list.append() method?
- Adds an item to the end of a list
- Arguments: Item to add
- Return value: None
- Mutates the list
- Example: `lst.append(4)` mutates lst by adding 4 to the end

## What is the purpose of the list.extend() method?
- Adds all items from an iterable to the end of a list
- Arguments: Iterable containing items to add
- Return value: None
- Mutates the list
- Example: `lst.extend([4, 5])` adds each item from [4, 5] to lst

## What is the purpose of the list.insert() method?
- Inserts an item at a specific position
- Arguments:
  - Index to insert at
  - Item to insert
- Return value: None
- Mutates the list
- Example: `lst.insert(0, 'x')` adds 'x' at the beginning of lst

## What is the purpose of the list.remove() method?
- Removes the first occurrence of a value
- Arguments: Value to remove
- Return value: None
- Mutates the list
- Raises ValueError if the value is not in the list
- Example: `lst.remove('x')` removes the first 'x' from lst

## What is the purpose of the list.pop() method?
- Removes and returns an item at a specific position
- Arguments: Optional index (default: last item)
- Return value: The removed item
- Mutates the list
- Raises IndexError if list is empty or index is out of range
- Example: `lst.pop()` removes and returns the last item

## What is the purpose of the list.sort() method?
- Sorts the list in place
- Arguments: Optional keyword arguments:
  - `key`: Function to compute comparison key
  - `reverse`: Whether to sort in descending order
- Return value: None
- Mutates the list
- Example: `lst.sort()` sorts lst in place

## What is the purpose of the list.reverse() method?
- Reverses the elements of the list in place
- Arguments: None
- Return value: None
- Mutates the list
- Example: `lst.reverse()` reverses the order of items in lst

## What is the purpose of the dict.keys() method?
- Returns a view of all keys in the dictionary
- Arguments: None
- Return value: A dict_keys view object
- Not mutating, but view is dynamic (reflects changes to dict)
- Example: `dict.keys()` returns all keys

## What is the purpose of the dict.values() method?
- Returns a view of all values in the dictionary
- Arguments: None
- Return value: A dict_values view object
- Not mutating, but view is dynamic (reflects changes to dict)
- Example: `dict.values()` returns all values

## What is the purpose of the dict.items() method?
- Returns a view of all key-value pairs in the dictionary
- Arguments: None
- Return value: A dict_items view object (tuples of key, value)
- Not mutating, but view is dynamic (reflects changes to dict)
- Example: `dict.items()` returns all (key, value) pairs

## What is the purpose of the dict.get() method?
- Gets the value for a key with a default if key doesn't exist
- Arguments:
  - Key to look up
  - Optional default value (default: None)
- Return value: Value for key or default
- Not mutating
- Example: `dict.get('key', 'default')` returns the value for 'key' or 'default'

## What is the purpose of the set.add() method?
- Adds an element to the set
- Arguments: Element to add
- Return value: None
- Mutates the set
- Example: `s.add('x')` adds 'x' to the set s

## What is the purpose of the set.remove() method?
- Removes an element from the set
- Arguments: Element to remove
- Return value: None
- Mutates the set
- Raises KeyError if element is not in the set
- Example: `s.remove('x')` removes 'x' from the set s

## What is the purpose of the set.discard() method?
- Removes an element from the set if present
- Arguments: Element to remove
- Return value: None
- Mutates the set
- Does not raise an error if the element is not present
- Example: `s.discard('x')` removes 'x' from the set s if present

## What is the purpose of the copy.copy() function?
- Creates a shallow copy of an object
- Arguments: Object to copy
- Return value: A new shallow copy
- Not mutating
- Requires import: `import copy`
- Only duplicates the top-level container, not nested objects

## What is the purpose of the copy.deepcopy() function?
- Creates a deep copy of an object
- Arguments: Object to copy
- Return value: A new deep copy
- Not mutating
- Requires import: `import copy`
- Recursively duplicates the object and all nested objects

## How do the `is` and `==` operators differ?
- `is` compares identity (memory addresses)
- `==` compares value equality
- `a is b` returns True if a and b reference the same object
- `a == b` returns True if a and b have the same value
- Example: `[1, 2, 3] == [1, 2, 3]` is True, but `[1, 2, 3] is [1, 2, 3]` is False

## How do augmented assignment operators work with mutable vs. immutable objects?
- With immutable objects (int, float, str, tuple): creates a new object
- With mutable objects (list, dict, set): modifies the existing object
- For example: `x += y` with lists is equivalent to `x.extend(y)`
- For strings: `s += 'abc'` creates a new string since strings are immutable

## What are the falsy values in Python?
- `False`
- `None`
- Zero of any numeric type: `0`, `0.0`, `0j`
- Empty sequences: `''`, `()`, `[]`, `{}`
- Empty sets: `set()`, `frozenset()`
- Range with length zero: `range(0)`
- All other values are truthy

## How does short-circuit evaluation work with logical operators?
- `and` returns the first falsy operand, or the last operand if all are truthy
- `or` returns the first truthy operand, or the last operand if all are falsy
- Evaluation stops as soon as the result is determined
- Examples:
  - `False and print('Hello')` → `False` (print never executes)
  - `True or print('Hello')` → `True` (print never executes)

## What is the difference between shallow and deep copies?
- Shallow copy: duplicates the container but references the same nested objects
- Deep copy: recursively duplicates all nested objects
- Shallow copies are created by constructor functions like `list()`, `dict()`
- Deep copies require the `copy.deepcopy()` function
- Example: For `lst = [[1, 2], 3]`, a shallow copy shares the inner list

## How does string slicing work?
- Syntax: `string[start:stop:step]`
- All parameters are optional: `string[:]` creates a full copy
- Negative indices count from the end: `-1` is the last character
- Out of range indices are handled gracefully (no error)
- Examples:
  - `'hello'[1:4]` → `'ell'`
  - `'hello'[::-1]` → `'olleh'` (reverses string)
  - `'hello'[::2]` → `'hlo'` (every second character)

## How do list comprehensions work?
- Creates a new list by applying an expression to each item in an iterable
- Syntax: `[expression for item in iterable if condition]`
- The `if condition` part is optional
- Examples:
  - `[x*2 for x in range(5)]` → `[0, 2, 4, 6, 8]`
  - `[x for x in range(10) if x % 2 == 0]` → `[0, 2, 4, 6, 8]`

## How do dictionary comprehensions work?
- Creates a new dictionary by applying expressions to each item in an iterable
- Syntax: `{key_expr: value_expr for item in iterable if condition}`
- The `if condition` part is optional
- Examples:
  - `{x: x**2 for x in range(5)}` → `{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}`
  - `{x: x**2 for x in range(10) if x % 2 == 0}` → `{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}`

## How do set comprehensions work?
- Creates a new set by applying an expression to each item in an iterable
- Syntax: `{expression for item in iterable if condition}`
- The `if condition` part is optional
- Examples:
  - `{x**2 for x in range(5)}` → `{0, 1, 4, 9, 16}`
  - `{x for x in range(10) if x % 2 == 0}` → `{0, 2, 4, 6, 8}`

## What is the difference between `global` and `nonlocal` statements?
- `global` declares that a variable refers to a global variable
- `nonlocal` declares that a variable refers to a variable in an enclosing (but not global) scope
- `global` can create new global variables if they don't exist
- `nonlocal` requires that the variable already exists in an enclosing scope
- Both prevent Python from creating a new local variable when assigning to the variable
