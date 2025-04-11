# Intro to Programming - Flow Control

## Conditionals

- Control the path data takes through a program
- Use combinations of `if`, `elif`, and `else` with comparison operators
- Basic syntax:
  ```python
  value = int(input('Enter a number: '))
  
  if value == 3:
      print('value is 3')
  else:
      print('value is NOT 3')
  ```
- Multiple conditions with `elif`:
  ```python
  if value == 3:
      print('value is 3')
  elif value == 4:
      print('value is 4')
  else:
      print('value is NOT 3 or 4')
  ```
- `if` blocks can contain multiple statements:
  ```python
  if value == 3:
      print('value is 3')
      print('value is an odd number')
      print('value is a prime number')
  ```
- Use `pass` for empty blocks:
  ```python
  if value == 9:
      pass  # We don't care about 9
  ```
- All statements in a block must be indented consistently

## Comparisons

### Equality (`==`)
- Returns `True` when operands have equal values:
  ```python
  print(5 == 5)                 # True
  print(5 == 4)                 # False
  print('abc' == 'abc')         # True
  print('abc' == 'abcd')        # False
  print(5 == '5')               # False
  print([1, 2, 3] == [1, 2, 3]) # True
  ```
- For case-insensitive string comparison:
  ```python
  print('abc'.lower() == 'aBc'.lower())  # True
  print('abc'.upper() == 'aBc'.upper())  # True
  print('abc'.casefold() == 'aBc'.casefold())  # True
  ```
- `casefold()` preferred for international text

### Inequality (`!=`)
- Returns `True` when operands are not equal:
  ```python
  print(5 != 5)             # False
  print(5 != 4)             # True
  print('abc' != 'abc')     # False
  print('abc' != 'aBc')     # True
  ```

### Less Than (`<`) and Less Than or Equal To (`<=`)
- `<` returns `True` when left operand is less than right:
  ```python
  print(4 < 5)              # True
  print(5 < 4)              # False
  print(5 < 5)              # False
  ```
- `<=` also returns `True` when operands are equal:
  ```python
  print(4 <= 5)             # True
  print(5 <= 4)             # False
  print(5 <= 5)             # True
  ```
- String comparison is character-by-character:
  ```python
  print('42' < '402')       # False
  print('42' < '420')       # True
  ```

### Greater Than (`>`) and Greater Than or Equal To (`>=`)
- `>` returns `True` when left operand is greater than right:
  ```python
  print(4 > 5)              # False
  print(5 > 4)              # True
  print(5 > 5)              # False
  ```
- `>=` also returns `True` when operands are equal:
  ```python
  print(4 >= 5)             # False
  print(5 >= 4)             # True
  print(5 >= 5)             # True
  ```

## Logical Operators

### `not` Operator
- Unary operator that negates a Boolean value:
  ```python
  print(not True)           # False
  print(not False)          # True
  print(not(4 == 4))        # False
  print(not(4 != 4))        # True
  ```

### `and` and `or` Operators
- Truth table:

| A | B | A and B | A or B |
|---|---|---------|--------|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

- Examples:
  ```python
  print((4 == 4) and (7 == 7))  # True
  print((4 == 4) and (7 == 3))  # False
  
  print((4 == 4) or (7 == 7))   # True
  print((4 == 4) or (7 == 3))   # True
  print((4 == 9) or (7 == 3))   # False
  ```

## Short Circuits

- `and` and `or` use **short circuit evaluation**
- `and`: If first operand is `False`, second isn't evaluated
- `or`: If first operand is `True`, second isn't evaluated
- Example:
  ```python
  # If item is not red, is_portable() won't be called
  is_red(item) and is_portable(item)
  
  # If item is green, has_wheels() won't be called
  is_green(item) or has_wheels(item)
  ```

## Truthiness

- All values can be evaluated as either **truthy** or **falsy**
- Falsy values:
  - `False`, `None`
  - Zero values: `0`, `0.0`
  - Empty collections: `''`, `[]`, `()`, `{}`, `set()`, `range(0)`
- Everything else is truthy
- Examples:
  ```python
  value = 5  # 5 is truthy
  if value:
      print(f'{value} is truthy')
  else:
      print(f'{value} is falsy')
  ```

### Truthiness and Short-Circuit Evaluation

- Logical operators return the last evaluated value, not just `True`/`False`:
  ```python
  print(3 and 'foo')   # 'foo'
  print(0 and 'foo')   # 0
  print(3 or 'foo')    # 3
  print(0 or 'foo')    # 'foo'
  ```
- Converting non-Boolean values to Boolean:
  ```python
  is_ok = bool(foo or bar)  # True if either is truthy
  ```

## Logical Operator Precedence

From highest to lowest:
1. Comparison operators (`==`, `!=`, `<=`, `<`, `>`, `>=`)
2. `not`
3. `and`
4. `or`

- Best practice: Use parentheses to control evaluation order
- Avoid mixing `and` and `or` without parentheses

## match/case Statement

- Introduced in Python 3.10
- Compares a single value against multiple patterns
- Basic syntax:
  ```python
  value = 5
  
  match value:
      case 5:
          print('value is 5')
      case 6:
          print('value is 6')
      case _:  # default case
          print('value is neither 5 nor 6')
  ```
- Match multiple values with `|`:
  ```python
  match value:
      case 1 | 2 | 3 | 4:
          print('value is < 5')
      case 5 | 6:
          print('value is 5 or 6')
      case _:
          print('value is not 1, 2, 3, 4, 5, or 6')
  ```
- Can be rewritten as `if`/`elif`/`else` statements

## Ternary Expressions

- Concise way to choose between two values
- Syntax: `value1 if condition else value2`
- Examples:
  ```python
  print("Triangle" if shape.sides() == 3 else "Square")
  print('N/A' if value == None else value)
  ```
- Use judiciously for readability
- Keep simple and on a single line
