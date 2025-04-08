## What are classes and objects in Ruby?
Classes are basic outlines or blueprints of what an object should be made of and what it should be able to do. Objects are instantiated from classes and contain methods and state as defined by the class and its inheritances.

## What are states and behaviors in OOP?
State refers to the data associated with an individual object (tracked by instance variables). Behaviors are what objects are capable of doing (defined by methods).

## What are instance variables? How are they scoped?
Instance variables keep track of object state and begin with an @ symbol. They exist as long as the object instance exists and are one of the ways we tie data to objects. They are scoped at the object level.

## What are class variables? How are they scoped?
Class variables track data for a class and begin with @@. They are accessible from all instances of the class. One use case is keeping track of how many objects are instantiated from a class. Class variables are scoped at the class level and are shared among all instances of the class.

## What are constants? How are they scoped?
Constants are used for variables that should never change. They begin with a capital letter and are usually completely upcased. Constants override all scope boundaries but cannot be declared in method definitions.

## What are getter and setter methods? How are they created?
Getter methods return the value in an instance variable. Setter methods set the value of an instance variable. They can be created manually or by using `attr_reader`, `attr_writer`, or `attr_accessor`.

```ruby
# Manual getter
def name
  @name
end

# Manual setter
def name=(name)
  @name = name
end

# Shorthand
attr_reader :name    # getter
attr_writer :name    # setter
attr_accessor :name  # both getter and setter
```

## What is the difference between instance methods and class methods?
Instance methods are called on objects and expose behavior for those objects. Class methods are called directly on the class and are used for functionality that does not pertain to individual objects. Class methods are defined with `self.` prefix.

## What is method access control? What are the different access modifiers?
Method access control allows or restricts access to methods through access modifiers: `public`, `private`, and `protected`. Public methods form the interface of a class. Private methods can only be called within the class itself without explicit receiver. Protected methods are like private methods but can be called by any instance of the same class.

## What is class inheritance?
Class inheritance is when a class inherits behavior from another class. The class that is inheriting behavior is called the subclass, and the class it inherits from is called the superclass. A class can only have one parent class, and inheritance is used for is-a relationships.

## What is encapsulation in OOP?
Encapsulation is bundling or combining the data (variables/state) and the operations (methods) that work on that data into a single entity (object). It hides functionality, provides data protection, and enables greater complexity through interfaces.

## What is polymorphism in OOP?
Polymorphism is the ability for different types of data to respond to a common interface. It can be achieved through class inheritance or duck typing.

## What are modules in Ruby? How are they used?
Modules are collections of behaviors that can be used in other classes via mixins. A module is "mixed in" to a class using the `include` method. Modules are used for non-hierarchical inheritance (has-a relationships), namespacing, and as containers for methods.

## What is the method lookup path in Ruby?
The method lookup path is the order in which classes are inspected when you call a method. It first looks in the receiver's class, then any included modules (in reverse order of inclusion), then the superclass and its modules, and so on, ending with Object, Kernel, and BasicObject.

## What is method overriding?
Method overriding occurs when a subclass defines a method with the same name as a method in its superclass. The subclass method overrides the superclass method. You can use `super` to call the superclass's implementation of the method.

## What is `self` in Ruby?
`self` is a special keyword that references the current object. In an instance method, `self` refers to the object instance. In a class method, `self` refers to the class itself. It's used to explicitly call setters within the class and to define class methods.

## What are collaborator objects?
Collaborator objects are objects that are stored as state within another object. They help establish connections between different objects and represent relationships between them in your program design.
