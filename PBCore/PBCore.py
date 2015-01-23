# from xml.dom.minidom import parse, Element as elmt, Document, Node
from collections import OrderedDict
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

__author__ = 'California Audiovisual Preservation Project'
# PBCore metadata
from xml.dom import minidom


# class PBData():
#     def __init__(self):
#         self.elements = []
#         self.addData("dafsd")
#         pass
#
#     def printData(self):
#         if self.elements:
#             for element in self.elements:
#                 print element
#
#     def addData(self, newDataMember):
#         self.elements.append(newDataMember)
#
#     def xml(self):
#
#         # branch = etree.ElementTree(self.pbcoreRelationType)
#         XML = self._makeXML()
#         return XML
#
#     def xmlString(self):
#         XML = self._makeXML()
#         return etree.tostring(XML)




class PBCore():
    """

    :Description: This is the main class for creating PBCore objects
    :PBCore Homepage: http://pbcore.org/
    """
    def __init__(self):
        """

        :return: None
        """
        # self.root = None
        self.intellectualContent = None
        self.intellectualProperty = None
        self.extensions = None
        self.instantiation = None

    def getIntellectualContent(self):
        """

        :return:
        """
        return self.intellectualContent

    def setIntellectualContent(self, newIntellectualContent):
        """

        :param          newIntellectualContent:
        :type           newIntellectualContent: pbcoreDescriptionDocument
        :Example Value: ""
        :return:        None
        """
        
        if isinstance(newIntellectualContent, pbcoreDescriptionDocument):
            self.intellectualContent = newIntellectualContent
        else:
            raise TypeError("setIntellectualContent expected type: pbcoreDescriptionDocument")

    def getIntellectualProperty(self):
        """

        :return:
        """
        return self.intellectualProperty

    def setIntellectualProperty(self, newIntellectualProperty):
        """

        :param          newIntellectualProperty:
        :type           newIntellectualProperty: IntellectualProperty
        :Example Value: ""
        :return:        None
        """
        
        if isinstance(newIntellectualProperty, IntellectualProperty):
            self.intellectualProperty = newIntellectualProperty
        else:
            raise TypeError("setIntellectualProperty expected type: IntellectualProperty")

    def getextensions(self):
        """

        :return:
        """
        return self.extensions

    def setextensions(self, newextensions):
        """

        :param          newextensions:
        :type           newextensions: Extensions
        :Example Value: ""
        :return:        None
        """
        
        if isinstance(newextensions, pbcoreExtension):
            self.extensions = newextensions
        else:
            raise TypeError("setextensions expected type: pbcoreExtension")

    def getinstantiation(self):
        """

        :return:
        """
        return self.instantiation

    def setinstantiation(self, newinstantiation):
        """

        :param          newinstantiation:
        :type           newinstantiation: pbcoreInstantiation
        :Example Value: ""
        :return:        None
        """
        
        if isinstance(newinstantiation, pbcoreInstantiation):
            self.instantiation = newinstantiation
        else:
            raise TypeError("setinstantiation expected type: pbcoreInstantiation")




##################################
# root Elements
##################################

# Unsure if this is needed!

# class RootElements():
#     def __init__(self):
#         self.pbcoreDescriptionDocument = None
#         # URI: http://pbcore.org/v2/elements/pbcoreDescriptionDocument
#
#         self.pbcoreCollection = None
#         # URI: http://pbcore.org/v2/elements/pbcoreCollection
#
#         self.pbcoreInstantiationDocument = None
#         # URI: http://pbcore.org/v2/elements/pbcoreInstantiationDocument
#
#
#     def getpbcoreDescriptionDocument(self):
#         return self.pbcoreDescriptionDocument
#
#     def setpbcoreDescriptionDocument(self, newpbcoreDescriptionDocument):
#         # create Docstring for setpbcoreDescriptionDocument
#         self.pbcoreDescriptionDocument = newpbcoreDescriptionDocument
#
#     def getpbcoreCollection(self):
#         return self.pbcoreCollection
#
#     def setpbcoreCollection(self, newpbcoreCollection):
#         # create Docstring for setpbcoreCollection
#         self.pbcoreCollection = newpbcoreCollection
#
#     def getpbcoreInstantiationDocument(self):
#         return self.pbcoreInstantiationDocument
#
#     def setpbcoreInstantiationDocument(self, newpbcoreInstantiationDocument):
#         # create Docstring for setpbcoreInstantiationDocument
#         self.pbcoreInstantiationDocument = newpbcoreInstantiationDocument

##################################
# Intellectual Content
##################################

