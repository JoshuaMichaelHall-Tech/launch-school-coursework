# Collections and Iteration - Intro

## Collection Types

Python has numerous built-in and auxiliary collection types, which contain zero or more member objects (elements). The main categories are:

### Collection Type Categories

| Type | Class | Category | Kind | Mutable |
|------|-------|----------|------|---------|
| ranges | `range` | sequences | Non-primitive | No |
| tuples | `tuple` | sequences | Non-primitive | No |
| lists | `list` | sequences | Non-primitive | **Yes** |
| dictionaries | `dict` | mappings | Non-primitive | **Yes** |
| sets | `set` | sets | Non-primitive | **Yes** |
| frozen sets | `frozenset` | sets | Non-primitive | No |
| strings | `str` | text sequences | Primitive | No |

- **Strings** are not true collections but are treated similarly to sequence collections
- Some collections are mutable (can be changed); others are immutable (cannot be changed)
- Lists and tuples differ primarily in mutability (lists mutable, tuples immutable)
- The same applies to sets (mutable) and frozen sets (immutable)

## What are Sequences?

- **Ordered** collections of objects that can be **indexed** by whole numbers
- First element is at index 0, second at index 1, etc.
- Examples:
  ```python
  letters = ['a', 'b', 'c']
  print(letters[0])         # a (first element)
  print(letters[1])         # b (second element)
  print(letters[2])         # c (third element)
  ```
- Lists and tuples are **heterogeneous** (can contain different types of objects):
  ```python
  my_list = [
      'May',
      2.99,
      {None, True, False},
      [1, 2, 3],
  ]
  ```
- Ranges are **homogenous** (contain only integers)

### Strings as Sequences

