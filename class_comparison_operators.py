# same as the class numeric operators it is possible to override
# class 'comparison' operators such as :-
# - object.__gt__(self, other) : self > other
# - object.__ge__(self, other) : self >= other
# .....

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Richard", 21)
p2 = Person("Dawn", 22)
print(dir(p1)) # ['__class__', .... '__ge__', '__ne__' ...]

# using the 'default' comparison operators
print(p1 == p2) # False

class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        """
        Custom __eq__ function - compare by 'name' only
        Returns boolean - true / False
        """
        return self.name == other.name

e1 = Employee("Richard", 21)
e2 = Employee("Richard", 22)

# using the 'custom' comparison operator
print(e1 == e2) # True

# note that 'custom' comparison operators can / will affect sort order of an
# array of objects.