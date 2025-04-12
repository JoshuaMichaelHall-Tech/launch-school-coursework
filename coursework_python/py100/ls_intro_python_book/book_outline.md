Master Mind Map (Text Outline)
Python
├── Getting Started
│   ├── Introduction
│   ├── Preparations
│   └── Using Python
├── Intro to Programming
│   ├── Data Types
│   ├── Basic Operations
│   ├── Variables
│   ├── Input/Output
│   └── Functions and Methods
├── Flow Control
│   └── Conditionals and Loops
├── Collections and Iteration
│   ├── Introduction to Collections
│   ├── Using Collections
│   └── Loops and Iterating
└── Additional Topics
    ├── Variables as Pointers
    └── More Stuff
Chapter Mind Maps (Text Outlines)
1. Getting Started - Introduction
Introduction to Python
├── Python History
│   ├── Created by Guido van Rossum in late 1980s
│   ├── First public release in 1991
│   ├── Python 1.0 released in 1994
│   ├── Python 2 was popular for many years
│   ├── Python 3 released in 2008
│   └── Python 2 support ended in 2020
├── Python's Future
│   ├── Continued popularity and growth
│   ├── Unlikely to see Python 4 soon
│   └── Ongoing improvements through minor versions
├── Abstraction
│   ├── Concept of hiding underlying details
│   ├── Different levels of abstraction
│   │   ├── User level
│   │   ├── Developer level
│   │   └── Systems level
│   ├── Python as an abstraction layer
│   └── Higher-level abstractions built on Python
├── Who This Book is For
│   ├── Inexperienced or new programmers
│   ├── Can benefit experienced programmers too
│   └── Focused on fundamentals and practice
└── What's Not Covered
    ├── 3rd Party Libraries
    ├── Asynchronous Programming
    ├── Object-Oriented Python
    ├── Testing
    ├── Intermediate Language Constructs
    └── Unicode and ASCII details
2. Getting Started - Preparations
Preparations
├── Command Line Basics
│   ├── Shell commands
│   ├── Prompts ($, %)
│   └── Essential commands
│       ├── cd, mkdir, rmdir
│       ├── touch, rm
│       └── git
├── Installing Python
│   ├── Version recommendations (3.10.x or higher)
│   ├── Installation by platform
│   │   ├── Mac (using Homebrew)
│   │   ├── GitHub Codespaces
│   │   ├── AWS Cloud9
│   │   ├── Other Linux systems
│   │   └── Windows (with WSL2)
│   └── Starting over when things go wrong
├── Using a Code Editor
│   ├── Recommendation for VS Code
│   └── Avoiding word processors
└── Python Documentation
    ├── Finding Python docs
    ├── Language Reference
    ├── Library Reference
    ├── Glossary
    └── Complete Table of Contents
3. Getting Started - Using Python
Using Python
├── Indentation
│   ├── Python requires proper indentation
│   ├── Indentation marks code blocks
│   └── Consistent indentation rules
├── Using the REPL
│   ├── Read-Eval-Print Loop
│   ├── Interactive Python environment
│   ├── The help function
│   └── Exiting the REPL
├── Running Python Code From a File
│   ├── Python file execution
│   ├── Compiler and interpreter process
│   └── Stopping long-running programs
├── Stylish Python
│   ├── Style conventions
│   ├── Indentation (4 spaces)
│   ├── Line length (79 characters)
│   ├── Spacing around operators
│   └── Comments with #
├── PEPs (Python Enhancement Proposals)
│   └── PEP 8 (Style Guide)
├── Continuation Lines
│   ├── String continuation
│   ├── Collection continuation
│   ├── Parenthesized expressions
│   └── Backslash continuation
├── Using JupyterLab/Jupyter Notebook
│   ├── Alternatives to standard REPL
│   ├── Browser-based options
│   └── Installation options
└── Debugging with print
    ├── Basic print debugging technique
    └── Example of print debugging
