# 'Abstract Base Class' - 
# - create a class 'blueprint' where sub-classes must provide the 'concrete'
#   implementations of methods ...
# - use to enforce a set of 'constraints' on a class hierarchy - in this case
#   each class that inherits from 'Shape' must implement its 'own' version of the
#   'calcArea' method.

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self) -> None:
        super().__init__()

    # this 'decorator' means that there is no implementation in the
    # 'base' class and that each 'sub-class' must provide its own
    # implementation
    @abstractmethod
    def calcArea(self):
        pass

class Square(Shape):
    def __init__(self, side) -> None:
        super().__init__()
        self.side = side

    def calcArea(self):
        return self.side * self.side


# so its NOT possible to instantiate an instance of an abstract class
try:
    shape = Shape()
except TypeError:
    print("Trying to instantiate a abstract class failed.")

# 
sq1 = Square(12.5)
print(f"The area of my square is : {sq1.calcArea()}")