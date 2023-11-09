# define an 'enumeration'
from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    KIWI = 4
    PEAR = auto()

print(Fruit.APPLE) # Fruit.APPLE
print(type(Fruit.APPLE)) # <enum 'Fruit'>
print(repr(Fruit.APPLE)) # <Fruit.APPLE: 1>

print(Fruit.APPLE.name, Fruit.APPLE.value) # APPLE 1

# Note that you cannot have duplicate 'names' in an Enum - but you can
# have duplicate 'values'
# However if you want to prevent duplicate 'values' then you can use the 
# 'unique' decorator.

# if you don't care what the 'values' are then you use the 'auto' function
print(repr(Fruit.PEAR))

# you can use enums as dictionary 'keys'
fruit_dict = {}
fruit_dict[Fruit.APPLE] = 'Coxes'
print(fruit_dict)
print(fruit_dict[Fruit.APPLE])