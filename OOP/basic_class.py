# create a 'basic' class ...

# note - the __init__ function is a object 'initialiser` rather than a 'constructor' - 
# the object has already been created when this method is called. 

import random

class Book:
    # properties can be defined at a 'class' level - shared by 'all' instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # a 'class' method to return the 'book types' - note use of 'cls' not 'self'
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES


    # note - 'title', 'author' 'pagecount' and 'price' are all 'instance' variables - that is they
    # are all associated with a particular 'instance' of the class ....
    def __init__(self, title, author, pagecount, price, booktype):
        self.title = title
        self.author = author 
        self.pagecount = pagecount
        self.price = price
        # any attribute (or method name) that starts with a double underscore cannot be 
        # accessed 'outside' of this class (or in subclasses) so I wouldn't be able to
        # do this - print(b2.__library_code) -> an AttributeError exception would be
        # raised.
        self.__library_code = ''.join((random.choice('abcnhsajhgeyg') for i in range(8)))

        # here an instance variable is validated against a class-level property.
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

    ## instance methods ...
    # note that instance attributes can be defined elsewhere in the class

    def set_discount(self, discount):
        """
        populate a 'private' attribute on the object - a discount percentage
        """
        self._discount = discount

    def get_library_code(self):
        return self.__library_code

    def get_price(self):
        """
        get_price - if this instance of the BOOK class has an attribute of
        '_discount' then apply its value to reduce the book's price.
        """
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount / 100)
        else:
            return self.price  


## do 'things' with the Book class ##

b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.99, "HARDCOVER")
print(f"This object is of type {type(b1)} and has the title of {b1.title}")
b1.set_discount(10)
print(f"Book : {b1.title} now costs {b1.get_price():.2f}")

# trying to access a 'double underscore' attributes directly will fail ...
try:
    print(f"My books library code is {b1.__library_code}")
except AttributeError:
    print(f"An exception was raised when trying to access the '__library_code' attribute.")

# accessing a 'double underscore' attribute using a class instance method will work
print(f"My library code is : {b1.get_library_code()}")

# sometimes it is useful to what 'type' an object is :-
print(type(b1))  # <class '__main__.Book'>

# and you can check if two objects have the same type
b2 = Book("The Catcher In The Rye", "SD Sallinder", 423, 12.99, "EBOOK")
print(type(b1) == type(b2)) # True

# whilst it is possible to parse the type string it is 'cleaner' to make use of
# the 'isInstance' method (a builtin)
print(isinstance(b1, Book)) # True
print(isinstance(b1, object)) # True - everything is a 'subclass' of the 'object' type

# call a class method
print(b1.getbooktypes())
# or ....
print(Book.getbooktypes())

try:
    b3 = Book("Jack and Jill went up the hill", "James Ross", 44, 3.99, "CHILDRENS")
except ValueError as e:
    print("Incorrect Book Type used when instansiating a instance of a BOOK : {e}")

# just a note about 'static' methods
# define a method with the @staticmethod decorator - ensures that the method 'exists' 
# outside of the class / instance definitions. This can be useful if you want access
# a 'singleton' or if you want to place a method in a class as a means of 'giving' it a 
# particular namespace - rather hna creating a 'global' function ....
