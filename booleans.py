# True / False / None
# 0 / 0.0 etc are also considered 'False'
# empty sets or seqencies / collections are also 'False'

a = []
if (a):
    print("this is considered true")
else:
    print("this is false")

# we could also do :-
print(bool(a))
print(bool(0))
print(bool(""))
print(bool(1))
print(bool("Richard"))

r = range(0)
if (r):
    print("This could be true ...")
else:
    print("A range of '0' is considered to be false")

if (True):
    print("This is True")

# booelan operations - 'and' / 'or' / 'not'
print(bool(1) and bool("ABC")) # this returns 'True'
print(bool(0) or bool(1)) # also returns 'True'
print(bool(1) and not bool(1)) # returns 'False'