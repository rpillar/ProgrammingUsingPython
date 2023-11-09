# lambda - small anonymous functions, can be passed as arguments (like callbacks)
# to define :-

x = lambda x,y : x + y
print(x) # <function <lambda> at 0x10975beb0>

# so you could do (convert celius to fahrenheit):-
def convert(temp):
    return (temp * 9/5) + 32

print(list(map(convert, [0,12,34,100])))

# this works but it is possible to write this simple function as an 'in-line' lambda :-
print(list(map(lambda t : (t * 9/5) + 32, [0,12,34,100])))