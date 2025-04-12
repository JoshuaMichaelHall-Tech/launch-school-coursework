# Python Functions, Methods & Operators Reference Chart

## Arithmetic Operators
| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3` → `8` |
| `-` | Subtraction | `5 - 3` → `2` |
| `*` | Multiplication | `5 * 3` → `15` |
| `/` | Division (returns float) | `5 / 2` → `2.5` |
| `//` | Integer division | `5 // 2` → `2` |
| `%` | Modulo (remainder) | `5 % 2` → `1` |
| `**` | Exponentiation | `5 ** 2` → `25` |

## Assignment Operators
| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Assignment | `x = 5` |
| `+=` | Add and assign | `x += 3` (same as `x = x + 3`) |
| `-=` | Subtract and assign | `x -= 3` (same as `x = x - 3`) |
| `*=` | Multiply and assign | `x *= 3` (same as `x = x * 3`) |
| `/=` | Divide and assign | `x /= 3` (same as `x = x / 3`) |
| `//=` | Integer divide and assign | `x //= 3` (same as `x = x // 3`) |
| `%=` | Modulo and assign | `x %= 3` (same as `x = x % 3`) |
| `**=` | Exponentiate and assign | `x **= 3` (same as `x = x ** 3`) |

## Comparison Operators
| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal to | `5 == 5` → `True` |
| `!=` | Not equal to | `5 != 3` → `True` |
| `<` | Less than | `3 < 5` → `True` |
| `<=` | Less than or equal to | `3 <= 3` → `True` |
| `>` | Greater than | `5 > 3` → `True` |
| `>=` | Greater than or equal to | `5 >= 5` → `True` |
| `is` | Identity comparison | `a is b` (True if a and b reference the same object) |
| `is not` | Negated identity comparison | `a is not b` |

## Logical Operators
| Operator | Description | Example |
|----------|-------------|---------|
| `and` | Logical AND | `True and False` → `False` |
| `or` | Logical OR | `True or False` → `True` |
| `not` | Logical NOT | `not True` → `False` |

## Membership Operators
| Operator | Description | Example |
|----------|-------------|---------|
| `in` | Membership test | `'a' in 'abc'` → `True` |
| `not in` | Negated membership test | `'d' not in 'abc'` → `True` |

## Built-in Functions

### Type Conversion Functions
| Function | Description | Example |
|----------|-------------|---------|
| `int()` | Convert to integer | `int('42')` → `42` |
| `float()` | Convert to float | `float('3.14')` → `3.14` |
| `str()` | Convert to string | `str(42)` → `'42'` |
| `bool()` | Convert to boolean | `bool(0)` → `False` |
| `list()` | Convert to list | `list('abc')` → `['a', 'b', 'c']` |
| `tuple()` | Convert to tuple | `tuple([1, 2, 3])` → `(1, 2, 3)` |
| `set()` | Convert to set | `set([1, 2, 2, 3])` → `{1, 2, 3}` |
| `dict()` | Convert to dictionary | `dict([('a', 1), ('b', 2)])` → `{'a': 1, 'b': 2}` |
| `frozenset()` | Convert to frozenset | `frozenset({1, 2, 3})` → `frozenset({1, 2, 3})` |

### I/O Functions
| Function | Description | Example |
|----------|-------------|---------|
| `print()` | Print objects to console | `print("Hello")` |
| `input()` | Read input from user | `name = input("Enter name: ")` |

### Collection/Sequence Functions
| Function | Description | Example |
|----------|-------------|---------|
| `len()` | Return length of object | `len([1, 2, 3])` → `3` |
| `range()` | Create sequence of numbers | `range(3)` → `0, 1, 2` |
| `sorted()` | Return sorted list | `sorted([3, 1, 2])` → `[1, 2, 3]` |
| `reversed()` | Return reversed iterator | `reversed([1, 2, 3])` → `<iterator>` |
| `enumerate()` | Return index, value pairs | `enumerate(['a', 'b'])` → `(0, 'a'), (1, 'b')` |
| `zip()` | Combine multiple iterables | `zip([1, 2], ['a', 'b'])` → `(1, 'a'), (2, 'b')` |
| `min()` | Return minimum value | `min([3, 1, 2])` → `1` |
| `max()` | Return maximum value | `max([3, 1, 2])` → `3` |
| `sum()` | Sum of all elements | `sum([1, 2, 3])` → `6` |
| `any()` | True if any element is truthy | `any([False, True, False])` → `True` |
| `all()` | True if all elements are truthy | `all([True, True, True])` → `True` |

