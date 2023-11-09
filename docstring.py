# see PEP 257 for Docstring conventions

def sumX(a, b=0) -> int:
    return sum(a,b)

# use the '__doc__' dunder method to display a function / method / class docstring
# nothing in this case  - prints None 
print(sumX.__doc__)

def sumY(a,b) -> int:
    """
    Add two integers together and return the result.
    Arguments :-
    a - a positive integer
    b - a positive integer
    Returns the sum of arguments a and b

    >>> sumY(2,3)
    5
    """
    return a + b

# NOTE - also it is possible to add 'doctest's to the docstring as we have done in the sumY function. The 'test'
# is included by placing (on a new line) the 'interactive python prompt' followed by a function call - and then
# a new line with the expected result.
# run the 'doctest' as follows - 'python -m doctest -v docstring.py'

print(sumY.__doc__)