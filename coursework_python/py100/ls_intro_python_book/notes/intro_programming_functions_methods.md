# Intro to Programming - Functions and Methods

## Purpose of Functions

- Reduce repetitive code
- Enable code reuse
- Improve readability and maintenance
- Organize code into logical blocks

## Calling Functions

- Using a function means **calling**, **invoking**, **executing**, or **running** it
- Invoke by writing function name followed by parentheses: `hello()`
- Functions may return values that can be used or ignored:
  ```python
  def hello():
      print('Hello')
      return True
  
  hello()                # Call function, ignore return value
  print(hello())         # Print the return value
  ```
- Functions often take **arguments**:
  ```python
  print('hello', 'good-bye', 'farewell')
  ```
- Multiple arguments are separated by commas
- Long argument lists can be spread over multiple lines:
  ```python
  print(
      'hello',
      'good-bye',
      'farewell',
      'adios',
  )
  ```

## Built-in Functions

- Functions always available in Python (about 70 as of Python 3.11.4)
- Examples:
  - `float`, `int` (type conversion)
  - `str`, `list`, `tuple`, `set`, `frozenset` (constructors)
  - `input`, `print` (I/O functions)
  - `type`, `len` (information functions)

### `min` and `max`

- Determine minimum and maximum values in collections:
  ```python
  print(min(-10, 5, 12, 0, -20))    # -20
  print(max(-10, 5, 12, 0, -20))    # 12
  
  print(min('over', 'the', 'moon')) # 'moon'
  print(max('over', 'the', 'moon')) # 'the'
  ```
- Can use with a single iterable:
  ```python
  my_tuple = ('i', 'tawt', 'i', 'taw', 'a', 'puddy', 'tat')
  print(min(my_tuple))  # 'a'
  print(max(my_tuple))  # 'tawt'
  ```

### `ord` and `chr`

- `ord`: Returns Unicode code point for a character:
  ```python
  print(ord('a'))      # 97
  print(ord('A'))      # 65
  ```
- `chr`: Converts code point to character:
  ```python
  print(chr(97))       # a
  print(chr(65))       # A
  ```

### Truthy and Falsy Values

- **Falsy** values:
  - `False`, `None`
  - Zero values: `0`, `0.0`
  - Empty collections: `''`, `[]`, `()`, `{}`, `set()`, `range(0)`
- All other values are **truthy**

### `any` and `all`

- `any`: Returns `True` if any element is truthy:
  ```python
  collection1 = [False, False, False]
  print(any(collection1))  # False
  
  collection2 = (False, True, False)
  print(any(collection2))  # True
  ```
- `all`: Returns `True` if all elements are truthy:
  ```python
  collection3 = {True, True, True}
  print(all(collection3))  # True
  
  print(all([]))           # True (vacuously true)
  ```
- Useful with comprehensions:
  ```python
  numbers = [2, 5, 8, 10, 13]
  print(any([number % 2 == 0 for number in numbers]))  # True
  print(all([number % 2 == 0 for number in numbers]))  # False
  ```

### REPL Helper Functions

#### `id` Function
- Returns unique identity integer for an object:
  ```python
  x = 5
  y = 5
  print(id(x) == id(y))  # True (due to interning)
  
  s = 'Hello, world!'
  t = 'Hello, world!'
  print(id(s) == id(t))  # May be False
  ```

#### `dir` Function
- Lists names in current scope or object attributes:
  ```python
  dir()  # Names in current scope
  dir(5) # Attributes of integer 5
  ```
- Can be combined with `sorted`:
  ```python
  sorted(dir(range(1)))
  ```

#### `help` Function
- Shows documentation:
  ```python
  help()             # General help
  help(str)          # Help on string class
  help(list.append)  # Help on list.append method
  ```

## Creating Functions

- Use `def` keyword followed by name, parentheses, colon:
  ```python
  def say():
      print('Hi!')
  ```
- Call the function to execute it:
  ```python
  say()  # Prints: Hi!
  ```
- Example with execution flow:
  ```python
  def say():
      print('Output from say')
  
  print('First')
  say()
  print('Last')
  # Output:
  # First
  # Output from say
  # Last
  ```