class pbcoreDescriptionDocument():
    """
    :Description:
    :URL: http://pbcore.org/elements/
    """

    # @property
    def __init__(self):
        """
        @type           self.pbcoreAssetType:           PB_Element
        @type           self.pbcoreAssetDate:           PB_Element
        @type           self.pbcoreIdentifier:          PB_Element
        @type           self.pbcoreTitle:               PB_Element
        @type           self.pbcoreSubject:             PB_Element
        @type           self.pbcoreDescription:         PB_Element
        @type           self.pbcoreGenre:               PB_Element
        @type           self.pbcoreRelation:            PB_Element
        @type           self.pbcoreCoverage:            PB_Element
        @type           self.pbcoreAudienceLevel:       PB_Element
        @type           self.pbcoreAudienceRating:      PB_Element
        @type           self.pbcoreAnnotation:          PB_Element
        @type           self.pbcoreCreator:             pbcoreCreator
        @type           self.pbcoreContributor:         pbcoreContributor
        @type           self.pbcorePublisher:           pbcorePublisher
        @type           self.pbcoreRightsSummary:       pbcoreRightsSummary
        @type           self.pbcoreExtension:           PB_Element
        @type           self.pbcorePart:                PB_Element

    def getpbcoreAssetType
        :return: None
        """
        self.pbcoreAssetType = None
        self.pbcoreAssetDate = []
        self.pbcoreIdentifier = []
        self.pbcoreTitle = []
        self.pbcoreSubject = None
        self.pbcoreDescription = []
        self.pbcoreGenre = None
        self.pbcoreRelation = []
        self.pbcoreCoverage = []
        self.pbcoreAudienceLevel = None
        self.pbcoreAudienceRating = None
        self.pbcoreAnnotation = None
        self.pbcoreCreator = []
        self.pbcoreContributor = []
        self.pbcorePublisher = []
        self.pbcoreRightsSummary = []
        self.pbcoreExtension = []
        self.pbcorePart = None

        # Valid attributes
        self.pbcoreDescriptionDocumentAttributesRequired = [
            # Must Contain:
            "xmlns",                        # (text, specific value: "http://pbcore.org/PBCore/PBCoreNamespace.html")
            "xsi",                          # (text, specific value: "http://www.w3.org/2001/XMLSchema-instance")
            "schemaLocation"                # (text, specific value: "http://pbcore.org/PBCore/PBCoreNamespace.html")
        ]

        self.pbcoreDescriptionDocumentAttributesOptional = [
            # 5 or less optional attributes, specific:
            "collectionTitle",              # (text, may be empty)
            "collectionDescription",        # (text, may be empty)
            "collectionSource",             # (text, may be empty)
            "collectionRef",                # (text, may be empty)
            "collectionDate"                # (text, may be empty)
        ]

        self.pbcoreAssetTypeAttributesOptional = [
            # May Contain:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

        self.pbcoreAssetDateAttributesOptional = [
            # May Contain
            "dateType"                      # ( may be empty)
        ]

        self.pbcoreIdentifierAttributesRequired = [
            # Must Contain:
            # 1 required attribute, specific:
            "source"                        # (text, may be empty)
        ]

        self.pbcoreIdentifierAttributesOptional = [
            # May Contain:
            # 3 or less optional attributes, specific:
            "ref"                           # (text, may be empty)
            "version"                       # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

        self.pbcoreTitleAttributesOptional = [
            # May Contain:
            # 1 or less optional attributes, specific:
            "titleType",                    # ( may be empty)

            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation",                   # (text, may be empty)

            # 3 or less optional attributes, specific:
            "startTime",                    # (text, may be empty)
            "endTime",                      # (text, may be empty)
            "timeAnnotation"                # (text, may be empty)

        ]

        self.pbcoreSubjectAttributesOptional = [
            # May Contain:
            # 1 or less optional attributes, specific:
            "subjectType"                   # (text, may be empty)

            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation",                   # (text, may be empty)

            # 3 or less optional attributes, specific:
            "startTime",                    # (text, may be empty)
            "endTime",                      # (text, may be empty)
            "timeAnnotation"                # (text, may be empty)
        ]

        self.pbcoreDescriptionAttributesOptional = [
            # May Contain:
            # 5 or less optional attributes, specific:
            "descriptionType",              # (text, may be empty)
            "descriptionTypeSource",        # (text, may be empty)
            "descriptionTypeRef",           # (text, may be empty)
            "descriptionTypeVersion",       # (text, may be empty)
            "descriptionTypeAnnotation",    # (text, may be empty)

            # 5 or less optional attributes, specific:
            "segmentType",                  # (text, may be empty)
            "segmentTypeSource",            # (text, may be empty)
            "segmentTypeRef",               # (text, may be empty)
            "segmentTypeVersion",           # (text, may be empty)
            "segmentTypeAnnotation",        # (text, may be empty)

            # 3 or less option attributes, specific:
            "startTime",                    # (text, may be empty)
            "endTime",                      # (text, may be empty)
            "timeAnnotation",               # (text, may be empty)

            # 1 or less optional attributes, specific:
            "annotation"                    # (text, may be empty)
        ]

        self.pbcoreGenreAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation",                   # (text, may be empty)

            # 3 or less optional attributes, specific:
            "startTime",                    # (text, may be empty)
            "endTime",                      # (text, may be empty)
            "timeAnnotation"                # (text, may be empty)
        ]

        self.pbcoreAudienceLevelAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

        self.pbcoreAudienceRatingAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:

            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

        self.pbcoreAnnotationAttributesOptional = [
            # May Contain:
            # 2 or less optional attributes, specific:
            "annotationType",               # ( may be empty)
            "ref"                           # ( may be empty)
        ]

    def getpbcoreAssetType(self):
        return self.pbcoreAssetType

    def getpbcoreAssetTypeElement(self):
        return self.pbcoreAssetType.getETreeElement()

    def setpbcoreAssetType(self, newpbcoreAssetType):
        """

        :param          newpbcoreAssetType:
        :type           newpbcoreAssetType: PB_Element
        :Example Value: PB_Element(tag="pbcoreAssetType", value="Media Object")
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreassettype/
        :return:        None
        """

        if isinstance(newpbcoreAssetType, PB_Element):
            self.pbcoreAssetType = newpbcoreAssetType
        else:
            raise TypeError("Expected Type: PB_Element")

    def getpbcoreAssetDate(self):
        """

        :return: str
        """
        return self.pbcoreAssetDate

    def getpbcoreAssetDateElement(self):
        """

        :return:    xml.etree.ElementTree.Element
        """
        return self.pbcoreAssetDate.getETreeElement()

    def addpbcoreAssetDate(self, newpbcoreAssetDate):
        """

        :param          newpbcoreAssetDate:
        :type           newpbcoreAssetDate: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreassetdate/
        :return:        None
        """
        # TODO: Give example value for addpbcoreAssetDate

        if isinstance(newpbcoreAssetDate, PB_Element):
            self.pbcoreAssetDate.append(newpbcoreAssetDate)
        else:
            raise TypeError("Expected Type: PB_Element")

    def getpbcoreIdentifier(self):
        """

        :return:
        """
        return self.pbcoreIdentifier

    def addpbcoreIdentifier(self, newIdentifier):
        """

        :param          newIdentifier:
        :type           newIdentifier: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreidentifier/
        :return:        None
        """
        # TODO: Give example value for addpbcoreIdentifier

        if isinstance(newIdentifier, PB_Element):
            self.pbcoreIdentifier.append(newIdentifier)
        else:
            raise TypeError("Expected Type: PB_Element")

    def getpbcoreTitle(self):
        """

        :return: None
        """
        return self.pbcoreTitle

    def addpbcoreTitle(self, newTitle):
        """

        :param          newTitle:
        :type           newTitle: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoretitle/
        :return:        None
        """
        # TODO: Give example value for addpbcoreTitle

        if isinstance(newTitle, PB_Element):
            self.pbcoreTitle.append(newTitle)
        else:
            raise TypeError("Expected Type: PB_Element")

    def getpbcoreSubject(self):
        """

        :return: None
        """
        return self.pbcoreSubject

    def setpbcoreSubject(self, newpbcoreSubject):
        """

        :param          newpbcoreSubject:
        :type           newpbcoreSubject: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreSubject/
        :return:        None
        """
        # TODO: Give example value for setpbcoreSubject
        # TODO: Create Docstring for setpbcoreSubject
        if isinstance(newpbcoreSubject, PB_Element):
            self.pbcoreSubject = newpbcoreSubject
        else:
            raise TypeError("Expected Type: PB_Element")

    def getpbcoreDescription(self):
        """

        :return:
        """
        return self.pbcoreDescription

    def addpbcoreDescription(self, newDescription):
        """

        :param          newDescription:
        :type           newDescription: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreDescription
        :return:        None
        """
        # TODO: Give example value for addpbcoreDescription
        if isinstance(newDescription, PB_Element):
            self.pbcoreDescription.append(newDescription)
        else:
            raise TypeError("Expected Type: PB_Element")

    def getpbcoreGenre(self):
        """

        :return:    None
        """
        return self.pbcoreGenre

    def getpbcoreGenreElement(self):
        """

        :return:    xml.etree.ElementTree.Element
        """
        return self.pbcoreGenre.getETreeElement()

    def setpbcoreGenre(self, newpbcoreGenre):
        """

        :param          newpbcoreGenre:
        :type           newpbcoreGenre: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreGenre
        :return:        None
        """
        # TODO: Give example value for setpbcoreGenre
        # TODO: Create Docstring for setpbcoreGenre
        if isinstance(newpbcoreGenre, PB_Element):
            self.pbcoreGenre = newpbcoreGenre
        else:
            raise TypeError("Expected Type: PB_Element")

    def getpbcoreRelation(self):
        """

        :return:
        """
        return self.pbcoreRelation

    def addpbcoreRelation(self, newpbcoreRelation):
        """

        :param          newpbcoreRelation:
        :type           newpbcoreRelation: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreRelation
        :return:        None
        """
        # TODO: Give example value for addpbcoreRelation

        if isinstance(newpbcoreRelation, pbcoreRelation):
            self.pbcoreRelation.append(newpbcoreRelation)
        else:
            raise TypeError("Expected Type: pbcoreRelation")

    def getpbcoreCoverage(self):
        """

        :return:
        """
        return self.pbcoreCoverage

    def addpbcoreCoverage(self, newpbcoreCoverage):
        """

        :param          newpbcoreCoverage:
        :type           newpbcoreCoverage: pbcoreCoverage
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreCoverage
        :return:        None
        """
        # TODO: Give example value for addpbcoreCoverage

        if isinstance(newpbcoreCoverage, pbcoreCoverage):
            self.pbcoreCoverage.append(newpbcoreCoverage)
        else:
            raise TypeError("Expected type: pbcoreCoverage")

    def getpbcoreAudienceLevel(self):
        """

        :return:
        """
        return self.pbcoreAudienceLevel

    def getpbcoreAudienceLevelElement(self):
        """

        :return:    xml.etree.ElementTree.Element
        """
        return self.pbcoreAudienceLevel.getETreeElement()

    def setpbcoreAudienceLevel(self, newpbcoreAudienceLevel):
        """

        :param          newpbcoreAudienceLevel:
        :type           newpbcoreAudienceLevel: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreAudienceLevel
        :return:        None
        """
        # TODO: Give example value for setpbcoreAudienceLevel
        # TODO: Create Docstring for setpbcoreAudienceLevel
        if isinstance(newpbcoreAudienceLevel, PB_Element):
            self.pbcoreAudienceLevel = newpbcoreAudienceLevel
        else:
            raise TypeError("Expected type: PB_Element")

    def getpbcoreAudienceRating(self):
        """

        :return:    None
        """
        return self.pbcoreAudienceRating

    def getpbcoreAudienceRatingElement(self):
        """

        :return:    xml.etree.ElementTree.Element
        """
        return self.pbcoreAudienceRating.getETreeElement()

    def setpbcoreAudienceRating(self, newpbcoreAudienceRating):
        """

        :param          newpbcoreAudienceRating:
        :type           newpbcoreAudienceRating: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreAudienceRating
        :return:        None
        """
        # TODO: Give example value for setpbcoreAudienceRating
        # TODO: Create Docstring for setpbcoreAudienceRating
        if isinstance(newpbcoreAudienceRating, PB_Element):
            self.pbcoreAudienceRating = newpbcoreAudienceRating
        else:
            raise TypeError("Expected type: PB_Element")

    def getpbcoreAnnotation(self):
        """

        :return:
        """
        return self.pbcoreAnnotation

    def getpbcoreAnnotationElement(self):
        """

        :return:    xml.etree.ElementTree.Element
        """
        return self.pbcoreAnnotation.getETreeElement()

    def setpbcoreAnnotation(self, newpbcoreAnnotation):
        """

        :param          newpbcoreAnnotation:
        :type           newpbcoreAnnotation:    PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreAnnotation
        :return:        None
        """
        # TODO: Give example value for setpbcoreAnnotation
        # TODO: Create Docstring for setpbcoreAnnotation
        if isinstance(newpbcoreAnnotation, PB_Element):
            self.pbcoreAnnotation = newpbcoreAnnotation
        else:
            raise TypeError("Expected type: PB_Element")

    def getpbcoreCreator(self):
        """

        :return:
        """
        return self.pbcoreCreator

    def addpbcoreCreator(self, newpbcoreCreator):
        """

        :param          newpbcoreCreator:
        :type           newpbcoreCreator: pbcoreCreator
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecreator/
        :return:        None
        """

        if isinstance(newpbcoreCreator, pbcoreCreator):
            self.pbcoreCreator.append(newpbcoreCreator)
        else:
            raise TypeError("Expected Type: pbcoreCreator")

    def getpbcoreContributor(self):
        """

        :return:
        """
        return self.pbcoreContributor

    def addpbcoreContributor(self, newpbcoreContributor):
        """

        :param          newpbcoreContributor:
        :type           newpbcoreContributor: pbcoreContributor
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreContributor
        :return:        None
        """
        # TODO: Give example value for addpbcoreContributor
        if isinstance(newpbcoreContributor, pbcoreContributor):
            self.pbcoreContributor.append(newpbcoreContributor)
        else:
            raise TypeError("Expected Type: pbcoreContributor")

    def getpbcorePublisher(self):
        """

        :return:
        """
        # TODO: Create Docstring for getpbcorePublisher
        return self.pbcorePublisher

    def addpbcorePublisher(self, newpbcorePublisher):
        """

        :param          newpbcorePublisher:
        :type           newpbcorePublisher: pbcorePublisher
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorePublisher
        :return:        None
        """
        # TODO: Give example value for addpbcorePublisher
        if isinstance(newpbcorePublisher, pbcorePublisher):
            self.pbcorePublisher.append(newpbcorePublisher)
        else:
            raise TypeError("Expected Type: pbcorePublisher")

    def getpbcoreRightsSummary(self):
        """

        :return:
        """
        # TODO: Create Docstring for getpbcoreRightsSummary
        return self.pbcoreRightsSummary

    def addpbcoreRightsSummary(self, newpbcoreRightsSummary):
        """

        :param          newpbcoreRightsSummary:
        :type           newpbcoreRightsSummary: pbcoreRightsSummary
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreRightsSummary
        """
        # TODO: Give example value for addpbcoreRightsSummary
        # TODO: Create an example Value for addpbcoreRightsSummary

        if isinstance(newpbcoreRightsSummary, pbcoreRightsSummary):
            self.pbcoreRightsSummary.append(newpbcoreRightsSummary)
        else:
            raise TypeError("Expected Type: pbcoreRightsSummary")

    def _makeXML(self):
        branch = Element("pbcoreDescriptionDocument")
        if self.pbcoreAssetType:
            branch.append(self.getpbcoreAssetTypeElement())

        if self.pbcoreAssetDate:
            for node in self.pbcoreAssetDate:
                branch.append(node.getETreeElement())

        if self.pbcoreIdentifier:
            for node in self.pbcoreIdentifier:
                branch.append(node.getETreeElement())

        if self.pbcoreTitle:
            for node in self.pbcoreTitle:
                branch.append(node.getETreeElement())

        if self.pbcoreSubject:
            branch.append(self.getpbcoreAssetTypeElement())

        if self.pbcoreDescription:
            for node in self.pbcoreDescription:
                branch.append(node.getETreeElement())

        if self.pbcoreGenre:
            branch.append(self.getpbcoreGenre())

        if self.pbcoreRelation:
            for node in self.pbcoreRelation:
                branch.append(node.xml())

        if self.pbcoreCoverage:
            for node in self.pbcoreCoverage:
                branch.append(node.xml)

        if self.pbcoreAudienceLevel:
            for node in self.pbcoreAudienceLevel:
                branch.append(node)

        if self.pbcoreAudienceRating:
            for node in self.pbcoreAudienceRating:
                branch.append(node)

        if self.pbcoreAnnotation:
            for node in self.pbcoreAnnotation:
                branch.append(node)

        if self.pbcoreCreator:
            for node in self.pbcoreCreator:
                branch.append(node.xml())

        if self.pbcoreContributor:
            for node in self.pbcoreContributor:
                branch.append(node.xml)

        if self.pbcorePublisher:
            for node in self.pbcorePublisher:
                branch.append(node.xml)

        if self.pbcoreRightsSummary:
            for node in self.pbcoreRightsSummary:
                branch.append(node.xml())

        if self.pbcoreExtension:
            for node in self.pbcoreExtension:
                branch.append(node.xml)

        if self.pbcorePart:
            for node in self.pbcorePart.getNode:
                branch.append(node)
        # branch.append(self.pbcoreRelationIdentifier.getETreeElement())
        # branch.append(self.pbcoreRelationType.getETreeElement())
        return branch

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()

        return etree.tostring(XML)

    def addpbcoreExtension(self, newpbcoreExtension):
        """

        :param          newpbcoreExtension:
        :type           newpbcoreExtension: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/
        :return:        None
        """

        if isinstance(newpbcoreExtension, pbcoreExtension):
            self.pbcoreExtension.append(newpbcoreExtension)
        else:
            raise TypeError("Expected type: pbcoreExtension")

    def getpbcoreExtension(self):
        """

        :return:
        """

        return self.pbcoreExtension

    def getpbcoreExtensionElement(self):
        """

        :return:    xml.etree.ElementTree.Element
        """

        return self.pbcoreExtension.getETreeElement()

    def setpbcorePart(self, newpbcorePart):
        """

        :param          newpbcorePart:
        :type           newpbcorePart:  PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorepart/
        :return:        None
        """
        # TODO: Add example of pbcorePart

        if isinstance(newpbcorePart, PB_Element):
            self.pbcorePart = newpbcorePart
        else:
            raise TypeError("Expected type: PB_Element")

    def getpbcorePart(self):
        """

        :return:
        """
        return self.pbcorePart

# __________________________________
class pbcoreRelation():
    """
    :Description:
    :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerelation/
    """
    # TODO: Create Docstring for pbcoreRelation
    def __init__(self):
        """
        @type           self.pbcoreRelationType:            PB_Element
        @type           self.pbcoreRelationIdentifier:      PB_Element

        :return:    None
        """
        self.pbcoreRelationType = None
        self.pbcoreRelationIdentifier = None

        self.pbcoreRelationIdentifier = [
            # May Contain:
            # 4 or less optional attributes, specific:

            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]


    def getpbcoreRelationType(self):
        """

        :return:
        """
        return self.pbcoreRelationType

    def setpbcoreRelationType(self, newpbcoreRelationType):
        """

        :param          newpbcoreRelationType:
        :type           newpbcoreRelationType: PB_Element
        :Example Value: Has Part
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerelation/pbcorerelationtype/
        :return:        None
        """
        # TODO: Create Docstring for setpbcoreRelationType
        # etree.tostring(newpbcoreRelationType)

        if isinstance(newpbcoreRelationType, PB_Element):
            self.pbcoreRelationType = newpbcoreRelationType
        else:
            raise TypeError("Expected type: PB_Element")

    def getpbcoreRelationIdentifier(self):
        """

        :return:
        """
        return self.pbcoreRelationIdentifier

    def setpbcoreRelationIdentifier(self, newpbcoreRelationIdentifier):
        """

        :param          newpbcoreRelationIdentifier:
        :type           newpbcoreRelationIdentifier: PB_Element
        :Example Value: cscrm_000012_r3
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerelation/pbcoreRelationIdentifier/
        :return:        None
        """
        # TODO: Create Docstring for setpbcoreRelationIdentifier
        if isinstance(newpbcoreRelationIdentifier, PB_Element):
            self.pbcoreRelationIdentifier = newpbcoreRelationIdentifier
        else:
            raise TypeError("Expected type: PB_Element")

    def _makeXML(self):
        branch = Element("pbcoreRelation")
        # branch.append(etree.tostring(self.pbcoreRelationType))
        branch.append(self.pbcoreRelationIdentifier.getETreeElement())
        branch.append(self.pbcoreRelationType.getETreeElement())
        return branch

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()
        return etree.tostring(XML)


# __________________________________
class pbcoreCoverage():
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecoverage/
    """
    # TODO: Create Docstring for pbcoreCoverage
    def __init__(self):
        """

        @type           self.coverage:          PB_Element
        @type           self.coverageType:      PB_Element
        :return:        None
        """
        self.coverage = None
        self.coverageType = None
        self.coverageAttributesOptional = [
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation",                   # (text, may be empty)

            # 3 or less optional attributes, specific:
            "startTime",                    # (text, may be empty)
            "endTime",                      # (text, may be empty)
            "timeAnnotation"                # (text, may be empty)
        ]

    def getCoverage(self):
        """

        :return:
        """
        return self.coverage

    def setCoverage(self, newCoverage):

        """

        :param          newCoverage:
        :type           newCoverage:    PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecoverage/coverage/
        :return:        None
        """
        # TODO: Give example value for setCoverage
        # TODO: Create Docstring for setCoverage
        if isinstance(newCoverage, PB_Element):
            self.coverage = newCoverage
        else:
            raise TypeError("Expected type: PB_Element")

    def getCoverageType(self):
        """

        :return:
        """
        return self.coverageType

    def setCoverageType(self, newCoverageType):
        """

        :param          newCoverageType:
        :type           newCoverageType:    PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecoverage/coveragetype/
        :return:        None
        """
        # TODO: Give example value for setCoverageType
        # TODO: Create Docstring for setCoverageType
        if isinstance(newCoverageType, PB_Element):
            self.coverageType = newCoverageType
        else:
            raise TypeError("Expected type: PB_Element")


##################################
# intellectual Property classes
##################################


class IntellectualProperty():
    """
    :Description:
    :URL: http://pbcore.org/elements/
    """
    # TODO: Create Docstring for IntellectualProperty
    def __init__(self):
        """

        :return:        None
        """


# __________________________________
class pbcoreCreator():
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecreator/
    """
    # TODO: Create Docstring for pbcoreCreator
    def __init__(self):
        """
        @type           self.creator:           PB_Element
        @type           self.creatorRole:       PB_Element
        :return:
        """
        self.creator = None
        self.creatorRole = []
        self.creatorAttributesOptional = [

            # May Contain:
            # 3 or less optional attributes, specific:

            "affiliation",                  # ( may be empty)
            "ref",                          # ( may be empty)
            "annotation",                   # ( may be empty)
            # 3 or less optional attributes, specific:

            "startTime",                    # (text, may be empty)
            "endTime",                      # (text, may be empty)
            "timeAnnotation"                # (text, may be empty)
        ]

        self.creatorRoleAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:

            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

    def getCreator(self):
        """

        :return:
        """
        return self.creator

    def setCreator(self, newCreator):
        """

        :param          newCreator:
        :type           newCreator: PB_Element
        :return:        None
        :Example Value: Unknown
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecreator/creator/
        """
        # TODO: Create Docstring for setCreator
        if isinstance(newCreator, PB_Element):
            self.creator = newCreator
        else:
            raise TypeError("Expected type: PB_Element. Got", type(newCreator))

    def getCreatorRole(self):
        """

        :return:
        """
        return self.creatorRole

    def addCreatorRole(self, newCreatorRole):
        """

        :param          newCreatorRole:
        :type           newCreatorRole: PB_Element
        :return:        None
        :Example Value: Producer
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecreator/creatorRole/
        """
        # TODO: Create Docstring for setCreatorRole
        if isinstance(newCreatorRole, PB_Element):
            self.creatorRole.append(newCreatorRole)
        else:
            raise TypeError("Expected type: PB_Element")

    def _makeXML(self):
        branch = Element("pbcoreCreator")
        # branch.append(etree.tostring(self.pbcoreRelationType))

        branch.append(self.creator.getETreeElement())
        for role in self.creatorRole:
            branch.append(role.getETreeElement())
        return branch

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()
        return etree.tostring(XML)

# __________________________________
class pbcoreContributor:
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecontributor/
    """
    # TODO: Create Docstring for pbcoreContributor
    def __init__(self):
        """
        @type           self.contributor:           PB_Element
        @type           self.contributorRole:       PB_Element
        :return:
        """
        self.contributor = None
        self.contributorRole = None
        self.contributorAttributesOptional = [
            # May Contain:
            # 3 or less optional attributes, specific:

            "affiliation",              # ( may be empty)
            "ref",                      # ( may be empty)
            "annotation",               # ( may be empty)
            # 3 or less optional attributes, specific:

            "startTime",                # (text, may be empty)
            "endTime",                  # (text, may be empty)
            "timeAnnotation"            # (text, may be empty)
        ]

        self.contributorRoleAttributesOptional = [
            # May Contain:
            # 1 or less optional attributes, specific:

            "portrayal",                # (text, may be empty)
            # 4 or less optional attributes, specific:

            "source",                   # (text, may be empty)
            "ref",                      # (text, may be empty)
            "version",                  # (text, may be empty)
            "annotation",               # (text, may be empty)

        ]

    def setContributor(self, newContributor):
        """

        :param          newContributor:
        :type           newContributor: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecontributor/contributor/
        :return:        None
        """
        # TODO: Give example of contributor
        # TODO: Create Docstring for setContributor
        if isinstance(newContributor, PB_Element):
            self.contributor = newContributor
        else:
            raise TypeError("Expected type: PB_Element")

    def getContributor(self):
        """

        :return:
        """
        return self.contributor

    def setContributoRoler(self, newContributoRole):
        """

        :param          newContributoRole:
        :type           newContributoRole:  PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecontributor/contributorrole/
        :return:        None
        """
        # TODO: Give example of contributorRole
        # TODO: Create Docstring for setContributoRoler
        if isinstance(newContributoRole, PB_Element):
            self.contributorRole = newContributoRole
        else:
            raise TypeError("Expected type: PB_Element")

    def getContributoRoler(self):
        """

        :return:
        """
        return self.contributorRole


# __________________________________
class pbcorePublisher():
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorepublisher/
    """
    # TODO: Create Docstring for pbcorePublisher
    def __init__(self):
        """
        @type           self.publisher:             PB_Element
        @type           self.publisherRole:         PB_Element

        :return:        None
        """
        self.publisher = None
        self.publisherRole = None
        self.publisherAttributesOptional = [
            # May Contain:
            # 3 or less optional attributes, specific:
            "affiliation",                  # ( may be empty)
            "ref",                          # ( may be empty)
            "annotation",                   # ( may be empty)

            # 3 or less optional attributes, specific:
            "startTime",                    # (text, may be empty)
            "endTime",                      # (text, may be empty)
            "timeAnnotation"                # (text, may be empty)
        ]

        self.publisherRoleAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                   # (text, may be empty)
            "ref",                      # (text, may be empty)
            "version",                  # (text, may be empty)
            "annotation"                # (text, may be empty)

        ]



    def getPublisher(self):
        """
        :return:
        """

        return self.publisher

    def setPublisher(self, newPublisher):
        """
        :param          newPublisher:
        :type           newPublisher:   PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorepublisher/publisher/
        :return:        None
        """

        # TODO: Give example of publisher
        # TODO: Create Docstring for setPublisher
        if isinstance(newPublisher, PB_Element):
            self.publisher = newPublisher
        else:
            raise TypeError("Expected type: PB_Element")

    def getPublisherRole(self):
        """
        :return:
        """
        return self.publisherRole

    def setPublisherRole(self, newPublisherRole):
        """
        :param          newPublisherRole:
        :type           newPublisherRole:   PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorepublisher/publisherRole/http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorepublisher/publisherRole/
        :return:        None
        """
        # For example: "" TODO: Give example of publisherRole
        # TODO: Create Docstring for setPublisherRole
        if isinstance(newPublisherRole, PB_Element):
            self.publisherRole = newPublisherRole
        else:
            raise TypeError("Expected type: PB_Element")


