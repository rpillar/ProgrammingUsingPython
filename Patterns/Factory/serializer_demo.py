import json
import xml.etree.ElementTree as et

class User:
    def __init__(self, fname, lname, age) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age

    
class UserSerializer:
    def serialize(self, user, format):
        if format == 'JSON':
            user_info = {
                'fname': user.fname,
                'lname': user.lname,
                'age': user.age
            }
            return json.dumps(user_info)
        elif format == 'XML':
            user_info = et.Element('user', attrib={'fname': user.fname})
            lname = et.SubElement(user_info, 'lname')
            lname.text = user.lname
            age = et.SubElement(user_info, 'age')
            age.text = user.age
            return et.tostring(user_info, encoding='unicode')
        else:
            raise ValueError(format)


u1 = User("Richard", "Pillar", "21")
serializer = UserSerializer()

data = serializer.serialize(u1, 'JSON')
print(f"User (JSON) : {data}") # User (JSON) : {"fname": "Richard", "lname": "Pillar", "age": "21"}

u2 = User("Dawn", "Pillar", "22")
serializer = UserSerializer()

data = serializer.serialize(u2, 'XML')
print(f"User (XML) : {data}") # User (XML) : <user fname="Dawn"><lname>Pillar</lname><age>22</age></user>

"""
The code above is hard to maintain because it is doing too much. The single responsibility principle states that a module, a 
class, or even a method should have a single, well-defined responsibility. It should do just one thing and have only 
one reason to change.

The .serialize() method in UserSerializer class will require changes for many different reasons. This increases the risk of introducing 
new defects or breaking existing functionality when changes are made. The ideal situation would be if any of those changes in 
requirements could be implemented without changing the .serialize() method.
"""