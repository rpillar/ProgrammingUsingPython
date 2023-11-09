# it is possible to create 'immutable' dataclasses - add the 'frozen'
# attribute to the dataclass decorator. 
# Attributes cannot be amended inside (class functions) or outside the class.

import datetime
from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: datetime.date


p1 = Person("Richard", datetime.date(2023, 3, 21))
print(p1)
print(type(p1.date_of_birth))

try:
    p1.name = "Dawn"
except FrozenInstanceError:
    print("Cannot amend a 'frozen' / 'immutable' dataclasses object instance")