### Type Inspection Functions
| Function | Description | Example |
|----------|-------------|---------|
| `type()` | Return the type of an object | `type(42)` → `<class 'int'>` |
| `isinstance()` | Check if object is of a type | `isinstance(42, int)` → `True` |
| `id()` | Return identity of an object | `id(x)` → unique integer |
| `dir()` | List attributes of object | `dir([])` → list of list methods |
| `help()` | Interactive help | `help(str)` → help on strings |

### String Functions
| Function | Description | Example |
|----------|-------------|---------|
| `ord()` | Unicode code point for character | `ord('A')` → `65` |
| `chr()` | Character from Unicode code point | `chr(65)` → `'A'` |
| `repr()` | Return string representation | `repr('test')` → `"'test'"` |

## String Methods
| Method | Description | Example |
|--------|-------------|---------|
| `upper()` | Convert to uppercase | `'abc'.upper()` → `'ABC'` |
| `lower()` | Convert to lowercase | `'ABC'.lower()` → `'abc'` |
| `casefold()` | More aggressive lowercase | `'ß'.casefold()` → `'ss'` |
| `capitalize()` | Capitalize first letter | `'hello'.capitalize()` → `'Hello'` |
| `title()` | Capitalize all words | `'hello world'.title()` → `'Hello World'` |
| `swapcase()` | Swap case of all characters | `'Hello'.swapcase()` → `'hELLO'` |
| `strip()` | Remove leading/trailing whitespace | `' abc '.strip()` → `'abc'` |
| `lstrip()` | Remove leading whitespace | `' abc'.lstrip()` → `'abc'` |
| `rstrip()` | Remove trailing whitespace | `'abc '.rstrip()` → `'abc'` |
| `split()` | Split string into list | `'a b c'.split()` → `['a', 'b', 'c']` |
| `splitlines()` | Split by line breaks | `'a\nb'.splitlines()` → `['a', 'b']` |
| `join()` | Join items with string | `','.join(['a', 'b'])` → `'a,b'` |
| `find()` | Find substring (return index) | `'abc'.find('b')` → `1` |
| `rfind()` | Find substring from right | `'abcbc'.rfind('b')` → `3` |
| `replace()` | Replace substring | `'abc'.replace('b', 'X')` → `'aXc'` |
| `startswith()` | Check if starts with | `'abc'.startswith('a')` → `True` |
| `endswith()` | Check if ends with | `'abc'.endswith('c')` → `True` |
| `isalpha()` | Check if all alphabetic | `'abc'.isalpha()` → `True` |
| `isdigit()` | Check if all digits | `'123'.isdigit()` → `True` |
| `isalnum()` | Check if alphanumeric | `'abc123'.isalnum()` → `True` |
| `isspace()` | Check if all whitespace | `'  '.isspace()` → `True` |
| `islower()` | Check if all lowercase | `'abc'.islower()` → `True` |
| `isupper()` | Check if all uppercase | `'ABC'.isupper()` → `True` |

## List Methods
| Method | Description | Example |
|--------|-------------|---------|
| `append()` | Add item to end | `lst.append(4)` |
| `extend()` | Add multiple items | `lst.extend([4, 5])` |
| `insert()` | Insert at position | `lst.insert(0, 'x')` |
| `remove()` | Remove first occurrence | `lst.remove('x')` |
| `pop()` | Remove and return item | `lst.pop()` or `lst.pop(0)` |
| `clear()` | Remove all items | `lst.clear()` |
| `index()` | Return first index of value | `lst.index('x')` |
| `count()` | Count occurrences | `lst.count('x')` |
| `sort()` | Sort in place | `lst.sort()` |
| `reverse()` | Reverse in place | `lst.reverse()` |
| `copy()` | Create shallow copy | `new_lst = lst.copy()` |

