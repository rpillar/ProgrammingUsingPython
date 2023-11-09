# template strings -  as described in PEP 292

from string import Template

# using 'f' strings
name = "Richard"
print(f"My name is {name}")

# using template strings - if you don't need all the bells and whistles ...
t1 = Template("My name is ${name} and I am ${age} years old")
s1 = t1.substitute(name="Richard", age=21)
print(s1)

# with template strings we can also use a dictionary to hold the values tht we want to 'substitute' in
d = {"name": "Dawn", "age": 22}
s2 = t1.substitute(d)
print(s2)