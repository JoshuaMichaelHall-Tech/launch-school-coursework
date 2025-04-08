## What are closures in Ruby?
Closures are blocks of code that can be passed around and executed later. They capture and carry the surrounding binding (methods and variables) available when defined. In Ruby, closures are implemented through blocks, procs, and lambdas.

## What is a binding in the context of closures?
A binding refers to the surrounding artifacts (variables, methods, etc.) that a closure has access to when it is created. The closure retains references to these artifacts when it's executed, even if the execution happens in a different scope.

## How do blocks work in Ruby and when should you use them?
Blocks are unnamed chunks of code passed to methods. They're used when:
1. You want to defer some implementation details to the method caller
2. You need to perform "before" and "after" actions (sandwich code)

Examples include iteration, custom error handling, resource management, or executing code at specific times.

## How do blocks interact with variable scope?
Blocks create a new scope but can access variables defined in their surrounding scope. Variables defined inside a block are not accessible outside of it. This applies to normal blocks but not to "false blocks" like `for` loops, which don't create a new scope.

## How do you create custom methods that use blocks and procs?
You can create methods that yield to blocks using the `yield` keyword:
```ruby
def custom_method
  yield if block_given?
end
```

For procs, you can pass them as arguments:
```ruby
def custom_method(a_proc)
  a_proc.call
end
```

## What is the difference between methods with implicit and explicit block parameters?
Implicit blocks are passed without special syntax and called using `yield`:
```ruby
def implicit_block
  yield if block_given?
end
implicit_block { puts "Hello" }
```

Explicit blocks are converted to Proc objects using `&` and called using `.call`:
```ruby
def explicit_block(&block)
  block.call if block
end
explicit_block { puts "Hello" }
```

## How do blocks handle arguments and return values?
Blocks can accept arguments when yielded to:
```ruby
def my_method
  yield(1, 2)
end
my_method { |a, b| puts a + b }
```

Blocks, like methods, always return the value of the last evaluated expression:
```ruby
result = [1, 2, 3].map { |n| n * 2 }  # returns [2, 4, 6]
```

## When can you pass blocks to methods in Ruby?
You can pass a block to any method in Ruby, though the method needs to explicitly call `yield` or use an explicit block parameter to make use of it. All Ruby methods can accept an optional block.

## What is arity in Ruby blocks and methods?
Arity refers to the rules regarding the number of arguments you must pass to a block, proc, lambda, or method.
- Methods and lambdas have strict arity - they raise errors if you pass the wrong number of arguments.
- Blocks and procs have lenient arity - they ignore extra arguments or assign nil to missing arguments.

## What is the difference between `yield` and `call` for blocks?
`yield` is used to call implicit blocks:
```ruby
def with_yield
  yield if block_given?
end
with_yield { puts "Called with yield" }
```

`.call` is used with explicit blocks or procs:
```ruby
def with_call(&block)
  block.call if block
end
with_call { puts "Called with call" }
```

## What testing frameworks are used in Ruby?
Ruby has two main testing frameworks:
- Minitest: Ruby's default testing library, which comes with Ruby
- RSpec: A domain-specific language for testing that's more expressive

Minitest can be used in both assertion style and expectation style syntax.

## What is the SEAT approach in testing?
SEAT stands for:
- **Setup**: Prepare necessary objects for the test
- **Execute**: Run the code being tested
- **Assert**: Check that the executed code did what it should
- **Teardown**: Clean up any lingering artifacts

## How do you test for equality in Ruby tests?
Testing for equality can be done in several ways:
- `assert_equal(expected, actual)`: Tests for value equality using `==`
- `assert_same(expected, actual)`: Tests for object identity (same object)
For custom classes, you need to define the `==` method to use `assert_equal` effectively.

## What core tools are commonly used in Ruby projects?
Common Ruby core tools include:
- Rubygems: Package manager for distributing code
- Bundler: Tool to manage gem dependencies
- Rake: Task automation tool similar to Make
- RVM/rbenv: Ruby version managers

## What is Bundler and what is a Gemfile?
Bundler is a dependency manager that ensures consistent gem installations across environments. A Gemfile is a text file that specifies the gems and versions a project needs. Running `bundle install` reads the Gemfile and installs the required gems.

## What is Rake and how is it used?
Rake is a Ruby build utility similar to Make. It uses a Rakefile to define tasks that can be run from the command line. Tasks can include running tests, database migrations, building assets, and more.

Sample Rakefile:
```ruby
desc 'Run tests'
task :test do
  ruby 'test/test_suite.rb'
end

# Default task when just 'rake' is run
task :default => :test
```
