From FreeCodeCamp.org :-

The Strategy Design Pattern is a behavioral design pattern. It allows you to dynamically change the behavior of an object by encapsulating it into different strategies.

This pattern enables an object to choose from multiple algorithms and behaviors at runtime, rather than statically choosing a single one.

It is based on the principle of composition over inheritance. It defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime. The core 
idea behind this pattern is to separate the algorithms from the main object. This allows the object to delegate the algorithm's behavior to one of its contained strategies.

In simpler terms, the Strategy Design Pattern provides a way to extract the behavior of an object into separate classes that can be swapped in and out at runtime. 
This enables the object to be more flexible and reusable, as different strategies can be easily added or modified without changing the object's core code.

A shopping cart application may use the Strategy Design Pattern to encapsulate credit card, PayPal, and cryptocurrency payment methods into separate strategies 
that can be swapped at runtime. The application's payment processing system would delegate the payment processing logic to the current payment method's strategy, 
allowing for easy modification and extension of the payment processing logic.