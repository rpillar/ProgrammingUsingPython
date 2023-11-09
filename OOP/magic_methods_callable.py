# call an object as if it was a function - useful if you have an
# object whose attributes are often updated together.

from typing import Any


class Book:
    def __init__(self, title: str, author: str, price: float) -> None:
        super().__init__()
        self.title = title
        self.author = author 
        self.price = price
        self._discount = 0.1

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}, costs {self.price:.2f}"

    # the __call__ methods allows us to 'call' the object like a function
    def __call__(self, title: str, author: str, price: float) -> Any:
        self.title = title
        self.author = author 
        self.price = price

    
b1 = Book("War and Peace", "Leo Tolstoy", 39.99)
b2 = Book("Catcher in the Rye", "JD Sallinger", float(24))

print(b1)
b1("Anna Karenia", "Leo Tolstoy", 31.99) # 'call' the object ...
print(b1)