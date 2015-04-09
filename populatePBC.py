__author__ = 'Henry'

from xml.dom.minidom import parse
from PBCore.PBCore import *

dom1 = parse("sample_records/cscrm_000012_PBCore.xml")

print dom1.toprettyxml()