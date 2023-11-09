# how to create functions where the number of arguments is 'variable'

# '*args' - the name 'args' is used (by convention) but is not mandatory for the 'list' with a 
# variable number of arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(addition(1,2,3,4))
print(addition(3,2,4,5,2,7,4,5))

# we can also do this - 'literal unpacking' :-
arr = [1,2,3,4,5]
print(addition(*arr))

# note that if you have positional AND variable arguments then the 'variable' arguments must always 
# come after the positional args
