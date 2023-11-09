# create classes that represent some sort of 'data' hierarchy
# that can (amoung other things) remove unnecessary duplication ...

# create 'base' class
class Publication:
    def __init__(self, title, price) -> None:
        self.title = title
        self.price = price


# another 'base' class - inheriting from 'Publication'
class Periodical(Publication):
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


# classes
class Book(Publication):
    def __init__(self, title, price, author, pages) -> None:
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price, period, publisher)


class Newspaper(Periodical):
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price, period, publisher)

book1 = Book("Touching the void", 12.55, "John Doe", "Harper")
print(book1.author)