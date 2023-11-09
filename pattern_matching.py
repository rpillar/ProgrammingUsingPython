# simple pattern matching - using literal values
# note that the 'type' of the 'match' can be _anything_ - so we can match to
# strings, booleans, None .....
x = 1
match x:
    case 0:
        print("Its zero")
    case "Zero":
        print("Its a literal zero")
    case 1:
        print("Its one")
    case None:
        print("None")
    case _:
        print("no match")

# 'capture' pattern
name = "Dawn"
match name:
    case "":
        print("No name supplied")
    case "Richard" | "Rich" as s:
        print(f"Hello {s}")
    case name:
        print(f"Hello {name}")

# 'class' patterns
class Square:
    def __init__(self, side):
        self.side = side

    def getarea(self):
        return self.side * self.side

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getarea(self):
        return self.width * self.height

shapes = [Square(6), Rectangle(3,4), Rectangle(5,5),Square(2)]

## we can use 'pattern matching' to process each 'different' shape
## the 'matching' performs a type of 'isInstance' checking ...
for shape in shapes:
    match shape:
        case Square():
            print(f"The square has an area of : {shape.getarea()}")
        case Rectangle():
            print(f"The rectangle has an area of : {shape.getarea()}")
        case _:
            print(f"Unrecognized shape found : {type(shape)}")

# 'sequence' patterns
import math
operations = [
    ["Add", 1, 2, 3, 4, 5],
    ["Mul", 5, 6],
    ["Add", 10, 20],
    ["Sqrt", 9],
]

# note - where we have a variable number of arguments we use the '*' notation
# also note that for the 'Add' operation it is possible to specify that at
# least 'one' argument is required by using a 'case' statment like :-
#   case "Add", num, *nums
result = 0
for op in operations:
    match op:
        case "Mul", num1, num2:
            result = num1 * num2
        case "Sqrt", num:
            result = math.sqrt(num)
        case "Add", *nums:
            result = sum(nums)
        case _:
            continue

    print(f"{op} : {result}")

# pattern 'guards' (use 'shapes' data for this example)
# note that the ordering of the patterns / guards is important - the first one that
# matches will be used ....
for shape in shapes:
    match shape:
        case Square(side=s) if s > 5:
            print(f"Large square has an area of : {shape.getarea()}")
        case Square():
            print(f"The square has an area of : {shape.getarea()}")
        case Rectangle(width=w, height=h) if w == h:
            print(f"The rectangle is a square - area of {shape.getarea()}")
        case Rectangle():
            print(f"The rectangle has an area of : {shape.getarea()}")
        case _:
            print(f"Unrecognized shape found : {type(shape)}")

# a more 'shopisticated' example - note that as Python treats booleans as integers then 
# checking for booleans need to be performed before integers :-
dataset = ["UPPER", 5, "Mixed Case", True, None]
for d in dataset:
    match d:
        case str() as s if s.isupper():
            print(f"{d} : is UpperCase")
        case str():
            print(f"{d} : is a mixed case / lower case string")
        case bool():
            print(f"{d} : is a Boolean")
        case int():
            print(f"{d} : is an integer")
        case _:
            print("No Match")