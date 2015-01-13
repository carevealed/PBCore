__author__ = 'California Audiovisual Preservation Project'
# PBCore metadata


##################################
# Intellectual Content
##################################

class IntellectualContent():
    def __init__(self):

        self.pbcoreAssetType = None
        # For example: "Media Object"
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreassettype/
        # TODO: Add URI to pbcoreAssetType

        self.pbcoreAssetDate = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreassetdate/
        # TODO: add URI to pbcoreAssetDate

        self.pbcoreIdentifier = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreidentifier/
        # TODO: add URI to pbcoreIdentifier

        self.pbcoreTitle = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoretitle/
        # TODO: add URI to pbcoreTitle

        self.pbcoreSubject = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreSubject/
        # For example: TODO add example of pbcoreSubject

        self.pbcoreDescription = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreDescription

        self.pbcoreGenre = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreGenre
        # For example: TODO add example of pbcoreGenre

        self.pbcoreRelation = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreRelation

        self.pbcoreCoverage = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreCoverage

        self.pbcoreAudienceLevel = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreAudienceLevel
        # For example: TODO add example of pbcoreAudienceLevel

        self.pbcoreAudienceRating = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreAudienceRating
        # For example: TODO add example of pbcoreAudienceRating

        self.pbcoreAnnotation = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreAnnotation
        # For example: TODO add example of pbcoreAnnotation


    def getpbcoreAssetType(self):
        return self.pbcoreAssetType

    def addpbcoreAssetType(self, key, value):
        """Adds an Asset type

        Args:
          key (str): The type of attribute to be added
          value (str): The value of the attribute added

        Example from http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html
        """
        self.pbcoreAssetType[key] = value

    def getpbcoreAssetDate(self):
        return self.pbcoreAssetDate

    def setpbcoreAssetDate(self, newpbcoreAssetDate):
        # TODO: Create Docstring for setpbcoreAssetDate
        self.pbcoreAssetDate = newpbcoreAssetDate

    def getpbcoreIdentifier(self):
        return self.pbcoreIdentifier

    def addpbcoreIdentifier(self, newIdentifier):
        # TODO: Create Docstring for addpbcoreIdentifier
        self.pbcoreIdentifier.append(newIdentifier)

    def getpbcoreTitle(self):
        return self.pbcoreTitle

    def addpbcoreTitle(self, newTitle):
        # TODO: Create Docstring for addpbcoreTitle
        self.pbcoreTitle.append(newTitle)

    def getpbcoreSubject(self):
        return self.pbcoreSubject

    def setpbcoreSubject(self, newpbcoreSubject):
        # TODO: Create Docstring for setpbcoreSubject
        self.pbcoreSubject = newpbcoreSubject

    def getpbcoreDescription(self):
        return self.pbcoreDescription

    def addpbcoreDescription(self, newDescription):
        # TODO: Create Docstring for addpbcoreDescription
        self.pbcoreDescription.append(newDescription)

    def getpbcoreGenre(self):
        return self.pbcoreGenre

    def setpbcoreGenre(self, newpbcoreGenre):
        # TODO: Create Docstring for setpbcoreGenre
        self.pbcoreGenre = newpbcoreGenre

    def getpbcoreRelation(self):
        return self.pbcoreRelation

    def addpbcoreRelation(self, newpbcoreRelation):
        # TODO: Create Docstring for addpbcoreRelation
        self.pbcoreRelation.append(newpbcoreRelation)

    def getpbcoreCoverage(self):
        return self.pbcoreCoverage

    def addpbcoreCoverage(self, newpbcoreCoverage):
        # TODO: Create Docstring for addpbcoreCoverage
        self.pbcoreCoverage.append(newpbcoreCoverage)

    def getpbcoreAudienceLevel(self):
        return self.pbcoreAudienceLevel

    def setpbcoreAudienceLevel(self, newpbcoreAudienceLevel):
        # TODO: Create Docstring for setpbcoreAudienceLevel
        self.pbcoreAudienceLevel = newpbcoreAudienceLevel

    def getpbcoreAudienceRating(self):
        return self.pbcoreAudienceRating

    def setpbcoreAudienceRating(self, newpbcoreAudienceRating):
        # TODO: Create Docstring for setpbcoreAudienceRating
        self.pbcoreAudienceRating = newpbcoreAudienceRating

    def getpbcoreAnnotation(self):
        return self.pbcoreAnnotation

    def setpbcoreAnnotation(self, newpbcoreAnnotation):
        # TODO: Create Docstring for setpbcoreAnnotation
        self.pbcoreAnnotation = newpbcoreAnnotation


