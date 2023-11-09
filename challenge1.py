# write a fuction :-
# accepts a variable number of args - strings and numbers
# accepts a single keyword-only arg - return a 'unique-only' result
# returns a string - combine all the args into a single string
# has a docstring
# If the 'unique' arg is True (default is False) then the result
# (the combined string) will not contain any duplicate characters

from argparse import ArgumentParser
from collections import OrderedDict

def string_combiner(*args, unique=False) -> str:
    """
    Function to combine a set of arguments into a string. 
    Arguments :-
    args - a Namespace object (tuple) from the ArgumentParser
    Returns a string with all arguments (no spaces)
    """

    # only process strings and ints
    l = []
    for e in args[0]:
        if isinstance(e, int):
            l.append(str(e))
        if isinstance(e, str):
            l.append(e)

    if unique == True:
        s = ''.join([el for el in l])
        return ''.join(OrderedDict.fromkeys(s))
    
    return ''.join([el for el in l])


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-args', nargs="+", required=True, help='a set of strings / numbers separated by a space') 
    parser.add_argument('-unique', action='store_const', const=True, required=False, help='if True remove all duplicate characters')
    args = parser.parse_args()
    
    s = string_combiner(args.args, unique=args.unique)
    print(s)