- Functions can have **docstrings**:
  ```python
  def say():
      """
      The say function prints "Hi!"
      """
      print('Hi!')
  ```

## Scope

- **Scope**: Where you can use an identifier
- Python identifiers have **function scope**
- Variables initialized inside a function are local to that function:
  ```python
  def well_howdy(who):
      greeting = 'Howdy'
      print(f'{greeting}, {who}')
  
  well_howdy('Angie')
  print(greeting)  # NameError: greeting not defined
  ```
- Variables from outer scope are accessible but not assignable:
  ```python
  greeting = 'Salutations'
  
  def well_howdy(who):
      print(f'{greeting}, {who}')
  
  well_howdy('Angie')  # Salutations, Angie
  ```
- **Variable shadowing**: Local variables hide (shadow) outer scope variables:
  ```python
  greeting = 'Salutations'
  
  def well_howdy(who):
      greeting = 'Howdy'     # Local variable
      print(f'{greeting}, {who}')
  
  well_howdy('Angie')       # Howdy, Angie
  print(greeting)           # Salutations
  ```

## Namespaces

- **Namespace**: Mapping of identifiers to objects
- Python looks in namespaces in this order:
  1. Local namespace (local scope)
  2. Enclosing namespaces (outer scopes)
  3. Global namespace (global scope)
  4. Built-in namespace

## Arguments & Parameters

- **Parameters**: Placeholders in function definition
- **Arguments**: Values passed when calling the function
- Example:
  ```python
  def say(text):           # text is a parameter
      print(text)
  
  say('hello')             # 'hello' is an argument
  ```
- Parameters are local variables in the function
- Function names and parameters are both considered variable names

### Multiple Parameters

- Functions can take multiple parameters:
  ```python
  def add(left, right):
      sum = left + right
      return sum
  
  sum = add(3, 6)          # 9
  ```
- Python validates argument count:
  ```python
  add(3)  # TypeError: missing 1 required positional argument
  ```

## Return Values

- Functions return values using the `return` statement
- Without explicit return, functions return `None` (implicit return)
- Examples:
  ```python
  def add(a, b):
      return a + b
  
  result = add(2, 3)      # result = 5
  ```
- **Predicates**: Functions that return Boolean values:
  ```python
  def is_digit(char):
      if char >= '0' and char <= '9':
          return True
      return False
  ```

## Default Parameters

- Provide default values for parameters:
  ```python
  def say(text='hello'):
      print(text + '!')
  
  say('Howdy')            # Howdy!
  say()                   # hello!
  ```
- After a default parameter, all subsequent parameters must have defaults
- Cannot skip parameters with defaults:
  ```python
  def say(msg1, msg2, msg3='dummy message', msg4='omitted message'):
      print(msg1)
      print(msg2)
      print(msg3)
      print(msg4)
      
  say('a', 'b')  # Uses defaults for msg3 and msg4
  ```

## Functions vs. Methods

- Functions are invoked as: `function_name(obj, ...)`
- Methods are invoked as: `obj.method_name(...)`
- Methods belong to a class and require an object of that class
- All methods are functions, but not all functions are methods
- Example:
  ```python
  my_str = 'abc-123-def'
  print(my_str.upper())    # ABC-123-DEF
  
  import math
  print(math.sqrt(5))      # 2.23606797749979
  ```
- `math.sqrt` is a function, not a method, despite the dot notation

## Mutating the Caller

- Some methods change the object used to call them:
  ```python
  odd_numbers = [1, 3, 5, 7, 9]
  odd_numbers.pop()
  print(odd_numbers)       # [1, 3, 5, 7]
  ```
- Functions can mutate their arguments:
  ```python
  def add_new_number(my_list):
      my_list.append(9)    # Mutates the argument
  
  numbers = [1, 2, 3, 4, 5]
  add_new_number(numbers)
  print(numbers)           # [1, 2, 3, 4, 5, 9]
  ```
- Better practice: Return a new object instead of mutating:
  ```python
  def add_new_number(my_list):
      return my_list + [9]
  
  numbers = [1, 2, 3, 4, 5]
  new_numbers = add_new_number(numbers)
  print(new_numbers)       # [1, 2, 3, 4, 5, 9]
  print(numbers)           # [1, 2, 3, 4, 5]
  ```
