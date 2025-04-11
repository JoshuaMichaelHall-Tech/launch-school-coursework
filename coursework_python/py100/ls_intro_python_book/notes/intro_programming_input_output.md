# Intro to Programming - Input Output

## Computer Interaction

- Computers need to take input, process it, and provide output
- Input sources: mice, keyboards, disks, networks, sensors
- Output destinations: screens, files, networks, other computers
- Programs connect input with output through processing

## Terminal Output

### Using `print()`

- `print()` function displays values in the terminal
- Works with all data types:
  ```python
  name = 'Jane'
  print(f'Good morning, {name}!')  # Good morning, Jane!
  
  print({ 'a': 1, "b": 42 })       # {'a': 1, 'b': 42}
  
  import time
  print(time.asctime())            # Current date and time
  ```

### Printing Multiple Items

- Pass multiple arguments to `print()`:
  ```python
  print(1, 2, 3, 'a', 'b')       # 1 2 3 a b
  print([1, 2, 3], 4, False)     # [1, 2, 3] 4 False
  ```

### Customizing Separators with `sep`

- Default separator is a space
- Change with `sep` parameter:
  ```python
  print(1, 2, 3, 'a', 'b', sep=',')     # 1,2,3,a,b
  print('a', 'b', 'c', 'd', 'e', sep='') # abcde
  ```

### Customizing Line Endings with `end`

- Default end character is newline (`\n`)
- Change with `end` parameter:
  ```python
  print(1, 2, 'a', 'b', end=' <-\n')    # 1 2 a b <-
  print('a', 'b', end=''); print('c', 'd')  # abcd
  ```

### Empty print

- `print()` with no arguments prints a blank line

## Terminal Input

### Using `input()`

- `input()` reads user input from the terminal
- Basic usage:
  ```python
  print("What's your name?")
  name = input()
  
  print(f'Good Morning, {name}!')
  ```

### Input with Prompt

- `input()` can display a prompt message:
  ```python
  name = input("What's your name? ")
  print(f'Good Morning, {name}!')
  ```
- Add space at end of prompt for readability
- Use `\n` in prompt for newline:
  ```python
  name = input("What's your name?\n")
  print(f'Good Morning, {name}!')
  ```

### Working with Numeric Input

- `input()` always returns a string
- Must convert to numbers for calculations:
  ```python
  number1 = input('Enter the first number: ')
  number2 = input('Enter the second number: ')
  
  # Wrong: concatenates strings
  sum = number1 + number2  # If inputs are 2 and 3, sum is '23'
  
  # Correct: converts to numbers first
  sum = float(number1) + float(number2)  # sum is 5.0
  ```

## Complete Input/Output Example

Here's a complete example showing reading input and displaying output:

```python
def greet_user():
    name = input("What's your name? ")
    age = int(input("How old are you? "))
    
    print(f"Hello, {name}!")
    print(f"In 10 years, you will be {age + 10} years old.")
    
greet_user()
```

This program:
1. Asks for the user's name and stores it as a string
2. Asks for the user's age and converts it to an integer
3. Outputs a greeting with the name
4. Calculates and displays the user's age in 10 years

The input/output cycle is the heart of interactive programs - software that accepts no input and provides no output would be useless.