class pbcoreRelation():
    def __init__(self):
        self.pbcoreRelationType = None
        # For example: "Has Part"
        # TODO: Add URI link for pbcoreRelationType

        self.pbcoreRelationIdentifier = None
        # For example: "cscrm_000012_r3"
        # TODO: Add URI link for pbcoreRelationIdentifier

    def getpbcoreRelationType(self):
        return self.pbcoreRelationType

    def setpbcoreRelationType(self, newpbcoreRelationType):
        self.pbcoreRelationType = newpbcoreRelationType

    def getpbcoreRelationIdentifier(self):
        return self.pbcoreRelationIdentifier

    def setpbcoreRelationIdentifier(self, newpbcoreRelationIdentifier):
        self.pbcoreRelationIdentifier = newpbcoreRelationIdentifier


##################################
# intellectual Property classes
##################################


class IntellectualProperty():
    def __init__(self):
        self.pbcoreCreator = []
        # TODO: Add URI link to pbcoreCreator

        self.pbcoreContributor = []
        # TODO: Add URI link to pbcoreContributor

        self.pbcorePublisher = []
        # TODO: Add URI link to pbcorePublisher

        self.pbcoreRightsSummary = []
        # TODO: Add URI link to pbcoreRightsSummary


    def getpbcoreCreator(self):
        return self.pbcoreCreator

    def addpbcoreCreator(self, newpbcoreCreator):
        self.pbcoreCreator.append(newpbcoreCreator)

    def getpbcoreContributor(self):
        return self.pbcoreContributor

    def addpbcoreContributor(self, newpbcoreContributor):
        self.pbcoreContributor.append(newpbcoreContributor)

    def getpbcorePublisher(self):
        return self.pbcorePublisher

    def addpbcorePublisher(self, newpbcorePublisher):
        self.pbcorePublisher.append(newpbcorePublisher)

    def getpbcoreRightsSummary(self):
        return self.pbcoreRightsSummary

    def addpbcoreRightsSummary(self, newpbcoreRightsSummary):
        self.pbcoreRightsSummary.append(newpbcoreRightsSummary)


class pbcoreCreator():
    def __init__(self):
        self.creator = None
        # For example: "Unknown"
        # TODO: Add URI link for creator

        self.creatorRole = None
        # For example: "Producer"
        # TODO: Add URI link for creatorRole


    def getCreator(self):
        return self.creator

    def setCreator(self, newCreator):
        self.creator = newCreator

    def getCreatorRole(self):
        return self.creatorRole

    def setCreatorRole(self, newCreatorRole):
        self.creatorRole = newCreatorRole


class pbcoreContributor:
    def __init__(self):
        self.contributor = None
        # For example: "" TODO: Give example of contributor
        # TODO: Add URI link for contributor

        self.contributorRole = None
        # For example: "" TODO: Give example of contributorRole
        # TODO: Add URI link for contributorRole


    def setContributor(self,newContributor):
        self.contributor = newContributor

    def getContributor(self):
        return self.contributor

    def setContributoRoler(self,newContributoRole):
        self.contributorRole = newContributoRole

    def getContributoRoler(self):
        return self.contributorRole


