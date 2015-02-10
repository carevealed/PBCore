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
#     def xml_string(self):
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

    def get_IntellectualContent(self):
        """

        :return:
        """
        return self.intellectualContent

    def set_IntellectualContent(self, newIntellectualContent):
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

    def get_IntellectualProperty(self):
        """

        :return:
        """
        return self.intellectualProperty

    def set_IntellectualProperty(self, newIntellectualProperty):
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

    def get_extensions(self):
        """

        :return:
        """
        return self.extensions

    def set_extensions(self, newextensions):
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

    def get_instantiation(self):
        """

        :return:
        """
        return self.instantiation

    def set_instantiation(self, newinstantiation):
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

# FIXME Add _makeXML method for PBCore

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()


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
        self.pbcorePart = []

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

    def get_pbcoreAssetType(self):
        return self.pbcoreAssetType

    def get_pbcoreAssetTypeElement(self):
        return self.pbcoreAssetType.get_etree_element()

    def set_pbcoreAssetType(self, newpbcoreAssetType):
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

    def get_pbcoreAssetDate(self):
        """

        :return: str
        """
        return self.pbcoreAssetDate

    def get_pbcoreAssetDateElement(self):
        """

        :return:    xml.etree.ElementTree.Element
        """
        return self.pbcoreAssetDate.get_etree_element()

    def add_pbcoreAssetDate(self, newpbcoreAssetDate):
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

    def get_pbcoreIdentifier(self):
        """

        :return:
        """
        return self.pbcoreIdentifier

    def add_pbcoreIdentifier(self, newIdentifier):
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

    def get_pbcoreTitle(self):
        """

        :return: None
        """
        return self.pbcoreTitle

    def add_pbcoreTitle(self, newTitle):
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

    def get_pbcoreSubject(self):
        """

        :return: None
        """
        return self.pbcoreSubject

    def set_pbcoreSubject(self, newpbcoreSubject):
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

    def get_pbcoreDescription(self):
        """

        :return:
        """
        return self.pbcoreDescription

    def add_pbcoreDescription(self, newDescription):
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

    def get_pbcoreGenre(self):
        """

        :return:    None
        """
        return self.pbcoreGenre

    def get_pbcoreGenreElement(self):
        """

        :return:    xml.etree.ElementTree.Element
        """
        return self.pbcoreGenre.get_etree_element()

    def set_pbcoreGenre(self, newpbcoreGenre):
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

    def get_pbcoreRelation(self):
        """

        :return:
        """
        return self.pbcoreRelation

    def add_pbcoreRelation(self, newpbcoreRelation):
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

    def get_pbcoreCoverage(self):
        """

        :return:
        """
        return self.pbcoreCoverage

    def add_pbcoreCoverage(self, newpbcoreCoverage):
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

    def get_pbcoreAudienceLevel(self):
        """

        :return:
        """
        return self.pbcoreAudienceLevel

    def get_pbcoreAudienceLevelElement(self):
        """

        :return:    xml.etree.ElementTree.Element
        """
        return self.pbcoreAudienceLevel.get_etree_element()

    def set_pbcoreAudienceLevel(self, newpbcoreAudienceLevel):
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

    def get_pbcoreAudienceRating(self):
        """

        :return:    None
        """
        return self.pbcoreAudienceRating

    def get_pbcoreAudienceRatingElement(self):
        """

        :return:    xml.etree.ElementTree.Element
        """
        return self.pbcoreAudienceRating.get_etree_element()

    def set_pbcoreAudienceRating(self, newpbcoreAudienceRating):
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

    def get_pbcoreAnnotation(self):
        """

        :return:
        """
        return self.pbcoreAnnotation

    def get_pbcoreAnnotationElement(self):
        """

        :return:    xml.etree.ElementTree.Element
        """
        return self.pbcoreAnnotation.get_etree_element()

    def set_pbcoreAnnotation(self, newpbcoreAnnotation):
        """

        :param          newpbcoreAnnotation:
        :type           newpbcoreAnnotation:    PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreAnnotation
        :return:        None
        """
        # TODO: Give example value for set_pbcoreAnnotation
        # TODO: Create Docstring for set_pbcoreAnnotation
        if isinstance(newpbcoreAnnotation, PB_Element):
            self.pbcoreAnnotation = newpbcoreAnnotation
        else:
            raise TypeError("Expected type: PB_Element")

    def get_pbcoreCreator(self):
        """

        :return:
        """
        return self.pbcoreCreator

    def add_pbcoreCreator(self, newpbcoreCreator):
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

    def get_pbcoreContributor(self):
        """

        :return:
        """
        return self.pbcoreContributor

    def add_pbcoreContributor(self, newpbcoreContributor):
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

    def get_pbcorePublisher(self):
        """

        :return:
        """
        # TODO: Create Docstring for getpbcorePublisher
        return self.pbcorePublisher

    def add_pbcorePublisher(self, newpbcorePublisher):
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

    def get_pbcoreRightsSummary(self):
        """

        :return:
        """
        # TODO: Create Docstring for getpbcoreRightsSummary
        return self.pbcoreRightsSummary

    def add_pbcoreRightsSummary(self, newpbcoreRightsSummary):
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
            branch.append(self.get_pbcoreAssetTypeElement())

        if self.pbcoreAssetDate:
            for node in self.pbcoreAssetDate:
                branch.append(node.get_etree_element())

        if self.pbcoreIdentifier:
            for node in self.pbcoreIdentifier:
                branch.append(node.get_etree_element())

        if self.pbcoreTitle:
            for node in self.pbcoreTitle:
                branch.append(node.get_etree_element())

        if self.pbcoreSubject:
            branch.append(self.get_pbcoreAssetTypeElement())

        if self.pbcoreDescription:
            for node in self.pbcoreDescription:
                branch.append(node.get_etree_element())

        if self.pbcoreGenre:
            branch.append(self.get_pbcoreGenre())

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
            for node in self.pbcorePart:
                branch.append(node.xml())
        # branch.append(self.pbcoreRelationIdentifier.get_etree_element())
        # branch.append(self.pbcoreRelationType.get_etree_element())
        return branch

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xml_string(self):
        XML = self._makeXML()

        return etree.tostring(XML)

    def add_pbcore_extension(self, newpbcoreExtension):
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

    def get_pbcore_extension(self):
        """

        :return:
        """

        return self.pbcoreExtension

    def get_pbcore_extension_element(self):
        """

        :return:    xml.etree.ElementTree.Element
        """

        return self.pbcoreExtension.get_etree_element()

    def add_pbcore_part(self, newpbcorePart):
        """

        :param          newpbcorePart:
        :type           newpbcorePart:  PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorepart/
        :return:        None
        """
        # TODO: Add example of pbcorePart

        if isinstance(newpbcorePart, CAVPP_Part):
            self.pbcorePart.append(newpbcorePart)
        else:
            raise TypeError("Expected type: PB_Element. Recieved: " + str(type(newpbcorePart)))

    def get_pbcore_part(self):
        """

        :return:
        """
        return self.pbcorePart
