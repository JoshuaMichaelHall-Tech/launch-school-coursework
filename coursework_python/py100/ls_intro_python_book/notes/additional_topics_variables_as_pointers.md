# Additional Topics - Variables as Pointers

## Variables As Pointers

- In Python, all variables are pointers to objects
- Variables don't contain values directly; they reference objects
- If multiple variables reference the same object, they act like aliases
- Reassignment changes what object a variable points to, not the object itself
- Mutation changes the object, not the variable pointing to it

### Assignment vs. Mutation

- **Reassignment**: Changes which object a variable references
  ```python
  numbers = [1, 2, 3, 4]
  numbers = [1, 2, 3]  # Reassignment - new object
  ```
- **Mutation**: Changes the object itself
  ```python
  numbers = [1, 2, 3, 4]
  numbers[2] = 6  # Mutation - same object, new content
  ```
- The indexing syntax `numbers[2] = 6` mutates the list; it does not reassign the `numbers` variable
- Augmented assignment with immutable types acts like reassignment
  ```python
  a = 42
  a += 2  # Equivalent to a = a + 2 (reassignment)
  ```
- Augmented assignment with mutable types usually mutates
  ```python
  a = [1, 2, 3]
  a += [4, 5]  # Mutates list (similar to a.extend([4, 5]))
  ```

## Variables and Objects

- Variables are named locations in memory (usually in the stack)
- Objects are stored elsewhere in memory (typically in the heap)
- When creating a variable, Python:
  1. Allocates space for the object in the heap
  2. Creates the object at that location
  3. Stores the object's address in the variable's stack location
- Example:
  ```python
  numbers = [1, 2, 3]
  ```
  This stores the address of the list object in the variable `numbers`
- When accessing a variable:
  1. Python finds the variable on the stack
  2. Gets the object's address from the stack
  3. Uses the address to find and access the object

## Variables and Shared Objects

- Assigning one variable to another copies the pointer, not the object
- Both variables reference the same object in memory
- Example:
  ```python
  numbers = [1, 2, 3]
  numbers2 = numbers  # Both reference the same list
  
  print(id(numbers) == id(numbers2))  # True
  print(numbers is numbers2)          # True
  ```
- Memory layout:
  ```
  Stack:              Heap:
  +-----------+       +-------------+
  | numbers   |------>| [1, 2, 3]   |
  +-----------+       +-------------+
  | numbers2  |------/
  +-----------+
  ```

## Equality and Identity

- **Equality** (`==`): Checks if objects have the same value
- **Identity** (`is`): Checks if variables reference the same object
- Example 1 - Same object:
  ```python
  numbers = [1, 2, 3]
  numbers2 = numbers
  
  print(numbers == numbers2)  # True (equal values)
  print(numbers is numbers2)  # True (same object)
  ```
- Example 2 - Different objects with same value:
  ```python
  numbers = [1, 2, 3]
  numbers2 = [1, 2, 3]
  
  print(numbers == numbers2)  # True (equal values)
  print(numbers is numbers2)  # False (different objects)
  ```

## Shallow vs. Deep Copies

### Memory Layout of Nested Objects

- Nested objects are stored separately in memory
- Example with nested list `[[1, 2], 3, 4]`:
  ```
  Outer list:                  Inner list:
  +--------------------+       +--------+
  | [pointer, 3, 4]    |------>| [1, 2] |
  +--------------------+       +--------+
  ```

### Shallow Copies

- Duplicate only the outermost level of an object
- Inner objects are still shared between original and copy
- Created by:
  - List constructor: `list(original)`
  - Slicing: `original[:]`
  - `copy.copy(original)`
- Example:
  ```python
  import copy
  
  orig = [[1, 2], 3, 4]
  dup = copy.copy(orig)
  
  print(orig is dup)           # False (different outer lists)
  print(orig[0] is dup[0])     # True (same inner list)
  
  orig[0][1] = 22
  print(dup[0])                # [1, 22] (change is visible in both)
  ```

### Deep Copies

- Duplicate the entire object hierarchy - outer object and all nested objects
- No sharing of objects between original and copy
- Created by `copy.deepcopy(original)`
- Example:
  ```python
  import copy
  
  orig = [[1, 2], 3, 4]
  dup = copy.deepcopy(orig)
  
  print(orig is dup)           # False (different outer lists)
  print(orig[0] is dup[0])     # False (different inner lists)
  
  orig[0][1] = 22
  print(dup[0])                # [1, 2] (change not visible in copy)
  ```
- Note: `copy.deepcopy` doesn't necessarily duplicate immutable objects

### When to Use Shallow vs. Deep Copies

- **Use shallow copies when**:
  - Working with non-collection objects
  - Working with immutable objects
  - Working with collections that have no mutable elements
  - Performance is critical (shallow copies are faster)
  - You don't care if mutable components are shared

- **Use deep copies when**:
  - Working with collections that have mutable elements
  - You need complete isolation between original and copy
