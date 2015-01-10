__author__ = 'Henry'

from xml.dom.minidom import parse

dom1 = parse("sample_records/cscrm_000012_PBCore.xml")

print dom1.toprettyxml()