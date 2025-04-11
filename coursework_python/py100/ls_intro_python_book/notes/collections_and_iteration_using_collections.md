# Collections and Iteration - Using Collections

## Indexing

- Access elements of sequences using whole number indices
- Python uses zero-based indexing (first element is at position 0)
- Examples:
  ```python
  seq = ('a', 'b', 'c')
  print(seq[0])  # a (1st element)
  print(seq[1])  # b (2nd element)
  print(seq[2])  # c (3rd element)
  ```
- Out-of-range indexes cause `IndexError`
- Last element is at index `len(sequence) - 1`
- Negative indices count from the end:
  ```python
  seq = ('a', 'b', 'c')
  print(seq[-1])  # c (last element)
  print(seq[-2])  # b (next to last element)
  print(seq[-3])  # a (2nd to last element)
  ```
- Mutable sequences allow indexing for assignment:
  ```python
  seq = ['a', 'b', 'c']
  seq[1] = 'B'
  print(seq)      # ['a', 'B', 'c']
  ```

## Slicing

- Extract multiple consecutive elements from sequences
- Basic syntax: `seq[start:stop]` (from `start` to `stop - 1`)
- Can use negative indices
- Extended syntax: `seq[start:stop:step]` (every "step-th" element)
- Examples:
  ```python
  seq = 'abcdefghi'
  print(seq[3:7])       # defg
  print(seq[-6:-2])     # defg
  print(seq[2:8:2])     # ceg
  print(seq[3:3])       # '' (empty)
  print(seq[:])         # abcdefghi (full copy)
  print(seq[::-1])      # ihgfedcba (reversed)
  ```
- Works with all sequence types:
  ```python
  seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  print(seq[3:7])       # [4, 5, 6, 7]
  print(seq[-6:-2])     # [5, 6, 7, 8]
  ```
- Slicing creates shallow copies:
  ```python
  seq = [[1, 2], [3, 4]]
  seq_dup = seq[:]
  print(seq[0] is seq_dup[0])   # True
  ```

## Key-Based Access

- Mappings use keys instead of numeric indices
- Similar syntax: `my_dict[key]`
- Keys can be any hashable object (often strings):
  ```python
  my_dict = {
      'a': 'abc',
      37: 'def',
      (5, 6, 7): 'ghi',
      frozenset([1, 2]): 'jkl',
  }
  
  print(my_dict['a'])                # abc
  print(my_dict[37])                 # def
  print(my_dict[(5, 6, 7)])          # ghi
  ```
- Non-existent keys cause `KeyError`
- `dict.get` method is safer (returns None or default for missing keys):
  ```python
  print(my_dict.get('nothing'))           # None
  print(my_dict.get('nothing', 'N/A'))    # N/A
  ```
- Key-based assignment:
  ```python
  my_dict['a'] = 'ABC'
  my_dict['xyz'] = 'Hey there!'  # Adds new key/value pair
  ```
- Keys must be immutable:
  ```python
  my_dict[[1, 2, 3]] = 'Hey there!'  # TypeError: unhashable type
  ```

## Common Collection Operations

### Non-Mutating Operations

#### Collection Membership

- `in` operator checks if item is in collection
- `not in` is the inverse of `in`
- Examples:
  ```python
  seq = [4, 'abcdef', (True, False, None)]
  print(4 in seq)                     # True
  print('abcdef' in seq)              # True
  print('cde' in seq[1])              # True
  print('acde' in seq[1])             # False
  print((True, False, None) in seq)   # True
  ```

#### Minimum and Maximum Members

- `min()` and `max()` return minimum and maximum members
- Elements must be comparable with `<` and `>`
- Examples:
  ```python
  my_set1 = {1, 4, -9, 16, 25, -36, -63, -1}
  print(min(my_set1), max(my_set1))     # -63 25
  ```
- Usually can't mix types:
  ```python
  my_set = {1, 4, '-9', 16, '25', -36}  # TypeError
  ```
- Can take multiple arguments instead of collection:
  ```python
  print(min(3, 5, -1), max(3, 5, -1))  # -1 5
  ```

#### Summation

- `sum()` function adds all numbers in collection:
  ```python
  numbers = (1, 1, 2, 3, 5, 8, 13, 21, 34)
  print(sum(numbers))                    # 88
  ```
- Only works with numeric values, not strings

#### Locating Indices and Counting