## Dictionary Methods
| Method | Description | Example |
|--------|-------------|---------|
| `keys()` | Return view of keys | `dict.keys()` |
| `values()` | Return view of values | `dict.values()` |
| `items()` | Return view of key-value pairs | `dict.items()` |
| `get()` | Get value with default | `dict.get('key', 'default')` |
| `pop()` | Remove and return item | `dict.pop('key')` |
| `popitem()` | Remove and return last item | `dict.popitem()` |
| `clear()` | Remove all items | `dict.clear()` |
| `update()` | Update with another dict | `dict.update({'a': 1})` |
| `copy()` | Create shallow copy | `new_dict = dict.copy()` |

## Set Methods
| Method | Description | Example |
|--------|-------------|---------|
| `add()` | Add element | `s.add('x')` |
| `remove()` | Remove element (error if missing) | `s.remove('x')` |
| `discard()` | Remove if present | `s.discard('x')` |
| `pop()` | Remove and return arbitrary element | `s.pop()` |
| `clear()` | Remove all elements | `s.clear()` |
| `union()` | Return union | `s1.union(s2)` or `s1 | s2` |
| `intersection()` | Return intersection | `s1.intersection(s2)` or `s1 & s2` |
| `difference()` | Return difference | `s1.difference(s2)` or `s1 - s2` |
| `symmetric_difference()` | Return symmetric difference | `s1.symmetric_difference(s2)` or `s1 ^ s2` |
| `update()` | Update with union | `s1.update(s2)` |
| `intersection_update()` | Update with intersection | `s1.intersection_update(s2)` |
| `difference_update()` | Update with difference | `s1.difference_update(s2)` |
| `symmetric_difference_update()` | Update with symmetric difference | `s1.symmetric_difference_update(s2)` |
| `issubset()` | Test if subset | `s1.issubset(s2)` |
| `issuperset()` | Test if superset | `s1.issuperset(s2)` |
| `isdisjoint()` | Test if no common elements | `s1.isdisjoint(s2)` |
| `copy()` | Create shallow copy | `new_set = s.copy()` |

## Control Flow Statements
| Statement | Description | Example |
|-----------|-------------|---------|
| `if`/`elif`/`else` | Conditional execution | `if x > 0: pass` |
| `while` | Loop while condition is true | `while x > 0: x -= 1` |
| `for` | Loop over iterable | `for i in range(5): pass` |
| `break` | Exit loop | `if x == 0: break` |
| `continue` | Skip to next iteration | `if x < 0: continue` |
| `pass` | Do nothing | `if x: pass` |
| `match`/`case` | Pattern matching (Python 3.10+) | `match value: case 1: pass` |

## Comprehensions
| Type | Description | Example |
|------|-------------|---------|
| List | Create list from iterable | `[x*2 for x in range(5)]` |
| Dictionary | Create dict from iterable | `{x: x*2 for x in range(5)}` |
| Set | Create set from iterable | `{x*2 for x in range(5)}` |

## Modules
| Module | Description | Example Functions/Constants |
|--------|-------------|----------------------------|
| `math` | Mathematical functions | `sqrt()`, `pi`, `cos()` |
| `datetime` | Date and time handling | `datetime.now()`, `strftime()` |
| `random` | Random number generation | `randrange()`, `choice()` |
| `copy` | Shallow and deep copy | `copy()`, `deepcopy()` |

## Special Statements
| Statement | Description | Example |
|-----------|-------------|---------|
| `global` | Access global variable | `global x` |
| `nonlocal` | Access variable in outer function | `nonlocal x` |
| `import` | Import a module | `import math` |
| `from ... import` | Import specific items | `from math import sqrt` |
| `import ... as` | Import with alias | `import math as m` |
