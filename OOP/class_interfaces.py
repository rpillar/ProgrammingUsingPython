# from java .....

# Another way to achieve abstraction in Java, is with interfaces.
# An interface is a completely "abstract class" that is used to group related methods with empty bodies
# so something like .....
# interface Animal {
#  public void animalSound(); // interface method (does not have a body)
#  public void sleep(); // interface method (does not have a body)
# }
#
# To access the interface methods, the interface must be "implemented" (kinda like inherited) by 
# another class with the implements keyword (instead of extends). 
# The body of the interface method is provided by the "implement" class:
#Pig "implements" the Animal interface
# class Pig implements Animal {
#   public void animalSound() {
#     // The body of animalSound() is provided here
#     System.out.println("The pig says: wee wee");
#   }
#   public void sleep() {
#     // The body of sleep() is provided here
#     System.out.println("Zzz");
#   }
# }

########

# python doesn't have explicit support for interfaces as a language feature - ensuring that a
# a class provides a concrete instance of a specific method (or set of methods). Abstract Base Classes and 
# multiple inheritance can help us here.

from abc import ABC, abstractmethod

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class Shape(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class Circle(Shape, JSONify):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius  ** 2)

    def toJSON(self):
        return f"{{\" circle\" : {str(self.calcArea())} }}"


c = Circle(12.44)
print(f"{c.calcArea():.2f}")
print(c.toJSON())