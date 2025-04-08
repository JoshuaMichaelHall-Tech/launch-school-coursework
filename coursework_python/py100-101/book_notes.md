# Notes on Launch School Intro to Python

## Getting Started

### Python Introduction Notes

#### About Python
- Created by Guido van Rossum in the late 1980s
- Named after the British comedy group "Monty Python's Flying Circus"
- First public release (v0.90) in 1991, first production version (1.0) in 1994
- Python 2 support ended in 2020; all developers should now use Python 3
- Python's future looks stable with gradual improvements rather than major version changes

#### Abstraction in Programming
- **Abstraction**: Users don't need to know what's happening "under the hood"
- Example: Phone users interact with UI without knowing internal workings
- Programming languages are abstraction layers:
  - User applications (highest level)
  - Python code (higher level)
  - Python interpreter (converts to byte code)
  - Machine code (1s and 0s, lowest level)
- Understanding Python fundamentals makes using higher-level tools easier

#### Python Environment Setup
- Recommended: Mac or AWS Cloud9
- Command invocation varies (`python` or `python3`)
- Terminal commands to know: `cd`, `mkdir`, `rmdir`, `touch`, `rm`, `git`

#### Installing Python
- Check if installed using `python3 --version` or `python --version`
- Mac: Install using Homebrew
- Cloud environments: GitHub Codespaces or AWS Cloud9
- Linux: Often pre-installed
- Windows: WSL2 (Windows Subsystem for Linux) recommended

#### Using Code Editors
- Use plain text code editors, not word processors
- Recommended: Visual Studio Code (VSCode)
- Other options: Vim, Emacs

#### Python Documentation
- Documentation available at python.org/doc/
- Key sections:
  - Language Reference (especially Expressions, Simple Statements, Compound Statements)
  - Library Reference (Built-in Types, Functions, Constants)
  - Glossary for terminology
  - Complete Table of Contents

### Using Python

#### Indentation
- Python uses indentation to structure code blocks
- Proper indentation is required, not just for readability
- Standard is 4 spaces per indentation level
- Blocks begin with a colon (:) and end when indentation reduces

