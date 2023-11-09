# there are a number of class attribute functions :-
# - object.__getattribute__(self, attr) - object.attr
# - object.__getattr__(self, attr)      - object.attr
# - object.__setattr__(self, attr, val) - object.attr = val
# - object.__delattr__(self)            - del object.attr
# - object.__dir__(self)                - dir(object)

class Person():
    def __init__(self):
        self.name = "Richard"
        self.age  = 21

p1 = Person()
print(p1.name)    # calls object.__getattr__
p1.name = "James" # calls object.__setattr__
print(p1.name)

class MyColour():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # create a 'custom' getattr function
    def __getattr__(self, attr):
        """
        Custom __getattr__ function to enable the use of a 'computed'
        attribute - 'rgbcolor'.
        Returns a tuple containing the red, blue, green values
        """
        if attr == "rgbcolor":
            return(self.red, self.green, self.blue)

    def __setattr__(self, attr, val):
        """
        Custom __setattr__ function
        Allows the user the set the RGB color values by using the
        'rgbcolor' attribute and passing a 3 value tuple with the
        appropriate red, green, blue values.
        """
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

# Note - with the introduction of a 'custom' __setattr__ method it is necessary to
# have the 'else' clause call 'super()' so that the constructor (__init__) works as
# expected

mc = MyColour()
print(mc.rgbcolor)
print(mc.red)

mc.rgbcolor = (30, 44, 99)
print(mc.rgbcolor)

# Note - it is possible to create a custom __dir__ function - useful in this case
# where the class makes use of 'custom' attributes