from xml.dom.minidom import parse
from PBCore import *

test = parse("/Users/lpsdesk/PycharmProjects/PBcore/sample_records/cscrm_000012_PBCore.xml")

print test.toxml()