- Strings are text sequences with specific differences from standard sequences:
  1. Homogenous (all characters)
  2. Characters aren't distinct objects until referenced
  3. Characters are strings of length 1
  4. Not a true collection (characters aren't objects)
- Example:
  ```python
  letters = 'abθde'
  char = letters[2]
  print(char is letters[2])     # False (different objects)
  ```

## What are Sets?

- **Unordered** collections of unique objects (members)
- Cannot be indexed
- No defined order for objects
- No duplicate members allowed
- Two types:
  - Sets (`set`): Mutable
  - Frozen sets (`frozenset`): Immutable
- Example:
  ```python
  letters = {'a', 'b', 'c'}
  letters.add('d')
  print(letters)           # {'a', 'b', 'c', 'd'} (order may differ)
  
  frozen_letters = frozenset(letters)
  # frozen_letters.add('e')  # AttributeError: 'frozenset' has no attribute 'add'
  ```
- Sets and frozen sets are heterogeneous:
  ```python
  my_set = {
      'May',
      2.99,
      (None, True, False),  # Note: tuples, not lists
      range(5),
  }
  ```
- Duplicate members are silently ignored:
  ```python
  letters = {'a', 'b', 'c', 'b', 'a'}
  print(letters)           # {'a', 'c', 'b'}
  ```
- Order may appear consistent for simple sets but is not guaranteed:
  ```python
  numbers = { 1, 2, 37, 4, 5 }
  print(numbers)           # Order not guaranteed
  ```

## What are Mappings?

- **Unordered** collections of key/value pairs
- Accessed by keys, not indices
- Main mapping type is dictionary (`dict`)
- Dictionary characteristics:
  - Mutable
  - Keys must be unique
  - Keys must be hashable (usually immutable)
  - Values can be any object
- Example:
  ```python
  d = {'a': 1, (1, 3): 3, 1: 'x'}
  print(d['a'])            # 1
  print(d[(1, 3)])         # 3
  print(d[1])              # 'x'
  ```
- Since Python 3.7, dictionaries maintain insertion order
- Keys/values can be added, modified, or deleted:
  ```python
  d = {'a': 1, (1, 3): 3, 1: 'x'}
  del d['a']               # Delete key/value pair
  d['a'] = 42              # Add new key/value pair
  ```

## Sequence Constructors

### String Constructor
- `str()` or `str(something)` creates strings
- Examples:
  ```python
  str()                    # '' (empty string)
  str('abc')               # 'abc'
  str(42)                  # '42'
  str(3.141592)            # '3.141592'
  str(False)               # 'False'
  str(None)                # 'None'
  str([1, 2, 3])           # '[1,

# Collections and Iteration - Intro (Continued)

## Sequence Constructors (Continued)

### String Constructor
- `str()` or `str(something)` creates strings
- Examples:
  ```python
  str()                    # '' (empty string)
  str('abc')               # 'abc'
  str(42)                  # '42'
  str(3.141592)            # '3.141592'
  str(False)               # 'False'
  str(None)                # 'None'
  str([1, 2, 3])           # '[1, 2, 3]'
  ```

### Range Constructor
- Three forms:
  1. `range(start, stop, step)`: Generates sequence from `start` to `stop - 1` with increment of `step`
     ```python
     r = range(5, 12, 2)
     print(list(r))            # [5, 7, 9, 11]
     
     r = range(12, 8, -1)
     print(list(r))            # [12, 11, 10, 9]
     ```
  
  2. `range(start, stop)`: Same as `range(start, stop, 1)`
  
  3. `range(stop)`: Same as `range(0, stop, 1)`
  
- Ranges are **lazy sequences** (elements created only when needed)
- Convert to list or tuple to see all elements: `list(r)`, `tuple(r)`

### List, Tuple, Set, and Frozen Set Constructors
- Common forms:
  - `list()` or `list(iterable)`
  - `tuple()` or `tuple(iterable)`
  - `set()` or `set(iterable)`
  - `frozenset()` or `frozenset(iterable)`
- Empty collection forms: `list()`, `tuple()`, `set()`, `frozenset()`
- Conversions between collections:
  ```python
  my_str = 'Python'
  
  my_list = list(my_str)    # ['P', 'y', 't', 'h', 'o', 'n']
  my_tuple = tuple(my_list) # ('P', 'y', 't', 'h', 'o', 'n')
  my_set = set(my_tuple)    # {'t', 'o', 'n', 'h', 'P', 'y'}
  ```
- Create duplicates with constructors:
  ```python
  my_list = [5, 12, 2]
  another_list = list(my_list)
  
  print(my_list == another_list)  # True
  print(my_list is another_list)  # False
  ```
- Constructors perform shallow copies:
  ```python
  my_list = [[1, 2, 3], [4, 5, 6]]
  another_list = list(my_list)
  
  print(my_list[0] is another_list[0])  # True
  ```

## Nested Collections

- Collections can contain other collections
- Example:
  ```python
  nested_list = [
      {'foo': 42, 'bar': [1, 2, 3], 'qux': None},
      {'Kim', ('Leslie', 'Les'), ('Pete', 'Peter')},
      (4, 5, (1, 2, 3), 6, 7),
      ['a', 'b', 'cde', -3.141592],
  ]
  ```
- Limitations:
  - Can't nest mutable collections inside sets:
    ```python
    # These cause errors:
    my_set = {1, 2, 3, [4, 5]}      # TypeError: unhashable type: 'list'
    my_set = {1, 2, 3, {4, 5}}      # TypeError: unhashable type: 'set'
    
    # This works:
    my_set = {1, 2, 3, frozenset([4, 5])}
    ```
  - Mutable collections can be nested inside tuples:
    ```python
    my_tuple = (1, 2, 3, [4, 5], {6, 7}, {'x': 'a dict'})
    ```
- Practical example - deck of cards:
  ```python
  deck = [
      { 'suit': 'Clubs', 'value': '2' },
      { 'suit': 'Clubs', 'value': '3' },
      # ...more cards...
      { 'suit': 'Spades', 'value': 'King' },
      { 'suit': 'Spades', 'value': 'Ace' },
  ]
  
  print(f"{deck[49]['value']} of {deck[49]['suit']}") # Queen of Spades
  ```
- Accessing nested elements:
  ```python
  nested_seq = [
      [1, 2, [3, 4, (5, 6, 7, 8)]],
      [9, [10, (11,)]],
      [12, 13, [14, 15, (16, 17)]],
      [18, [19, 20, (21, 22)]],
  ]
  
  print(nested_seq[1])          # [9, [10, (11,)]]
  print(nested_seq[3][0])       # 18
  print(nested_seq[0][2][2])    # (5, 6, 7, 8)
  print(nested_seq[2][2][2][1]) # 17
  ```

## Comparing Collections

- Equal collections must meet all criteria:
  - Same type (list, tuple, set, etc.)
  - Same number of elements
  - For sequences, corresponding elements must be equal
  - For sets, same members (order doesn't matter)
  - For mappings, same key/value pairs (order doesn't matter)
- Examples:
  ```python
  print([2, 3] == [2, 3])    # True
  print([2, 3] == [3, 2])    # False (different sequence)
  print([2, 3] == [2])       # False (different lengths)
  print([2, 3] == (2, 3))    # False (different types)
  print({2, 3} == {3, 2})    # True (same members)
  
  dict1 = {'a': 1, 'b': 2}
  dict2 = {'b': 2, 'a': 1}
  print(dict1 == dict2)      # True (same pairs)
  ```
- Inequality with `!=` works as expected
- Sequences also support ordered comparisons (`<`, `<=`, `>`, `>=`)
