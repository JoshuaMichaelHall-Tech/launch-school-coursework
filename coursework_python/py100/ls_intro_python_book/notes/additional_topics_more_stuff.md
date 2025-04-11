# Additional Topics - More Stuff

## Function Composition

- Using a function call as an argument to another function
- Return value of inner function becomes argument for outer function
- Example:
  ```python
  print(list(range(3, 17, 4)))
  # Evaluation order: range(3, 17, 4) → list(...) → print(...)
  ```
- Can chain multiple function calls:
  ```python
  def add(a, b):
    return a + b
  
  def subtract(a, b):
    return a - b
    
  def times(num1, num2):
    return num1 * num2
  
  print(times(add(20, 45), subtract(80, 10)))  # 4550
  # ((20 + 45) * (80 - 10)) = 65 * 70 = 4550
  ```
- Equivalent to:
  ```python
  total = add(20, 45)            # 65
  difference = subtract(80, 10)  # 70
  result = times(total, difference)  # 4550
  print(result)                  # 4550
  ```
- Most useful when inner functions return non-None values
- Keep nesting simple for readability

## Method Chaining

- Calling methods in sequence on an object or its return values
- Each method in the chain (except the last) must return an object with useful methods
- Example with strings:
  ```python
  tv_show = "Monty Python's Flying Circus"
  tv_show = tv_show.upper().split()
  # ['MONTY', "PYTHON'S", 'FLYING', 'CIRCUS']
  ```
- Can format over multiple lines for readability:
  ```python
  letters = 'abcdefghijklmnoqrstuvwxyz'
  
  # Note parentheses for multi-line chaining
  consonants = (letters.replace('a', '').
                       replace('e', '').
                       replace('i', '').
                       replace('o', '').
                       replace('u', ''))
  print(consonants)  # bcdfghjklmnqrstvwxyz
  ```
- Less common in Python than other languages because many methods return `None`

## Modules

- Code files that can be imported and reused in other programs
- Types of modules:
  - **Built-in modules**: Included with Python
  - **Standard library modules**: Included but must be imported
  - **Third-party modules**: Available from PyPI
  - **Custom modules**: Created by you
- Every Python file can be a module
- Primary way Python programmers reuse code

### Import Statements

- Basic import: `import module_name`
  ```python
  import math
  
  print(math.sqrt(math.pi))  # 1.7724538509055159
  ```
- Import specific names: `from module import name1, name2`
  ```python
  from math import pi, sqrt
  
  print(sqrt(pi))  # 1.7724538509055159
  ```
- Import with alias: `import module_name as alias`
  ```python
  import math as m
  
  print(m.sqrt(m.pi))  # 1.7724538509055159
  ```

## The math Module

- Provides mathematical functions and constants
- Examples:
  ```python
  import math
  print(math.sqrt(36))        # 6.0
  print(math.sqrt(2))         # 1.4142135623730951
  print(math.pi)              # 3.141592653589793
  ```
- Useful when you need mathematical operations beyond basic arithmetic

## The datetime Module

- Provides classes for manipulating dates and times
- Example - determining day of week:
  ```python
  from datetime import datetime as dt
  
  date = dt.strptime("July 16, 2022", "%B %d, %Y")
  weekday_name = date.strftime('%A')
  print(weekday_name)         # Saturday
  ```
- Format codes:
  - `%B`: Full month name (July)
  - `%d`: Day of month (16)
  - `%Y`: 4-digit year (2022)
  - `%A`: Full weekday name (Saturday)
- Handles complex date/time issues:
  - Leap years
  - Time zones
  - Daylight savings time
  - International calendar differences

## Function Definition Order

- Python reads function definitions into memory before executing them
- Functions can call other functions defined later in the file:
  ```python
  def top():
      bottom()  # This works even though bottom() is defined later
  
  def bottom():
      print('Reached the bottom')
  
  top()  # Prints: Reached the bottom
  ```
- However, you can't call functions before they're defined:
  ```python
  top()  # NameError: name 'top' is not defined
  
  def top():
      bottom()
  ```
- Best practice: Define all functions before calling any of them
- Put main program code at the bottom after all function definitions

## Nested Functions

- Functions can be defined inside other functions
- Nested functions are created and destroyed each time the outer function runs
- They are private to the outer function:
  ```python
  def foo():
      def bar():
          print('BAR')
  
      bar()  # Works
  
  foo()      # Prints: BAR
  bar()      # NameError: name 'bar' is not defined
  ```

## The global and nonlocal Statements

- By default, variables in outer scope are accessible but not assignable in inner scopes
- Assignment in a function creates a new local variable
- The `global` statement lets you use a global variable inside a function:
  ```python
  greeting = 'Salutations'
  
  def well_howdy(who):
      global greeting
      greeting = 'Howdy'  # Changes the global variable
      print(f'{greeting}, {who}')
  
  well_howdy('Angie')  # Howdy, Angie
  print(greeting)      # Howdy
  ```
- Creates global variable if it doesn't exist:
  ```python
  def set_pi():
      global pi
      pi = 3.1415
  
  set_pi()
  print(pi)  # 3.1415
  ```
- The `nonlocal` statement refers to variables in outer (non-global) functions:
  ```python
  def outer():
      def inner1():
          def inner2():
              nonlocal foo  # Refers to foo from inner1
              foo = 3
              print(f"inner2 -> {foo}")
  
          foo = 2
          inner2()
          print(f"inner1 -> {foo}")  # foo is now 3
  
      foo = 1
      inner1()
      print(f"outer -> {foo}")  # Still 1 (unchanged)
  
  outer()
  ```
- Multiple `nonlocal` statements can affect multiple levels:
  ```python
  def outer():
      def inner1():
          def inner2():
              nonlocal foo
              foo = 3
  
          nonlocal foo  # Refers to foo from outer
          foo = 2
          inner2()
  
      foo = 1
      inner1()
      print(f"outer -> {foo}")  # Now 3 (changed)
  
  outer()
  ```
- Use `global` and `nonlocal` sparingly - they often indicate poor design
- Unlike `global`, `nonlocal` requires the variable to already exist
