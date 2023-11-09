# strings and bytes in python
b = bytes([0x41, 0x42, 0x43, 0x44])
s = "This is a string"

print(b)
print(s)

# note that you cannot treat the 'bytes' value as a string (even though it is 'ABCD')
# the variable b (in this case) needs to be properly decoded before you can use it with a string

try:
    print(s + b)
except TypeError:
    print("I got an error")

# so we can do this ...
print(f"{s}, {b.decode('utf-8')}")

# the opposite of 'decode' is 'encode' - so we can 'encode' our string
s2 = s.encode("utf-8")
print(s2)

print(s2.__class__) # <class 'bytes'>
