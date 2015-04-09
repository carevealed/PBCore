from xml.etree. ElementTree import ElementTree, Element, tostring

root = Element("person")
tree = ElementTree(root)
root.text = "s"
# root.append(PB_Element("name"))
# print tree

print tostring(root)