# __________________________________
class pbcoreRightsSummary():
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/
    """
    # TODO: Create Docstring for pbcoreRightsSummary
    def __init__(self):
        """

        @type           self.rightsSummary:         PB_Element
        @type           self.rightsLink:            PB_Element
        @type           self.rightsEmbedded:        PB_Element

        :return:        None
        """
        self.rightsSummary = []
        self.rightsLink = []
        self.rightsEmbedded = []
        self.pbcoreRightsSummaryAttributesOptional = [
            # 3 or less optional attributes, specific:

            "startTime",                    # (text, may be empty)
            "endTime",                      # (text, may be empty)
            "timeAnnotation"                # (text, may be empty)
        ]
        self.rightsSummaryAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                   # (text, may be empty)
            "ref",                      # (text, may be empty)
            "version",                  # (text, may be empty)
            "annotation"                # (text, may be empty)
        ]

        self.rightsLinkAttributesOptional = [
            # May Contain:
            # 1 or less optional attributes, specific:

            "annotation"                # (text, may be empty)
        ]

        self.rightsEmbeddedAttributes = [
            # May Contain:
            # 1 or less optional attributes, specific:

            "annotation"                # (text, may be empty)
        ]

    def getRightsSummary(self):
        """

        :return:
        """
        return self.rightsSummary

    def addRightsSummary(self, newRightsSummary):
        """

        :param          newRightsSummary:
        :type           newRightsSummary:       PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/rightssummary/
        """
        # TODO: Give example of addRightsSummary
        # TODO: Create Docstring for addRightsSummary

        if isinstance(newRightsSummary, PB_Element):
            self.rightsSummary.append(newRightsSummary)
        else:
            raise TypeError("Expected type: PB_Element")

    def getRightsLink(self):
        """

        :return:
        """
        return self.rightsLink

    def addRightsLink(self, newRightsLink):
        """

        :param          newRightsLink:
        :type           newRightsLink:  PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/rightsLink/
        """
        # TODO: Give example of rightsLink
        # TODO: Create Docstring for setRightsLink

        if isinstance(newRightsLink, PB_Element):
            self.rightsLink.append(newRightsLink)
        else:
            raise TypeError("Expected type: PB_Element")

    def getRightsEmbedded(self):
        """

        :return:
        """
        return self.rightsEmbedded

    def addRightsEmbedded(self, newRightsEmbedded):
        """

        :param          newRightsEmbedded:
        :type           newRightsEmbedded:  PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/rightsEmbedded/
        """
        # TODO: Give example of rightsEmbedded
        # TODO: Create Docstring for setRightsEmbedded
        if isinstance(newRightsEmbedded, PB_Element):
            self.rightsEmbedded.append(newRightsEmbedded)
        else:
            raise TypeError("Expected type: PB_Element")

    def _makeXML(self):
        branch = Element("pbcoreRightsSummary")
        # branch.append(etree.tostring(self.pbcoreRelationType))
        for rightsSum in self.rightsSummary:
            branch.append(rightsSum.getETreeElement())

        for link in self.rightsLink:
            branch.append(link.getETreeElement())

        for rightsEmb in self.rightsEmbedded:
            branch.append(rightsEmb.getETreeElement())
        return branch

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()
        return etree.tostring(XML)


##################################
# instantiation classes
##################################

class pbcoreInstantiation():
    # TODO: Create Docstring for pbcoreInstantiation
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/
    """
    def __init__(self, instantiationType=None):
        """

        @type           self.instantiationIdentifier:               PB_Element
        @type           self.instantiationDate:                     PB_Element
        @type           self.instantiationDimensions:               PB_Element
        @type           self.instantiationPhysical:                 PB_Element
        @type           self.instantiationDigital:                  PB_Element
        @type           self.instantiationStandard:                 PB_Element
        @type           self.instantiationLocation:                 PB_Element
        @type           self.instantiationMediaType:                PB_Element
        @type           self.instantiationGenerations:              PB_Element
        @type           self.instantiationFileSize:                 PB_Element
        @type           self.instantiationTimeStart:                PB_Element
        @type           self.instantiationDuration:                 PB_Element
        @type           self.instantiationDataRate:                 PB_Element
        @type           self.instantiationColors:                   PB_Element
        @type           self.instantiationTracks:                   PB_Element
        @type           self.instantiationChannelConfiguration:     PB_Element
        @type           self.instantiationLanguage:                 PB_Element
        @type           self.instantiationAlternativeModes:         PB_Element
        @type           self.InstantiationEssenceTrack:             PB_Element
        @type           self.InstantiationRelation:                 PB_Element
        @type           self.instantiationAnnotation:               PB_Element
        @type           self.instantiationPart:                     PB_Element
        @type           self.instantiationExtension:                PB_Element

        :param instantiationType:
        :return:
        """
        self.instantiationAssetType = instantiationType
        # For example: "Physical Asset" instantiationAssetType

        self.instantiationIdentifier = []
        self.instantiationDate = None
        self.instantiationDimensions = None
        self.instantiationPhysical = None
        self.instantiationDigital = None
        self.instantiationStandard = None
        self.instantiationLocation = None
        self.instantiationMediaType = None
        self.instantiationGenerations = None
        self.instantiationFileSize = None
        self.instantiationTimeStart = None
        self.instantiationDuration = None
        self.instantiationDataRate = None
        self.instantiationColors = None
        self.instantiationTracks = None
        self.instantiationChannelConfiguration = None
        self.instantiationLanguage = None
        self.instantiationAlternativeModes = None
        self.instantiationEssenceTrack = []
        self.instantiationRelation = []
        self.instantiationAnnotation = []
        self.instantiationPart = None
        self.instantiationExtension = None
        self.instantiationIdentifierAttributesRequired = [
            # Must Contain:
            # 1 required attribute, specific:
            "source"                        # (text, may be empty)
        ]

        self.instantiationIdentifierAttributesOptional = [
            # May Contain:
            # 3 or less optional attributes, specific:

            "ref"                           # (text, may be empty)
            "version"                       # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

        self.instantiationDateAttributesOptional = [
            # May Contain:
            # 1 or less optional attributes, specific:
            "dateType"                      # ( may be empty)
        ]

        self.instantiationDimensionsAttributesOptional = [
            # May Contain:
            # 2 or less optional attributes, specific:

            "unitsOfMeasure",               # ( may be empty)
            "annotation"                    # ( may be empty)
        ]

        self.instantiationPhysicalAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)

        ]

        self.instantiationDigitalAttributesOptional = [
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

        self.instantiationStandardAttributesOptional = [
            # May Contain:
            # 1 or less optional attributes, specific:

            "profile",                      # ( may be empty)
            # 4 or less optional attributes, specific:

            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

        self.instantiationMediaTypeAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:

            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

        self.instantiationGenerationsAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

        self.instantiationFileSizeAttributesOptional = [
            # May Contain:
            # 2 or less optional attributes, specific:
            "unitsOfMeasure",               # ( may be empty)
            "annotation"                    # ( may be empty)
        ]

        self.instantiationDataRateAttributesOptional = [
            # May Contain:
            # 2 or less optional attributes, specific:
            "unitsOfMeasure",               # ( may be empty)
            "annotation"                    # ( may be empty)
        ]

        self.instantiationColorsAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

        self.instantiationLanguageAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)

        ]
        self.instantiationAnnotationOptional = [
            # May Contain:
            # 2 or less optional attributes, specific:

            "annotationType",               # ( may be empty)
            "ref"                           # ( may be empty)
        ]

        self.instantiationPartOptional = [
            "startTime",                    # (text, may be empty)
            "endTime",                      # (text, may be empty)
            "timeAnnotation"                # (text, may be empty)
        ]

    def getInstantiationIdentifier(self):
        return self.instantiationIdentifier

    def addInstantiationIdentifier(self, newInstantiationIdentifier):
        """

        :param          newInstantiationIdentifier:
        :type           newInstantiationIdentifier:     PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationIdentifier/
        """

        if isinstance(newInstantiationIdentifier, PB_Element):
            self.instantiationIdentifier.append(newInstantiationIdentifier)
        else:
            raise TypeError

    def getInstantiationDate(self):
        """

        :return:
        """
        return self.instantiationDate

    def setInstantiationDate(self, newInstantiationDate):
        """

        :param          newInstantiationDate:
        :type           newInstantiationDate:   PB_Element
        :Example Value: UTC 2014-10-24 21:37:34
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDate/
        """
        # TODO: Create Docstring for setInstantiationDate
        if isinstance(newInstantiationDate, PB_Element):
            self.instantiationDate = newInstantiationDate
        else:
            raise TypeError

    def getInstantiationDimensions(self):
        """

        :return:
        """
        return self.instantiationDimensions

    def setInstantiationDimensions(self, newInstantiationDimensions):
        """

        :param          newInstantiationDimensions:
        :type           newInstantiationDimensions: PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDimensions/
        """
        # TODO: Give example instantiationDimensions
        # TODO: Create Docstring for setInstantiationDimensions
        if isinstance(newInstantiationDimensions, PB_Element):
            self.instantiationDimensions = newInstantiationDimensions
        else:
            raise TypeError

    def getInstantiationPhysical(self):
        """

        :return:
        """
        return self.instantiationPhysical

    def setInstantiationPhysical(self, newInstantiationPhysical):
        """

        :param          newInstantiationPhysical:
        :type           newInstantiationPhysical:   PB_Element
        :Example Value: Film: 16mm
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationPhysical/
        """
        # TODO: Create Docstring for setInstantiationPhysical
        if isinstance(newInstantiationPhysical, PB_Element):
            self.instantiationPhysical = newInstantiationPhysical
        else:
            raise TypeError

    def getInstantiationDigital(self):
        """

        :return:
        """
        return self.instantiationDigital

    def setInstantiationDigital(self, newInstantiationDigital):
        """

        :param          newInstantiationDigital:
        :type           newInstantiationDigital: PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDigital/
        """

        if isinstance(newInstantiationDigital, PB_Element):
            self.instantiationDigital = newInstantiationDigital
        else:
            raise TypeError

    def getInstantiationStandard(self):
        """

        :return:
        """
        return self.instantiationStandard

    def setInstantiationStandard(self, newInstantiationStandard):
        """

        :param          newInstantiationStandard:
        :type           newInstantiationStandard:   PB_Element
        :Example Value: Blackmagic v210 YUV
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationStandard/
        """
        # TODO: Create Docstring for setInstantiationStandard

        if isinstance(newInstantiationStandard, PB_Element):
            self.instantiationStandard = newInstantiationStandard
        else:
            raise TypeError

    def getInstantiationLocation(self):
        """

        :return:
        """
        return self.instantiationLocation

    def setInstantiationLocation(self, newInstantiationLocation):
        """

        :param          newInstantiationLocation:
        :type           newInstantiationLocation:   PB_Element
        :Example Value: California State Railroad Museum Library
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationLocation/
        """
        # TODO: Create Docstring for setInstantiationLocation

        if isinstance(newInstantiationLocation, PB_Element):
            self.instantiationLocation = newInstantiationLocation
        else:
            raise TypeError

    def getInstantiationMediaType(self):
        """

        :return:
        """
        return self.instantiationMediaType

    def setInstantiationMediaType(self, newInstantiationMediaType):
        """

        :param          newInstantiationMediaType:
        :type           newInstantiationMediaType:  PB_Element
        :Example Value: Moving Image
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationMediaType/
        """
        # TODO: Create Docstring for setInstantiationMediaType

        if isinstance(newInstantiationMediaType, PB_Element):
            self.instantiationMediaType = newInstantiationMediaType
        else:
            raise TypeError

    def getInstantiationGenerations(self):
        """

        :return:
        """
        return self.instantiationGenerations

    def setInstantiationGenerations(self, newInstantiationGenerations):
        """

        :param          newInstantiationGenerations:
        :type           newInstantiationGenerations:    PB_Element
        :Example Value: Unknown
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationGenerations/
        """
        # TODO: Create Docstring for setInstantiationGenerations
        if isinstance(newInstantiationGenerations, PB_Element):
            self.instantiationGenerations = newInstantiationGenerations
        else:
            raise TypeError

    def getInstantiationFileSize(self):
        """

        :return:
        """
        return self.instantiationFileSize

    def setInstantiationFileSize(self, newInstantiationFileSize):
        """

        :param          newInstantiationFileSize:
        :type           newInstantiationFileSize:   PB_Element
        :Example Value: ""
        :return:        None
        :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationFileSize/
        """

        if isinstance(newInstantiationFileSize, PB_Element):
            self.instantiationFileSize = newInstantiationFileSize
        else:
            raise TypeError

    def getInstantiationTimeStart(self):
        """

        :return:
        """
        return self.instantiationTimeStart

    def setInstantiationTimeStart(self, newInstantiationTimeStart):
        """

        :param          newInstantiationTimeStart:
        :type           newInstantiationTimeStart: PB_Element
        :Example Value: 00:00:00
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationTimeStart/

        """

        if isinstance(newInstantiationTimeStart, PB_Element):
            self.instantiationTimeStart = newInstantiationTimeStart
        else:
            raise TypeError

    def getInstantiationDuration(self):
        """

        :return:
        """
        return self.instantiationDuration

    def setInstantiationDuration(self, newInstantiationDuration):
        """

        :param          newInstantiationDuration:
        :type           newInstantiationDuration:   PB_Element
        :Example Value: 00:10:52
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDuration/
        """
        # TODO: Create Docstring for setInstantiationDuration

        if isinstance(newInstantiationDuration, PB_Element):
            self.instantiationDuration = newInstantiationDuration
        else:
            raise TypeError

    def getInstantiationDataRate(self):
        """

        :return:
        """
        return self.instantiationDataRate

    def setInstantiationDataRate(self, newInstantiationDataRate):
        """

        :param          newInstantiationDataRate:
        :type           newInstantiationDataRate:   PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDataRate/
        """
        # TODO: Give example instantiationDataRate
        # TODO: Create Docstring for setInstantiationDataRate

        if isinstance(newInstantiationDataRate, PB_Element):
            self.instantiationDataRate = newInstantiationDataRate
        else:
            raise TypeError

    def getInstantiationColors(self):
        """

        :return:
        """
        return self.instantiationColors

    def setInstantiationColors(self, newInstantiationColors):
        """

        :param          newInstantiationColors:
        :type           newInstantiationColors: PB_Element
        :Example Value: Color
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationColors/
        """
        # TODO: Create Docstring for setInstantiationColors

        if isinstance(newInstantiationColors, PB_Element):
            self.instantiationColors = newInstantiationColors
        else:
            pass
        raise TypeError("Expected type: PB_Element")

    def getInstantiationTracks(self):
        """

        :return:
        """
        return self.instantiationTracks

    def setInstantiationTracks(self, newInstantiationTracks):
        """

        :param          newInstantiationTracks:
        :type           newInstantiationTracks: PB_Element
        :For example:   Silent
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationTracks/
        """
        # TODO: Create Docstring for setInstantiationTracks

        if isinstance(newInstantiationTracks, PB_Element):
            self.instantiationTracks = newInstantiationTracks
        else:
            pass
        raise TypeError("Expected type: PB_Element")

    def getInstantiationChannelConfiguration(self):
        """

        :return:
        """
        return self.instantiationChannelConfiguration

    def setInstantiationChannelConfiguration(self, newInstantiationChannelConfiguration):
        """

        :param          newInstantiationChannelConfiguration:
        :type           newInstantiationChannelConfiguration:   PB_Element
        :Example Value: No Audio
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationChannelConfiguration/
        """
        # TODO: Create Docstring for setInstantiationChannelConfiguration

        if isinstance(newInstantiationChannelConfiguration, PB_Element):
            self.instantiationChannelConfiguration = newInstantiationChannelConfiguration
        else:
            pass
        raise TypeError("Expected type: PB_Element")

    def getInstantiationLanguage(self):
        """

        :return:
        """
        return self.instantiationLanguage

    def setInstantiationLanguage(self, newInstantiationLanguage):
        """

        :param          newInstantiationLanguage:
        :type           newInstantiationLanguage:   PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationLanguage/
        """
        # TODO: Give example instantiationLanguage
        # TODO: Create Docstring for setInstantiationLanguage

        if isinstance(newInstantiationLanguage, PB_Element):
            self.instantiationLanguage = newInstantiationLanguage
        else:
            pass
        raise TypeError("Expected type: PB_Element")

    def getInstantiationAlternativeModes(self):
        """

        :return:
        """
        return self.instantiationAlternativeModes

    def setInstantiationAlternativeModes(self, newInstantiationAlternativeModes):
        """

        :param          newInstantiationAlternativeModes:
        :type           newInstantiationAlternativeModes:   PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationAlternativeModes/
        """
        # TODO: Give example instantiationAlternativeModes
        # TODO: Create Docstring for setInstantiationAlternativeModes
        self.instantiationAlternativeModes = newInstantiationAlternativeModes

    def addInstantiationRelation(self, newinstantiationRelation):
        """

        :param          newinstantiationRelation:
        :type           newinstantiationRelation: InstantiationRelation
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/InstantiationRelation/
        """
        # TODO: Give example for addInstantiationRelation
        # TODO: Create Docstring for addInstantiationRelation

        if isinstance(newinstantiationRelation, InstantiationRelation):
            self.instantiationRelation.append(newinstantiationRelation)
        else:
            raise TypeError("Expected type: InstantiationRelation")

    def getInstantiationEssenceTrack(self):
        """

        :return:
        """
        return InstantiationEssenceTrack

    def addInstantiationEssenceTrack(self, newInstantiationEssenceTrack):
        """

        :param          newInstantiationEssenceTrack:
        :type           newInstantiationEssenceTrack: InstantiationEssenceTrack
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/InstantiationEssenceTrack/

        """

        if isinstance(newInstantiationEssenceTrack, InstantiationEssenceTrack):
            self.instantiationEssenceTrack.append(newInstantiationEssenceTrack)
        else:
            raise TypeError("Expected type: InstantiationEssenceTrack")


    def getInstantiationRelation(self):
        """

        :return:
        """
        return InstantiationRelation

    def setInstantiationRelation(self, newInstantiationRelation):
        """
        :param          newInstantiationRelation:
        :type           newInstantiationRelation:   PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationrelation/
        """

        if isinstance(newInstantiationRelation, PB_Element):
            self.instantiationRelation = newInstantiationRelation
        else:
            raise TypeError("Expected type: PB_Element")


    def getInstantiationAnnotation(self):
        """

        :return:
        """
        return self.instantiationAnnotation

    def addInstantiationAnnotation(self, newAnnotation):
        """

        :param          newAnnotation:
        :type           newAnnotation:      PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationAnnotation/
        """
        # TODO: Give example for addInstantiationAnnotation
        # TODO: Create Docstring for addInstantiationAnnotation

        if isinstance(newAnnotation, PB_Element):
            self.instantiationAnnotation.append(newAnnotation)
        else:
            raise TypeError("Expected type: PB_Element")

    def getInstantiationPart(self):
        """
        :return:
        """

        return self.instantiationPart

    def setInstantiationPart(self, newInstantiationPart):
        """

        :param          newInstantiationPart:
        :type           newInstantiationPart:   PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationPart/
        """
        # TODO: Give example instantiationPart
        # TODO: Create Docstring for setInstantiationPart
        if isinstance(newInstantiationPart, PB_Element):
            self.instantiationPart = newInstantiationPart
        else:
            raise TypeError("Expected type: PB_Element")

    def getInstantiationExtension(self):
        """
        :return:
        """
        return self.instantiationExtension

    def setInstantiationExtension(self, newnstantiationExtension):
        """
        :param          newnstantiationExtension:
        :type           newnstantiationExtension:   PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationExtension/
        """
        # TODO: Give example instantiationExtension
        # TODO: Create Docstring for setInstantiationExtension

        if isinstance(newnstantiationExtension, PB_Element):
            self.instantiationExtension = newnstantiationExtension
        else:
            raise TypeError("Expected type: PB_Element")