class pbcorePublisher():
    def __init__(self):
        self.publisher = None
        # For example: "" TODO: Give example of publisher
        # TODO: Add URI link to publisher

        self.publisherRole = None
        # For example: "" TODO: Give example of publisherRole
        # TODO: Add URI link to publisherRole


        def getPublisher(self):
            return self.publisher

        def setPublisher(self, newPublisher):
            self.publisher = newPublisher

        def getPublisherRole(self):
            return self.publisherRole

        def setPublisherRole(self, newPublisherRole):
            self.publisherRole = newPublisherRole


class pbcoreRightsSummary():
    def __init__(self):
        self.rightsSummary = []
        # TODO: Add URI link to rightsSummary

        self.rightsLink = None
        # For example: "" TODO: Give example of rightsLink
        # TODO: Add URI link to rightsLink

        self.rightsEmbedded = None
        # For example: "" TODO: Give example of rightsEmbedded
        # TODO: Add URI link to rightsEmbedded


    def getRightsSummary(self):
        return self.rightsSummary

    def addRightsSummary(self, newRightsSummary):
        self.rightsSummary.append(newRightsSummary)

    def getRightsLink(self):
        return self.rightsLink

    def setRightsLink(self, newRightsLink):
        self.rightsLink = newRightsLink

    def getRightsEmbedded(self):
        return self.rightsEmbedded

    def setRightsEmbedded(self, newRightsEmbedded):
        self.rightsEmbedded = newRightsEmbedded


##################################
# instantiation classes
##################################

