## What is a variable in Ruby?
A name for a memory location that contains data. Variables in Ruby are references or pointers to objects in memory.

## What are variables as pointers?
Variables point to objects in memory. When a variable is set to the value of another variable, it creates a pointer to the object in memory to which the other variable points. They're two separate pointers to the same object in memory. Modifying one of those pointers later does not affect the other.

## What is variable shadowing?
When block parameters (between pipes ||) match a variable in an outer scope, they are said to shadow the outer variable, blocking it.

## What is local variable scope in relation to method definitions?
Method definitions define a local variable scope. Variables initialized in a method definition are not accessible from outside the definition and vice versa.

## What is local variable scope in relation to blocks?
Blocks can access variables initialized outside the block, but not vice versa. This does not apply to false blocks: for, while, and until, as these are part of Ruby language and not method invocations.

## What is the scope of constants?
Constants override all scope boundaries and cannot be declared in method definitions. They are used rarely due to unexpected consequences.

## What is the difference between mutating values and reassigning variables?
Reassignment changes the object id bound to a reference. It does not mutate the original object and therefore has no effect on other variables bound to the original object id. Mutating values changes the object at the object id in memory for all variables pointing to that id.

## What are mutable vs. immutable data types?
Some objects in Ruby can be mutated, others cannot. Objects and numbers are immutable. When code manipulates immutable objects, it is actually reassignment, not mutation, and the object id will change, not the object in memory.

## What is the difference between method definition and method invocation?
Method definition is where we define a method to be used later, perhaps multiple times. Method invocation is when we actually call the method to use it.

## What are parameters vs. arguments?
A parameter is part of a method definition. It is a stand-in for the argument which is passed into the method when it is called.

## What are default parameters?
Default parameters are part of a method definition. They are the arguments passed to the method when no argument is given at the method invocation.

## What is the difference between implicit vs. explicit return values?
Methods return the last evaluated expression by definition, so this return is implicit. Explicit return is when a return call is made in the definition.

## What is the difference between mutating vs. non-mutating methods?
No method can mutate an immutable argument. Most methods do not mutate, some mutate the caller, few mutate the argument. Assignment is non-mutating.

## What is pass-by-reference vs. pass-by-value?
Ruby is neither, but rather *pass by value of the reference* or *call by sharing*. When an operation within the method mutates the caller or argument, it will affect the original object.

## What is the difference between output vs. return?
Output is what an expression does, like print to STDOUT. Return is the expression's hidden evaluation, the object passed to the caller.

## How can you use method return values as arguments to other methods?
When a method is passed as an argument to another method, Ruby first evaluates the return value of the first method and then passes that object as an argument to the second method.

## What is truthiness in Ruby?
Only false and nil are falsy. Everything else is truthy.

## What is passing and using blocks with methods?
You can pass blocks to methods by enclosing code in `do...end` or `{...}`. Method definitions cannot directly access local variables initialized outside of the method definition, nor can local variables initialized outside of the method definition be reassigned from within it. A block can access local variables initialized outside of the block and can reassign those variables.
