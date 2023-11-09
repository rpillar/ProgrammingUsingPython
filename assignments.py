# assign a value to a variable
x = 1

print(x)

## PEP 572 ##
# how we have the 'walrus' operator - must be part of an expression - that allows an
# assignment to be part of a condition / loop (for example)
if (x := 10):
    print(x)

# the example above doesn't make any sense ...
while (mystr := input()) != "exit":
    print(mystr)

# another example where using the 'walrus' operator can make code cleaner and more expressive
a = [1,3,5,6,7,2,3,8,9,22,9,12,44,32,64]
data = {
    "length": (l := len(a)),
    "sum": (s := sum(a)),
    "average": (s / l)
}
print(data)