class pbcoreInstantiation():
    def __init__(self, instantiationType=None):
        self.instantiationAssetType = instantiationType
        # For example: "Physical Asset" instantiationAssetType
        # TODO: Add URI link for instantiationAssetType

        self.instantiationIdentifier = []
        # Use ONLY Element objects
        # TODO: Add URI link for instantiationIdentifier

        self.instantiationDate = None
        # For example: "UTC 2014-10-24 21:37:34"
        # TODO: Add URI link for instantiationDate

        self.instantiationDimensions = None
        # For example: "" TODO: Give example instantiationDimensions

        self.instantiationPhysical = None
        # For example: "Film: 16mm"
        # TODO: Add URI link for instantiationPhysical

        self.instantiationDigital = None
        # Use ONLY Element objects
        # TODO: Add URI link for instantiationDigital

        self.instantiationStandard = None
        # For example: "Blackmagic v210 YUV"
        # TODO: Add URI link for instantiationStandard

        self.instantiationLocation = None
        # For example: "California State Railroad Museum Library"
        # TODO: Add URI link for instantiationLocation

        self.instantiationMediaType = None
        # For example: "Moving Image"
        # TODO: Add URI link for instantiationMediaType

        self.instantiationGenerations = None
        # For example: "Unknown"
        # TODO: Add URI link for instantiationGenerations

        self.instantiationFileSize = None
        # Use ONLY Element objects
        # TODO: Add URI link for instantiationFileSize

        self.instantiationTimeStart = None
        # For example: "00:00:00"
        # TODO: Add URI link for instantiationTimeStart

        self.instantiationDuration = None
        # For example: "00:10:52"
        # TODO: Add URI link for instantiationDuration

        self.instantiationDataRate = None
        # For example: "" TODO: Give example instantiationDataRate
        # TODO: Add URI link for instantiationDataRate

        self.instantiationColors = None
        # For example: "Color"
        # TODO: Add URI link for instantiationColors

        self.instantiationTracks = None
        # For example: "Silent"
        # TODO: Add URI link for instantiationTracks

        self.instantiationChannelConfiguration = None
        # For example: "No Audio"
        # TODO: Add URI link for instantiationChannelConfiguration

        self.instantiationLanguage = None
        # For example: "" TODO: Give example instantiationLanguage
        # TODO: Add URI link for instantiationLanguage

        self.instantiationAlternativeModes = None
        # For example: "" TODO: Give example instantiationAlternativeModes

        self.instantiationEssenceTrack = []
        # TODO: Add URI link for instantiationEssenceTrack

        self.instantiationRelation = []
        # TODO: Add URI link for instantiationRelation

        self.instantiationAnnotation = []
        # TODO: Add URI link for instantiationAnnotation

        self.instantiationPart = None
        # For example: "" TODO: Give example instantiationPart
        # TODO: Add URI link for instantiationPart

        self.instantiationExtension = None
        # For example: "" TODO: Give example instantiationExtension
        # TODO: Add URI link for instantiationExtension

    def getInstantiationIdentifier(self):
        return self.instantiationIdentifier

    def setInstantiationIdentifier(self, newInstantiationIdentifier):
        # Must be an Element object!
        checkIfElement(newInstantiationIdentifier)
        self.instantiationIdentifier = newInstantiationIdentifier

    def getInstantiationDate(self):
        return self.instantiationDate

    def setInstantiationDate(self, newInstantiationDate):
        self.instantiationDate = newInstantiationDate

    def getInstantiationDimensions(self):
        return self.instantiationDimensions

    def setInstantiationDimensions(self, newInstantiationDimensions):
        # TODO: Add URI link for instantiationDimensions
        self.instantiationDimensions = newInstantiationDimensions

    def getInstantiationPhysical(self):
        return self.instantiationPhysical

    def setInstantiationPhysical(self, newInstantiationPhysical):
        self.instantiationPhysical = newInstantiationPhysical

    def getInstantiationDigital(self):
        return self.instantiationDigital

    def setInstantiationDigital(self, newInstantiationDigital):
        # Must be an Element object!
        checkIfElement(newInstantiationDigital)
        self.instantiationDigital = newInstantiationDigital

    def getInstantiationStandard(self):
        return self.instantiationStandard

    def setInstantiationStandard(self, newInstantiationStandard):
        self.instantiationStandard = newInstantiationStandard

    def getInstantiationLocation(self):
        return self.instantiationLocation

    def setInstantiationLocation(self, newInstantiationLocation):
        self.instantiationLocation = newInstantiationLocation

    def getInstantiationMediaType(self):
        return self.instantiationMediaType

    def setInstantiationMediaType(self, newInstantiationMediaType):
        self.instantiationMediaType = newInstantiationMediaType

    def getInstantiationGenerations(self):
        return self.instantiationGenerations

    def setInstantiationGenerations(self, newInstantiationGenerations):
        self.instantiationGenerations = newInstantiationGenerations

    def getInstantiationFileSize(self):
        return self.instantiationFileSize

    def setInstantiationFileSize(self, newInstantiationFileSize):
        # Must be an Element object!
        checkIfElement(newInstantiationFileSize)
        self.instantiationFileSize = newInstantiationFileSize

    def getInstantiationTimeStart(self):
        return self.instantiationTimeStart

    def setInstantiationTimeStart(self, newInstantiationTimeStart):
        # Must be an Element object!
        checkIfElement(newInstantiationTimeStart)
        self.instantiationTimeStart = newInstantiationTimeStart

    def getInstantiationDuration(self):
        return self.instantiationDuration

    def setInstantiationDuration(self, newInstantiationDuration):
        self.instantiationDuration = newInstantiationDuration

    def getInstantiationDataRate(self):
        return self.instantiationDataRate

    def setInstantiationDataRate(self, newInstantiationDataRate):
        self.instantiationDataRate = newInstantiationDataRate

    def getInstantiationColors(self):
        return self.instantiationColors

    def setInstantiationColors(self, newInstantiationColors):
        self.instantiationColors = newInstantiationColors

    def getInstantiationTracks(self):
        return self.instantiationTracks

    def setInstantiationTracks(self, newInstantiationTracks):
        self.instantiationTracks = newInstantiationTracks

    def getInstantiationChannelConfiguration(self):
        return self.instantiationChannelConfiguration

    def setInstantiationChannelConfiguration(self, newInstantiationChannelConfiguration):
        self.instantiationChannelConfiguration = newInstantiationChannelConfiguration

    def getInstantiationLanguage(self):
        return self.instantiationLanguage

    def setInstantiationLanguage(self, newInstantiationLanguage):
        self.instantiationLanguage = newInstantiationLanguage

    def getInstantiationAlternativeModes(self):
        return self.instantiationAlternativeModes

    def setInstantiationAlternativeModes(self, newInstantiationAlternativeModes):

        self.instantiationAlternativeModes = newInstantiationAlternativeModes

    def addinstantiationRelation(self, newinstantiationEssenceTrack):
        self.instantiationEssenceTrack.append(newinstantiationEssenceTrack)

    def getinstantiationEssenceTrack(self):
        return instantiationEssenceTrack

    def addinstantiationEssenceTrack(self, newinstantiationRelation):
        self.instantiationRelation.append(newinstantiationRelation)

    def getinstantiationRelation(self):
        return instantiationRelation

    def getInstantiationAnnotation(self):
        return self.instantiationAnnotation

    def addInstantiationAnnotation(self, newAnnotation):
        self.instantiationAnnotation.append(newAnnotation)

    def getInstantiationPart(self):
        return self.instantiationPart

    def setInstantiationPart(self, newInstantiationPart):
        self.instantiationPart = newInstantiationPart

    def getInstantiationExtension(self):
        return self.instantiationExtension

    def setInstantiationExtension(self, newnstantiationExtension):
        self.instantiationExtension = newnstantiationExtension


