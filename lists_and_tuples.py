# List and tuples are essentially Python's most use data types.
# a list is a collection of arbitrary objects, something like an array in 
# many other programming languages but more flexible

## LISTS ##
#  =====  #
###########

# define a 'list'
from re import A


l1 = [1,2,3,4]
print(type(l1))
print(l1)

# so :-
## Lists are ordered.
l2 = ['Richard', 'Dawn', 'Sam', "Veronica"]
print(l2[0])   # 'Richard'

## Lists can contain any arbitrary objects. A list can contain all sorts of types from
## strings, numbers, dictionaries, tuples, functions etc.
l3 = ['Richard', {"name": "Richard", "age": 21}, 1, 2, 3]
print(l3)
print(type(l3[1])) # <class 'dict'>

## List elements can be accessed by index.
l4 = [1,2,3,4,5,6,7]
print(l4[0])     # print the 'first' element in the list - '1'
print(l4[-1])    # prints the 'last' element - in thsi case '5'
print(l4[1:3])   # we can access a 'slice' - [2, 3] - note this is an 'from and up to but not including' slice
print(l4[1:6:2]) # access a 'stride' - [2, 4, 6]
print(l4[::-1])  # using indexing to reverse a list

print(l4[:] is l4) # returns 'False' - note that 'l4[:]' returns a 'copy' of l4 whereas if you did this on a 
                   # string it returns a reference to the same object.

## Lists can be nested to arbitrary depth.
l5 = [0, [1], [2, 3, [4, 5, [6, 7]]]]
print(l5[2][2][0])  # prints '4'

## Lists are mutable (can be changed).
l6 = [0, 1, 2, 3, 4, 5, 6]
l6[0] = 99
print(l6)  # [99, 1, 2, 3, 4, 5, 6]

del l6[-1] # remove the last element in this list
print(l6)  # [99, 1, 2, 3, 4, 5]

l6[0:4] = ["Richard"]
print(l6)  # the list becomes - ['Richard', 4, 5], the first elements are replaced by the string 'Richard'
l6[0:1] = ["Sam", "Dawn", "Dave"]
print(l6)  # it is possible to replace a single element with multiple elements - ['Sam', 'Dawn', 'Dave', 4, 5]
l6[0:0] = [99, 98, 97, 96]
print(l6)  # [99, 98, 97, 96, 'Sam', 'Dawn', 'Dave', 4, 5] - add an element (or elements) at a particular index without replacing anything
           # by specifying a 'zero' length slice.

## Lists are dynamic.

## other python operators can be used on lists - in the same way as strings - this is to be expected as
## they are both special cases of a more general object type called an iterable
lx = [1,2,3,4,5,6,7,8,9,0]
print(0 in lx)       # returns True
print(99 in lx)      # returns False
print (99 not in lx) # returns True

ly = lx + [99]
print(ly)            # list concatenation

print(len(lx))       # 10
print(max(lx))       # 9
print(min(lx))       # 0

# if you want to perform a change to the list that replaces a single element with more then one element then once again we can use a 'slice'
ly = [1,2,3,4,5]
ly[0:1] = [6,7,8,9]
print(ly) # [6, 7, 8, 9, 2, 3, 4, 5]

# to 'add' elements to a list - just specify a zero length 'slice'
lz = [1,2,3,4]
lz[4:4] = [5,6,7,8]
print(lz) # [1, 2, 3, 4, 5, 6, 7, 8]

# NOTE - a list MUST be concatenated with a list .... (or more accurately - an 'iterable')
# to add data to a list - at the start
lz = ['x','y'] + lz
print(lz) # ['x', 'y', 1, 2, 3, 4, 5, 6, 7, 8]
# to add data to a list - or at the start
lz += [21]
print(lz) # ['x', 'y', 1, 2, 3, 4, 5, 6, 7, 8, 21]

s1 = {1,2,3} # a 'set' - another 'iterable'
lz += s1
print(lz) # ['x', 'y', 1, 2, 3, 4, 5, 6, 7, 8, 21, 1, 2, 3]

# It should not be forgotten that Python has a number of methods that can be used to modify lists
la = [1,2,3]
la.append('Richard') # add an element to the 'end' of a list
print(la)            # [1, 2, 3, 'Richard']

# other methods include extend(<iterable>) / insert(<index>. <object>) / remove(<object>) etc. 

## TUPLES ##
#  ======  #
############

# note that a 'tuple' is defined using parentheses (not square brackets)
t1 = (1,2,3,4)
print(type(t1)) # <class 'tuple'>

# NOTE - the indexing and slicing operations that we have seen with lists also work with tuples
# BUT tuples are immutable - cannot be changed - so we cannot 'add' / 'remove' elements
try:
    t1[1] = 12
except TypeError:
    print("A TypeError Exception has occurred ....")

# if you should (not sure why) wnat to create a tuple with a single element then :-
t2 = (1)
print(type(t2)) # <class 'int'>
t3 = (1,)
print(type(t3)) # <class 'tuple'> - note that we have a trailing ',' in t3 - this is what denaotes that it is a 'tuple' rather than a plain 'int'

a,b = 1,2
print(f"a is {a} and b is {b}") # a is 1 and b is 2 - note that we have to have the 'same' number of elements on the left / right sides.

# a curious bit of idiomatic Python - variable swapping ...
a = "Richard"
b = "Dawn"
a,b = b,a 
print(f"a is {a} and b is {b}") # a is Dawn and b is Richard


