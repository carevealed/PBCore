__author__ = 'lpsdesk'
from PBCore.PBCore import *

testPBRelation1 = pbcoreRelation()

# IC1 = pbcoreDescriptionDocument()
IC1 = pbcoreDescriptionDocument()
IC1.set_pbcoreAssetType(PB_Element(tag="pbcoreAssetType", value="Media Object"))
pbcoreRelationType1 = PB_Element(tag="pbcoreRelationType", value="Has Part")
testPBRelation1.set_pbcoreRelationType(pbcoreRelationType1)

pbrelationIdentifier1 = PB_Element(tag="pbcoreRelationIdentifier", value="cscrm_000012_r1")
testPBRelation1.set_pbcoreRelationIdentifier(pbrelationIdentifier1)
IC1.add_pbcoreRelation(testPBRelation1)

testPBRelation2 = pbcoreRelation()
testPBRelation2.set_pbcoreRelationType(PB_Element(tag="pbcoreRelationType", value="Has Part"))
testPBRelation2.set_pbcoreRelationIdentifier(PB_Element(tag="pbcoreRelationIdentifier", value="cscrm_000012_r2"))
IC1.add_pbcoreRelation(testPBRelation2)


temp = PB_Element(tag="pbcoreAssetDate", value="Unknown")
IC1.add_pbcoreAssetDate(temp)

temp = PB_Element(["source", "CAVPP"], ["annotation", "Object Identifier"], tag="pbcoreIdentifier", value="cscrm_000012")
IC1.add_pbcoreIdentifier(temp)

temp = PB_Element(["source", "CAVPP"], ["annotation", "Project Identifier"], tag="pbcoreIdentifier", value="cavpp002541")
IC1.add_pbcoreIdentifier(temp)

temp = PB_Element(["source", "CDL"], ["annotation", "Object ARK"], tag="pbcoreIdentifier", value="ark:/13030/c88w3g4p")
IC1.add_pbcoreIdentifier(temp)

temp = PB_Element(["titleType", "main"], tag="pbcoreTitle", value="Sugar Pine Special : logging and saw mills")
IC1.add_pbcoreIdentifier(temp)

temp = PB_Element(["typeType", "Main"], tag="pbcoreDescription", value="Film footage includes the Yosemite Sugar Pine Lumber Company line, "
                                                 "which was organized in 1934 and abandoned in 1942 in Merced Falls, "
                                                 "Mariposa County. Shows historic logging and saw mill operations.")
IC1.add_pbcoreIdentifier(temp)

creator = pbcoreCreator()
creator.set_creator(PB_Element(tag="creator", value="Unknown"))
creator.add_creatorRole(PB_Element(tag="creatorRole", value="Producer"))
IC1.add_pbcoreCreator(creator)

rightsSum = pbcoreRightsSummary()
rightsSum.add_rightsSummary(PB_Element(["annotation", "Copyright Statement"],
                                      tag="rightsSummary", value="Copyright status unknown. This work may be protected "
                                                                 "by the U.S. Copyright Law (Title 17, U.S.C.). In "
                                                                 "addition, its reproduction may be restricted by "
                                                                 "terms of gift or purchase agreements, donor "
                                                                 "restrictions, privacy and publicity rights, "
                                                                 "licensing and trademarks. This work is accessible "
                                                                 "for purposes of education and research. Transmission "
                                                                 "or reproduction of works protected by copyright "
                                                                 "beyond that allowed by fair use requires the written "
                                                                 "permission of the copyright owners. Works not in the "
                                                                 "public domain cannot be commercially exploited "
                                                                 "without permission of the copyright owner. "
                                                                 "Responsibility for any use rests exclusively with "
                                                                 "the user. California State Railroad Museum attempted "
                                                                 "to find rights owners without success but is eager "
                                                                 "to hear from them so that we may obtain permission, "
                                                                 "if needed. Upon request to "
                                                                 "Library.CSRM@parks.ca.gov, digitized works can be "
                                                                 "removed from public view if there are rights issues "
                                                                 "that need to be resolved."))
