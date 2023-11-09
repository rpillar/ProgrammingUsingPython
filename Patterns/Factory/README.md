Factory pattern notes and exmaples based on this Real Python article - https://realpython.com/factory-method-python/

The GoF (Gang of Four) book describes Factory Method as a creational design pattern. Creational design patterns are related to the creation 
of objects, and Factory Method is a design pattern that creates objects with a common interface.

For example, an application requires an object with a specific interface to perform its tasks. The concrete implementation 
of the interface is identified by some parameter.

Instead of using a complex if/elif/else conditional structure to determine the concrete implementation, the application 
delegates that decision to a separate component that creates the concrete object. With this approach, the application 
code is simplified, making it more reusable and easier to maintain.

Complex conditional code is hard to maintain because it is probably doing too much. The single responsibility principle (https://en.wikipedia.org/wiki/Single-responsibility_principle)
states that a module, a class, or even a method should have a single, well-defined responsibility. It should do just one thing 
and have only one reason to change.

The first step when attemping to refactor complex conditional code is to identify the common goal of each of the 
execution paths.

Code that uses if/elif/else usually has a common goal that is implemented in different ways in each logical path. The code (in our example)
converts a User object to its string representation using a different format in each logical path.

Based on the goal, you look for a common interface that can be used to replace each of the paths. The UserSerializer example requires an interface that 
takes a User object and returns a string.

Once you have a common interface, you provide separate implementations for each logical path. In our case we will provide an implementation to serialize 
to JSON and another for XML.

Then, you provide a separate component that decides the concrete implementation to use based on the specified format. This component evaluates 
the value of format and returns the concrete implementation identified by its value.