# __________________________________
class InstantiationEssenceTrack():
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/
    """
    # TODO: Create Docstring for InstantiationEssenceTrack
    def __init__(self):
        """
        @type           self.essenceTrackType:              PB_Element
        @type           self.essenceTrackIdentifier:        PB_Element
        @type           self.essenceTrackStandard:          PB_Element
        @type           self.essenceTrackEncoding:          PB_Element
        @type           self.essenceTrackDataRate:          PB_Element
        @type           self.essenceTrackFrameRate:         PB_Element
        @type           self.essenceTrackPlaybackSpeed:     PB_Element
        @type           self.essenceTrackSamplingRate:      PB_Element
        @type           self.essenceTrackBitDepth:          PB_Element
        @type           self.essenceTrackFrameSize:         PB_Element
        @type           self.essenceTrackAspectRatio:       PB_Element
        @type           self.essenceTrackTimeStart:         PB_Element
        @type           self.essenceTrackDuration:          PB_Element
        @type           self.essenceTrackLanguage:          PB_Element
        @type           self.essenceTrackAnnotation:        PB_Element
        @type           self.essenceTrackExtension:         PB_Element



        :return:        None
        """
        self.essenceTrackType = None
        self.essenceTrackIdentifier = None
        self.essenceTrackStandard = None
        self.essenceTrackEncoding = None
        self.essenceTrackDataRate = None
        self.essenceTrackFrameRate = None
        self.essenceTrackPlaybackSpeed = None
        self.essenceTrackSamplingRate = None
        self.essenceTrackBitDepth = None
        self.essenceTrackFrameSize = None
        self.essenceTrackAspectRatio = None
        self.essenceTrackTimeStart = None
        self.essenceTrackDuration = None
        self.essenceTrackLanguage = None
        self.essenceTrackAnnotation = None
        self.essenceTrackExtension = None
        self.essenceTrackIdentifierAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)

        ]

        self.essenceTrackStandardAttributes = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)

        ]

        self.essenceTrackEncodingAttributes = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)

        ]

        self.essenceTrackDataRateAttributes = [
            # May Contain:
            # 2 or less optional attributes, specific:

            "unitsOfMeasure",               # ( may be empty)
            "annotation"                    # ( may be empty)
        ]

        self.essenceTrackFrameRateAttributes = [
            # May Contain:
            # 2 or less optional attributes, specific:

            "unitsOfMeasure",               # ( may be empty)
            "annotation"                    # ( may be empty)

        ]

        self.essenceTrackPlaybackSpeedAttributes = [
            # May Contain:
            # 2 or less optional attributes, specific:

            "unitsOfMeasure",               # ( may be empty)
            "annotation"                    # ( may be empty)

        ]

        self.essenceTrackSamplingRateAttributes = [
            # May Contain:
            # 2 or less optional attributes, specific:

            "unitsOfMeasure",               # ( may be empty)
            "annotation"                    # ( may be empty)

        ]

        self.essenceTrackFrameSizeAttributes = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)

        ]

        self.essenceTrackAspectRatioAttributes = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)

        ]

        self.essenceTrackLanguageAttributes = [
            # May Contain:
            # 4 or less optional attributes, specific:
            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

        self.essenceTrackAnnotationAttributes = [
            # May Contain:
            # 2 or less optional attributes, specific:

            "annotationType",               # ( may be empty)
            "ref"                           # ( may be empty)
        ]

    def getEssenceTrackType(self):

        """

        :return:
        """

        return self.essenceTrackType

    def setEssenceTrackType(self, newEssenceTrackType):

        """

        :param          newEssenceTrackType:
        :type           newEssenceTrackType:    PB_Element
        :Example Value: Video
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essencetracktype/
        :return:        None
        """

        if isinstance(newEssenceTrackType, PB_Element):
            self.essenceTrackType = newEssenceTrackType
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackIdentifier(self):
        """

        :return:
        """

        return self.essenceTrackIdentifier

    def setEssenceTrackIdentifier(self, newEssenceTrackIdentifier):
        """

        :param          newEssenceTrackIdentifier:
        :type           newEssenceTrackIdentifier:  PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackIdentifier/
        :return:        None
        """
        #TODO: add example of essenceTrackIdentifier

        if isinstance(newEssenceTrackIdentifier, PB_Element):
            self.essenceTrackIdentifier = newEssenceTrackIdentifier
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackStandard(self):
        """

        :return:
        """
        return self.essenceTrackStandard

    def setEssenceTrackStandard(self, newEssenceTrackStandard):

        """

        :param          newEssenceTrackStandard:
        :type           newEssenceTrackStandard:    PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackStandard/
        :return:        None
        """
        # TODO: add example of essenceTrackStandard

        if isinstance(newEssenceTrackStandard, PB_Element):
            self.essenceTrackStandard = newEssenceTrackStandard
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackEncoding(self):
        """

        :return:
        """
        return self.essenceTrackEncoding

    def setEssenceTrackEncoding(self, newEssenceTrackEncoding):
        """

        :param          newEssenceTrackEncoding:
        :type           newEssenceTrackEncoding:    PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackEncoding/
        :return:        None
        """
        # TODO: add example of essenceTrackEncoding

        if isinstance(newEssenceTrackEncoding, PB_Element):
            self.essenceTrackEncoding = newEssenceTrackEncoding
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackDataRate(self):
        """

        :return:
        """
        return self.essenceTrackDataRate

    def setEssenceTrackDataRate(self, newEssenceTrackDataRate):
        """

        :param          newEssenceTrackDataRate:
        :type           newEssenceTrackDataRate: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackDataRate/
        :return:        None

        """

        if isinstance(newEssenceTrackDataRate, PB_Element):
            self.essenceTrackDataRate = newEssenceTrackDataRate
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackFrameRate(self):
        """

        :return:
        """
        return self.essenceTrackFrameRate

    def setEssenceTrackFrameRate(self, newEssenceTrackFrameRate):

        """

        :param          newEssenceTrackFrameRate:
        :type           newEssenceTrackFrameRate: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackFrameRate/
        :return:        None
        """
        # TODO: Add example of setEssenceTrackFrameRate
        if isinstance(newEssenceTrackFrameRate, PB_Element):
            self.essenceTrackFrameRate = newEssenceTrackFrameRate
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackPlaybackSpeed(self):
        """

        :return:
        """

        return self.essenceTrackPlaybackSpeed

    def setEssenceTrackPlaybackSpeed(self, newEssenceTrackPlaybackSpeed):
        """

        :param          newEssenceTrackPlaybackSpeed:
        :type           newEssenceTrackPlaybackSpeed: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackPlaybackSpeed/
        :return:        None
        """
        # TODO: Add example of setEssenceTrackPlaybackSpeed
        if isinstance(newEssenceTrackPlaybackSpeed, PB_Element):
            self.essenceTrackPlaybackSpeed = newEssenceTrackPlaybackSpeed
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackSamplingRate(self):
        """

        :return:
        """
        return self.essenceTrackSamplingRate

    def setEssenceTrackSamplingRate(self, newEssenceTrackSamplingRate):

        """

        :param          newEssenceTrackSamplingRate:
        :type           newEssenceTrackSamplingRate: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackSamplingRate/
        :return:        None
        """
        # TODO: Add example of setEssenceTrackSamplingRate
        if isinstance(newEssenceTrackSamplingRate, PB_Element):
            self.essenceTrackSamplingRate = newEssenceTrackSamplingRate
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackBitDepth(self):
        """

        :return:
        """

        return self.essenceTrackBitDepth

    def setEssenceTrackBitDepth(self, newEssenceTrackBitDepth):
        """

        :param          newEssenceTrackBitDepth:
        :type           newEssenceTrackBitDepth:    PB_Element
        :Example Value: 10
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackBitDepth/
        :return:        None
        """

        if isinstance(newEssenceTrackBitDepth, PB_Element):
            self.essenceTrackBitDepth = newEssenceTrackBitDepth
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackFrameSize(self):
        """

        :return:
        """
        return self.essenceTrackFrameSize

    def setEssenceTrackFrameSize(self, newEssenceTrackFrameSize):
        """

        :param          newEssenceTrackFrameSize:
        :type           newEssenceTrackFrameSize:   PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackFrameSize/
        :return:        None
        """
        # TODO: Add example of essenceTrackFrameSize
        # TODO: Create Docstring for setEssenceTrackFrameSize
        if isinstance(newEssenceTrackFrameSize, PB_Element):
            self.essenceTrackFrameSize = newEssenceTrackFrameSize
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackAspectRatio(self):
        """

        :return:
        """

        return self.essenceTrackAspectRatio

    def setEssenceTrackAspectRatio(self, newEssenceTrackAspectRatio):
        """

        :param          newEssenceTrackAspectRatio:
        :type           newEssenceTrackAspectRatio: PB_Element
        :Example Value: 4:3
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackAspectRatio/
        :return:        None
        """

        if isinstance(newEssenceTrackAspectRatio, PB_Element):
            self.essenceTrackAspectRatio = newEssenceTrackAspectRatio
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackTimeStart(self):
        """

        :return:
        """

        return self.essenceTrackTimeStart

    def setEssenceTrackTimeStart(self, newEssenceTrackTimeStart):
        """

        :param          newEssenceTrackTimeStart:
        :type           newEssenceTrackTimeStart:   PB_Element
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackTimeStart/
        :Example Value: 00:00:00
        :return:        None
        """
        # TODO: Create Docstring for setEssenceTrackTimeStart
        if isinstance(newEssenceTrackTimeStart, PB_Element):
            self.essenceTrackTimeStart = newEssenceTrackTimeStart
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackDuration(self):
        """

        :return:
        """
        return self.essenceTrackDuration

    def setEssenceTrackDuration(self, newEssenceTrackDuration):
        """

        :param          newEssenceTrackDuration:
        :type           newEssenceTrackDuration:    PB_Element
        :Example Value: 00:10:52
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackDuration/
        :return:        None
        """
        # TODO: Create Docstring for setEssenceTrackDuration
        if isinstance(newEssenceTrackDuration, PB_Element):
            self.essenceTrackDuration = newEssenceTrackDuration
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackLanguage(self):
        """

        :return:
        """

        return self.essenceTrackLanguage

    def setEssenceTrackLanguage(self, newEssenceTrackLanguage):
        """

        :param          newEssenceTrackLanguage:
        :type           newEssenceTrackLanguage:    PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackLanguage/
        :return:        None
        """
        # TODO: Add example of essenceTrackLanguage
        # TODO: Create Docstring for setEssenceTrackLanguage
        if isinstance(newEssenceTrackLanguage, PB_Element):
            self.essenceTrackLanguage = newEssenceTrackLanguage
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackAnnotation(self):
        """

        :return:
        """
        return self.essenceTrackAnnotation

    def setEssenceTrackAnnotation(self, newEssenceTrackAnnotation):

        """

        :param          newEssenceTrackAnnotation:
        :type           newEssenceTrackAnnotation: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackAnnotation/
        :return:        None
        """
        # TODO: add example of setEssenceTrackAnnotation

        if isinstance(newEssenceTrackAnnotation, PB_Element):
            self.essenceTrackAnnotation = newEssenceTrackAnnotation
        else:
            raise TypeError("Expected type: PB_Element")

    def getEssenceTrackExtension(self):
        """

        :return:
        """

        return self.essenceTrackExtension

    def setEssenceTrackExtension(self, newEssenceTrackExtension):
        """

        :param          newEssenceTrackExtension:
        :type           newEssenceTrackExtension:   PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackExtension/
        :return:        None
        """
        # TODO: add example of essenceTrackExtension
        # TODO: Create Docstring for setEssenceTrackExtension
        if isinstance(newEssenceTrackExtension, PB_Element):
            self.essenceTrackExtension = newEssenceTrackExtension
        else:
            raise TypeError("Expected type: PB_Element")


# __________________________________
class InstantiationRelation():
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationrelation/
    """
    # TODO: Create Docstring for InstantiationRelation

    def __init__(self):
        """
        @type           self.instantiationRelationType:             PB_Element
        @type           self.instantiationRelationIdentifier:       PB_Element

        :return:    None
        """
        self.instantiationRelationType = None
        self.instantiationRelationIdentifier = None
        self.instantiationRelationTypeAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:

            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

        self.instantiationRelationIdentifierAttributesOptional = [
            # May Contain:
            # 4 or less optional attributes, specific:

            "source",                       # (text, may be empty)
            "ref",                          # (text, may be empty)
            "version",                      # (text, may be empty)
            "annotation"                    # (text, may be empty)
        ]

    def getInstantiationRelationType(self):
        """

        :return:
        """
        return self.instantiationRelationType

    def setInstantiationRelationType(self, newInstantiationRelationType):

        """

        :param          newInstantiationRelationType:
        :type           newInstantiationRelationType: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationrelation/instantiationrelationtype/
        :return:        None
        """
        # TODO: Add example of instantiationRelationType

        if isinstance(newInstantiationRelationType, PB_Element):
            self.instantiationRelationType = newInstantiationRelationType
        else:
            raise TypeError("Expected type: PB_Element")

    def getInstantiationRelationIdentifier(self):
        """

        :return:
        """
        return self.instantiationRelationIdentifier

    def setInstantiationRelationIdentifier(self, newInstantiationRelationIdentifier):
        """

        :param          newInstantiationRelationIdentifier:
        :type           newInstantiationRelationIdentifier: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationRelationIdentifier/
        :return:        None
        """
        # TODO: Add example of instantiationRelationIdentifier

        if isinstance(newInstantiationRelationIdentifier, PB_Element):
            self.instantiationRelationIdentifier = newInstantiationRelationIdentifier
        else:
            raise TypeError("Expected type: PB_Element")