class instantiationEssenceTrack():
    def __init__(self):
        self.essenceTrackType = None
        # For example "Video"
        # TODO: Add URI link for essenceTrackType

        self.essenceTrackIdentifier = None
        # For example "" TODO: add example of essenceTrackIdentifier
        # TODO: Add URI link for essenceTrackIdentifier

        self.essenceTrackStandard = None
        # For example "" TODO: add example of essenceTrackStandard
        # TODO: Add URI link for essenceTrackStandard

        self.essenceTrackEncoding = None
        # For example "" TODO: add example of essenceTrackEncoding
        # TODO: Add URI link for essenceTrackEncoding

        self.essenceTrackDataRate = None
        # Use ONLY Element objects
        # TODO: Add URI link for essenceTrackDataRate

        self.essenceTrackFrameRate = None
        # Use ONLY Element objects
        # TODO: Add URI link for essenceTrackFrameRate

        self.essenceTrackPlaybackSpeed = None
        # Use ONLY Element objects
        # TODO: Add URI link for essenceTrackPlaybackSpeed


        self.essenceTrackSamplingRate = None
        # Use ONLY Element objects
        # TODO: Add URI link for essenceTrackSamplingRate

        self.essenceTrackBitDepth = None
        # For example "10"
        # TODO: Add URI link for essenceTrackBitDepth

        self.essenceTrackFrameSize = None
        # For example "" TODO: add example of essenceTrackFrameSize
        # TODO: Add URI link for essenceTrackFrameSize

        self.essenceTrackAspectRatio = None
        # For example "4:3"
        # TODO: Add URI link for essenceTrackAspectRatio

        self.essenceTrackTimeStart = None
        # For example "00:00:00"
        # TODO: Add URI link for essenceTrackTimeStart

        self.essenceTrackDuration = None
        # For example "00:10:52"
        # TODO: Add URI link for essenceTrackDuration

        self.essenceTrackLanguage = None
        # For example "" TODO: add example of essenceTrackLanguage
        # TODO: Add URI link for essenceTrackLanguage

        self.essenceTrackAnnotation = None
        # Use ONLY Element objects
        # TODO: Add URI link for essenceTrackAnnotation

        self.essenceTrackExtension = None
        # For example "" TODO: add example of essenceTrackExtension
        # TODO: Add URI link for essenceTrackExtension


    def getEssenceTrackType(self):
        return self.essenceTrackType

    def setEssenceTrackType(self, newEssenceTrackType):
        self.essenceTrackType = newEssenceTrackType

    def getEssenceTrackIdentifier(self):
        return self.essenceTrackIdentifier

    def setEssenceTrackIdentifier(self, newEssenceTrackIdentifier):
        self.essenceTrackIdentifier = newEssenceTrackIdentifier

    def getEssenceTrackStandard(self):
        return self.essenceTrackStandard

    def setEssenceTrackStandard(self, newEssenceTrackStandard):
        self.essenceTrackStandard = newEssenceTrackStandard

    def getEssenceTrackEncoding(self):
        return self.essenceTrackEncoding

    def setEssenceTrackEncoding(self, newEssenceTrackEncoding):
        self.essenceTrackEncoding = newEssenceTrackEncoding

    def getEssenceTrackDataRate(self):
        return self.essenceTrackDataRate

    def setEssenceTrackDataRate(self, newEssenceTrackDataRate):
        # Must be an Element object!
        checkIfElement(newEssenceTrackDataRate)
        self.essenceTrackDataRate = newEssenceTrackDataRate

    def getEssenceTrackFrameRate(self):
        return self.essenceTrackFrameRate

    def setEssenceTrackFrameRate(self, newEssenceTrackFrameRate):
        # Must be an Element object!
        checkIfElement(newEssenceTrackFrameRate)
        self.essenceTrackFrameRate = newEssenceTrackFrameRate

    def getEssenceTrackPlaybackSpeed(self):
        return self.essenceTrackPlaybackSpeed

    def setEssenceTrackPlaybackSpeed(self, newEssenceTrackPlaybackSpeed):
        # Must be an Element object!
        checkIfElement(newEssenceTrackPlaybackSpeed)
        self.essenceTrackPlaybackSpeed = newEssenceTrackPlaybackSpeed

    def getEssenceTrackSamplingRate(self):
        return self.essenceTrackSamplingRate

    def setEssenceTrackSamplingRate(self, newEssenceTrackSamplingRate):
        # Must be an Element object!
        checkIfElement(newEssenceTrackSamplingRate)
        self.essenceTrackSamplingRate = newEssenceTrackSamplingRate

    def getEssenceTrackBitDepth(self):
        return self.essenceTrackBitDepth

    def setEssenceTrackBitDepth(self, newEssenceTrackBitDepth):
        self.essenceTrackBitDepth = newEssenceTrackBitDepth

    def getEssenceTrackFrameSize(self):
        return self.essenceTrackFrameSize

    def setEssenceTrackFrameSize(self, newEssenceTrackFrameSize):
        self.essenceTrackFrameSize = newEssenceTrackFrameSize

    def getEssenceTrackAspectRatio(self):
        return self.essenceTrackAspectRatio

    def setEssenceTrackAspectRatio(self, newEssenceTrackAspectRatio):
        self.essenceTrackAspectRatio = newEssenceTrackAspectRatio

    def getEssenceTrackTimeStart(self):
        return self.essenceTrackTimeStart

    def setEssenceTrackTimeStart(self, newEssenceTrackTimeStart):
        self.essenceTrackTimeStart = newEssenceTrackTimeStart

    def getEssenceTrackDuration(self):
        return self.essenceTrackDuration

    def setEssenceTrackDuration(self, newEssenceTrackDuration):
        self.essenceTrackDuration = newEssenceTrackDuration

    def getEssenceTrackLanguage(self):
        return self.essenceTrackLanguage

    def setEssenceTrackLanguage(self, newEssenceTrackLanguage):
        self.essenceTrackLanguage = newEssenceTrackLanguage

    def getEssenceTrackAnnotation(self):
        return self.essenceTrackAnnotation

    def setEssenceTrackAnnotation(self, newEssenceTrackAnnotation):
        # Must be an Element object!
        checkIfElement(newEssenceTrackAnnotation)
        self.essenceTrackAnnotation = newEssenceTrackAnnotation

    def getEssenceTrackExtension(self):
        return self.essenceTrackExtension

    def setEssenceTrackExtension(self, newEssenceTrackExtension):
        self.essenceTrackExtension = newEssenceTrackExtension