- `index()` returns first matching element's position:
  ```python
  names = ['Karl', 'Grace', 'Clare', 'Victor']
  print(names.index('Clare'))   # 2
  print(names.index('Trevor'))  # ValueError if not found
  ```
- `count()` returns number of occurrences:
  ```python
  numbers = [1, 3, 6, 5, 4, 10, 1, 5, 4, 4, 5, 4]
  print(numbers.count(1))       # 2
  print(numbers.count(4))       # 4
  ```

#### Merging Collections with `zip()`

- Combines multiple iterables into tuples
- Returns lazy sequence of tuples
- Each tuple contains one element from each iterable
- Examples:
  ```python
  iterable1 = [1, 2, 3]
  iterable2 = ('Kim', 'Leslie', 'Bertie')
  iterable3 = [None, True, False]
  
  zipped_iterables = zip(iterable1, iterable2, iterable3)
  print(list(zipped_iterables))
  # [(1, 'Kim', None), (2, 'Leslie', True), (3, 'Bertie', False)]
  ```
- With unequal lengths, stops after shortest iterable:
  ```python
  result = zip(range(5, 10),    # length is 5
               range(1, 3),     # length is 2 (shortest)
               range(3, 7))     # length is 4
  print(list(result))  # [(5, 1, 3), (6, 2, 4)]
  ```
- Can enforce equal lengths with `strict=True`
- Iterators can only be consumed once

#### Operations on Dictionaries

- `dict.keys()`: Returns view of dictionary keys
- `dict.values()`: Returns view of dictionary values
- `dict.items()`: Returns view of key/value pairs as tuples
- Examples:
  ```python
  people_phones = {
      'Chris': '111-2222',
      'Pete':  '333-4444',
      'Clare': '555-6666',
  }
  
  print(people_phones.keys())    # dict_keys(['Chris', 'Pete', 'Clare'])
  print(people_phones.values())  # dict_values(['111-2222', '333-4444', '555-6666'])
  print(people_phones.items())   # dict_items([('Chris', '111-2222'), ...])
  ```
- Views are dynamic (reflect changes to dictionary):
  ```python
  keys = people_phones.keys()
  people_phones['Max'] = '123-4567'  # Add new entry
  print(keys)  # dict_keys(['Chris', 'Pete', 'Clare', 'Max'])
  ```

### Operations for Mutable Sequences

#### Adding Elements

- `append()`: Adds single element to end
  ```python
  numbers = [1, 2]
  numbers.append(10)      # [1, 2, 10]
  ```
- `insert()`: Inserts element at specific position
  ```python
  numbers = [1, 2]
  numbers.insert(0, 8)    # [8, 1, 2]
  numbers.insert(2, 6)    # [8, 1, 6, 2]
  ```
- `extend()`: Appends elements from iterable
  ```python
  numbers = [1, 2]
  numbers.extend([7, 8])  # [1, 2, 7, 8]
  ```

#### Removing Elements

- `remove()`: Removes first occurrence of value
  ```python
  my_list = [2, 4, 6, 8, 10]
  my_list.remove(8)       # [2, 4, 6, 10]
  ```
- `pop()`: Removes and returns element at index (or last element)
  ```python
  my_list = [2, 4, 6, 8, 10]
  print(my_list.pop(1))   # 4
  print(my_list)          # [2, 6, 8, 10]
  print(my_list.pop())    # 10 (default: last element)
  ```
- `clear()`: Removes all elements
  ```python
  my_list = [2, 4, 6, 8, 10]
  my_list.clear()         # []
  ```

### Sorting Collections

- `sorted()`: Creates sorted list from any iterable
  ```python
  names = ('Grace', 'Clare', 'Allison', 'Trevor')
  print(sorted(names))    # ['Allison', 'Clare', 'Grace', 'Trevor']
  ```
- `list.sort()`: Sorts list in-place (mutates list)
  ```python
  names = ['Grace', 'Clare', 'Allison', 'Trevor']
  names.sort()
  print(names)            # ['Allison', 'Clare', 'Grace', 'Trevor']
  ```
- Reverse sorting with `reverse=True`:
  ```python
  print(sorted(names, reverse=True))  # ['Trevor', 'Grace', 'Clare', 'Allison']
  ```
- Custom sorting with `key` function:
  ```python
  words = ['abc', 'DEF', 'xyz', '123']
  print(sorted(words, key=str.casefold))  # ['123', 'abc', 'DEF', 'xyz']
  
  numbers = ['1', '5', '100', '15']
  numbers.sort(key=int)   # ['1', '5', '15', '100']
  ```