#### Using the REPL
- REPL (Read-Eval-Print Loop) for interactive Python coding
- Start with `python` or `python3` command
- `>>>` is the prompt (don't type this)
- Multi-line statements use `...` as continuation prompt
- Exit REPL with `exit()`, `quit()`, or Control-D
- Help function: `help()` or `help(object)`

#### Running Python Code From Files
- Save Python code in files with `.py` extension
- Run with `python filename.py`
- Python compiler converts code to byte code, then interpreter executes it
- Use Control-C to stop running programs

#### Python Style Conventions
- Use 4 spaces for indentation (not tabs)
- Limit lines to 79 characters 
- Use spaces around operators (except `**`)
- Comments start with `#` and continue to end of line
- Code blocks indicated by `:` and indentation
- PEP 8: The official Python style guide

#### Continuation Lines
- Multiple ways to continue code over several lines:
  - String literals in parentheses
  - Triple-quoted strings
  - Multi-value literals with line breaks
  - Parentheses for expressions
  - Backslash (`\`) at line end

#### Using JupyterLab/Jupyter Notebook
- Alternative to standard REPL
- Browser-based options: jupyterlab.org/try
- Can install locally with `brew install jupyterlab`
- Run with `jupyter lab` or `jupyter notebook`

#### Debugging with print
- Use `print()` statements to display variable values
- Strategic placement helps identify issues
- Example: Comparing strings vs. numbers

### Data Types

#### Objects and Values
- Everything with a value in Python is an object
- Each object has a data type/class
- Terms object/value and class/data type/type can be used interchangeably

#### Primary Data Types
- **Numerics**: 
  - `int` (integers) - immutable
  - `float` (floating point) - immutable
- **Booleans**: 
  - `bool` (True/False) - immutable
- **Text Sequences**: 
  - `str` (strings) - immutable
- **Sequences**:
  - `range` (range of numbers) - immutable
  - `tuple` (ordered collection) - immutable
  - `list` (ordered collection) - mutable
- **Mappings**:
  - `dict` (key-value pairs) - mutable
- **Sets**:
  - `set` (unique values) - mutable
  - `frozenset` (unique values) - immutable
- **Functions**: `function` - mutable
- **NoneType**: `None` - immutable

#### Literals
- Direct representation of values in code:
  - String: `'Hello, world!'`
  - Float: `3.141592`
  - Boolean: `True`
  - Dictionary: `{'a': 1, 'b': 2}`
  - List: `[1, 2, 3]`
  - Tuple: `(4, 5, 6)`
  - Set: `{7, 8, 9}`

#### Numeric Values

##### Integers
- Whole numbers without fractional parts: `1`, `2`, `-3`
- Can use underscores for readability: `131_587_465`
- No pre-defined size limit

##### Floating Point
- Numbers with decimal points: `1.0`, `3.14159`
- Can use scientific notation: `3.14e+20`
- Has representation limits (precision, max/min values)

#### Variables and Assignment
- Variables are names for values
- Created by assignment: `pi = 3.141592653589793`
- Initialization: First assignment to a variable
- Reassignment: Changing the value of an existing variable

#### Boolean Values
- Only two values: `True` and `False`
- Used to represent binary states
- Return values for comparison operations

#### Text Sequences (Strings)
- Sequences of Unicode characters
- String literals can use:
  - Single quotes: `'Hello'`
  - Double quotes: `"World"`
  - Triple quotes: `'''Multi-line'''` or `"""Multi-line"""`
- Escape characters with backslash: `\'`, `\"`
- Access characters with indexing: `mystr[0]`, `mystr[-1]`
- Raw strings: `r"C:\path\to\file"` (ignores escapes)
- f-strings: `f"Name: {name}"` (for string interpolation)

#### Functions
- Reusable code blocks that perform specific tasks
- Python functions have their own data type

#### None
- Represents absence of value
- Lone instance of NoneType class

#### Sequences

##### Lists and Tuples
- Ordered collections that can contain any object type
- Lists use `[]`, are mutable: `[1, 'xyz', True]`
- Tuples use `()`, are immutable: `(1, 'xyz', True)`
- Access elements by index: `my_list[0]`
- One-element tuple needs trailing comma: `(1,)`

##### Ranges
- Sequence of integers between endpoints
- Created with `range()` function
- Examples:
  - `range(5)`: 0, 1, 2, 3, 4
  - `range(5, 10)`: 5, 6, 7, 8, 9
  - `range(1, 10, 2)`: 1, 3, 5, 7, 9

#### Mappings (Dictionaries)
- Unordered collections of key-value pairs
- Created with curly braces: `{'dog': 'barks', 'cat': 'meows'}`
- Access values by keys: `my_dict['dog']`
- Keys must be immutable and hashable
- As of Python 3.7, insertion order is preserved

#### Sets
- Unordered collections of unique, immutable objects
- Created with curly braces: `{1, 2, 3}`
- Empty set must use constructor: `set()`
- Frozen sets (immutable sets): `frozenset([1, 2, 3])`
- Set members must be hashable

### Data Types

#### Basic Operations

In Python, different types share a lot of functionality.
- Most objects can be compared with the same type for equality, and often also 
  for less than or greater than operations.
- All collection objects respond to len()
- Most objects are convertable into a human-readable string.
- The same iteration syntax can be applied to different collection types.

Three Main Kinds of Types:
1. Built in: Part of Ruby and available in every program.
2. Standard: Available through importing.
3. Non-standard: Created by third parties (like me!).

#### Arithmetic Operations

All built-in and standard numeric data types work with all or most of these operations:

Here's the completed formatting for the operators table:

| Operator | Operation        |
|----------|------------------|
| +        | Addition         |
| -        | Subtraction      |
| *        | Multiplication   |
| /        | Division         |
| //       | Integer division |
| %        | Modulo           |
| **       | Exponentiation   |


