# if your classes need to support mathmatical / numerical operations then you
# can override the appropriate special class methods

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Point x:{self.x},y:{self.y}>"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

p1 = Point(12,19)
print(p1) # <Point x:12,y:19>

# using the 'default' '+' operator we get an error like :-
# - TypeError: unsupported operand type(s) for +: 'Point' and 'Point'

# When we add a custom '__add__' method we get the expected result.
p2 = Point(6,54)
p3 = p1 + p2
print(p3)

# When we add a custom '__sub__' method we get the expected result.
p4 = Point(8,22)
p5 = Point(5,18)
p6 = p4 - p5
print(p6)

# to perform 'in-place' operations we need to add the '__i***__' methods
# in this example we have created a 'custom' __iadd__ method
p7 = Point(10,15)
p8 = Point(1,2)
print(p7)
p7 += p8
print(p7)