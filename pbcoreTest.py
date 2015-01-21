__author__ = 'lpsdesk'
from PBCore.PBCore import *

testPBRelation1 = pbcoreRelation()

# IC1 = pbcoreDescriptionDocument()
IC1 = pbcoreDescriptionDocument()
IC1.setpbcoreAssetType(PB_Element(tag="pbcoreAssetType", value="Media Object"))
pbcoreRelationType1 = PB_Element(tag="pbcoreRelationType", value="Has Part")
testPBRelation1.setpbcoreRelationType(pbcoreRelationType1)

pbrelationIdentifier1 = PB_Element(tag="pbcoreRelationIdentifier", value="cscrm_000012_r1")
testPBRelation1.setpbcoreRelationIdentifier(pbrelationIdentifier1)



testPBRelation2 = pbcoreRelation()
testPBRelation2.setpbcoreRelationType(PB_Element(tag="pbcoreRelationType", value="Has Part"))
testPBRelation2.setpbcoreRelationIdentifier(PB_Element(tag="pbcoreRelationIdentifier", value="cscrm_000012_r2"))



temp = PB_Element(tag="pbcoreAssetDate", value="Unknown")
temp.addAttribute(key="dataType", value="Created")
IC1.addpbcoreAssetDate(temp)

temp = PB_Element(tag="pbcoreIdentifier", value="cscrm_000012")
temp.addAttribute(key="source", value="CAVPP")
temp.addAttribute(key="annotation", value="Object Identifier")
IC1.addpbcoreIdentifier(temp)

temp = PB_Element(tag="pbcoreIdentifier", value="cavpp002541")
temp.addAttribute(key="source", value="CAVPP")
temp.addAttribute(key="annotation", value="Project Identifier")
IC1.addpbcoreIdentifier(temp)

temp = PB_Element(tag="pbcoreIdentifier", value="ark:/13030/c88w3g4p")
temp.addAttribute(key="source", value="CDL")
temp.addAttribute(key="annotation", value="Object ARK")
IC1.addpbcoreIdentifier(temp)

temp = PB_Element(tag="pbcoreTitle", value="Sugar Pine Special : logging and saw mills")
temp.addAttribute(key="titleType", value="Main")
IC1.addpbcoreIdentifier(temp)

temp = PB_Element(tag="pbcoreDescription", value="Film footage includes the Yosemite Sugar Pine Lumber Company line, "
                                                 "which was organized in 1934 and abandoned in 1942 in Merced Falls, "
                                                 "Mariposa County. Shows historic logging and saw mill operations.")
temp.addAttribute(key="titleType", value="Main")
IC1.addpbcoreIdentifier(temp)

IC1.addpbcoreRelation(testPBRelation1)
IC1.addpbcoreRelation(testPBRelation2)



dom = minidom.parseString(IC1.xmlString())
print dom.toprettyxml()


