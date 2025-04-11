# Collections and Iteration - Loops and Iterating

## Why Loops Matter

- Most programs require code that runs repeatedly
- Loops execute a block of code while a condition is truthy
- Two main looping structures: `for` and `while`
- Other looping mechanisms: comprehensions, generators, functional loops

## while Loops

- Basic syntax: `while condition:` followed by code block
- Loop executes repeatedly while condition is truthy
- Loop must arrange to terminate (avoid infinite loops)
- Example - printing numbers 1 to 10:
  ```python
  counter = 1
  while counter <= 10:
      print(counter)
      counter += 1
  ```
- The `counter += 1` statement is crucial to avoid infinite loops

### Using while Loops with Sequences

- Common pattern: Loop through sequence elements with index
- Example - creating uppercase names:
  ```python
  names = ['Chris', 'Max', 'Karis', 'Victor']
  upper_names = []
  index = 0
  
  while index < len(names):
      upper_name = names[index].upper()
      upper_names.append(upper_name)
      index += 1
  
  print(upper_names)  # ['CHRIS', 'MAX', 'KARIS', 'VICTOR']
  ```
- Initialize variables before the loop (not inside)
- Increment index to move through sequence

## for Loops

- Specifically designed for iterating over collections
- Simpler syntax than `while` loops - no index management
- Works with any iterable (sequences, mappings, sets, strings)
- Basic syntax: `for element in collection:`
- Example - creating uppercase names:
  ```python
  names = ['Chris', 'Max', 'Karis', 'Victor']
  upper_names = []
  
  for name in names:
      upper_name = name.upper()
      upper_names.append(upper_name)
  
  print(upper_names)  # ['CHRIS', 'MAX', 'KARIS', 'VICTOR']
  ```

### for Loop with Different Collections

- Strings (character by character):
  ```python
  for char in 'Launch School':
      print(char)
  # L
  # a
  # u
  # n
  # ...
  ```
- Word by word using split:
  ```python
  for word in 'Launch School'.split():
      print(word)
  # Launch
  # School
  ```
- Sets (unordered):
  ```python
  my_set = {1000, 2000, 3000, 4000, 5000}
  for member in my_set:
      print(member)
  # Order may vary
  ```
- Dictionaries (iterates over keys by default):
  ```python
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  for key in my_dict:
      print(key)  # a, b, c
  ```
- Dictionary values:
  ```python
  for value in my_dict.values():
      print(value)  # 1, 2, 3
  ```
- Dictionary key/value pairs:
  ```python
  for key, value in my_dict.items():
      print(f'{key} = {value}')
  # a = 1
  # b = 2
  # c = 3
  ```

### Nested Loops

- Combine multiple loops with one inside another
- Example - creating a deck of cards:
  ```python
  suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
           'Jack', 'Queen', 'King', 'Ace']
  
  deck = []
  for suit in suits:
      for rank in ranks:
          card = f'{rank} of {suit}'
          deck.append(card)
  ```
- Outer loop runs once per element; inner loop runs completely for each outer loop iteration
- Nesting 3+ levels can become hard to understand
- Can mix `for` and `while` loops as needed

## Controlling Loops

### continue Statement

- Skips the rest of the current iteration and moves to the next
- Example - skipping a specific name:
  ```python
  names = ['Chris', 'Max', 'Karis', 'Victor']
  upper_names = []
  
  for name in names:
      if name == 'Max':
          continue
      
      upper_name = name.upper()
      upper_names.append(upper_name)
  
  print(upper_names)  # ['CHRIS', 'KARIS', 'VICTOR']
  ```
- Alternative using negated condition:
  ```python
  for name in names:
      if name != 'Max':
          upper_name = name.upper()
          upper_names.append(upper_name)
  ```
- `continue` helps reduce nesting and clarify intent
- Only affects the nearest enclosing loop

### break Statement

- Immediately terminates the entire loop
- Example - finding a value:
  ```python
  numbers = [3, 1, 5, 9, 2, 6, 4, 7]
  found_item = -1
  index = 0
  
  while index < len(numbers):
      if numbers[index] == 5:
          found_item = index
          break  # Stop searching once found
      
      index += 1
  
  print(found_item)  # 2
  ```
