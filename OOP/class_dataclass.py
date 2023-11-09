# in version 3.7 Python introduced 'dataclasses' - create classes
# that represent data .... creating more 'concise' classes

# note - dataclasses give us 'sensible' __repr__ and __eq__ methods

# It is also possible to provide default values for attributes. In this example
# it would be possible to create a Book instance - passing no arguments.
# However when using 'defaults', attributes that 'do not' have defaults 
# must come first in the attribute declaration
# Another way to provide a default value is to use the 'Field' class - and
# even provide a function that will 'build' the default for us.

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))


@dataclass
class Book:
    title: str = "Title"
    author: str = "Author"
    pages: int = field(default=0)
    price: float = field(default_factory=price_func)

    # dataclasses gives us (and executes) a '__init__' function but what about
    # if you want to add some 'custom' initialization to your class.
    # To enable this dataclasses gives us the '__post_init__' function - add a 
    # attribute.
    def __post_init__(self) -> None:
        self.description = f"{self.title} by {self.author}"


b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.99)
b2 = Book("Cather in the Rye", "JD Sallinger", 250, float(24))
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.99)

print(b1.title)
print(b1) # Book(title='War and Peace', author='Leo Tolstoy', pages=1225, price=39.99)
print(b1.description) # War and Peace by Leo Tolstoy
print(b1 == b3) # True

b4 = Book()
print(b4) # Book(title='Title', author='Author', pages=0, price=0.0)