# Intro to Programming - Basic Operations

## Shared Functionality

- Python data types share many operations
- Most features are remarkably consistent across types:
  - Compare almost any pair of objects for equality
  - Determine length of any collection with `len()`
  - Convert nearly any object to string form
  - Iterate over different collections with the same syntax

## Type Categories

- **Built-in types**: Part of core Python, available in every program
- **Standard types**: Available through module imports
- **Non-standard types**: Custom or third-party types

## Arithmetic Operations

All numeric types support these operations:

| Operator | Operation |
|----------|-----------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division (always returns float) |
| `//` | Integer division |
| `%` | Modulo (remainder) |
| `**` | Exponentiation |

Examples:
```python
38 + 4        # 42
38 - 4        # 34
38 * 4        # 152
16 / 4        # 4.0 (always a float)
16 // 3       # 5 (rounds down)
15 % 3        # 0 (no remainder)
16**3         # 4096 (16 to the power of 3)
```

### Floating Point Imprecision

- Floating point can have precision issues:
  ```python
  print(0.1 + 0.2 == 0.3)  # False
  ```
- Solutions:
  - Use `math.isclose`: 
    ```python
    import math
    math.isclose(0.1 + 0.2, 0.3)  # True
    ```
  - Use `decimal.Decimal`:
    ```python
    from decimal import Decimal
    Decimal('0.1') + Decimal('0.2') == Decimal('0.3')  # True
    ```

## Equality Comparison

- `==` compares values for equality (returns `True` or `False`)
- `!=` checks for inequality (inverse of `==`)
- Works with almost all data types
- Examples:
  ```python
  42 == 42        # True
  42 == 43        # False
  'foo' == 'foo'  # True
  'FOO' == 'foo'  # False (case matters)
  1 == 1.0        # True (numeric types can be compared)
  ```

## Ordered Comparisons

- `<` less than
- `<=` less than or equal to
- `>` greater than
- `>=` greater than or equal to
- Examples:
  ```python
  42 < 41           # False
  42 < 42           # False
  42 <= 42          # True
  42 < 43           # True
  ```

### String Comparison

- Strings compared lexicographically (character by character)
- Character codes determine order
- Examples:
  ```python
  'abcdf' < 'abcef'  # True
  'abc' < 'abcdef'   # True
  'A' < 'a'          # True (uppercase before lowercase)
  '3' < '24'         # False (compares first character only)
  ```

## Logical Operators

### `not` Operator
- Unary operator that negates Boolean values
- Examples:
  ```python
  not True           # False
  not False          # True
  not(4 == 4)        # False
  ```

### `and` and `or` Operators
- Binary operators that combine Boolean values
- Truth table:

| A | B | A and B | A or B |
|---|---|---------|--------|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

- Examples:
  ```python
  (4 == 4) and (7 == 7)  # True
  (4 == 4) and (7 == 3)  # False
  (4 == 4) or (7 == 3)   # True
  (4 == 9) or (7 == 3)   # False
  ```

### Short Circuit Evaluation
- `and` and `or` evaluate only as much as needed
- `and`: If first operand is false, second is not evaluated
- `or`: If first operand is true, second is not evaluated

## Truthiness

- All values can be evaluated as either **truthy** or **falsy**
- Falsy values:
  - `False`, `None`
  - Zero values: `0`, `0.0`, etc.
  - Empty strings: `''`
  - Empty collections: `[]`, `()`, `{}`, `set()`, `range(0)`
- Everything else is truthy
- Logical operators return the last evaluated operand, not necessarily a Boolean:
  ```python
  3 and 'foo'   # 'foo'
  0 and 'foo'   # 0
  3 or 'foo'    # 3
  0 or 'foo'    # 'foo'
  ```

## Logical Operator Precedence

From highest to lowest:
1. Comparison operators (`==`, `!=`, `<=`, `<`, `>`, `>=`)
2. `not`
3. `and`
4. `or`

Best practice: Use parentheses to control evaluation order

## String Operations

### String Concatenation
- `+` operator joins strings
- `*` operator repeats strings
- Examples:
  ```python
  'foo' + 'bar'     # 'foobar'
  '1' + '2'         # '12' (not 3)
  'abc' * 3         # 'abcabcabc'
  3 * 'abc'         # 'abcabcabc'
  ```

## Coercion

### Strings to Numbers
- `int()` and `float()` convert strings to numbers
  ```python
  int('5')           # 5
  float('3.141592')  # 3.141592
  ```

### Numbers to Strings
- `str()` converts numbers to strings
  ```python
  str(5)             # '5'
  str(3.141592)      # '3.141592'
  ```

### Implicit Coercion
- Some conversions happen automatically
- Example: `print()` implicitly coerces to string
- Mixing number types causes implicit coercion:
  - `int` + `float` → `float`
  - `int` + `Decimal` → `Decimal`
  - `int` + `Fraction` → `Fraction`
- Booleans can be coerced to numbers (`True` = 1, `False` = 0)

## Determining Types

- `type()` function returns an object's class
  ```python
  type(1)            # <class 'int'>
  type('abc')        # <class 'str'>
  type(True)         # <class 'bool'>
  ```
- Access just the name with `__name__` property:
  ```python
  type('abc').__name__   # 'str'
  ```
- Use with `is` operator:
  ```python
  type('abc') is str     # True
  ```

## String Representations

- `str()` function returns human-readable representation
- `repr()` function returns developer representation
- Example:
  ```python
  my_str = 'abc'
  print(str(my_str))   # abc
  print(repr(my_str))  # 'abc' (note the quotes)
  ```

## Collection and String Lengths

- `len()` function returns number of elements
- Examples:
  ```python
  len('Launch School')       # 13 (string)
  len(range(5, 15))          # 10 (range)
  len([1, 2, 3])             # 3 (list)
  len((4, 5, 6, 7))          # 4 (tuple)
  len({'foo': 42, 'bar': 7}) # 2 (dict)
  len({1, 2, 3})             # 3 (set)
  ```

## Indexing and Key Access

- Sequences use numeric indexes starting at 0
  ```python
  seq = ('a', 'b', 'c')
  print(seq[0])  # a (first element)
  print(seq[1])  # b (second element)
  ```
- Out-of-range indexes cause IndexError
- Dictionaries use keys instead of indexes
  ```python
  my_dict = {'a': 1, 'b': 2}
  print(my_dict['a'])    # 1
  ```
- Mutating lists:
  ```python
  seq = ['a', 'b', 'c']
  seq[1] = 'B'
  print(seq)      # ['a', 'B', 'c']
  ```

## Expressions and Statements

- **Expression**: Combines values, variables, operators to produce a value
  - Examples: `5`, `x + y`, `'x' == 'x'`, `len([1, 2, 3])`
- **Statement**: Instruction that performs an action
  - Examples: Assignments, control flow, function definitions
- Expressions are part of statements
- Some expressions can be standalone but are still expressions

## Expression Evaluation

- Python evaluates most expressions from left to right
- Operator precedence determines evaluation order
- Use parentheses to explicitly control evaluation order
  ```python
  ((4 * 5) - 1) + (2 * 3)    # 25
  (4 * ((5 - 1) + 2)) * 3    # 72
  ```

## Output vs. Return Values

- Output: Displaying information (usually with `print()`)
- Return values: Results of functions/expressions
- REPL shows both outputs and return values
- Running programs only show explicit outputs