# FIXME Add _makeXML method for pbcoreDescriptionDocument

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()
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


    def get_pbcoreRelationType(self):
        """

        :return:
        """
        return self.pbcoreRelationType

    def set_pbcoreRelationType(self, newpbcoreRelationType):
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

    def get_pbcoreRelationIdentifier(self):
        """

        :return:
        """
        return self.pbcoreRelationIdentifier

    def set_pbcoreRelationIdentifier(self, newpbcoreRelationIdentifier):
        """

        :param          newpbcoreRelationIdentifier:
        :type           newpbcoreRelationIdentifier: PB_Element
        :Example Value: cscrm_000012_r3
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerelation/pbcoreRelationIdentifier/
        :return:        None
        """
        # TODO: Create Docstring for set_pbcoreRelationIdentifier
        if isinstance(newpbcoreRelationIdentifier, PB_Element):
            self.pbcoreRelationIdentifier = newpbcoreRelationIdentifier
        else:
            raise TypeError("Expected type: PB_Element")

    def _makeXML(self):
        branch = Element("pbcoreRelation")
        # branch.append(etree.tostring(self.pbcoreRelationType))
        branch.append(self.pbcoreRelationIdentifier.get_etree_element())
        branch.append(self.pbcoreRelationType.get_etree_element())
        return branch

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xml_string(self):
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

    def get_coverage(self):
        """

        :return:
        """
        return self.coverage

    def set_coverage(self, newCoverage):

        """

        :param          newCoverage:
        :type           newCoverage:    PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecoverage/coverage/
        :return:        None
        """
        # TODO: Give example value for set_coverage
        # TODO: Create Docstring for set_coverage
        if isinstance(newCoverage, PB_Element):
            self.coverage = newCoverage
        else:
            raise TypeError("Expected type: PB_Element")

    def get_coverageType(self):
        """

        :return:
        """
        return self.coverageType

    def set_coverageType(self, newCoverageType):
        """

        :param          newCoverageType:
        :type           newCoverageType:    PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecoverage/coveragetype/
        :return:        None
        """
        # TODO: Give example value for set_coverageType
        # TODO: Create Docstring for set_coverageType
        if isinstance(newCoverageType, PB_Element):
            self.coverageType = newCoverageType
        else:
            raise TypeError("Expected type: PB_Element")

# FIXME Add _makeXML method for pbcoreCoverage

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()

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

    def get_creator(self):
        """

        :return:
        """
        return self.creator

    def set_creator(self, newCreator):
        """

        :param          newCreator:
        :type           newCreator: PB_Element
        :return:        None
        :Example Value: Unknown
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecreator/creator/
        """
        # TODO: Create Docstring for set_creator
        if isinstance(newCreator, PB_Element):
            self.creator = newCreator
        else:
            raise TypeError("Expected type: PB_Element. Got", type(newCreator))

    def get_creatorRole(self):
        """

        :return:
        """
        return self.creatorRole

    def add_creatorRole(self, newCreatorRole):
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

        branch.append(self.creator.get_etree_element())
        for role in self.creatorRole:
            branch.append(role.get_etree_element())
        return branch

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xml_string(self):
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

    def set_contributor(self, newContributor):
        """

        :param          newContributor:
        :type           newContributor: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecontributor/contributor/
        :return:        None
        """
        # TODO: Give example of contributor
        # TODO: Create Docstring for set_contributor
        if isinstance(newContributor, PB_Element):
            self.contributor = newContributor
        else:
            raise TypeError("Expected type: PB_Element")

    def get_contributor(self):
        """

        :return:
        """
        return self.contributor

    def set_contributorRole(self, newContributoRole):
        """

        :param          newContributoRole:
        :type           newContributoRole:  PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecontributor/contributorrole/
        :return:        None
        """
        # TODO: Give example of contributorRole
        # TODO: Create Docstring for set_contributorRole
        if isinstance(newContributoRole, PB_Element):
            self.contributorRole = newContributoRole
        else:
            raise TypeError("Expected type: PB_Element")

    def get_contributorRole(self):
        """

        :return:
        """
        return self.contributorRole