class instantiationRelation():
    def __init__(self):
        self.instantiationRelationType = None
        # For example: "" TODO: Add example of instantiationRelationType
        # Use ONLY Element objects
        # TODO: Add URI link for instantiationRelationType

        self.instantiationRelationIdentifier = None
        # For example: "" TODO: Add example of instantiationRelationIdentifier
        # Use ONLY Element objects
        # TODO: Add URI link for instantiationRelationIdentifier


    def getInstantiationRelationType(self):
        return self.instantiationRelationType

    def setInstantiationRelationType(self, newInstantiationRelationType):
        # # Must be an Element object!
        checkIfElement(newInstantiationRelationType)
        self.instantiationRelationType = newInstantiationRelationType

    def getInstantiationRelationIdentifier(self):
        return self.instantiationRelationIdentifier

    def setInstantiationRelationIdentifier(self, newInstantiationRelationIdentifier):
        # Must be an Element object!
        checkIfElement(newInstantiationRelationIdentifier)
        self.instantiationRelationIdentifier = newInstantiationRelationIdentifier


##################################
# Extensions classes
##################################

class extensions():
    def __init__(self):
        self.pbcoreExtension = []
        # TODO: Add URI link for pbcoreExtension

        self.pbcorePart = None
        # For example: "" TODO: Add example of pbcorePart
        # TODO: Add URI link for pbcorePart dfsdf"""

    def addpbcoreExtension(self, newpbcoreExtension):
        self.pbcoreExtension.append(newpbcoreExtension)

    def getpbcoreExtension(self):
        return self.pbcoreExtension

    def setpbcorePart(self, newpbcorePart):
        self.pbcorePart = newpbcorePart

    def getpbcorePart(self):
        return self.pbcorePart