class InstantiationRights():
    """
    Description: Instantiation Rights
    URI:                http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationrights/
    """
    def __init__(self):
        """
        @type           self.rightsSummary:                 list
        @type           self.rightsLink:                    list
        @type           self.rightsEmbedded:                list

        :return:    None
        """
        self.rightsSummary = []
        self.rightsLink = []
        self.rightsEmbedded = []

    def addRightsSummary(self, newRightsSummary):
        """

        :param          newRightsSummary:
        :type           newRightsSummary: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/rightssummary/
        :return:        None
        """
        if isinstance(newRightsSummary, PB_Element):
            self.rightsSummary.append(newRightsSummary)

    def getRightsSummary(self):
        """
        :return:
        """

        return self.rightsSummary

    def addRightsLink(self, newRightsLink):
        """

        :param          newRightsLink:
        :type           newRightsLink: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/rightslink/
        :return:        None
        """

        if isinstance(newRightsLink, PB_Element):
            self.rightsLink.append(newRightsLink)
        else:
            raise ValueError("Expected type: PB_Element")

    def getRightsLink(self):
        """

        :return:
        """

        return self.rightsLink

    def addRightsEmbedded(self, newRightsEmbedded):
        """

        :param          newRightsEmbedded:
        :type           newRightsEmbedded: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/rightsembedded/
        :return:        None
        """
        if isinstance(newRightsEmbedded, PB_Element):
            self.rightsEmbedded.append(newRightsEmbedded)
        else:
            raise ValueError("Expected type: PB_Element")

    def getRightsEmbedded(self):
        return self.rightsEmbedded




