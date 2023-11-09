# using the __str__ and __repr__ magic mathods

class Book:
    def __init__(self, title, author, price) -> None:
        self.title = title
        self.author = author
        self.price = price

    # use the __str__ method to return a string - a 'user' friendly description
    # of the object
    def __str__(self) -> str:
        return f"{self.title} by {self.author}, costs {self.price}"

    # use the __repr__ method to return an object representation - 'developer' focused
    def __repr__(self) -> str:
        return f"{type(self)} : title={self.title}, author={self.author}, price={self.price}"

b1 = Book("War and Peace", "Leo Tolstoy", 39.99)

# the 'print' function will call the 'default' or 'custom' __str__ function as appropriate
# by default - <__main__.Book object at 0x109e10c10>
# with the 'custom' __str__ function - War and Peace by Leo Tolstoy, costs 39.99
print(b1)

# we can call these 'magic' methods directly
print(str(b1))
print(repr(b1))