# FIXME Add _makeXML method for pbcoreContributor

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()

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



    def get_publisher(self):
        """
        :return:
        """

        return self.publisher

    def set_publisher(self, newPublisher):
        """
        :param          newPublisher:
        :type           newPublisher:   PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorepublisher/publisher/
        :return:        None
        """

        # TODO: Give example of publisher
        # TODO: Create Docstring for set_publisher
        if isinstance(newPublisher, PB_Element):
            self.publisher = newPublisher
        else:
            raise TypeError("Expected type: PB_Element")

    def get_publisherRole(self):
        """
        :return:
        """
        return self.publisherRole

    def set_publisherRole(self, newPublisherRole):
        """
        :param          newPublisherRole:
        :type           newPublisherRole:   PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorepublisher/publisherRole/http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorepublisher/publisherRole/
        :return:        None
        """
        # For example: "" TODO: Give example of publisherRole
        # TODO: Create Docstring for set_publisherRole
        if isinstance(newPublisherRole, PB_Element):
            self.publisherRole = newPublisherRole
        else:
            raise TypeError("Expected type: PB_Element")

# FIXME Add _makeXML method for pbcorePublisher

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()

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

    def get_rightsSummary(self):
        """

        :return:
        """
        return self.rightsSummary

    def add_rightsSummary(self, newRightsSummary):
        """

        :param          newRightsSummary:
        :type           newRightsSummary:       PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/rightssummary/
        """
        # TODO: Give example of add_rightsSummary
        # TODO: Create Docstring for add_rightsSummary

        if isinstance(newRightsSummary, PB_Element):
            self.rightsSummary.append(newRightsSummary)
        else:
            raise TypeError("Expected type: PB_Element")

    def get_rightsLink(self):
        """

        :return:
        """
        return self.rightsLink

    def add_rightsLink(self, newRightsLink):
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

    def get_rightsEmbedded(self):
        """

        :return:
        """
        return self.rightsEmbedded

    def add_rightsEmbedded(self, newRightsEmbedded):
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
            branch.append(rightsSum.get_etree_element())

        for link in self.rightsLink:
            branch.append(link.get_etree_element())

        for rightsEmb in self.rightsEmbedded:
            branch.append(rightsEmb.get_etree_element())
        return branch

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xml_string(self):
        XML = self._makeXML()
        return etree.tostring(XML)