4. Intro to Programming - Data Types
Data Types
├── Python Object Types
│   ├── Primitive Types
│   │   ├── integers (int)
│   │   ├── floats (float)
│   │   ├── boolean (bool)
│   │   └── strings (str)
│   └── Non-primitive Types
│       ├── Sequences (range, tuple, list)
│       ├── Mappings (dict)
│       ├── Sets (set, frozenset)
│       └── Functions
├── Literals
│   └── Syntax for representing values directly
├── Numeric Values
│   ├── Integers
│   │   ├── Whole numbers
│   │   └── Unlimited size
│   └── Floats
│       ├── Real numbers
│       ├── Working with large/small floats
│       └── Scientific notation
├── Variables and Assignment
│   ├── Creating variables
│   ├── Initialization
│   └── Reassignment
├── Boolean Values
│   ├── True and False
│   └── Boolean operations
├── Text Sequences
│   ├── Strings
│   ├── String literals and quotes
│   ├── Indexing strings
│   ├── Raw strings (r-strings)
│   └── f-strings (formatted strings)
├── Functions
│   └── Reusable code blocks
├── None
│   └── Representing absence of value
├── Sequences
│   ├── Lists and Tuples
│   │   ├── Creating lists and tuples
│   │   ├── Heterogeneous collections
│   │   └── Accessing elements
│   └── Ranges
│       └── Sequence of integers
├── Sets
│   ├── Unordered collections of unique objects
│   ├── Sets vs. Frozen Sets
│   └── Set operations
└── Mappings
    ├── Key-value pairs
    ├── Dictionary creation
    └── Dictionary operations