IC1.add_pbcoreRightsSummary(rightsSum)

newPart = CAVPP_Part()
newPart.add_pbcoreIdentifier(PB_Element(["source", "CAVPP"], ["annotation", "Object Identifier"], tag="pbcoreIdentifier", value="cscrm_000012_r2"))
newPart.set_pbcoreTitle(PB_Element(["titleType", "Main"], tag="pbcoreTitle", value="Sugar Pine Special : logging and saw mills"))
newPart.add_pbcoreDescription(PB_Element(tag="pbcoreTitle", value="Film footage includes the Yosemite Sugar Pine Lumber Company line, which was organized in 1934 and abandoned in 1942 in Merced Falls, Mariposa County. Shows historic logging and saw mill operations." ))

newInstatiation = pbcoreInstantiation(instantiationType="Physical Asset")
newInstatiation.add_instantiationIdentifier(PB_Element(["source", "CAVPP"], ["annotation", "Object Identifier"], tag="instantiationIdentifier", value="cscrm_000012_r1"))
newInstatiation.set_instantiationPhysical(PB_Element(tag="instantiationPhysical", value="Film 16mm"))
# newInstatiation.set_instantiationLocation(PB_Element(tag="instantiationLocation", value="California State Railroad Museum Library"))
newInstatiation.set_instantiationMediaType(PB_Element(tag="instantiationMediaType", value="Moving Image"))
newInstatiation.set_instantiationGenerations(PB_Element(tag="instantiationGenerations", value="Unknown"))
newInstatiation.set_instantiationTimeStart(PB_Element(tag="instantiationTimeStart", value="00:00:00"))
newInstatiation.set_instantiationDuration(PB_Element(tag="instantiationDuration", value="00:07:28"))
newInstatiation.set_instantiationColors(PB_Element(tag="instantiationColors", value="B&amp;W"))
newInstatiation.set_instantiationTracks(PB_Element(tag="instantiationTracks", value="Silent"))
newInstatiation.set_instantiationChannelConfiguration(PB_Element(tag="instantiationChannelConfiguration", value="No AudioNone"))
newEsstrack = InstantiationEssenceTrack()
newEsstrack.set_essenceTrackType(PB_Element(tag="essenceTrackType", value="Video"))
newEsstrack.set_essenceTrackFrameRate(PB_Element(["unitsOfMeasure", "fps"], tag="essenceTrackFrameRate", value="29.97fps"))
newEsstrack.set_essenceTrackBitDepth(PB_Element(tag="essenceTrackBitDepth", value="8"))
newEsstrack.set_essenceTrackAspectRatio(PB_Element(tag="essenceTrackAspectRatio", value="4:3"))
newEsstrack.set_essenceTrackTimeStart(PB_Element(tag="essenceTrackTimeStart", value="00:00:00"))
newEsstrack.set_essenceTrackDuration(PB_Element(tag="essenceTrackDuration", value="00:07:28"))
newEsstrack.add_essenceTrackAnnotation(PB_Element(["annotationType", "Frame Count"], tag="essenceTrackAnnotation", value="13427"))
newEsstrack.add_essenceTrackAnnotation(PB_Element(["annotationType", "Scan Type"], tag="essenceTrackAnnotation", value="Progressive"))
newEsstrack.add_essenceTrackAnnotation(PB_Element(["annotationType", "Color Sampling"], tag="essenceTrackAnnotation", value="Color Sampling"))
newEsstrack.add_essenceTrackAnnotation(PB_Element(["annotationType", "Frame Size Vertical"], tag="essenceTrackAnnotation", value="540"))
newEsstrack.add_essenceTrackAnnotation(PB_Element(["annotationType", "Frame Size Horizontal"], tag="essenceTrackAnnotation", value="720"))
newInstatiation.add_instantiationEssenceTrack(newEsstrack)
newPart.add_pbcoreInstantiation(newInstatiation)


IC1.add_pbcore_part(newPart)
dom = minidom.parseString(IC1.xml_string())
print dom.toprettyxml()


