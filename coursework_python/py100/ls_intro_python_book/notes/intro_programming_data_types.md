# Intro to Programming - Data Types

## Data Types Overview

- Everything with a value in Python is an **object**
- Each object has an associated **data type** or **type** with a corresponding **class**
- Terms *object/value* and *class/data type/type* can be used interchangeably

### Data Type Categories

| Data Type | Class | Category | Kind | Mutable |
|-----------|-------|----------|------|---------|
| integers | `int` | numerics | Primitive | No |
| floats | `float` | numerics | Primitive | No |
| boolean | `bool` | booleans | Primitive | No |
| strings | `str` | text sequences | Primitive | No |
| ranges | `range` | sequences | Non-primitive | No |
| tuples | `tuple` | sequences | Non-primitive | No |
| lists | `list` | sequences | Non-primitive | **Yes** |
| dictionaries | `dict` | mappings | Non-primitive | **Yes** |
| sets | `set` | sets | Non-primitive | **Yes** |
| frozen sets | `frozenset` | sets | Non-primitive | No |
| functions | `function` | functions | Non-primitive | **Yes** |
| `NoneType` | `NoneType` | nulls | -- | No |

- First 4 types are Python's **primitive** types (fundamental data types)
- Sequences, mappings, and sets are **collection** types
- **Mutable** types can be altered after creation; **immutable** types cannot

## Literals

- Direct representation of values in code:
  ```python
  'Hello, world!'   # str literal
  3.141592          # float literal
  True              # bool literal
  {'a': 1, 'b': 2}  # dict literal
  [1, 2, 3]         # list literal
  (4, 5, 6)         # tuple literal
  {7, 8, 9}         # set literal
  ```
- Some objects require constructors:
  ```python
  range(10)         # Range of numbers: 0-9
  range(1, 11)      # Range of numbers: 1-10
  set()             # Empty set
  frozenset([1, 2]) # Frozen set of values: 1 and 2
  ```

## Numeric Values

### Integers (`int`)
- Whole numbers without fractional parts: `1`, `2`, `-3`
- Can use underscores for readability: `131_587_465_014_410_491`
- No pre-defined size limit (can be as large as memory allows)

### Floating Point (`float`)
- Numbers with decimal points: `1.0`, `3.14159`
- Can use underscores for readability: `131_587_465.014_410_491`
- Can use scientific notation: `3.14e+20`, `3.14e-20`
- Has precision and size limitations

## Variables and Assignment

- Variables are names that identify values
- Created by **initializing** them with a value
- Example: `pi = 3.141592653589793`
- **Assignment** syntax: `foo = 'abc'`
- **Initialization**: First assignment to a variable
- **Reassignment**: Changing an already initialized variable

## Boolean Values

- Only two values: `True` and `False`
- Represent binary states: true/false, on/off, yes/no
- Can sometimes act like numeric values (but shouldn't be used that way)
- Used extensively with comparison operators

## Text Sequences (Strings)

- Sequences of Unicode characters
- String literals can use:
  - Single quotes: `'Hello'`
  - Double quotes: `"He's pining for the fjords!"`
  - Triple quotes: `'''Multi-line'''` or `"""Multi-line"""`
- Escape characters with backslash: `\'`, `\"`
- Access characters with indexing: `my_str[0]`, `my_str[-1]`
- Raw strings: `r"C:\path\to\file"` (ignores escapes)
- f-strings: `f'5 plus 5 equals {5 + 5}.'` (for string interpolation)

## Functions

- Chunks of reusable code designed to perform an action
- In Python, functions have their own data type
- Will be covered in more detail later

## None

- Represents absence of a value
- Lone instance of `NoneType` class
- Used to indicate missing, unset, or unavailable data

## Sequences

### Lists and Tuples
- Ordered collections that can contain any objects
- Lists use square brackets `[]`, are mutable: `[1, 'xyz', True]`
- Tuples use parentheses `()`, are immutable: `('xyz', [2, 3, 4], 1, True)`
- Access elements by index: `my_list[0]`
- Multi-line format:
  ```python
  [
      "Monty Python's Flying Circus",
      ('Eric Idle', 'John Cleese'),
  ]
  ```
- One-element tuple needs trailing comma: `(1,)`

### Ranges
- Sequence of integers between endpoints
- Created with `range()` function:
  - `range(5)`: 0, 1, 2, 3, 4
  - `range(5, 10)`: 5, 6, 7, 8, 9
  - `range(1, 10, 2)`: 1, 3, 5, 7, 9
  - `range(0, -5, -1)`: 0, -1, -2, -3, -4
- Memory-optimized (lazy sequences)
- Access elements with indexing: `my_range[0]`

## Mappings (Dictionaries)

- Unordered collection of key-value pairs
- Created with curly braces: `{'dog': 'barks', 'cat': 'meows'}`
- Access values by keys: `my_dict['cat']`
- Keys must be immutable and hashable (strings, numbers, tuples, frozensets)
- As of Python 3.7, insertion order is preserved
- Element access: `my_dict['dog']`
- `get` method protects against KeyError: `my_dict.get('lizard', 'N/A')`

## Sets

- Unordered collection of unique objects
- Created with curly braces: `{1, 2, 3}`
- No duplicates allowed
- Empty set must use constructor: `set()`
- Members must be hashable (immutable)
- Set operations: unions, intersections, etc.
- Two types:
  - Regular sets (`set`): Mutable
  - Frozen sets (`frozenset`): Immutable, created with constructor