5. Intro to Programming - Basic Operations
Basic Operations
├── Arithmetic Operations
│   ├── Addition (+)
│   ├── Subtraction (-)
│   ├── Multiplication (*)
│   ├── Division (/)
│   ├── Integer division (//)
│   ├── Modulo (%)
│   ├── Exponentiation (**)
│   └── Floating point imprecision
├── Equality Comparison
│   ├── Equality (==)
│   └── Inequality (!=)
├── Ordered Comparisons
│   ├── Less than (<)
│   ├── Less than or equal (<=)
│   ├── Greater than (>)
│   └── Greater than or equal (>=)
├── String Concatenation
│   ├── Using + operator
│   └── Repetition with * operator
├── Coercion
│   ├── Explicit Coercion
│   │   ├── String to number (int, float)
│   │   └── Number to string (str)
│   └── Implicit Coercion
├── Determining Types
│   ├── type function
│   ├── type.__name__ property
│   └── Using type with is operator
├── String Representations
│   ├── str function
│   └── repr function
├── Collection and String Lengths
│   └── len function
├── Indexing and Key Access
│   ├── Accessing elements by index
│   ├── Updating elements
│   └── Dictionary key access
├── Expressions and Statements
│   ├── Expressions (produce values)
│   └── Statements (perform actions)
├── Expression Evaluation
│   ├── Precedence rules
│   └── Using parentheses
└── Output vs. Return Values
    ├── Printing with print
    └── Returning values from functions
6. Intro to Programming - Variables
Variables
├── Variables and Variable Names
│   ├── Definition of variables
│   ├── Variable naming challenges
│   └── Identifiers
├── Naming Conventions
│   ├── snake_case for variables
│   ├── SCREAMING_SNAKE_CASE for constants
│   ├── PascalCase for classes
│   └── Legal vs. illegal names
├── Creating and Reassigning Variables
│   ├── Initialization
│   ├── Definition
│   └── Reassignment
├── Creating Constants
│   ├── Naming with SCREAMING_SNAKE_CASE
│   └── No true constants in Python
├── Expressions and Assignment
│   ├── Using expressions on the right side
│   └── Variable as target on the left side
├── Augmented Assignment
│   ├── Combined operations (+=, -=, etc.)
│   ├── With strings
│   ├── With lists
│   └── With sets
└── Reassignment vs. Mutation
    ├── Changing variable binding
    └── Changing object value
7. Intro to Programming - Input Output
Input/Output
├── Terminal Output
│   ├── print function
│   │   ├── Printing multiple items
│   │   ├── Separator (sep parameter)
│   │   ├── Line ending (end parameter)
│   │   └── Empty print for newline
│   └── Formatting output
├── Terminal Input
│   ├── input function
│   │   ├── Reading user input
│   │   ├── Using prompts
│   │   └── Getting different input types
│   └── Input/output cycle
│       ├── Reading input
│       ├── Processing data
│       └── Displaying output
└── Example Programs
    ├── Personalized greeting
    └── Adding numbers
8. Intro to Programming - Functions and Methods
Functions and Methods
├── Calling Functions
│   ├── Invoking functions
│   ├── Return values
│   └── Arguments
├── Built-in Functions
│   ├── min and max
│   ├── ord and chr
│   ├── any and all
│   └── REPL helper functions
│       ├── id
│       ├── dir
│       └── help
├── Creating Functions
│   ├── Function definition syntax
│   ├── Docstrings
│   └── Return values
├── Scope
│   ├── Function scope
│   ├── Variable shadowing
│   └── Lexical scope
├── Namespaces
│   ├── Local namespace
│   ├── Enclosing namespaces
│   ├── Global namespace
│   └── Built-in namespace
├── Arguments & Parameters
│   ├── Parameters as placeholders
│   ├── Arguments as values
│   └── Default parameters
├── Return Values
│   ├── Explicit returns with return
│   ├── Implicit returns (None)
│   └── Predicates (boolean-returning functions)
├── Default Parameters
│   ├── Parameter defaults
│   └── Argument omission
├── Functions vs. Methods
│   ├── Function invocation
│   └── Method invocation
└── Mutating the Caller
    ├── Methods that change objects
    └── Functions that change arguments
9. Intro to Programming - Flow Control
Flow Control
├── Conditionals
│   ├── if statement
│   ├── if/else statement
│   ├── if/elif/else statement
│   └── pass statement
├── Comparisons
│   ├── Equality (==)
│   ├── Inequality (!=)
│   ├── Less than (<) and less than or equal (<=)
│   └── Greater than (>) and greater than or equal (>=)
├── Logical Operators
│   ├── not operator
│   ├── and operator
│   └── or operator
├── Short Circuits
│   ├── Short circuit evaluation with and
│   └── Short circuit evaluation with or
├── Truthiness
│   ├── Truthy values
│   ├── Falsy values
│   └── Truthiness and short-circuit evaluation
├── Logical Operator Precedence
│   ├── Comparison operators
│   ├── not
│   ├── and
│   └── or
├── match/case Statement
│   ├── Basic match statement
│   ├── Multiple values in a case
│   └── Default case with _
└── Ternary Expressions
    └── condition ? value1 : value2 style expressions
10. Collections and Iteration - Intro
Introduction to Collections
├── Collection Types
│   ├── Sequences
│   │   ├── range
│   │   ├── tuple
│   │   └── list
│   ├── Mappings
│   │   └── dict
│   └── Sets
│       ├── set
│       └── frozenset
├── What are Sequences?
│   ├── Ordered collections
│   ├── Indexable by whole numbers
│   ├── Heterogeneous vs. homogenous
│   └── Text sequences (strings)
├── What are Sets?
│   ├── Unordered collections
│   ├── Unique elements
│   └── Set vs. frozenset
├── What are Mappings?
│   ├── Unordered collections of key/value pairs
│   ├── Dictionary characteristics
│   └── Dictionary order preservation
└── Sequence Constructors
    ├── String constructor
    ├── Range constructor
    ├── List, tuple, set, and frozen set constructors
    └── Converting between collection types
11. Collections and Iteration - Using Collections
Using Collections
├── Indexing
│   ├── Accessing sequence elements
│   ├── Index ranges
│   └── Negative indexing
├── Slicing
│   ├── Basic slice syntax
│   ├── Slice with step
│   ├── Omitted start/end indices
│   └── Reversing with slices
├── Key-Based Access
│   ├── Dictionary keys
│   ├── Error handling with get
│   └── Assigning values with keys
├── Common Collection Operations
│   ├── Non-Mutating Operations
│   │   ├── Collection membership (in, not in)
│   │   ├── Minimum and maximum (min, max)
│   │   ├── Summation (sum)
│   │   ├── Finding indices and counting (index, count)
│   │   └── Merging collections (zip)
│   ├── Dictionary Operations
│   │   ├── keys()
│   │   ├── values()
│   │   └── items()
│   ├── Operations for Mutable Sequences
│   │   ├── Adding elements (append, insert, extend)
│   │   └── Removing elements (remove, pop, clear)
│   └── Sorting and Reversing
│       ├── sorted function
│       ├── list.sort method
│       ├── reversed function
│       └── list.reverse method
├── String Operations
│   ├── Letter Case
│   │   ├── upper, lower, casefold
│   │   ├── capitalize, title
│   │   └── swapcase
│   ├── Character Classification
│   │   ├── isalpha, isdigit, isalnum
│   │   ├── islower, isupper
│   │   └── isspace
│   ├── Stripping Characters
│   │   ├── strip, lstrip, rstrip
│   │   └── Removing specific characters
│   ├── startswith and endswith
│   └── Splitting and Joining
│       ├── split
│       └── join
├── Nested Collections
│   ├── Collections inside collections
│   └── Limitations on nesting
└── Comparing Collections
    ├── Equality comparison
    └── Requirements for equality
12. Collections and Iteration - Loops and Iterating
Loops and Iterating
├── while Loops
│   ├── Basic while loop structure
│   ├── Iteration control
│   └── Using while with sequences
├── for Loops
│   ├── Basic for loop structure
│   ├── Iterating over sequences
│   ├── Iterating over strings
│   ├── Iterating over sets
│   ├── Iterating over dictionaries
│   │   ├── Keys
│   │   ├── Values
│   │   └── Items
│   └── Nested Loops
├── Controlling Loops
│   ├── continue statement
│   ├── break statement
│   └── Emulating do/while loops
├── Simultaneous Iteration
│   └── Using zip function
└── Comprehensions
    ├── List Comprehensions
    │   ├── Basic syntax
    │   ├── Transformation
    │   ├── Selection
    │   └── Multiple for/if components
    ├── Dictionary Comprehensions
    ├── Set Comprehensions
    └── Why no tuple, range, or string comprehensions
13. Additional Topics - Variables as Pointers
Variables as Pointers
├── Variables As Pointers
│   ├── Variables reference objects
│   ├── Reassignment changes references
│   └── Mutation changes objects
├── Variables and Objects
│   ├── Stack and heap memory
│   ├── Object storage
│   └── Variable references
├── Variables and Shared Objects
│   ├── Multiple variables, same object
│   └── Pointer behavior
├── Equality and Identity
│   ├── Equal values (==)
│   ├── Same object (is)
│   └── Object identity (id)
└── Shallow vs. Deep Copies
    ├── Shallow Copies
    │   ├── Duplicating outer level only
    │   └── Nested objects remain shared
    ├── Deep Copies
    │   ├── Duplicating all levels
    │   └── Complete independence
    └── When to use each type of copy
14. Additional Topics - More Stuff
More Stuff
├── Function Composition
│   ├── Functions as arguments
│   ├── Nested function calls
│   └── Building complex operations
├── Method Chaining
│   ├── Sequential method calls
│   ├── Format for readability
│   └── Limitations in Python
├── Modules
│   ├── Code reuse through modules
│   ├── Built-in modules
│   ├── PyPI modules
│   └── Custom modules
│   ├── Import Statements
│   │   ├── import
│   │   ├── from import
│   │   └── import as
├── The math Module
│   ├── Mathematical functions
│   ├── Constants
│   └── Example uses
├── The datetime Module
│   ├── Date and time manipulation
│   ├── strptime and strftime
│   └── Handling complex date/time issues
├── Function Definition Order
│   ├── How Python processes function definitions
│   └── Function definition placement
├── Nested Functions
│   ├── Functions inside functions
│   └── Scope of nested functions
└── The global and nonlocal Statements
    ├── Variable scope in functions
    ├── global statement
    ├── nonlocal statement
    └── Best practices
Comprehensive Mind Map (Text Outline)
Python Programming
├── Language Fundamentals
│   ├── Python History & Evolution
│   │   ├── Created by Guido van Rossum (1980s)
│   │   ├── First release in 1991
│   │   ├── Python 3 released in 2008
│   │   └── Python 2 support ended in 2020
│   ├── Setup & Environment
│   │   ├── Installation by platform
│   │   ├── Command line basics
│   │   ├── Code editors
│   │   └── Documentation resources
│   ├── Core Concepts
│   │   ├── Abstraction
│   │   ├── Indentation & whitespace significance
│   │   └── Python philosophy
│   └── Execution Methods
│       ├── REPL
│       ├── Running files
│       ├── Jupyter notebooks
│       └── Debugging techniques
├── Data & Types
│   ├── Primitive Types
│   │   ├── Integers (int)
│   │   ├── Floating Point (float)
│   │   ├── Booleans (bool)
│   │   └── Strings (str)
│   ├── Collections
│   │   ├── Sequences
│   │   │   ├── Lists (mutable)
│   │   │   ├── Tuples (immutable)
│   │   │   └── Ranges
│   │   ├── Mappings
│   │   │   └── Dictionaries
│   │   └── Sets
│   │       ├── Sets (mutable)
│   │       └── Frozen sets (immutable)
│   ├── Special Values
│   │   ├── None
│   │   └── Functions as objects
│   └── Type Operations
│       ├── Type checking
│       ├── Conversion/coercion
│       └── String representations
├── Operations & Expressions
│   ├── Arithmetic
│   │   ├── Basic operations (+, -, *, /)
│   │   ├── Integer division (//)
│   │   ├── Modulo (%)
│   │   └── Exponentiation (**)
│   ├── Comparisons
│   │   ├── Equality (==, !=)
│   │   └── Ordered (<, <=, >, >=)
│   ├── Logical Operations
│   │   ├── and, or, not
│   │   └── Short-circuit evaluation
│   ├── Collection Operations
│   │   ├── Indexing & slicing
│   │   ├── Membership testing (in)
│   │   ├── Sorting & ordering
│   │   └── Aggregation (min, max, sum)
│   └── String Operations
│       ├── Concatenation & repetition
│       ├── Case manipulation
│       ├── Splitting & joining
│       └── Searching & replacement
├── Variables & State
│   ├── Variable Fundamentals
│   │   ├── Assignment & initialization
│   │   ├── Naming conventions
│   │   └── Constants
│   ├── Variable Mechanics
│   │   ├── Variables as pointers
│   │   ├── Memory model (stack & heap)
│   │   ├── Object identity vs equality
│   │   └── Shallow vs deep copies
│   ├── Scope & Namespaces
│   │   ├── Local scope
│   │   ├── Global scope
│   │   ├── Enclosing scopes
│   │   └── Built-in scope
│   └── State Manipulation
│       ├── Reassignment vs mutation
│       ├── Augmented assignment
│       └── global & nonlocal statements
├── Control Flow
│   ├── Conditionals
│   │   ├── if/elif/else statements
│   │   ├── match/case statements
│   │   ├── Ternary expressions
│   │   └── Truthiness concept
│   ├── Loops
│   │   ├── while loops
│   │   ├── for loops
│   │   ├── Loop control (break, continue)
│   │   └── Nested loops
│   └── Iteration Techniques
│       ├── Iterating different collections
│       ├── Simultaneous iteration (zip)
│       ├── Comprehensions
│       │   ├── List comprehensions
│       │   ├── Dictionary comprehensions
│       │   └── Set comprehensions
│       └── Emulating do-while loops
├── Functions & Modularity
│   ├── Function Basics
│   │   ├── Defining functions
│   │   ├── Parameters & arguments
│   │   ├── Return values
│   │   └── Default parameters
│   ├── Function Concepts
│   │   ├── Scopes & namespaces
│   │   ├── Nested functions
│   │   ├── Function composition
│   │   └── Function definition order
│   ├── Methods vs Functions
│   │   ├── Method invocation
│   │   ├── Method chaining
│   │   └── Side effects
│   └── Code Organization
│       ├── Modules & imports
│       ├── Standard library modules
│       │   ├── math
│       │   └── datetime
│       └── External modules
└── Input & Output
    ├── Terminal I/O
    │   ├── Input from keyboard
    │   ├── Output to terminal
    │   └── Input validation
    ├── Output Formatting
    │   ├── print parameters
    │   ├── f-strings
    │   └── String formatting
    └── File I/O (not covered in depth)
