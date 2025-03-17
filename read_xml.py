import xmlschema
import xml.etree.ElementTree as ET

xsd = xmlschema.XMLSchema("test.xsd")

xt = ET.fromstring(requests.get(url1).text)
print("xml1 valid=", xsd.is_valid(xt), sep="")