##################################
# Extensions classes
##################################

# class Extensions():
#     """
#     :Description:
#     :URL: http://pbcore.org/elements/
#     """
#     # TODO: Create Docstring for extensions
#     def __init__(self):
#         """
#         :URL:           http://pbcore.org/elements/
#         :return:        None
#         """
#
#
#
#

# __________________________________
class pbcoreExtension():
    """
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/
    """
    # TODO: Create Docstring for pbcoreExtension
    def __init__(self):
        """
        @type           self.extensionWrap:                 PB_Element
        @type           self.extensionElement:              PB_Element
        @type           self.extensionValue:                PB_Element
        @type           self.extensionAuthorityUsed:        PB_Element
        @type           self.extensionEmbedded:             PB_Element

        :return:    None
        """
        self.extensionWrap = []
        self.extensionElement = None
        self.extensionValue = None
        self.extensionAuthorityUsed = None
        self.extensionEmbedded = None

    def addExtensionWrap(self, newExtensionWrap):
        """

        :param          newExtensionWrap:
        :type           newExtensionWrap:   PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionWrap/
        :return:        None
        """
        # TODO: Create Docstring for addExtensionWrap
        # TODO: Create Example value for addExtensionWrap
        self.extensionWrap.append(newExtensionWrap)

    def getExtensionWrap(self):
        """

        :return:
        """
        return self.extensionWrap

    def setExtensionElement(self, newExtensionElement):
        """

        :param          newExtensionElement:
        :type           newExtensionElement:    PB_Element
        :Example Value: countryOfCreation
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionElement/
        :return:        None
        """
        # TODO: Create Docstring for setExtensionElement
        if isinstance(newExtensionElement, PB_Element):
            self.extensionElement = newExtensionElement
        else:
            raise TypeError("Expected type: PB_Element")

    def getExtensionElement(self):
        """

        :return:
        """
        return self.extensionElement

    def setExtensionValue(self, newExtensionValue):
        """

        :param          newExtensionValue:
        :type           newExtensionValue:  PB_Element
        :Example Value: US
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionValue/
        :return:        None
        """
        # TODO: Create Docstring for setExtensionValue
        if isinstance(newExtensionValue, PB_Element):
            self.extensionValue = newExtensionValue
        else:
            raise TypeError("Expected type: PB_Element")

    def getExtensionValue(self):
        """

        :return:
        """
        return self.extensionValue

    def setExtensionAuthorityUsed(self, newExtensionAuthorityUsed):
        """

        :param          newExtensionAuthorityUsed:
        :type           newExtensionAuthorityUsed:  PB_Element
        :Example Value: ISO 3166.1
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionAuthorityUsed/
        :return:        None
        """
        # TODO: Create Docstring for setExtensionAuthorityUsed
        if isinstance(newExtensionAuthorityUsed, PB_Element):
            self.extensionAuthorityUsed = newExtensionAuthorityUsed
        else:
            raise TypeError("Expected type: PB_Element")

    def getExtensionAuthorityUsed(self):
        """

        :return:
        """
        return self.extensionAuthorityUsed

    def setExtensionEmbedded(self, newExtensionEmbedded):
        """

        :param          newExtensionEmbedded:
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionEmbedded/
        :return:        None
        """
        # TODO: Add example of extensionEmbedded
        # TODO: Create Docstring for setExtensionEmbedded
        if isinstance(newExtensionEmbedded, PB_Element):
            self.extensionEmbedded = newExtensionEmbedded
        else:
            raise TypeError("Expected type: PB_Element")

    def getExtensionEmbedded(self):
        """

        :return:
        """
        return self.extensionEmbedded


