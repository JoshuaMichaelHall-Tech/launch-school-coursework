# Getting Started - Using Python

## Indentation in Python

- Python uses indentation to structure code blocks (unlike most languages)
- Indentation is required, not just for readability
- Standard is 4 spaces per indentation level
- Blocks begin with a colon (`:`) and end when indentation reduces
- Example:
  ```python
  def double_list(input_list):
      # some code here
      for index, element in enumerate(input_list):
          # some more code here
          input_list[index] = 2 * element
  ```
- Inconsistent indentation causes syntax errors

## Using the REPL

- **REPL**: Read-Eval-Print Loop for interactive Python coding
- Start with `python` or `python3` command with no arguments
- `>>>` is the default prompt (don't type this when following examples)
- Multi-line statements use `...` as continuation prompt
- Outputs are shown without a prompt
- Example:
  ```python
  >>> print('hello world!')
  hello world!
  ```
- Last expression value is automatically displayed without needing `print()`
- Multi-line statements require proper indentation and extra Return/Enter
- Define and call functions directly in the REPL
- Use `help()` function to get documentation
- Exit REPL with `exit()`, `quit()`, or Control-D
- Navigate history with Up and Down arrow keys
- As of Python 3.13.0, you can type just `exit` or `quit` without parentheses

## Running Python Code From Files

- Save Python code in files with `.py` extension
- Run with `python filename.py`
- Python compiler converts code to byte code, then interpreter executes it
- Example file `example.py`:
  ```python
  print('I wish to complain about this parrot.')
  print("It's probably pining for the fjords!")
  ```
- Run with `python example.py`
- Use Control-C to stop running programs (especially infinite loops)

## Stylish Python

- Python community has developed style conventions for readability
- Recommended guidelines:
  - Use four space characters (not tabs) for indentation
  - Configure text editor to expand tabs to spaces
  - Limit lines to 79 characters
  - Use spaces around operators (except `**`)
  - Comments start with `#` and continue to end of line
  - Code blocks indicated by `:` and indentation
  - Follow variable naming conventions

## PEPs

- PEP = Python Enhancement Proposal
- Numbered design documents that provide information and standards
- PEP 8 is the style guide for Python code
- Review PEP 8 occasionally as you develop Python skills

## Continuation Lines

- Multiple ways to continue code over several lines when exceeding 79 characters:
  - String literals in parentheses:
    ```python
    return ("This is a long string. "
            "It's actually very long.")
    ```
  - Triple-quoted strings (preserves whitespace):
    ```python
    return """
        This is a long string.
        It's actually very long.
    """
    ```
  - Multi-value literals with line breaks:
    ```python
    my_list = [
        "Antonina",
        "Brandi",
        "Trevor",
    ]
    ```
  - Parentheses for expressions:
    ```python
    return (obj.bar1
          + obj.bar2
          + obj.bar3)
    ```
  - Backslash (`\`) at line end:
    ```python
    result = value1 + \
             value2 + \
             value3
    ```

## Using JupyterLab/Jupyter Notebook

- Alternative to standard REPL
- Benefits include writing/trying code and easy copy-paste
- Browser-based options at jupyter.org/try
- Can install locally (not recommended for Cloud9)
- Run with `jupyter lab` or `jupyter notebook`
- Execute code in cells with {Shift}{Enter}

## Debugging Python Code with print

- `print()` statements help debug programs
- Place strategically to trace values and execution flow
- Example debugging a function to find maximum value:
  ```python
  numbers = [3, 1, 5, 9, 2, 6, 4, 7]
  found_item = -1
  index = 0
  
  while index < len(numbers):
      print('max =', max, 'number =', numbers[index])
      if numbers[index] == 5:
          found_item = index
      
      index += 1
  ```
- Debugging with `print` works in all environments, including Coderpad

## About the Exercises

- Multiple solutions may exist for a single problem
- Your solution doesn't need to match Launch School's exactly
- Important to understand both your solution and Launch School's
- Ensure your answer satisfies all requirements
- Focus on building awareness of Python syntax and approaches
