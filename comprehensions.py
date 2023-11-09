# comprehensions can be used on lists, dictionaries and sets and provide a
# concise way to derive a 'new' sequence of values from an existing sequence
# of values.
# using our temperature conversion algorithm from earlier we can do :-

## list comprehensions

# fahrenheit to celcius
f2c_temps = [(t * 9/5) + 32 for t in [32, 65, 104, 212]]

print(f2c_temps)

# or to square a list of even numbers
evens = [2,4,6,8,10]
evens_squared = [e ** 2 for e in evens]
print(evens_squared)

# we can also add a 'predeicate' condition
odds = [3,5,7,9,11,15,17,19]
odds_squared = [e ** 2 for e in odds if e > 3 and e < 17]
print(odds_squared)

## dictionary comprehensions

# so to map all Celcius temps to their equiv Fahrenheit temp ...
# and create a dictionary where the key is the Celcius temp ....
temp_dict = {t: (t * 9/5) + 32 for t in range(1,20)}
print(temp_dict)

# we can also merge two dictionaries using comprehensions
team1 = {"Jones": 11, "Smith": 1}
team2 = {"Doe": 4, "Harris": 10, "Stevens": 6}
new_team = {k: v for team in (team1, team2) for k, v in team.items()}
print(new_team)

## set comprehensions

# for set comprehensions the 'comprehension' is 'surrounded by' '{}' (curly braces)
# in this case duplicate temps in the input list are filtered out.
ctemps = [5,10,12,14,10,23,41,30,12,24,12,18,29]
c2f_temps = {(t * 9/4) + 32 for t in ctemps} 
print(c2f_temps)

my_str = "The quick brown fox jumped over the lazy dog"
chars = {c.upper() for c in my_str if not c.isspace()}
print(chars)