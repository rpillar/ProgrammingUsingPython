# Note that when we use 'inheritance' we (generally) model an 'is' relationship - 
# a Book 'is a' Publication .....

# 'composition' however is where we build objects out of 'other' objects. So a 'Book'
# object may have an 'author' attribute that is actually an instance of a Author 'object'.
# This models more of a 'has' relationship - rather than defining all of the object attributes
# within the class hierarchy.

class Author:
    def __init__(self, fname, sname) -> None:
        self.fname = fname
        self.sname = sname

    def __str__(self) -> str:
        return f"{self.fname} {self.sname}"


class Book:
    def __init__(self, title, price, author=None) -> None:
        self.title = title
        self.price = price
        self.author = author

        self.chapters = []

    def addchapter(self, name, pages) -> None:
        self.chapters.append((name, pages))

    """
    Override the default __str__ method. Note that because the Author class also
    has its own __str__ method we only need to provide the attribute - rather than
    self.author.fname (for example)
    """
    def __str__(self) -> str:
        return f"Title : {self.title}, Author : {self.author}, Cost : {self.price}"


b1 = Book("War and Peace", 39.00, Author("Leo", "Tolstoy"))
print(b1)