class pbcoreExtension():
    def __init__(self):
        self.extensionWrap = []
        # TODO: Add URI link for extensionWrap

        self.extensionElement = None
        # For example: "countryOfCreation"
        # TODO: Add URI link for extensionElement

        self.extensionValue = None
        # For example: "US"
        # TODO: Add URI link for extensionValue

        self.extensionAuthorityUsed = None
        # For example: "ISO 3166.1"
        # TODO: Add URI link for extensionAuthorityUsed

        self.extensionEmbedded = None
        # For example: "" TODO: Add example of extensionEmbedded
        # TODO: Add URI link for extensionEmbedded


    def addExtensionWrap(self, newExtensionWrap):
        self.extensionWrap.append(newExtensionWrap)

    def getExtensionWrap(self):
        return self.extensionWrap

    def setExtensionElement(self, newExtensionElement):
        self.extensionElement = newExtensionElement

    def getExtensionElement(self):
        return self.extensionElement

    def setExtensionValue(self, newExtensionValue):
        self.extensionValue = newExtensionValue

    def getExtensionValue(self):
        return self.extensionValue

    def setExtensionAuthorityUsed(self, newExtensionAuthorityUsed):
        self.extensionAuthorityUsed = newExtensionAuthorityUsed

    def getExtensionAuthorityUsed(self):
        return self.extensionAuthorityUsed

    def setExtensionEmbedded(self, newExtensionEmbedded):
        self.extensionEmbedded = newExtensionEmbedded

    def getExtensionEmbedded(self):
        return self.extensionEmbedded


##################################
# Other classes
##################################

class Element():
    def __init__(self, tag=None, value=None):
        self.tag = tag
        self.value = value
        self.attribute = dict()

    def getAttribute(self):
        return self.attribute

    def addAttribute(self, key, value):
        self.attribute[key] = value

    def deleteAttribute(self, key):
        del self.attribute[key]

    def getTag(self):
        return self.tag

    def setTag(self, tag):
        self.tag = tag

    def getValue(self):
        return self.getvalue()

    def setValue(self, value):
        self.value = value


##################################
# Utility functions
##################################
def checkIfElement(objectInQuestion):
    if not isinstance(objectInQuestion, Element):
        raise TypeError
