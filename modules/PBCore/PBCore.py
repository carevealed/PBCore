# from xml.dom.minidom import parse, Element as elmt, Document, Node
from collections import OrderedDict
from abc import ABCMeta, abstractmethod
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
import re

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

# Interface
class XML_PBCore(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def _makeXML(self):
        pass

    def xml(self):
        XML = self._makeXML()
        return XML

    def xmlString(self):
        XML = self._makeXML()
        return etree.tostring(XML)

    def valid_file_size(self, fileSize):
        valid = True
        if len(fileSize.split(' ')) != 2:
            return False
        if not re.search('\d*(\.\d)?\s[K,M,G,T,P,E,Z,Y]?[B,b]', fileSize):
            return False
        return valid

    def valid_entry(self, entry, options):
        if any(word in entry.lower() for word in options):
            return True
        else:
            return False

    pass




class PBCore(XML_PBCore):
    """

    :Description: This is the main class for creating PBCore objects
    :PBCore Homepage: http://pbcore.org/
    """
    def __init__(self, collectionTitle = "", collectionSource = "", collectionRef = "", collectionDate="for institutional reference"):
        """

        :return: None
        """
        # self.root = None
        self.intellectualContent = None
        self.intellectualProperty = None
        self.extensions = []
        self.instantiation = None
        self.collectionTitle = collectionTitle
        self.collectionSource = collectionSource
        self.collectionRef = collectionRef
        self.collectionDate = collectionDate

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

    def add_extensions(self, newextensions):
        """

        :param          newextensions:
        :type           newextensions: Extensions
        :Example Value: ""
        :return:        None
        """
        
        if isinstance(newextensions, pbcoreExtension):
            self.extensions.append(newextensions)
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

    def _makeXML(self):
        # collectionSource="California State Railroad Museum Library" collectionRef="">

        branch = Element("pbcoreCollection", attrib={
            "xmlns":                    "http://www.pbcore.org/PBCore/PBCoreNamespace.html",
            "xmlns:xsi":                "http://www.w3.org/2001/XMLSchema-instance",
            "xsi:schemaLocation":       "http://www.pbcore.org/PBCore/PBCoreNamespace.html http://pbcore.org/xsd/pbcore-2.0.xsd",
            "collectionDate":           self.collectionDate,
            "collectionTitle":          self.collectionTitle,
            "collectionSource":         self.collectionSource,
            "collectionRef":            self.collectionRef
            })
        if self.intellectualContent:
            branch.append(self.intellectualContent.xml())
        if self.intellectualProperty:
            branch.append(self.intellectualProperty.xml())
        if self.extensions:
            for node in self.extensions:
                branch.append(node.xml())
        if self.instantiation:
            branch.append(self.instantiation.xml())
        return branch



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

class pbcoreDescriptionDocument(XML_PBCore):
    """
    :Description:
    :URL: http://pbcore.org/elements/
    """

    def __init__(self,
                assetType="Media Object",
                mainTitle=None,
                parentObjectID=None,
                projectID=None,
                addTitle=None,
                seriesTitle=None,
                description=None,
                objectARK=None,
                institutionName=None,
                institutionARK=None,
                institutionURL=None,
                producer=None,
                director=None,
                writer=None,
                interviewer=None,
                performer=None,
                camera=None,
                editor=None,
                sound=None,
                music=None,
                cast=None,
                interviewee=None,
                speaker=None,
                musician=None,
                publisher=None,
                distributor=None,
                genre=[]):
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
        self.pbcoreAssetType = PB_Element(tag="pbcoreAssetType", value=assetType)
        self.pbcoreAssetDate = []
        self.pbcoreIdentifier = []
        if parentObjectID and parentObjectID != "":
            self.pbcoreIdentifier.append(PB_Element(['source', 'CAVPP'], ['annotation', 'Object Identifier'], tag="pbcoreIdentifier", value=parentObjectID))

        if projectID and projectID != "":
            self.pbcoreIdentifier.append(PB_Element(['source', 'CAVPP'], ['annotation', 'Project Identifier'], tag="pbcoreIdentifier", value=projectID))

        if objectARK and objectARK != "":
            if institutionName and institutionName != '':
                self.pbcoreIdentifier.append(PB_Element(['source', institutionName], ['annotation', 'Object ARK'], tag="pbcoreIdentifier", value=objectARK))
            else:
                self.pbcoreIdentifier.append(PB_Element(['annotation', 'Object ARK '], tag="pbcoreIdentifier", value=objectARK))

        if institutionARK and institutionARK != "":
            if institutionName and institutionName != '':
                self.pbcoreIdentifier.append(PB_Element(['source', institutionName], ['annotation', 'Institution ARK'], tag="pbcoreIdentifier", value=institutionARK))
            else:
                self.pbcoreIdentifier.append(PB_Element(['annotation', 'Institution ARK'], tag="pbcoreIdentifier", value=institutionARK))

        if institutionURL and institutionURL != "":
            if institutionName and institutionName != '':
                self.pbcoreIdentifier.append(PB_Element(['source', institutionName], ['annotation', 'Institution URL'], tag="pbcoreIdentifier", value=institutionURL))
            else:
                self.pbcoreIdentifier.append(PB_Element(['annotation', 'Institution URL'], tag="pbcoreIdentifier", value=institutionURL))


        self.pbcoreTitle = []
        if mainTitle and mainTitle != "":
            self.pbcoreTitle.append((PB_Element(['titleType', 'Main or Supplied Title'], tag="pbcoreTitle", value=mainTitle)))

        if addTitle and addTitle != "":
            self.pbcoreTitle.append((PB_Element(['titleType', 'Additional Title'], tag="pbcoreTitle", value=addTitle)))

        if seriesTitle and seriesTitle != "":
            self.pbcoreTitle.append((PB_Element(['titleType', 'Series Title'], tag="pbcoreTitle", value=seriesTitle)))

        self.pbcoreSubject = []
        self.pbcoreDescription = []
        if description and description != "":
            self.pbcoreDescription.append(PB_Element(['descriptionType', 'Content Summary'], tag="pbcoreDescription", value=description))
        self.pbcoreGenre = []
        if genre and genre != "":
            if self.genreAutority and self.genreAutority != "":
                self.pbcoreGenre.append(PB_Element(['source', self.genreAutority], tag="pbcoreGenre", value=genre))
            else:
                self.pbcoreGenre.append(PB_Element(tag="pbcoreGenre", value=genre))
            pass
        self.pbcoreRelation = []
        self.pbcoreCoverage = []
        self.pbcoreAudienceLevel = None
        self.pbcoreAudienceRating = None
        self.pbcoreAnnotation = None
        self.pbcoreCreator = []
        if producer and producer != "":
            self.pbcoreCreator.append(PB_Element(["role", "Producer"], tag="pbcoreCreator", value=producer))

        if director and director != "":
            self.pbcoreCreator.append(PB_Element(["role", "Director"], tag="pbcoreCreator", value=director))

        if writer and writer != "":
            self.pbcoreCreator.append(PB_Element(["role", "writer"], tag="pbcoreCreator", value=writer))

        if interviewer and interviewer != "":
            self.pbcoreCreator.append(PB_Element(["role", "interviewer"], tag="pbcoreCreator", value=interviewer))

        if performer and performer != "":
            self.pbcoreCreator.append(PB_Element(["role", "performer"], tag="pbcoreCreator", value=performer))

        self.pbcoreContributor = []
        if camera and camera != "":
            self.pbcoreContributor.append(PB_Element(["role", "camera"], tag="pbcoreContributor", value=camera))

        if editor and editor != "":
            self.pbcoreContributor.append(PB_Element(["role", "editor"], tag="pbcoreContributor", value=editor))

        if sound and sound != "":
            self.pbcoreContributor.append(PB_Element(["role", "sound"], tag="pbcoreContributor", value=sound))

        if music and music != "":
            self.pbcoreContributor.append(PB_Element(["role", "music"], tag="pbcoreContributor", value=music))

        if cast and cast != "":
            self.pbcoreContributor.append(PB_Element(["role", "cast"], tag="pbcoreContributor", value=cast))

        if interviewee and interviewee != "":
            self.pbcoreContributor.append(PB_Element(["role", "interviewee"], tag="pbcoreContributor", value=interviewee))

        if speaker and speaker != "":
            self.pbcoreContributor.append(PB_Element(["role", "speaker"], tag="pbcoreContributor", value=speaker))

        if musician and musician != "":
            self.pbcoreContributor.append(PB_Element(["role", "musician"], tag="pbcoreContributor", value=musician))

        self.pbcorePublisher = []
        if publisher and publisher != "":
            self.pbcorePublisher.append(PB_Element(["role", "publisher"], tag="pbcorePublisher", value=publisher))

        if distributor and distributor != "":
            self.pbcorePublisher.append(PB_Element(["role", "distributor"], tag="pbcorePublisher", value=distributor))

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
        return self.pbcoreAssetDate

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

    def add_pbcoreSubject(self, newpbcoreSubject):
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
            self.pbcoreSubject.append(newpbcoreSubject)
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

    def add_pbcoreGenre(self, newpbcoreGenre):
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
            self.pbcoreGenre.append(newpbcoreGenre)
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
        :type           newpbcoreRelation: pbcoreRelation
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
            for node in self.pbcoreSubject:
                branch.append(node.get_etree_element())

        if self.pbcoreDescription:
            for node in self.pbcoreDescription:
                branch.append(node.get_etree_element())

        if self.pbcoreGenre:
            for node in self.pbcoreGenre:
                branch.append(node.get_etree_element())

        if self.pbcoreRelation:
            for node in self.pbcoreRelation:
                branch.append(node.xml())

        if self.pbcoreCoverage:
            for node in self.pbcoreCoverage:
                branch.append(node.xml())

        if self.pbcoreAudienceLevel:
            for node in self.pbcoreAudienceLevel:
                branch.append(node.get_etree_element())

        if self.pbcoreAudienceRating:
            for node in self.pbcoreAudienceRating:
                branch.append(node.get_etree_element())

        if self.pbcoreAnnotation:
            for node in self.pbcoreAnnotation:
                branch.append(node.get_etree_element())

        if self.pbcoreCreator:
            for node in self.pbcoreCreator:
                branch.append(node.xml())

        if self.pbcoreContributor:
            for node in self.pbcoreContributor:
                branch.append(node.xml())

        if self.pbcorePublisher:
            for node in self.pbcorePublisher:
                branch.append(node.xml())

        if self.pbcoreRightsSummary:
            for node in self.pbcoreRightsSummary:
                branch.append(node.xml())

        if self.pbcorePart:
            for node in self.pbcorePart:
                branch.append(node.xml())

        if self.pbcoreExtension:
            for node in self.pbcoreExtension:
                branch.append(node.xml())
        # branch.append(self.pbcoreRelationIdentifier.get_etree_element())
        # branch.append(self.pbcoreRelationType.get_etree_element())
        return branch

    # def xml(self):
    #     # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML
    #
    # def xml_string(self):
    #     XML = self._makeXML()
    #
    #     return etree.tostring(XML)

    def add_pbcore_extension(self, newpbcoreExtension):
        """

        :param          newpbcoreExtension:
        :type           newpbcoreExtension: newpbcoreExtension
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
        :type           newpbcorePart:  CAVPP_Part
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

    # def xml(self):
    #
    #     # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML

    # def xmlString(self):
    #     XML = self._makeXML()
# __________________________________
class pbcoreRelation(XML_PBCore):
    """
    :Description:
    :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerelation/
    """
    # TODO: Create Docstring for pbcoreRelation
    def __init__(self, reType=None, reID=None):
        """
        @type           self.pbcoreRelationType:            PB_Element
        @type           self.pbcoreRelationIdentifier:      PB_Element

        :return:    None
        """
        self.pbcoreRelationType = None
        if reType and reType != "":
            self.pbcoreRelationType = PB_Element(tag='pbcoreRelationType', value=reType)

        self.pbcoreRelationIdentifier = None
        if reID and reID != "":
            self.pbcoreRelationIdentifier = PB_Element(tag='pbcoreRelationIdentifier', value=reID)

        self.pbcoreRelationIdentifierAttributes = [
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
        if self.pbcoreRelationType and self.pbcoreRelationType != "":
            branch.append(self.pbcoreRelationType.get_etree_element())
        else:
            branch.append(PB_Element(tag="pbcoreRelationType", value="MISSING REQUIRED DATA").get_etree_element())
        if self.pbcoreRelationIdentifier and self.pbcoreRelationIdentifier != "":
            branch.append(self.pbcoreRelationIdentifier.get_etree_element())
        else:
            branch.append(PB_Element(tag="pbcoreRelationIdentifier", value="MISSING REQUIRED DATA").get_etree_element())

        return branch

    # def xml(self):
    #
    #     # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML
    #
    # def xmlString(self):
    #     XML = self._makeXML()
    #     return etree.tostring(XML)


# __________________________________
class pbcoreCoverage(XML_PBCore):
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecoverage/
    """
    # TODO: Create Docstring for pbcoreCoverage
    def __init__(self,
                 covItem=None,
                 covType=None):
        """

        @type           self.coverage:          PB_Element
        @type           self.coverageType:      PB_Element
        :return:        None
        """


        self.coverage = None
        if covItem and covItem != "":
            self.coverage = PB_Element(tag='coverage', value=covItem)

        self.coverageType = None

        if covType and covType != "":
            self.set_coverageType(PB_Element(tag='coverageType', value=covType))

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
        valid_types = ["spatial", "temporal"]
        if isinstance(newCoverageType, PB_Element):
            if self.valid_entry(newCoverageType.get_value(), valid_types):
                self.coverageType = newCoverageType
            else:
                raise ValueError("coverageType recieved " + newCoverageType.get_value() +" but can only accept " + str(valid_types))
        else:
            raise TypeError("Expected type: PB_Element")


    def _makeXML(self):
        branch = Element("pbcoreCoverage")
        if self.coverage:
            branch.append(self.coverage.get_etree_element())

        if self.coverageType:
            branch.append(self.coverageType.get_etree_element())

        return branch

    # def xml(self):
    #
    #     # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML
    #
    # def xmlString(self):
    #     XML = self._makeXML()

##################################
# intellectual Property classes
##################################


class IntellectualProperty(XML_PBCore):
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
class pbcoreCreator(XML_PBCore):
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecreator/
    """
    # TODO: Create Docstring for pbcoreCreator
    def __init__(self, name=None, role=None):
        """
        @type           self.creator:           PB_Element
        @type           self.creatorRole:       PB_Element
        :return:
        """
        self.creator = None
        if name and name != "":
            self.creator = PB_Element(tag="creator", value=name)
        self.creatorRole = []
        if role and role != "":
            self.creatorRole.append(PB_Element(tag="creatorRole", value=role))
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

        branch.append(self.creator.get_etree_element())
        for role in self.creatorRole:
            branch.append(role.get_etree_element())
        return branch

    # def xml(self):
    #
    #     # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML

    # def xmlString(self):
    #     XML = self._makeXML()
    #     return etree.tostring(XML)

# __________________________________
class pbcoreContributor(XML_PBCore):
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecontributor/
    """
    # TODO: Create Docstring for pbcoreContributor
    def __init__(self, name=None, role=None):
        """
        @type           self.contributor:           PB_Element
        @type           self.contributorRole:       PB_Element
        :return:
        """
        self.contributor = None
        if name and name != "":
            self.contributor = PB_Element(tag="contributor", value=name)

        self.contributorRole = []
        if role and role != "":
            self.contributorRole.append(PB_Element(tag="contributorRole", value=role))

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

    def add_contributorRole(self, newContributoRole):
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
            self.contributorRole.append(newContributoRole)
        else:
            raise TypeError("Expected type: PB_Element")

    def get_contributorRole(self):
        """

        :return:
        """
        return self.contributorRole

# TODO: Test _makeXML method for pbcoreContributor
    def _makeXML(self):
        branch = Element("pbcoreContributor")
        if self.contributor:
            branch.append(self.contributor.get_etree_element())
        if self.contributorRole:
            for node in self.contributorRole:
                branch.append(node.get_etree_element())
        return branch

    # def xml(self):

        # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML
    #
    # def xmlString(self):
    #     XML = self._makeXML()
    #     return etree.tostring(XML)

# __________________________________
class pbcorePublisher(XML_PBCore):
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorepublisher/
    """
    # TODO: Create Docstring for pbcorePublisher
    def __init__(self, name=None, role=None):
        """
        @type           self.publisher:             PB_Element
        @type           self.publisherRole:         PB_Element

        :return:        None
        """
        self.publisher = None
        if name and name != "":
            self.publisher = PB_Element(tag="publisher", value=name)

        self.publisherRole = []
        if role and role != "":
            self.publisherRole.append(PB_Element(tag="publisherRole", value=role))

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

    def add_publisherRole(self, newPublisherRole):
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
            self.publisherRole.append(newPublisherRole)
        else:
            raise TypeError("Expected type: PB_Element")

# TODO: Test _makeXML method for pbcorePublisher

    def _makeXML(self):
        branch = Element("pbcorePublisher")
        branch.append(self.publisher.get_etree_element())
        for node in self.publisherRole:
            branch.append(node.get_etree_element())
        return branch


    # def xml(self):
    #
    #     # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML
    #
    # def xmlString(self):
    #     XML = self._makeXML()
    #     return etree.tostring(XML)

# __________________________________
class pbcoreRightsSummary(XML_PBCore):
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/
    """
    # TODO: Create Docstring for pbcoreRightsSummary
    def __init__(self, copyright_holder=None, copyright_statement=None, copyright_holder_info=None):
        """

        @type           self.rightsSummary:         PB_Element
        @type           self.rightsLink:            PB_Element
        @type           self.rightsEmbedded:        PB_Element

        :return:        None
        """
        self.rightsSummary = None
        if copyright_statement and copyright_statement != "":
            self.rightsSummary = (PB_Element(['annotation', 'Copyright Statement'], tag="rightsSummary", value=copyright_statement))

        if copyright_holder and copyright_holder != "":
            self.rightsSummary = (PB_Element(['annotation', 'Copyright Holder'], tag="rightsSummary", value=copyright_holder))

        if copyright_holder_info and copyright_holder_info != "":
            self.rightsSummary = (PB_Element(['annotation', 'Copyright Holder Info'], tag="rightsSummary", value=copyright_holder_info))


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

    def set_rightsSummary(self, newRightsSummary):
        """

        :param          newRightsSummary:
        :type           newRightsSummary:       PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/rightssummary/
        """
        # TODO: Give example of set_rightsSummary
        # TODO: Create Docstring for set_rightsSummary

        if isinstance(newRightsSummary, PB_Element):
            self.rightsSummary = newRightsSummary
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
        if self.rightsSummary:
            branch.append(self.rightsSummary.get_etree_element())

        for link in self.rightsLink:
            branch.append(link.get_etree_element())

        for rightsEmb in self.rightsEmbedded:
            branch.append(rightsEmb.get_etree_element())
        return branch

    # def xml(self):
    #
    #     # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML
    #
    # def xmlString(self):
    #     XML = self._makeXML()
    #     return etree.tostring(XML)


##################################
# instantiation classes
##################################
class CAVPP_Part(XML_PBCore):
    def __init__(self,
                 objectID=None,
                 callNumber=None,
                 mainTitle=None,
                 description=None):

        self.pbcoreIdentifier = []
        if objectID and objectID != "":
            self.pbcoreIdentifier.append(PB_Element(['source', 'CAVPP'], ['annotation', 'Object Identifier'], tag='pbcoreIdentifier', value=objectID))
        if callNumber and callNumber != "":
            self.pbcoreIdentifier.append(PB_Element(['source', 'CAVPP'], ['annotation', 'Call Number'], tag='pbcoreIdentifier', value=callNumber))

        self.pbcoreTitle = []
        if mainTitle and mainTitle != "":
            self.pbcoreTitle.append(PB_Element(['titleType', 'Main'], tag='pbcoreTitle', value=mainTitle))

        self.pbcoreDescription = []
        if description and description != "":
            self.pbcoreDescription.append(PB_Element(tag='pbcoreDescription', value=description))

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
        """
        :return     list of PBCore Elements
        """
        return self.pbcoreInstantiation

    def add_pbcoreInstantiation(self, newpbcoreInstantiation):
        if isinstance(newpbcoreInstantiation, pbcoreInstantiation):
            self.pbcoreInstantiation.append(newpbcoreInstantiation)

    def _makeXML(self):
        branch = Element("pbcorePart")
        # branch.append(etree.tostring(self.pbcoreRelationType))
        if self.pbcoreIdentifier:
            for node in self.pbcoreIdentifier:
                branch.append(node.get_etree_element())
        else:
            branch.append(PB_Element(tag="pbcoreIdentifier", value="MISSING REQUIRED DATA").get_etree_element())

        if self.pbcoreTitle:
            for node in self.pbcoreTitle:
                branch.append(node.get_etree_element())
        else:
            branch.append(PB_Element(tag="pbcoreTitle", value="MISSING REQUIRED DATA").get_etree_element())

        if self.pbcoreDescription:
            for node in self.pbcoreDescription:
                branch.append(node.get_etree_element())
        else:
            branch.append(PB_Element(tag="pbcoreDescription", value="MISSING REQUIRED DATA").get_etree_element())

        if self.pbcoreInstantiation:
            for node in self.pbcoreInstantiation:
                branch.append(node.xml())
        return branch

    # def xml(self):
    #
    #     # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML
    #
    # def xmlString(self):
    #     XML = self._makeXML()
    #     return etree.tostring(XML)



class pbcoreInstantiation(XML_PBCore):
    # TODO: Create Docstring for pbcoreInstantiation
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/
    """
    def __init__(self,
                 type=None,
                 objectID=None,
                 date=None,
                 extent=None,
                 dimensions=None,
                 physical=None,
                 fileType=None,
                 fileTypeAuthority=None,
                 standard=None,
                 location=None,
                 mediaType=None,
                 generations=None,
                 fileName=None,
                 fileSize=None,
                 baseType=None,
                 stockManufacture=None,
                 baseThickness=None,
                 checksum=None,
                 vender='CAVPP',
                 cataloger='CAVPP',
                 timeStart=None,
                 duration=None,
                 dataRate=None,
                 colors=None,
                 aspectRatio=None,
                 tracks=None,
                 channelConfiguration=None,
                 language=None,
                 alternativeModes=None):
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
        @type           self.InstantiationPart:                     PB_Element
        @type           self.instantiationExtension:                PB_Element

        :param type:
        :return:
        """
        self.instantiationAssetType = None
        if type and type != "":
            self.instantiationAssetType = type
        # For example: "Physical Asset" instantiationAssetType

        self.instantiationIdentifier = []
        if objectID and objectID != "":
            self.instantiationIdentifier.append(PB_Element(['source', cataloger], tag='instantiationIdentifier', value=objectID))

        if fileName and fileName != "":
            self.instantiationIdentifier.append(PB_Element(['source', vender], tag='instantiationIdentifier', value=fileName))

        if checksum and checksum != "":
            self.instantiationIdentifier.append(PB_Element(['source', vender], tag='instantiationIdentifier', value=checksum))

        self.instantiationDate = []
        if date and date != "":
            self.instantiationDate.append(PB_Element(tag="instantiationDate", value=date))

        self.instantiationDimensions = []
        if dimensions and dimensions != "":
            self.instantiationDimensions.append(PB_Element(tag='instantiationDimensions', value=dimensions))

        self.instantiationPhysical = None
        if physical and physical != "":
            self.instantiationPhysical = PB_Element(tag="instantiationPhysical", value=physical)

        self.instantiationDigital = None
        if fileType and fileType != "":
            if fileTypeAuthority:
                self.instantiationDigital = PB_Element(['source', fileTypeAuthority], tag='instantiationDigital', value=fileType)
            else:
                raise ValueError("Using the fileType optional argument requires that you also specifiy a "
                                 "fileTypeAuthority")
        self.instantiationStandard = None
        if standard and standard != None:
            self.instantiationStandard = PB_Element(tag="instantiationStandard", value=standard)

        self.instantiationLocation = None
        if location and location != "":
            self.instantiationLocation = PB_Element(tag="instantiationLocation", value=location)

        self.instantiationMediaType = None
        if mediaType and mediaType != "":
            self.instantiationMediaType = PB_Element(tag="instantiationMediaType", value=mediaType)

        self.instantiationGenerations = None
        if generations and generations != "":
            self.instantiationGenerations = PB_Element(tag="instantiationGenerations", value=generations)

        self.instantiationFileSize = None
        if fileSize and fileSize != "":
            if self.valid_file_size(fileSize):
                size = fileSize.split(" ")[0]
                unit = fileSize.split(" ")[1]

                self.instantiationFileSize = PB_Element(['unitsOfMeasure', unit], tag="instantiationFileSize", value=size)

        self.instantiationTimeStart = None
        if timeStart and timeStart != "":
            self.instantiationTimeStart = PB_Element(tag="instantiationTimeStart", value=timeStart)

        self.instantiationDuration = None
        if duration and duration != "":
            self.instantiationDuration = PB_Element(tag="instantiationDuration", value=duration)

        self.instantiationDataRate = None

        self.instantiationColors = None
        if colors and colors != "":
            self.instantiationColors = PB_Element(tag='instantiationColors', value=colors)

        self.instantiationTracks = None
        if tracks and tracks != "":
            self.instantiationTracks = PB_Element(tag='instantiationTracks', value=tracks)

        self.instantiationChannelConfiguration = None
        if channelConfiguration and channelConfiguration != None:
            self.instantiationChannelConfiguration = PB_Element(tag='instantiationChannelConfiguration', value=channelConfiguration)

        self.instantiationLanguage = None
        if language and language != "":
            self.instantiationLanguage = PB_Element(['source', 'IS0 639.2'], tag='instantiationLanguage', value=language)

        self.instantiationAlternativeModes = []
        if alternativeModes and alternativeModes != None:
            self.instantiationAlternativeModes.append(PB_Element(tag='instantiationAlternativeModes', value=alternativeModes))

        self.instantiationEssenceTrack = []
        self.instantiationRelation = []
        self.instantiationAnnotation = []
        if extent and extent != "":
            self.instantiationAnnotation.append(PB_Element(['annotationType', 'Extent'], tag='instantiationAnnotation', value=extent))

        if stockManufacture and stockManufacture != "":
            self.instantiationAnnotation.append(PB_Element(['annotationType', 'StockManufacture'], tag="instantiationAnnotation", value=stockManufacture))

        if baseType and baseType != "":
            self.instantiationAnnotation.append(PB_Element(['annotationType', 'BaseType'], tag="instantiationAnnotation", value=baseType))

        if baseThickness and baseThickness != "":
            self.instantiationAnnotation.append(PB_Element(['annotationType', 'BaseThickness'], tag="instantiationAnnotation", value=baseThickness))

        self.instantiationPart = []
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

    def add_instantiationAlternativeModes(self, newInstantiationAlternativeModes):
        """

        :param          newInstantiationAlternativeModes:
        :type           newInstantiationAlternativeModes:   PB_Element
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationAlternativeModes/
        """
        # TODO: Give example instantiationAlternativeModes
        # TODO: Create Docstring for set_instantiationAlternativeModes
        self.instantiationAlternativeModes.append(newInstantiationAlternativeModes)

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

    def add_instantiationPart(self, newInstantiationPart):
        """

        :param          newInstantiationPart:
        :type           newInstantiationPart:   InstantiationPart
        :Example Value: ""
        :return:        None
        :URI:           http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/InstantiationPart/
        """
        # TODO: Give example InstantiationPart
        # FIXME: Change PB_Element to InstantiationPart object for add_add_instantiationPart()
        # TODO: Create Docstring for set_instantiationPart
        if isinstance(newInstantiationPart, InstantiationPart):
            self.instantiationPart.append(newInstantiationPart)
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
            for node in self.instantiationAlternativeModes:
                branch.append(node.get_etree_element())

        if self.instantiationEssenceTrack:
            for node in self.instantiationEssenceTrack:
                branch.append(node.xml())

        if self.instantiationRelation:
            for instRelation in self.instantiationRelation:
                branch.append(instRelation.get_etree_element())

        if self.instantiationAnnotation:
            for instAnnotation in self.instantiationAnnotation:
                branch.append(instAnnotation.get_etree_element())

        if self.instantiationPart:
            for node in self.instantiationPart:
                branch.append(node.xml())

        if self.instantiationExtension:
            branch.append(self.instantiationExtension)

        return branch

    # def xml(self):
    #
    #     # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML
    #
    # def xmlString(self):
    #     XML = self._makeXML()
    #     return etree.tostring(XML)
# __________________________________
class InstantiationEssenceTrack(XML_PBCore):
    """
    :Description:
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/
    """
    # TODO: Create Docstring for InstantiationEssenceTrack
    def __init__(self, type=None,
                objectID= None,
                standard=None,
                encoding=None,
                frameRate=None,
                ips=None,
                samplingRate=None,
                bitDepth=None,
                aspectRatio=None,
                timeStart=None,
                duration=None,
                language=None):
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
        if type and type != "":
            self.essenceTrackType = PB_Element(tag='essenceTrackType', value=type)

        self.essenceTrackIdentifier = None
        if objectID and objectID != "":
            self.essenceTrackIdentifier = PB_Element(['source', 'CAVPP'], ['annotation', 'Object Identifier'], tag="essenceTrackIdentifier", value=objectID)

        self.essenceTrackStandard = None
        if standard and standard != "":
            self.essenceTrackStandard = PB_Element(tag="essenceTrackStandard", value=standard)

        self.essenceTrackEncoding = None
        if encoding and encoding != "":
            self.essenceTrackEncoding = PB_Element(tag="essenceTrackEncoding", value=encoding)

        self.essenceTrackDataRate = None

        self.essenceTrackFrameRate = None
        if frameRate and frameRate != "":
            self.essenceTrackFrameRate = PB_Element(['unitsOfMeasure', 'fps'], tag="essenceTrackFrameRate", value=frameRate)

        self.essenceTrackPlaybackSpeed = None
        if ips and ips != "":
            self.essenceTrackPlaybackSpeed = PB_Element(["unitsOfMeasure", "ips"], tag="essenceTrackPlaybackSpeed", value=ips)

        self.essenceTrackSamplingRate = None
        if samplingRate and samplingRate != "":
            self.essenceTrackSamplingRate = PB_Element(['unitsOfMeasure', 'kHz'], tag="essenceTrackSamplingRate", value=samplingRate)

        self.essenceTrackBitDepth = None
        if bitDepth and bitDepth != "":
            self.essenceTrackBitDepth = PB_Element(tag="essenceTrackBitDepth", value=bitDepth)

        self.essenceTrackFrameSize = None

        self.essenceTrackAspectRatio = None
        if aspectRatio and aspectRatio != "":
            self.essenceTrackAspectRatio = PB_Element(tag="essenceTrackAspectRatio", value=aspectRatio)

        self.essenceTrackTimeStart = None
        if timeStart and timeStart != "":
            self.essenceTrackTimeStart = PB_Element(tag="essenceTrackTimeStart", value=timeStart)

        self.essenceTrackDuration = None
        if duration and duration != "":
            self.essenceTrackDuration = PB_Element(tag="essenceTrackDuration", value=duration)

        self.essenceTrackLanguage = None
        if language and language != "":
            self.essenceTrackLanguage = PB_Element(tag="essenceTrackLanguage", value=language)

        self.essenceTrackAnnotation = []
        self.essenceTrackExtension = []


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

    # def xml(self):
    #
    #     # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML
    #
    # def xmlString(self):
    #     XML = self._makeXML()


# __________________________________
class InstantiationRelation(XML_PBCore):
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
    # TODO: TEST _makeXML method for InstantiationRelation

    def _makeXML(self):
        branch = Element("InstantiationRelation")
        branch.append(self.instantiationRelationType.get_etree_element())
        branch.append(self.instantiationRelationIdentifier.get_etree_element())
        return branch

    # def xml(self):
    #
    #     # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML
    #
    # def xmlString(self):
    #     XML = self._makeXML()
    #     return etree.tostring(XML)

class InstantiationRights(XML_PBCore):
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

# TODO: Test _makeXML method for pbcoreRights
    def _makeXML(self):
        branch = Element("pbcoreRights")
        for node in self.rightsSummary:
            branch.append(node.get_etree_element())

        for node in self.rightsLink:
            branch.append(node.get_etree_element())

        for node in self.rightsEmbedded:
            branch.append(node.get_etree_element())

        return branch

    # def xml(self):
    #
    #     # branch = etree.ElementTree(self.pbcoreRelationType)
    #     XML = self._makeXML()
    #     return XML
    #
    # def xmlString(self):
    #     XML = self._makeXML()
    #     return etree.tostring(XML)

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



class InstantiationPart(XML_PBCore):


    def __init__(self,
                 objectID=None,
                 location=None,
                 duration=None,
                 fileSize=None):
        self.instantiationIdentifier = []
        if objectID and objectID != "":
            self.instantiationIdentifier.append(PB_Element(['source', 'CAVPP'],['annotation', 'Object Identifier'], tag="instantiationIdentifier", value=objectID))

        self.instantiationLocation = None
        if location and location != "":
            self.instantiationLocation = PB_Element(tag="instantiationLocation", value=location)

        self.instantiationFileSize = None
        if fileSize and fileSize != "":
            self.instantiationFileSize = PB_Element(tag="instantiationFileSize", value=fileSize)

        self.instantiationDuration = None
        if duration and duration != "":
            self.instantiationDuration = PB_Element(tag="instantiationDuration", value=duration)

        self.instantiationEssenceTrack = []


    def get_instantiationIdentifier(self):
        return self.instantiationIdentifier

    def add_instantiationIdentifier(self, newInstantiationIdentifier):
        if isinstance(newInstantiationIdentifier, PB_Element):
            self.instantiationIdentifier.append(newInstantiationIdentifier)
        else:
            raise TypeError("Expected Type: PB_Element")

    def get_instantiationLocation(self):
        return self.instantiationLocation

    def set_instantiationLocation(self, newInstantiationLocation):
        if isinstance(newInstantiationLocation, PB_Element):
            self.instantiationLocation = newInstantiationLocation
        else:
            raise TypeError("Expected Type: PB_Element")

    def get_instantiationFileSize(self):
        return self.instantiationFileSize

    def set_instantiationFileSize(self, newInstantiationFileSize):
        if isinstance(newInstantiationFileSize, PB_Element):
            self.instantiationFileSize = newInstantiationFileSize
        else:
            raise TypeError("Expected Type: PB_Element")

    def get_instantiationDuration(self):
        return self.instantiationDuration

    def set_instantiationDuration(self, newInstantiationDuration):
        if isinstance(newInstantiationDuration, PB_Element):
            self.instantiationDuration = newInstantiationDuration
        else:
            raise TypeError("Expected Type: PB_Element")

    def get_instantiationEssenceTrack(self):
        return self.instantiationEssenceTrack

    def add_instantiationEssenceTrack(self, newInstantiationEssenceTrack):
        if isinstance(newInstantiationEssenceTrack, InstantiationEssenceTrack):
            self.instantiationEssenceTrack.append(newInstantiationEssenceTrack)
        else:
            raise TypeError("Expected Type: InstantiationEssenceTrack")


    def _makeXML(self):
        branch = Element("instantiationPart")
        if self.instantiationIdentifier:
            for node in self.instantiationIdentifier:
                branch.append(node.get_etree_element())

        if self.instantiationLocation:
            branch.append(self.instantiationLocation.get_etree_element())
        else:
            branch.append(PB_Element(tag="instantiationLocation", value="MISSING REQUIRED DATA").get_etree_element())

        if self.instantiationFileSize:
            branch.append(self.instantiationFileSize.get_etree_element())

        if self.instantiationDuration:
            branch.append(self.instantiationDuration.get_etree_element())

        if self.instantiationEssenceTrack:
            for node in self.instantiationEssenceTrack:
                branch.append(node.xml())

        return branch


class pbcoreExtension(XML_PBCore):
    """
    :URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/
    """
    # TODO: Create Docstring for pbcoreExtension
    def __init__(self,
                exElement=None,
                exValue=None,
                exAuthority=None):
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
        if exElement and exElement != "":
            self.extensionElement =PB_Element(tag="extensionElement", value=exElement)

        self.extensionValue = None
        if exValue and exValue != "":
            self.extensionValue =PB_Element(tag="extensionValue", value=exValue)

        self.extensionAuthorityUsed = None
        if exAuthority and exAuthority != "":
            self.extensionAuthorityUsed =PB_Element(tag="extensionAuthorityUsed", value=exAuthority)

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

# TODO: Test _makeXML method for pbcoreExtension
    def _makeXML(self):
        longer_branch= Element("pbcoreExtension")
        branch = Element("extensionWrap")

        # for node in self.extensionWrap:
        #     branch.append(node.get_etree_element())

        if self.extensionElement:
            branch.append(self.extensionElement.get_etree_element())
        else:
            branch.append(PB_Element(tag="extensionElement", value="MISSING REQUIRED DATA").get_etree_element())

        if self.extensionValue:
            branch.append(self.extensionValue.get_etree_element())
        else:
            branch.append(PB_Element(tag="extensionValue", value="MISSING REQUIRED DATA").get_etree_element())

        if self.extensionAuthorityUsed:
            branch.append(self.extensionAuthorityUsed.get_etree_element())
        else:
            branch.append(PB_Element(tag="extensionAuthorityUsed", value="MISSING REQUIRED DATA").get_etree_element())

        if self.extensionEmbedded:
            branch.append(self.extensionEmbedded.get_etree_element())

        longer_branch.append(branch)
        return longer_branch


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
            "InstantiationPart",
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

