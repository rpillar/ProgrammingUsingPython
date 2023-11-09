# whenever python attempts to retrieve the value of a class attribute the
# '__getattribute__' method is called. Similarly whenever an attribute value 
# is set the '__setattribute__' method is called.
# Classes can define 'custom' versions of these methods

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

    # Note - cannot 'directly' access the attr name becuase this would get
    # us into a recursive loop. THis is why we have to call '__getattribute__'
    # on the 'super' class.
    def __getattribute__(self, __name: str) -> Any:
        if __name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)

        return super().__getattribute__(__name)

    # check the 'type' of the price attribute ....
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "price":
            if type(__value) is not float:
                raise ValueError("Price value 'type' must be a float")

        return super().__setattr__(__name, __value)

    # __getattr__ gets called only is a __getattribute__ method does not exist
    # or if __getattribute__ throws an exception or the class attribute
    # does not exist.
    def __getattr__(self, __name: str) -> Any:
        return f"Attribute : {__name} does not exist on this class."



b1 = Book("War and Peace", "Leo Tolstoy", 39.99)
b2 = Book("Cather in the Rye", "JD Sallinger", float(24))
print(b1) # note - price (from the __str__ method is discounted)
print(b2)

print(b1.randomAttr) # Attribute : randomAttr does not exist on this class.