#### Reversing Sequences

- `reversed()`: Returns reversed iterator
  ```python
  names = ('Grace', 'Clare', 'Allison', 'Trevor')
  print(tuple(reversed(names)))  # ('Trevor', 'Allison', 'Clare', 'Grace')
  ```
- `list.reverse()`: Reverses list in-place
  ```python
  names = ['Grace', 'Clare', 'Allison', 'Trevor']
  names.reverse()
  print(names)  # ['Trevor', 'Allison', 'Clare', 'Grace']
  ```

## String Operations

### Letter Case

- `str.lower()`: Converts to lowercase
- `str.upper()`: Converts to uppercase
- `str.capitalize()`: Capitalizes first character
  ```python
  print("what's up?".capitalize())  # What's up?
  print('456ABC'.capitalize())      # 456abc
  ```
- `str.title()`: Capitalizes every word
  ```python
  print("four SCORE and sEvEn".title())  # Four Score And Seven
  ```
- `str.swapcase()`: Swaps case of each letter
  ```python
  print("What's up?".swapcase())    # wHAT'S UP?
  ```

### Character Classification

- `str.isalpha()`: True if all characters are letters
- `str.isdigit()`: True if all characters are digits
- `str.isalnum()`: True if all characters are letters or digits
- `str.islower()`: True if all cased characters are lowercase
- `str.isupper()`: True if all cased characters are uppercase
- `str.isspace()`: True if all characters are whitespace

### Stripping Characters

- `str.strip()`: Removes leading/trailing whitespace
  ```python
  text = ' \t  abc def    \n\r'
  print(text.strip())     # 'abc def'
  ```
- Can specify characters to remove:
  ```python
  text = 'aaabaacccabxyzabccba'
  print(text.strip('abc'))  # xyz
  ```
- `str.lstrip()`: Removes only leading characters
- `str.rstrip()`: Removes only trailing characters

### startswith and endswith

- `str.startswith()`: True if string starts with substring
  ```python
  print('Four score'.startswith('Four'))  # True
  ```
- `str.endswith()`: True if string ends with substring
  ```python
  print('Four score'.endswith('score'))   # True
  ```
- Both accept tuples of strings:
  ```python
  print('abc def'.startswith(('abc', 'xyz')))  # True
  ```
- Both accept start/end indices:
  ```python
  print('abc def'.startswith('def', 4))   # True
  ```

### Splitting and Joining Strings

- `str.split()`: Splits string into list of words
  ```python
  text = '  Four     score and   seven years ago.   '
  print(text.split())  # ['Four', 'score', 'and', 'seven', 'years', 'ago.']
  ```
- Can specify delimiter:
  ```python
  text = 'Four<>score<:>and<>seven'
  print(text.split('<>'))  # ['Four', 'score<:>and', 'seven']
  ```
- `str.splitlines()`: Splits by line boundaries
  ```python
  text = "Line 1\nLine 2\nLine 3"
  print(text.splitlines())  # ['Line 1', 'Line 2', 'Line 3']
  ```
- `str.join()`: Concatenates collection with string as separator
  ```python
  words = ['You', 'were', 'lucky']
  print(' '.join(words))       # You were lucky
  print(','.join(words))       # You,were,lucky
  ```

### Finding Substrings

- `str.find()`: Returns index of first occurrence (or -1)
  ```python
  school = 'launch school'
  print(school.find('h'))      # 5
  print(school.find('x'))      # -1
  ```
- `str.rfind()`: Searches from right to left
  ```python
  print(school.rfind('h'))     # 9
  ```
- Both accept start/end indices:
  ```python
  text = 'abc abc def abc'
  print(text.find(' ', 4))     # 7
  ```

## Nested Collections

- Access elements through multiple levels of indexing:
  ```python
  nested_list = [
      {'foo': 42, 'bar': [1, 2, 3]},
      ('Kim', ('Leslie', 'Les')),
      (4, 5, (1, 2, 3), 6, 7),
  ]
  
  print(nested_list[0]['bar'][1])  # 2
  print(nested_list[1][1][0])      # Leslie
  ```
- Example - deck of cards:
  ```python
  deck = [
      { 'suit': 'Clubs', 'value': '2' },
      { 'suit': 'Clubs', 'value': '3' },
      # ...more cards...
  ]
  
  print(f"{deck[49]['value']} of {deck[49]['suit']}")
  ```
