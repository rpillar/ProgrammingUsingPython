"""
Here we have a simplified version of a Factory where we use functions rather then classes to define
the different behaviours that are required.
For simple cases this is probably the 'best' solution
"""

import json
import xml.etree.ElementTree as et

class User:
    def __init__(self, fname, lname, age) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age


class UserSerializer:
    def serialize(self, user, format):
        serializer = get_serializer(format)
        return serializer(user)


# Note - none of these functions / methods used the 'self' parameter - this is a good
# indication that they should not be methods of the UserSerializer class and therefore can
# become 'external' functions - part of a `serializer` module maybe

# Note that in this example we are using 'functions' to perform the serialization - we are not
# strictly creating an 'interface' that 'concrete' versions of the Serializer can build on.

def get_serializer(format):
    formats = {
        "JSON": _serialize_to_json,
        "XML": _serialize_to_xml
    }
    return formats[format]


def _serialize_to_json(user):
    payload = {
        'fname': user.fname,
        'lname': user.lname,
        'age': user.age
    }
    return json.dumps(payload)


def _serialize_to_xml(user):
    user_info = et.Element('user', attrib={'fname': user.fname})
    lname = et.SubElement(user_info, 'lname')
    lname.text = user.lname
    age = et.SubElement(user_info, 'age')
    age.text = user.age
    return et.tostring(user_info, encoding='unicode')


u1 = User("Richard", "Pillar", "21")
serializer = UserSerializer()

data = serializer.serialize(u1, 'JSON')
print(f"User (JSON) : {data}") # User (JSON) : {"fname": "Richard", "lname": "Pillar", "age": "21"}

u2 = User("Dawn", "Pillar", "22")
serializer = UserSerializer()

data = serializer.serialize(u2, 'XML')
print(f"User (XML) : {data}") # User (XML) : <user fname="Dawn"><lname>Pillar</lname><age>22</age></user>