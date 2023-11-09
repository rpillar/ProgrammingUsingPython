# by default objects don't know how to compare themselves but we can add methods :-
# - __eq__ - check for equality between two objects
# - __ge__ - is obj1 >= obj2
# - __lt__ - is obj1 < obj2

# Note - all the 'magic' methods are defined here - https://docs.python.org/3/reference/datamodel.html#special-method-names

class Book:
    def __init__(self, title, author, price) -> None:
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self) -> str:
        return f"{type(self)} : title={self.title}, author={self.author}, price={self.price}"

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Book):
            raise ValueError("Cannot compare objects of different types.")

        return (self.title == __o.title and
            self.author == __o.author and
            self.price == __o.price)

    # compare on 'price'
    def __ge__(self, __o: object) -> bool:
        if not isinstance(__o, Book):
            raise ValueError("Cannot compare objects of different types.")

        return self.price >= __o.price 

    def __lt__(self, __o: object) -> bool:
        if not isinstance(__o, Book):
            raise ValueError("Cannot compare objects of different types.")

        return self.price < __o.price 


b1 = Book("War and Peace", "Leo Tolstoy", 39.99)
b2 = Book("War and Peace", "Leo Tolstoy", 39.99)
b3 = Book("The Catcher in the Rye", "JD Salinger", 19.99)
print(repr(b1))
print(repr(b2))
print(repr(b3))

# when we compare objects b1 and b2 - the 'default' response is False because Python
# compares object instances and understands (in this case) that 'b1' is not 'b2'. We 
# can change this by implementing a 'custom' __eq__ method in our class. 
# In the Book class when comparing the values of the object attributes the comparison
# returns True.
print(b1 == b2)
print(b1 == b3) # False

try:
    print(b1 == 41)
except ValueError:
    print("When trying to compare different objects types we get a ValueError exception")

# perform '>=' / '<' comparisons using our 'custom' magic methods
print(b2 >= b3) # True
print(b1 < b3) # False

# having added these magic methods we can now sort our books - note that the 'builtin' sort function
# uses the '<' operator to perform sorting
books = [b1, b3, b2]
# sort the books - on price
books.sort()
print([book.title for book in books])