##################################
# Other classes
##################################

class PB_Element():
    """
    :Description: Basic element tag
    """

    # TODO: Create Docstring for PB_Element
    # def __init__(self, tag=None, value=None): # use if other one doesn't work
    def __init__(self, *args, **kwargs):
        """

        :param          tag:
        :param          value:
        :return:        None
        """
        self.validTags = [
            "contributor",
            "contributorRole",
            "coverage",
            "coverageType",
            "creator",
            "creatorRole",
            "essenceTrackAnnotation",
            "essenceTrackAspectRatio",
            "essenceTrackBitDepth",
            "essenceTrackDataRate",
            "essenceTrackDuration",
            "essenceTrackEncoding",
            "essenceTrackExtension",
            "essenceTrackFrameRate",
            "essenceTrackFrameSize",
            "essenceTrackIdentifier",
            "essenceTrackLanguage",
            "essenceTrackPlaybackSpeed",
            "essenceTrackSamplingRate",
            "essenceTrackStandard",
            "essenceTrackTimeStart",
            "essenceTrackType",
            "extensionAuthorityUsed",
            "extensionElement",
            "extensionEmbedded",
            "extensionValue",
            "extensionWrap",
            "instantiationAlternativeModes",
            "instantiationAnnotation",
            "instantiationChannelConfiguration",
            "instantiationColors",
            "instantiationDataRate",
            "instantiationDate",
            "instantiationDigital",
            "instantiationDimensions",
            "instantiationDuration",
            "instantiationEssenceTrack",
            "instantiationExtension",
            "instantiationFileSize",
            "instantiationGenerations",
            "instantiationIdentifier",
            "instantiationLanguage",
            "instantiationLocation",
            "instantiationMediaType",
            "instantiationPart",
            "instantiationPhysical",
            "instantiationRelation",
            "instantiationRelationIdentifier",
            "instantiationRelationType",
            "instantiationRights",
            "instantiationStandard",
            "instantiationTimeStart",
            "instantiationTracks",
            "pbcoreAnnotation",
            "pbcoreAssetDate",
            "pbcoreAssetType",
            "pbcoreAudienceLevel",
            "pbcoreAudienceRating",
            "pbcoreCollection",
            "pbcoreContributor",
            "pbcoreCoverage",
            "pbcoreCreator",
            "pbcoreDescription",
            "pbcoreDescriptionDocument",
            "pbcoreExtension",
            "pbcoreGenre",
            "pbcoreIdentifier",
            "pbcoreInstantiation",
            "pbcoreInstantiationDocument",
            "pbcorePart",
            "pbcorePublisher",
            "pbcoreRelation",
            "pbcoreRelationIdentifier",
            "pbcoreRelationType",
            "pbcoreRightsSummary",
            "pbcoreSubject",
            "pbcoreTitle",
            "publisher",
            "publisherRole",
            "rightsEmbedded",
            "rightsLink",
            "rightsSummary"
        ]

        if kwargs:
            if isinstance(kwargs["tag"], str):      # checks if the tag is a string
                if kwargs["tag"] in self.validTags:
                    self.tag = kwargs["tag"]
                else:
                    raise ValueError("Expected only PBCore elements. Received: ", kwargs["tag"])
            else:
                raise TypeError("Expected string. Received: " + type(kwargs["tag"]))
            if isinstance(kwargs["value"], str):    # checks if the value is a string
                self.value = kwargs["value"]
            else:
                raise TypeError("Expected string. Received: " + type(kwargs["value"]))
            self.attribute = OrderedDict()
        if args:
            for arg in args:
                if isinstance(arg[0], str) and isinstance(arg[1], str):     # checks if the attribute name and value are a string
                    self.addAttribute(arg[0], arg[1])
                else:
                    raise ValueError

    def getAttribute(self):
        """

        :return:
        """
        return self.attribute

    def addAttribute(self, key, value):
        """

        :param          key: name of the attribute
        :param          value: value of the attribute
        :return:        None
        """
        # TODO: Create Docstring for addAttribute

        self.attribute[key] = value

    def addAttributes(self, *args):
        """

        :param          args: Use a list in [attribute name, attribute value] format
        :return:        None
        """
        # TODO: Create Docstring for addAttributes
        if args:
            for arg in args:
                if not isinstance(arg, list):
                    raise TypeError("Arguments to addAttributes must be in format [attribute name, attribute value]")
            for arg in args:
                if isinstance(arg[0], str) and isinstance(arg[1], str):
                    self.addAttribute(arg[0], arg[1])
                else:
                    raise ValueError

        # self.attribute[key] = value

    def deleteAttribute(self, key):
        """

        :param          key: name of the attribute to be deleted
        :return:        None
        """
        # TODO: Create Docstring for deleteAttribute
        del self.attribute[key]

    def getTag(self):
        """

        :return:
        """
        return self.tag

    def setTag(self, tag):
        """

        :param          tag:
        :return:        None
        """
        # TODO: Create Docstring for setTag
        self.tag = tag

    def getValue(self):
        """

        :return:
        """
        return self.value

    def setValue(self, value):
        """

        :param          value:
        :return:        None
        """
        # TODO: Create Docstring for setValue
        self.value = value



    def getETreeElement(self):
        """
        :Description:   Gets a single element as an XML element to be passed down.
        :return:        xml.etree.ElementTree.Element
        """
        element = Element(self.tag)
        element.text = self.value
        if self.attribute:
            # print self.attribute.popitem()
            attributes = self.attribute
            while attributes:
                key, value = attributes.popitem(last=False)
                element.set(key, value)
            # print self.attribute
        return element
        #

    def xmlprint(self):
        """
        :Description:   For debugging. Prints the XML.
        :return:        None
        """
        element = Element(self.tag)
        element.text = self.value
        if self.attribute:
            for key in self.attribute:
                element.set(key, self.attribute[key])
        print etree.tostring(element)

