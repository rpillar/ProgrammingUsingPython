# there are four ways that a Class may represent itself as a string
# - object.__str__(self) -> called on str(object), print(object), f"{object}"
# - object.__repr__(self) -> repr(object)
# - object.__format__(self, format_spec) -> format(object, format_spec)
# - object.__bytes__(self) -> bytes(object)

class Person():
    def __init__(self, name, age):
        self.name = name 
        self.age  = age

p1 = Person("Richard", 21)
print(p1)       # <__main__.Person object at 0x10d1acc10>
print(repr(p1)) # <__main__.Person object at 0x103344c10>

# create a 'custom' repr function for a class
class Car():
    def __init__(self):
        self.brand = "Ford"
        self.model = "Cortina"
        self.age = 2

    def __repr__(self):
        return f"<Car Class - brand:{self.brand}, model:{self.model}, age:{self.age}>"

    def __str__(self):
        return f"Person {self.brand}, {self.model} is {self.age} years old."

    def __bytes__(self):
        data = f"Car {self.brand}:{self.model}:{self.age}"
        return bytes(data.encode("utf-8"))

c1 = Car()
print(repr(c1))  # makes use of the 'custom' __repr__ function
print(str(c1))   # makes use of the 'custom' __str__ function
print(c1)        # makes use of the 'custom' __str__ function
print(bytes(c1)) # b'Car Ford:Cortina:2'