##################################
# instantiation classes
##################################
class CAVPP_Part():
    def __init__(self):
        self.pbcoreIdentifier = []
        self.pbcoreTitle = None
        self.pbcoreDescription = []
        self.pbcoreInstantiation = []

    def get_pbcoreIdentifier(self):
        return self.pbcoreIdentifier

    def add_pbcoreIdentifier(self, newpbcoreIdentifier):
        if isinstance(newpbcoreIdentifier, PB_Element):
            self.pbcoreIdentifier.append(newpbcoreIdentifier)

    def get_pbcoreTitle(self):
        return self.pbcoreTitle

    def set_pbcoreTitle(self, newpbcoreTitle):
        if isinstance(newpbcoreTitle, PB_Element):
            self.pbcoreTitle = newpbcoreTitle

    def get_pbcoreDescription(self):
        return self.pbcoreDescription

    def add_pbcoreDescription(self, newpbcoreDescription):
        if isinstance(newpbcoreDescription, PB_Element):
            self.pbcoreDescription.append(newpbcoreDescription)

    def get_pbcoreInstantiation(self):
        return self.pbcoreInstantiation

    def add_pbcoreInstantiation(self, newpbcoreInstantiation):
        if isinstance(newpbcoreInstantiation, pbcoreInstantiation):
            self.pbcoreInstantiation.append(newpbcoreInstantiation)

    def _makeXML(self):
        branch = Element("pbcorePart")
        # branch.append(etree.tostring(self.pbcoreRelationType))
        for node in self.pbcoreIdentifier:
            branch.append(node.get_etree_element())

        # for pbTitle in self.pbcoreTitle:
        branch.append(self.pbcoreTitle.get_etree_element())

        for node in self.pbcoreDescription:
            branch.append(node.get_etree_element())

        for node in self.pbcoreInstantiation:
            branch.append(node.xml())
        return branch

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xml_string(self):
        XML = self._makeXML()
        return etree.tostring(XML)

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
        @type           self.instantiationEssenceTrack:             PB_Element
        @type           self.instantiationRelation:                 PB_Element
        @type           self.instantiationAnnotation:               PB_Element
        @type           self.instantiationPart:                     PB_Element
        @type           self.instantiationExtension:                PB_Element

        :param instantiationType:
        :return:
        """
        self.instantiationAssetType = instantiationType
        # For example: "Physical Asset" instantiationAssetType

        self.instantiationIdentifier = []
        self.instantiationDate = []
        self.instantiationDimensions = []
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


    def get_instantiationAssetType(self):
        return self.instantiationAssetType

    def set_instantiationAssetType(self, newInstantiationAssetType):
        self.instantiationAssetType = newInstantiationAssetType

    def get_instantiationIdentifier(self):
        return self.instantiationIdentifier

    def add_instantiationIdentifier(self, newInstantiationIdentifier):
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

    def get_instantiationDate(self):
        """

        :return:        list
        """
        return self.instantiationDate

    def add_instantiationDate(self, newInstantiationDate):
        """

        :param          newInstantiationDate:
        :type           newInstantiationDate:   PB_Element
        :Example Value: UTC 2014-10-24 21:37:34
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDate/
        """
        # TODO: Create Docstring for setInstantiationDate
        if isinstance(newInstantiationDate, PB_Element):
            self.instantiationDate.append(newInstantiationDate)
        else:
            raise TypeError

    def get_instantiationDimensions(self):
        """

        :return:        list
        """
        return self.instantiationDimensions

    def add_instantiationDimensions(self, newInstantiationDimensions):
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
            self.instantiationDimensions.append(newInstantiationDimensions)
        else:
            raise TypeError

    def get_instantiationPhysical(self):
        """

        :return:
        """
        return self.instantiationPhysical

    def set_instantiationPhysical(self, newInstantiationPhysical):
        """

        :param          newInstantiationPhysical:
        :type           newInstantiationPhysical:   PB_Element
        :Example Value: Film: 16mm
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationPhysical/
        """
        # TODO: Create Docstring for set_instantiationPhysical
        if isinstance(newInstantiationPhysical, PB_Element):
            self.instantiationPhysical = newInstantiationPhysical
        else:
            raise TypeError

    def get_instantiationDigital(self):
        """

        :return:
        """
        return self.instantiationDigital

    def set_instantiationDigital(self, newInstantiationDigital):
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

    def get_instantiationStandard(self):
        """

        :return:
        """
        return self.instantiationStandard

    def set_instantiationStandard(self, newInstantiationStandard):
        """

        :param          newInstantiationStandard:
        :type           newInstantiationStandard:   PB_Element
        :Example Value: Blackmagic v210 YUV
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationStandard/
        """
        # TODO: Create Docstring for set_instantiationStandard

        if isinstance(newInstantiationStandard, PB_Element):
            self.instantiationStandard = newInstantiationStandard
        else:
            raise TypeError

    def get_instantiationLocation(self):
        """

        :return:
        """
        return self.instantiationLocation

    def set_instantiationLocation(self, newInstantiationLocation):
        """

        :param          newInstantiationLocation:
        :type           newInstantiationLocation:   PB_Element
        :Example Value: California State Railroad Museum Library
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationLocation/
        """
        # TODO: Create Docstring for set_instantiationLocation

        if isinstance(newInstantiationLocation, PB_Element):
            self.instantiationLocation = newInstantiationLocation
        else:
            raise TypeError

    def get_instantiationMediaType(self):
        """

        :return:
        """
        return self.instantiationMediaType

    def set_instantiationMediaType(self, newInstantiationMediaType):
        """

        :param          newInstantiationMediaType:
        :type           newInstantiationMediaType:  PB_Element
        :Example Value: Moving Image
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationMediaType/
        """
        # TODO: Create Docstring for set_instantiationMediaType

        if isinstance(newInstantiationMediaType, PB_Element):
            self.instantiationMediaType = newInstantiationMediaType
        else:
            raise TypeError

    def get_instantiationGenerations(self):
        """

        :return:
        """
        return self.instantiationGenerations

    def set_instantiationGenerations(self, newInstantiationGenerations):
        """

        :param          newInstantiationGenerations:
        :type           newInstantiationGenerations:    PB_Element
        :Example Value: Unknown
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationGenerations/
        """
        # TODO: Create Docstring for set_instantiationGenerations
        if isinstance(newInstantiationGenerations, PB_Element):
            self.instantiationGenerations = newInstantiationGenerations
        else:
            raise TypeError

    def get_instantiationFileSize(self):
        """

        :return:
        """
        return self.instantiationFileSize

    def set_instantiationFileSize(self, newInstantiationFileSize):
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

    def get_instantiationTimeStart(self):
        """

        :return:
        """
        return self.instantiationTimeStart

    def set_instantiationTimeStart(self, newInstantiationTimeStart):
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

    def get_instantiationDuration(self):
        """

        :return:
        """
        return self.instantiationDuration

    def set_instantiationDuration(self, newInstantiationDuration):
        """

        :param          newInstantiationDuration:
        :type           newInstantiationDuration:   PB_Element
        :Example Value: 00:10:52
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDuration/
        """
        # TODO: Create Docstring for set_instantiationDuration

        if isinstance(newInstantiationDuration, PB_Element):
            self.instantiationDuration = newInstantiationDuration
        else:
            raise TypeError

    def get_instantiationDataRate(self):
        """

        :return:
        """
        return self.instantiationDataRate

    def set_instantiationDataRate(self, newInstantiationDataRate):
        """

        :param          newInstantiationDataRate:
        :type           newInstantiationDataRate:   PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDataRate/
        """
        # TODO: Give example instantiationDataRate
        # TODO: Create Docstring for set_instantiationDataRate

        if isinstance(newInstantiationDataRate, PB_Element):
            self.instantiationDataRate = newInstantiationDataRate
        else:
            raise TypeError

    def get_instantiationColors(self):
        """

        :return:
        """
        return self.instantiationColors

    def set_instantiationColors(self, newInstantiationColors):
        """

        :param          newInstantiationColors:
        :type           newInstantiationColors: PB_Element
        :Example Value: Color
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationColors/
        """
        # TODO: Create Docstring for set_instantiationColors

        if isinstance(newInstantiationColors, PB_Element):
            self.instantiationColors = newInstantiationColors
        else:
            raise TypeError("Expected type: PB_Element. Recieved: " + newInstantiationColors.__class__.__name__)

    def get_instantiationTracks(self):
        """

        :return:
        """
        return self.instantiationTracks

    def set_instantiationTracks(self, newInstantiationTracks):
        """

        :param          newInstantiationTracks:
        :type           newInstantiationTracks: PB_Element
        :For example:   Silent
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationTracks/
        """
        # TODO: Create Docstring for set_instantiationTracks

        if isinstance(newInstantiationTracks, PB_Element):
            self.instantiationTracks = newInstantiationTracks
        else:
            raise TypeError("Expected type: PB_Element. Received: " + newInstantiationTracks.__class__.__name__)

    def get_instantiationChannelConfiguration(self):
        """

        :return:
        """
        return self.instantiationChannelConfiguration

    def set_instantiationChannelConfiguration(self, newInstantiationChannelConfiguration):
        """

        :param          newInstantiationChannelConfiguration:
        :type           newInstantiationChannelConfiguration:   PB_Element
        :Example Value: No Audio
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationChannelConfiguration/
        """
        # TODO: Create Docstring for set_instantiationChannelConfiguration

        if isinstance(newInstantiationChannelConfiguration, PB_Element):
            self.instantiationChannelConfiguration = newInstantiationChannelConfiguration
        else:
            raise TypeError("Expected type: PB_Element")

    def get_instantiationLanguage(self):
        """

        :return:
        """
        return self.instantiationLanguage

    def set_instantiationLanguage(self, newInstantiationLanguage):
        """

        :param          newInstantiationLanguage:
        :type           newInstantiationLanguage:   PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationLanguage/
        """
        # TODO: Give example instantiationLanguage
        # TODO: Create Docstring for set_instantiationLanguage

        if isinstance(newInstantiationLanguage, PB_Element):
            self.instantiationLanguage = newInstantiationLanguage
        else:
            pass
        raise TypeError("Expected type: PB_Element")

    def get_instantiationAlternativeModes(self):
        """

        :return:
        """
        return self.instantiationAlternativeModes

    def set_instantiationAlternativeModes(self, newInstantiationAlternativeModes):
        """

        :param          newInstantiationAlternativeModes:
        :type           newInstantiationAlternativeModes:   PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationAlternativeModes/
        """
        # TODO: Give example instantiationAlternativeModes
        # TODO: Create Docstring for set_instantiationAlternativeModes
        self.instantiationAlternativeModes = newInstantiationAlternativeModes

    def add_instantiationRelation(self, newinstantiationRelation):
        """

        :param          newinstantiationRelation:
        :type           newinstantiationRelation: InstantiationRelation
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/InstantiationRelation/
        """
        # TODO: Give example for add_instantiationRelation
        # TODO: Create Docstring for add_instantiationRelation

        if isinstance(newinstantiationRelation, InstantiationRelation):
            self.instantiationRelation.append(newinstantiationRelation)
        else:
            raise TypeError("Expected type: InstantiationRelation")

    def get_instantiationEssenceTrack(self):
        """

        :return:
        """
        return InstantiationEssenceTrack

    def add_instantiationEssenceTrack(self, newInstantiationEssenceTrack):
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


    def get_instantiationRelation(self):
        """

        :return:
        """
        return InstantiationRelation

    def set_instantiationRelation(self, newInstantiationRelation):
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


    def get_instantiationAnnotation(self):
        """

        :return:
        """
        return self.instantiationAnnotation

    def add_instantiationAnnotation(self, newAnnotation):
        """

        :param          newAnnotation:
        :type           newAnnotation:      PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationAnnotation/
        """
        # TODO: Give example for add_instantiationAnnotation
        # TODO: Create Docstring for add_instantiationAnnotation

        if isinstance(newAnnotation, PB_Element):
            self.instantiationAnnotation.append(newAnnotation)
        else:
            raise TypeError("Expected type: PB_Element")

    def get_instantiationPart(self):
        """
        :return:
        """

        return self.instantiationPart

    def set_instantiationPart(self, newInstantiationPart):
        """

        :param          newInstantiationPart:
        :type           newInstantiationPart:   PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationPart/
        """
        # TODO: Give example instantiationPart
        # TODO: Create Docstring for set_instantiationPart
        if isinstance(newInstantiationPart, PB_Element):
            self.instantiationPart = newInstantiationPart
        else:
            raise TypeError("Expected type: PB_Element")

    def get_instantiationExtension(self):
        """
        :return:
        """
        return self.instantiationExtension

    def set_instantiationExtension(self, newnstantiationExtension):
        """
        :param          newnstantiationExtension:
        :type           newnstantiationExtension:   PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationExtension/
        """
        # TODO: Give example instantiationExtension
        # TODO: Create Docstring for set_instantiationExtension

        if isinstance(newnstantiationExtension, PB_Element):
            self.instantiationExtension = newnstantiationExtension
        else:
            raise TypeError("Expected type: PB_Element")

    def _makeXML(self):
        branch = Element("pbcoreInstantiation")
        # branch.append(etree.tostring(self.pbcoreRelationType))
        if self.instantiationAssetType:
            branch.append(etree.Comment(text=self.instantiationAssetType))
        if self.instantiationIdentifier:
            for instIdentifier in self.instantiationIdentifier:
                branch.append(instIdentifier.get_etree_element())

        if self.instantiationDate:
            for instDate in self.instantiationDate:
                branch.append(instDate.get_etree_element())

        if self.instantiationDimensions:
            for instDimensions in self.instantiationDimensions:
                branch.append(instDimensions.get_etree_element())

        if self.instantiationPhysical:
            branch.append(self.instantiationPhysical.get_etree_element())

        if self.instantiationDigital:
            branch.append(self.instantiationDigital.get_etree_element())

        if self.instantiationStandard:
            branch.append(self.instantiationStandard.get_etree_element())

        if self.instantiationLocation:
            branch.append(self.instantiationLocation.get_etree_element())
        else:
            # If no instantiationLocation is given, put a comment that says for institutional reference to
            # make the PBCore XML validate. Since instantiationLocation
            empty_Location = Element("instantiationLocation")
            empty_Location.append(etree.Comment(text="for institutional reference"))
            branch.append(empty_Location)

        if self.instantiationMediaType:
            branch.append(self.instantiationMediaType.get_etree_element())

        if self.instantiationGenerations:
            branch.append(self.instantiationGenerations.get_etree_element())

        if self.instantiationFileSize:
            branch.append(self.instantiationFileSize.get_etree_element())

        if self.instantiationTimeStart:
            branch.append(self.instantiationTimeStart.get_etree_element())

        if self.instantiationDuration:
            branch.append(self.instantiationDuration.get_etree_element())

        if self.instantiationDataRate:
            branch.append(self.instantiationDataRate.get_etree_element())

        if self.instantiationColors:
            branch.append(self.instantiationColors.get_etree_element())

        if self.instantiationTracks:
            branch.append(self.instantiationTracks.get_etree_element())

        if self.instantiationChannelConfiguration:
            branch.append(self.instantiationChannelConfiguration.get_etree_element())

        if self.instantiationLanguage:
            branch.append(self.instantiationLanguage.get_etree_element())

        if self.instantiationAlternativeModes:
            branch.append(self.instantiationAlternativeModes.get_etree_element())

        if self.instantiationEssenceTrack:
            for node in self.instantiationEssenceTrack:
                branch.append(node.xml())

        if self.instantiationRelation:
            for instRelation in self.instantiationRelation:
                branch.append(instRelation.get_etree_element())

        if self.instantiationAnnotation:
            for instAnnotation in self.instantiationAnnotation:
                # print instAnnotation.get_etree_element()
                branch.append(instAnnotation.get_etree_element())

        if self.instantiationPart:
            branch.append(self.instantiationPart)

        if self.instantiationExtension:
            branch.append(self.instantiationExtension)

        return branch

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()
        return etree.tostring(XML)
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
        self.essenceTrackAnnotation = []
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

    def get_essenceTrackType(self):

        """

        :return:
        """

        return self.essenceTrackType

    def set_essenceTrackType(self, newEssenceTrackType):

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

    def get_essenceTrackIdentifier(self):
        """

        :return:
        """

        return self.essenceTrackIdentifier

    def set_essenceTrackIdentifier(self, newEssenceTrackIdentifier):
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

    def get_essenceTrackStandard(self):
        """

        :return:
        """
        return self.essenceTrackStandard

    def set_essenceTrackStandard(self, newEssenceTrackStandard):

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

    def get_essenceTrackEncoding(self):
        """

        :return:
        """
        return self.essenceTrackEncoding

    def set_essenceTrackEncoding(self, newEssenceTrackEncoding):
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

    def get_essenceTrackDataRate(self):
        """

        :return:
        """
        return self.essenceTrackDataRate

    def set_essenceTrackDataRate(self, newEssenceTrackDataRate):
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

    def get_essenceTrackFrameRate(self):
        """

        :return:
        """
        return self.essenceTrackFrameRate

    def set_essenceTrackFrameRate(self, newEssenceTrackFrameRate):

        """

        :param          newEssenceTrackFrameRate:
        :type           newEssenceTrackFrameRate: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackFrameRate/
        :return:        None
        """
        # TODO: Add example of set_essenceTrackFrameRate
        if isinstance(newEssenceTrackFrameRate, PB_Element):
            self.essenceTrackFrameRate = newEssenceTrackFrameRate
        else:
            raise TypeError("Expected type: PB_Element")

    def get_essenceTrackPlaybackSpeed(self):
        """

        :return:
        """

        return self.essenceTrackPlaybackSpeed

    def set_essenceTrackPlaybackSpeed(self, newEssenceTrackPlaybackSpeed):
        """

        :param          newEssenceTrackPlaybackSpeed:
        :type           newEssenceTrackPlaybackSpeed: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackPlaybackSpeed/
        :return:        None
        """
        # TODO: Add example of set_essenceTrackPlaybackSpeed
        if isinstance(newEssenceTrackPlaybackSpeed, PB_Element):
            self.essenceTrackPlaybackSpeed = newEssenceTrackPlaybackSpeed
        else:
            raise TypeError("Expected type: PB_Element")

    def get_essenceTrackSamplingRate(self):
        """

        :return:
        """
        return self.essenceTrackSamplingRate

    def set_essenceTrackSamplingRate(self, newEssenceTrackSamplingRate):

        """

        :param          newEssenceTrackSamplingRate:
        :type           newEssenceTrackSamplingRate: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackSamplingRate/
        :return:        None
        """
        # TODO: Add example of set_essenceTrackSamplingRate
        if isinstance(newEssenceTrackSamplingRate, PB_Element):
            self.essenceTrackSamplingRate = newEssenceTrackSamplingRate
        else:
            raise TypeError("Expected type: PB_Element")

    def get_essenceTrackBitDepth(self):
        """

        :return:
        """

        return self.essenceTrackBitDepth

    def set_essenceTrackBitDepth(self, newEssenceTrackBitDepth):
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

    def get_essenceTrackFrameSize(self):
        """

        :return:
        """
        return self.essenceTrackFrameSize

    def set_essenceTrackFrameSize(self, newEssenceTrackFrameSize):
        """

        :param          newEssenceTrackFrameSize:
        :type           newEssenceTrackFrameSize:   PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackFrameSize/
        :return:        None
        """
        # TODO: Add example of essenceTrackFrameSize
        # TODO: Create Docstring for set_essenceTrackFrameSize
        if isinstance(newEssenceTrackFrameSize, PB_Element):
            self.essenceTrackFrameSize = newEssenceTrackFrameSize
        else:
            raise TypeError("Expected type: PB_Element")

    def get_essenceTrackAspectRatio(self):
        """

        :return:
        """

        return self.essenceTrackAspectRatio

    def set_essenceTrackAspectRatio(self, newEssenceTrackAspectRatio):
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

    def get_essenceTrackTimeStart(self):
        """

        :return:
        """

        return self.essenceTrackTimeStart

    def set_essenceTrackTimeStart(self, newEssenceTrackTimeStart):
        """

        :param          newEssenceTrackTimeStart:
        :type           newEssenceTrackTimeStart:   PB_Element
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackTimeStart/
        :Example Value: 00:00:00
        :return:        None
        """
        # TODO: Create Docstring for set_essenceTrackTimeStart
        if isinstance(newEssenceTrackTimeStart, PB_Element):
            self.essenceTrackTimeStart = newEssenceTrackTimeStart
        else:
            raise TypeError("Expected type: PB_Element")

    def get_essenceTrackDuration(self):
        """

        :return:
        """
        return self.essenceTrackDuration

    def set_essenceTrackDuration(self, newEssenceTrackDuration):
        """

        :param          newEssenceTrackDuration:
        :type           newEssenceTrackDuration:    PB_Element
        :Example Value: 00:10:52
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackDuration/
        :return:        None
        """
        # TODO: Create Docstring for set_essenceTrackDuration
        if isinstance(newEssenceTrackDuration, PB_Element):
            self.essenceTrackDuration = newEssenceTrackDuration
        else:
            raise TypeError("Expected type: PB_Element")

    def get_essenceTrackLanguage(self):
        """

        :return:
        """

        return self.essenceTrackLanguage

    def set_essenceTrackLanguage(self, newEssenceTrackLanguage):
        """

        :param          newEssenceTrackLanguage:
        :type           newEssenceTrackLanguage:    PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackLanguage/
        :return:        None
        """
        # TODO: Add example of essenceTrackLanguage
        # TODO: Create Docstring for set_essenceTrackLanguage
        if isinstance(newEssenceTrackLanguage, PB_Element):
            self.essenceTrackLanguage = newEssenceTrackLanguage
        else:
            raise TypeError("Expected type: PB_Element")

    def get_essenceTrackAnnotation(self):
        """

        :return:
        """
        return self.essenceTrackAnnotation

    def add_essenceTrackAnnotation(self, newEssenceTrackAnnotation):

        """

        :param          newEssenceTrackAnnotation:
        :type           newEssenceTrackAnnotation: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackAnnotation/
        :return:        None
        """
        # TODO: add example of set_essenceTrackAnnotation

        if isinstance(newEssenceTrackAnnotation, PB_Element):
            self.essenceTrackAnnotation.append(newEssenceTrackAnnotation)
        else:
            raise TypeError("Expected type: PB_Element")

    def get_essenceTrackExtension(self):
        """

        :return:
        """

        return self.essenceTrackExtension

    def set_essenceTrackExtension(self, newEssenceTrackExtension):
        """

        :param          newEssenceTrackExtension:
        :type           newEssenceTrackExtension:   PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackExtension/
        :return:        None
        """
        # TODO: add example of essenceTrackExtension
        # TODO: Create Docstring for set_essenceTrackExtension
        if isinstance(newEssenceTrackExtension, PB_Element):
            self.essenceTrackExtension = newEssenceTrackExtension
        else:
            raise TypeError("Expected type: PB_Element")

    def _makeXML(self):
        branch = Element("instantiationEssenceTrack")
        if self.essenceTrackType:
            branch.append(self.essenceTrackType.get_etree_element())

        if self.essenceTrackIdentifier:
            branch.append(self.essenceTrackIdentifier.get_etree_element())

        if self.essenceTrackStandard:
            branch.append(self.essenceTrackStandard.get_etree_element())

        if self.essenceTrackEncoding:
            branch.append(self.essenceTrackEncoding.get_etree_element())

        if self.essenceTrackDataRate:
            branch.append(self.essenceTrackDataRate.get_etree_element())

        if self.essenceTrackFrameRate:
            branch.append(self.essenceTrackFrameRate.get_etree_element())

        if self.essenceTrackPlaybackSpeed:
            branch.append(self.essenceTrackPlaybackSpeed.get_etree_element())

        if self.essenceTrackSamplingRate:
            branch.append(self.essenceTrackSamplingRate.get_etree_element())

        if self.essenceTrackBitDepth:
            branch.append(self.essenceTrackBitDepth.get_etree_element())

        if self.essenceTrackFrameSize:
            branch.append(self.essenceTrackFrameSize.get_etree_element())

        if self.essenceTrackAspectRatio:
            branch.append(self.essenceTrackAspectRatio.get_etree_element())

        if self.essenceTrackTimeStart:
            branch.append(self.essenceTrackTimeStart.get_etree_element())

        if self.essenceTrackDuration:
            branch.append(self.essenceTrackDuration.get_etree_element())

        if self.essenceTrackLanguage:
            branch.append(self.essenceTrackLanguage.get_etree_element())

        if self.essenceTrackAnnotation:
            for node in self.essenceTrackAnnotation:
                # node.xml_print()
                branch.append(node.get_etree_element())

        if self.essenceTrackExtension:
            branch.append(self.essenceTrackExtension.get_etree_element())
        # print branch
        return branch

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()


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

    def get_instantiationRelationType(self):
        """

        :return:
        """
        return self.instantiationRelationType

    def set_instantiationRelationType(self, newInstantiationRelationType):

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

    def get_instantiationRelationIdentifier(self):
        """

        :return:
        """
        return self.instantiationRelationIdentifier

    def set_instantiationRelationIdentifier(self, newInstantiationRelationIdentifier):
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
    # FIXME Add _makeXML method for InstantiationRelation

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()

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

    def add_rightsSummary(self, newRightsSummary):
        """

        :param          newRightsSummary:
        :type           newRightsSummary: PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/rightssummary/
        :return:        None
        """
        if isinstance(newRightsSummary, PB_Element):
            self.rightsSummary.append(newRightsSummary)

    def get_rightsSummary(self):
        """
        :return:
        """

        return self.rightsSummary

    def add_rightsLink(self, newRightsLink):
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

    def get_rightsLink(self):
        """

        :return:
        """

        return self.rightsLink

    def add_rightsEmbedded(self, newRightsEmbedded):
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

    def get_rightsEmbedded(self):
        return self.rightsEmbedded
# FIXME Add _makeXML method for pbcoreRights

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()

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

    def add_extensionWrap(self, newExtensionWrap):
        """

        :param          newExtensionWrap:
        :type           newExtensionWrap:   PB_Element
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionWrap/
        :return:        None
        """
        # TODO: Create Docstring for add_extensionWrap
        # TODO: Create Example value for add_extensionWrap
        self.extensionWrap.append(newExtensionWrap)

    def get_extensionWrap(self):
        """

        :return:
        """
        return self.extensionWrap

    def set_extensionElement(self, newExtensionElement):
        """

        :param          newExtensionElement:
        :type           newExtensionElement:    PB_Element
        :Example Value: countryOfCreation
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionElement/
        :return:        None
        """
        # TODO: Create Docstring for set_extensionElement
        if isinstance(newExtensionElement, PB_Element):
            self.extensionElement = newExtensionElement
        else:
            raise TypeError("Expected type: PB_Element")

    def get_extensionElement(self):
        """

        :return:
        """
        return self.extensionElement

    def set_extensionValue(self, newExtensionValue):
        """

        :param          newExtensionValue:
        :type           newExtensionValue:  PB_Element
        :Example Value: US
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionValue/
        :return:        None
        """
        # TODO: Create Docstring for set_extensionValue
        if isinstance(newExtensionValue, PB_Element):
            self.extensionValue = newExtensionValue
        else:
            raise TypeError("Expected type: PB_Element")

    def get_extensionValue(self):
        """

        :return:
        """
        return self.extensionValue

    def set_extensionAuthorityUsed(self, newExtensionAuthorityUsed):
        """

        :param          newExtensionAuthorityUsed:
        :type           newExtensionAuthorityUsed:  PB_Element
        :Example Value: ISO 3166.1
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionAuthorityUsed/
        :return:        None
        """
        # TODO: Create Docstring for set_extensionAuthorityUsed
        if isinstance(newExtensionAuthorityUsed, PB_Element):
            self.extensionAuthorityUsed = newExtensionAuthorityUsed
        else:
            raise TypeError("Expected type: PB_Element")

    def get_extensionAuthorityUsed(self):
        """

        :return:
        """
        return self.extensionAuthorityUsed

    def set_extensionEmbedded(self, newExtensionEmbedded):
        """

        :param          newExtensionEmbedded:
        :Example Value: ""
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionEmbedded/
        :return:        None
        """
        # TODO: Add example of extensionEmbedded
        # TODO: Create Docstring for set_extensionEmbedded
        if isinstance(newExtensionEmbedded, PB_Element):
            self.extensionEmbedded = newExtensionEmbedded
        else:
            raise TypeError("Expected type: PB_Element")

    def get_extensionEmbedded(self):
        """

        :return:
        """
        return self.extensionEmbedded

# FIXME Add _makeXML method for pbcoreExtension

    def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()

##################################
# Other classes
##################################

class PB_Element():
    """
    :Description: Basic element tag
    """

    # TODO: Create Docstring for PB_Element
    def __init__(self, *args, **kwargs):
        """

        :param          tag:
        :param          value:
        :return:        None
        """
        self.attributes = OrderedDict()
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
            if isinstance(kwargs.get("tag"), str):      # checks if the tag is a string
                if kwargs.get("tag") in self.validTags:
                    self.tag = kwargs.get("tag")
                else:
                    raise ValueError("Expected only PBCore elements. Received: ", kwargs.get("tag"))
            else:
                raise TypeError("Expected string. Received: " + type(kwargs.get("tag")))
            if isinstance(kwargs.get("value"), str):    # checks if the value is a string
                self.value = kwargs.get("value")
            else:
                raise TypeError("Expected string. Received: " + type(kwargs.get("value")))
            # self.attribute = OrderedDict()

        if args:
            for arg in args:
                if isinstance(arg[0], str) and isinstance(arg[1], str):     # checks if the attribute name and value are a string
                    self.add_attribute(arg[0], arg[1])
                    # print arg[0], arg[1]
                else:
                    raise ValueError

    def get_attribute(self):
        """

        :return:
        """
        return self.attribute

    def add_attribute(self, key, value):
        """

        :param          key: name of the attribute
        :param          value: value of the attribute
        :return:        None
        """
        # TODO: Create Docstring for add_attribute

        self.attributes[key] = value

    def add_attributes(self, *args):
        """

        :param          args: Use a list in [attribute name, attribute value] format
        :return:        None
        """
        # TODO: Create Docstring for add_attributes
        if args:
            for arg in args:
                if not isinstance(arg, list):
                    raise TypeError("Arguments to add_attributes must be in format [attribute name, attribute value]")
            for arg in args:
                if isinstance(arg[0], str) and isinstance(arg[1], str):
                    self.add_attribute(arg[0], arg[1])
                else:
                    raise ValueError

        # self.attribute[key] = value

    def delete_attribute(self, key):
        """

        :param          key: name of the attribute to be deleted
        :return:        None
        """
        # TODO: Create Docstring for delete_attribute
        del self.attributes[key]

    def get_tag(self):
        """

        :return:
        """
        return self.tag

    def set_tag(self, tag):
        """

        :param          tag:
        :return:        None
        """
        # TODO: Create Docstring for set_tag
        self.tag = tag

    def get_value(self):
        """

        :return:
        """
        return self.value

    def set_value(self, value):
        """

        :param          value:
        :return:        None
        """
        # TODO: Create Docstring for set_value
        self.value = value



    def get_etree_element(self):
        """
        :Description:   Gets a single element as an XML element to be passed down.
        :return:        xml.etree.ElementTree.Element
        """
        element = Element(self.tag)
        element.text = self.value
        if self.attributes:
            attributes = self.attributes
            while attributes:
                key, value = attributes.popitem(last=False)
                element.set(key, value)
            # print self.attribute
        return element
        #

    def xml_print(self):
        """
        :Description:   For debugging. Prints the XML.
        :return:        None
        """
        element = Element(self.tag)
        element.text = self.value
        if self.attributes:
            for key in self.attributes:
                element.set(key, self.attributes[key])
        print etree.tostring(element)