- Only terminates the nearest enclosing loop

### Emulating Do/While Loops

- Python has no built-in do/while loop
- Technique 1 - using a flag variable:
  ```python
  keep_going = True
  while keep_going:
      # main loop code here
      
      answer = input('Play again? (y/n) ')
      if answer == 'n':
          keep_going = False
  ```
- Technique 2 - using `while True` with `break`:
  ```python
  while True:
      # main loop code here
      
      answer = input('Play again? (y/n) ')
      if answer == 'n':
          break
  ```

## Simultaneous Iteration

- Iterate through multiple collections in parallel
- The `zip` function combines collections for iteration:
  ```python
  forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
  surnames = ['Camp', 'Blake', 'Flanagan', 'Short']
  
  zipped_names = zip(forenames, surnames)
  for forename, surname in zipped_names:
      print(f'{forename} {surname}')
  # Ken Camp
  # Lynn Blake
  # Pat Flanagan
  # Nancy Short
  ```
- `zip` handles collections of different lengths by stopping at the shortest

## Comprehensions

- Concise way to create collections from existing ones
- Are expressions, not statements (unlike most loops)
- Three types: list, dict, and set comprehensions

### List Comprehensions

- Syntax: `[expression for element in iterable if condition]`
- The `if condition` part is optional
- Example - creating squares:
  ```python
  squares = [number * number for number in range(5)]
  print(squares)  # [0, 1, 4, 9, 16]
  ```
- Compared to regular `for` loop:
  ```python
  squares = []
  for number in range(5):
      square = number * number
      squares.append(square)
  ```
- With selection - filtering elements:
  ```python
  multiples_of_6 = [number for number in range(20)
                    if number % 6 == 0]
  print(multiples_of_6)  # [0, 6, 12, 18]
  ```
- Combining selection and transformation:
  ```python
  even_squares = [number * number
                  for number in range(10)
                  if number % 2 == 0]
  print(even_squares)  # [0, 4, 16, 36, 64]
  ```
- With dictionaries - extracting keys:
  ```python
  cats_colors = {
      'Tess': 'brown',
      'Leo': 'orange',
      'Fluffy': 'gray',
      'Ben': 'black',
      'Kat': 'orange',
  }
  
  names = [name.upper() for name in cats_colors]
  print(names)  # ['TESS', 'LEO', 'FLUFFY', 'BEN', 'KAT']
  ```
- Multiple selection criteria:
  ```python
  names = [name.upper()
           for name in cats_colors
           if cats_colors[name] == 'orange'
           if name[0] == 'L']
  print(names)  # ['LEO']
  ```
- Multiple `for` components (nested loops):
  ```python
  deck = [f'{rank} of {suit}'
          for suit in suits
          for rank in ranks]
  ```

### Dictionary Comprehensions

- Syntax: `{key: value for element in iterable if condition}`
- Creates dictionaries instead of lists
- Example:
  ```python
  squares = {f'{number}-squared': number * number
             for number in range(1, 6)}
  print(squares)
  # {'1-squared': 1, '2-squared': 4, '3-squared': 9, ...}
  ```
- Otherwise identical to list comprehensions

### Set Comprehensions

- Syntax: `{expression for element in iterable if condition}`
- Creates sets instead of lists or dictionaries
- Example:
  ```python
  squares = {number * number for number in range(1, 6)}
  print(squares)  # {1, 4, 9, 16, 25}
  ```
- Otherwise identical to list comprehensions

### No Tuple, Range, or String Comprehensions

- No tuple comprehensions exist (immutable types can't be built incrementally)
- `(x for x in range(5))` creates a generator expression, not a tuple
- For tuples, convert list comprehension:
  ```python
  tuple_result = tuple([x for x in range(5)])
  ```
- Same for strings - use `str.join()` with list comprehension:
  ```python
  string_result = ''.join([x for x in 'hello' if x in 'aeiou'])
  ```
