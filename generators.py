# generators

# use cases
## reading from a file - using a generator ensures that the 'file handle' will be closed
## if an exception occurs ...

def generator_function():
    yield "hello"
    yield "world"
    print("That was a Hello from World")

gen = generator_function()
print(f"a generator function looks like this : {type(gen)}")

# run this a number of times to _iterate_ through the function (not sure if this is an adequate description)
print(f"The next yield is : {next(gen)}")

# so we could do this like :-
for nxt in generator_function():
    print(f"The yield value is : {nxt} ")

# processing a file
## assume a data row where elements are delimited by ':'
## here is a class that might represent a 'point'
from typing import NamedTuple

class DataPoint(NamedTuple):
    x: float
    y: float
    z: float

def read_data(file):
    for row in file:
        fields =  row.rstrip().split(':')   # split the 'row' into a list
        fields = [float(f) for f in fields] # coerce (if necessary) each element in the list to a float
        yield DataPoint._make(fields)       # just process 'this' row

def process_points(points):
    with open(points) as file:
        for row in read_data(file):
            print(f"The current point is : {row}")

process_points("points.txt")

# another example - multiply by two
def powers_of_two():
    x = 1
    while True:
        yield x
        print("I'm continuing from this point - calculating the next sum")
        x *= 2

p_gen = powers_of_two()
next(p_gen)

# calculate the squares of a set of numbers
def squares(x=0):
    while x < 10:
        x = x + 1
        yield x*x

sq_gen = squares()
[s for s in sq_gen] # create a list of the squares    
list(squares())     # or create the list of squares this way

# replace those 'brackets' with 'parens' and you get a generator comprehension
sq_gen_2 = (x*x for x in range(5))
next(sq_gen_2)

sum_sqs = sum(x*x for x in range(5)) 

# just an experiment - count the elements in a list - just like using len()
l1 = [1,2,3,4,5,5,6,7,8,8]
sum([1 for _ in l1])
len(l1)

# another possible use is for parsing / processing files - for example
# we have a file like :-
## 1
## 2
## # this is a comment
## 
## nan
##
## 43
# a mix of numbers, comments etc
def process_file():
    with open("mixed.txt") as file:
        nums = (row.partition('#')[0].rstrip() for row in file)
        nums = (row for row in nums if row)
        nums = (float(row) for row in nums)
        s = sum(nums)
        print(f"the sum of the nums in the file is : {s}")

process_file()