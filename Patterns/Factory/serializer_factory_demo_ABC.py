import json
import xml.etree.ElementTree as et

from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def serialize(self, data):
        """return a serialized version of the data in the appropriate format"""

class JSONSerializer(Serializer):
    def serialize(self, data):
        payload = {
            'fname': data.fname,
            'lname': data.lname,
            'age': data.age
        }
        return json.dumps(payload)

class XMLSerializer(Serializer):
    def serialize(self, data):
        user_info = et.Element('user', attrib={'fname': data.fname})
        lname = et.SubElement(user_info, 'lname')
        lname.text = data.lname
        age = et.SubElement(user_info, 'age')
        age.text = data.age
        return et.tostring(user_info, encoding='unicode')

class SerializerFactory(ABC):
    """
    A Factory that represents a Serializer
    Note that the Factory does not maintain any of the instances it creates
    """
    def get_serializer(self) -> Serializer:
        """returns a new Serializer instance"""

class JSONSerializerFactory(SerializerFactory):
    def get_serializer(self) -> Serializer:
       return JSONSerializer()

class XMLSerializerFactory(SerializerFactory):
    def get_serializer(self) -> Serializer:
       return XMLSerializer()

class User:
    def __init__(self, fname, lname, age) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age


def read_format() -> SerializerFactory:

    factories = {
        "json": JSONSerializerFactory(),
        "xml": XMLSerializerFactory()
    }

    while True:
        format = input("Enter the desired output format (json/xml): ")
        if format in factories:
            return factories[format]
        print(f"Unknown format : {format}")

    return 

def main(factory: SerializerFactory) -> None:
    u1 = User("Richard", "Pillar", "21")

    serializer = factory.get_serializer()
    print(f"data : {serializer.serialize(u1)}")

if __name__ == '__main__':
    factory = read_format()
    main(factory)

    
"""
Note :- separate 'creation' from 'use' ...... so that you can 'use' those objects without knowing the specifics.
We have here an 'Factory pattern' example that makes use of an 'abstract base class' (ABC).
"""
