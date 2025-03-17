# something that can be a useful tool but can cause issues - use with care ....

class A:
    def __init__(self) -> None:
        super().__init__()
        self.foo = "Foo"
        self.name = "Class A"

class B:
    def __init__(self) -> None:
        super().__init__()
        self.bar = "Bar"
        self.name = "Class B"

# class 'C' inherits from class A and class B ...
# note - as seen below pythons 'method resolution order' means that when we have multiple inheritance where classes
# might have methods with the same name the 'first' inherited class (class A in our example) 'wins' and its 'name' 
# method / property is used. 
class C(A, B):
    def __init__(self) -> None:
        super().__init__()

    def showmyprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name) # 'Class A' - note the value printed here is based on the order in which the inheritance is defined

c = C()
c.showmyprops()

# it is possible to inspect the 'method resolution order' of a class
print(C.__mro__) # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
