# Intro to Programming - Variables

## Variables and Variable Names

- Variables are labels attached to specific values stored in memory
- They can typically be changed (reassigned) to point to different values
- Example:
  ```python
  answer = 41
  print(answer)      # 41
  
  answer = 42
  print(answer)      # 42
  ```
- Properly naming variables is one of the hardest tasks in programming
- Variable names should accurately and concisely describe the variable's data
- Variable names are a type of **identifier**

## Naming Conventions

### For Most Identifiers (variables, functions, etc.)

- Use **snake_case** formatting:
  - Lowercase letters (a-z), digits (0-9), and underscores (`_`)
  - Begin with a letter
  - Separate words with a single underscore
  - Names with special meaning begin/end with one or two underscores
  - Use only ASCII character set
- Idiomatic examples:
  - `foo`
  - `answer_to_ultimate_question`
  - `eighty_seven`
  - `index_2`

### For Constants

- Use **SCREAMING_SNAKE_CASE** formatting:
  - Uppercase letters (A-Z), digits (0-9), and underscores (`_`)
  - Begin with a letter
  - Separate words with a single underscore
- Idiomatic examples:
  - `FOO`
  - `ANSWER_TO_ULTIMATE_QUESTION`
  - `EIGHTY_SEVEN`
- Note: Python doesn't enforce constants; this convention is advisory only

### For Class Names

- Use **PascalCase** (or CamelCase) formatting:
  - Uppercase and lowercase letters (A-Z, a-z) and digits (0-9)
  - Begin with uppercase letter
  - Capitalize each word
- Idiomatic examples:
  - `Foo`
  - `UltimateQuestion`
  - `FourLeggedPets`

### Invalid Identifiers

- Cannot use punctuation, special characters, or whitespace
- Cannot start with a digit
- Cannot use Python's reserved words (`if`, `def`, `while`, etc.)
- Examples of illegal names:
  - `pass` (reserved word)
  - `3xy` (starts with digit)
  - `ultimate-question` (hyphen)
  - `one two three` (whitespace)
  - `is_lowercase?` (punctuation)

## Creating and Reassigning Variables

- **Initialize** (create) variables by assigning them a value:
  ```python
  forename = 'Clare'      # initialization
  ```
- **Reassign** by giving a new value to an existing variable:
  ```python
  forename = 'Clare'      # initialization
  forename = 'Victor'     # reassignment
  ```
- Assignment can be described in two equivalent ways:
  1. The variable `foo` is assigned the value of `bar`
  2. The value of `bar` is assigned to the variable `foo`

### How Initialization and Reassignment Work

- When initializing, Python:
  1. Creates the value in memory
  2. Creates a variable spot in memory
  3. Stores the value's memory address in the variable
- When reassigning, Python:
  1. Creates the new value in memory
  2. Updates the variable to store the new value's address
  3. Breaks connection with original value

## Creating Constants

- Created the same way as variables: `PINING_FOR = 'fjords'`
- Use SCREAMING_SNAKE_CASE naming convention
- Usually defined in global scope at top of file
- Python doesn't enforce constancy; it's a convention for programmers

## Expressions and Assignment

- Right side of `=` can be any expression:
  ```python
  left_side = 5
  right_side = 32
  total = left_side + right_side  # total = 37
  ```
- Function calls can be used in assignments:
  ```python
  def square(number):
      return number * number
      
  forty_two_squared = square(42)
  print(forty_two_squared)        # 1764
  ```
- Right side is fully evaluated before assignment:
  ```python
  foo = 42
  foo = foo - 2      # foo becomes 40
  foo = foo * 3      # foo becomes 120
  ```

## Augmented Assignment

- Shorthand for operations that update a variable's value
- Examples:
  ```python
  foo = 42
  foo -= 2       # equivalent to: foo = foo - 2
  foo *= 3       # equivalent to: foo = foo * 3
  foo += 5       # equivalent to: foo = foo + 5
  foo //= 25     # equivalent to: foo = foo // 25
  ```
- Works with strings:
  ```python
  bar = 'xyz'
  bar += 'abc'   # bar is now 'xyzabc'
  bar *= 2       # bar is now 'xyzabcxyzabc'
  ```
- Works with lists and sets too:
  ```python
  bar = [1, 2, 3]
  bar += [4, 5]  # bar is now [1, 2, 3, 4, 5]
  
  bar = {1, 2, 3}
  bar |= {4, 5}  # bar is now {1, 2, 3, 4, 5}
  ```
- Augmented assignment is a statement, not an expression
- Can't be used as function arguments or return values

## Reassignment vs. Mutation

- **Reassignment**: Changes which object a variable references
  ```python
  num = 3
  num = 42        # Reassignment - variable now points to new object
  ```
- **Mutation**: Changes the object itself, not the variable reference
  ```python
  my_list = [1, 2, 3]
  my_list[1] = 42  # Mutation - same list object, different content
  ```
- Augmented assignment with immutable types acts like reassignment
- Augmented assignment with mutable types usually mutates the object

#### Key Distinctions
- Reassigning a variable doesn't change the original object
- Reassigning an element in a collection mutates the collection
- Mutation affects all variables pointing to the same object
