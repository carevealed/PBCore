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

        self.pbcoreAssetDate = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreassetdate/

        self.pbcoreIdentifier = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreidentifier/

        self.pbcoreTitle = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoretitle/

        self.pbcoreSubject = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreSubject/

        self.pbcoreDescription = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreDescription

        self.pbcoreGenre = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreGenre

        self.pbcoreRelation = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreRelation

        self.pbcoreCoverage = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreCoverage

        self.pbcoreAudienceLevel = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreAudienceLevel

        self.pbcoreAudienceRating = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreAudienceRating

        self.pbcoreAnnotation = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreAnnotation


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
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerelation/pbcorerelationtype/

        self.pbcoreRelationIdentifier = None
        # For example: "cscrm_000012_r3"
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerelation/pbcoreRelationIdentifier/

    def getpbcoreRelationType(self):
        return self.pbcoreRelationType

    def setpbcoreRelationType(self, newpbcoreRelationType):
        # TODO: Create Docstring for setpbcoreRelationType
        self.pbcoreRelationType = newpbcoreRelationType

    def getpbcoreRelationIdentifier(self):
        return self.pbcoreRelationIdentifier

    def setpbcoreRelationIdentifier(self, newpbcoreRelationIdentifier):
        # TODO: Create Docstring for setpbcoreRelationIdentifier
        self.pbcoreRelationIdentifier = newpbcoreRelationIdentifier


##################################
# intellectual Property classes
##################################


class IntellectualProperty():
    def __init__(self):
        self.pbcoreCreator = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecreator/

        self.pbcoreContributor = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreContributor

        self.pbcorePublisher = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorePublisher

        self.pbcoreRightsSummary = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreRightsSummary


    def getpbcoreCreator(self):
        return self.pbcoreCreator

    def addpbcoreCreator(self, newpbcoreCreator):
        # TODO: Create Docstring for addpbcoreCreator
        self.pbcoreCreator.append(newpbcoreCreator)

    def getpbcoreContributor(self):
        return self.pbcoreContributor

    def addpbcoreContributor(self, newpbcoreContributor):
        # TODO: Create Docstring for addpbcoreContributor
        self.pbcoreContributor.append(newpbcoreContributor)

    def getpbcorePublisher(self):
        # TODO: Create Docstring for getpbcorePublisher
        return self.pbcorePublisher

    def addpbcorePublisher(self, newpbcorePublisher):
        self.pbcorePublisher.append(newpbcorePublisher)

    def getpbcoreRightsSummary(self):
        # TODO: Create Docstring for getpbcoreRightsSummary
        return self.pbcoreRightsSummary

    def addpbcoreRightsSummary(self, newpbcoreRightsSummary):
        # TODO: Create Docstring for addpbcoreRightsSummary
        self.pbcoreRightsSummary.append(newpbcoreRightsSummary)


class pbcoreCreator():
    def __init__(self):
        self.creator = None
        # For example: "Unknown"
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecreator/creator/

        self.creatorRole = None
        # For example: "Producer"
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecreator/creatorRole/


    def getCreator(self):
        return self.creator

    def setCreator(self, newCreator):
        # TODO: Create Docstring for setCreator
        self.creator = newCreator

    def getCreatorRole(self):
        return self.creatorRole

    def setCreatorRole(self, newCreatorRole):
        # TODO: Create Docstring for setCreatorRole
        self.creatorRole = newCreatorRole


class pbcoreContributor:
    def __init__(self):
        self.contributor = None
        # For example: "" TODO: Give example of contributor
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecontributor/contributor/

        self.contributorRole = None
        # For example: "" TODO: Give example of contributorRole
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorecontributor/contributorrole/


    def setContributor(self,newContributor):
        # TODO: Create Docstring for setContributor
        self.contributor = newContributor

    def getContributor(self):
        return self.contributor

    def setContributoRoler(self,newContributoRole):
        # TODO: Create Docstring for setContributoRoler
        self.contributorRole = newContributoRole

    def getContributoRoler(self):
        return self.contributorRole


class pbcorePublisher():
    def __init__(self):
        self.publisher = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorepublisher/publisher/
        # For example: "" TODO: Give example of publisher

        self.publisherRole = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorepublisher/publisherRole/
        # For example: "" TODO: Give example of publisherRole


        def getPublisher(self):
            return self.publisher

        def setPublisher(self, newPublisher):
            # TODO: Create Docstring for setPublisher
            self.publisher = newPublisher

        def getPublisherRole(self):
            return self.publisherRole

        def setPublisherRole(self, newPublisherRole):
            # TODO: Create Docstring for setPublisherRole
            self.publisherRole = newPublisherRole


class pbcoreRightsSummary():
    def __init__(self):
        self.rightsSummary = []
        # TODO: Add URI link to rightsSummary
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/rightssummary/

        self.rightsLink = None
        # For example: "" TODO: Give example of rightsLink
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/rightsLink/

        self.rightsEmbedded = None
        # For example: "" TODO: Give example of rightsEmbedded
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcorerightssummary/rightsEmbedded/


    def getRightsSummary(self):
        return self.rightsSummary

    def addRightsSummary(self, newRightsSummary):
        #TODO: Create Docstring for addRightsSummary
        self.rightsSummary.append(newRightsSummary)

    def getRightsLink(self):
        return self.rightsLink

    def setRightsLink(self, newRightsLink):
        #TODO: Create Docstring for setRightsLink
        self.rightsLink = newRightsLink

    def getRightsEmbedded(self):
        return self.rightsEmbedded

    def setRightsEmbedded(self, newRightsEmbedded):
        #TODO: Create Docstring for setRightsEmbedded
        self.rightsEmbedded = newRightsEmbedded


##################################
# instantiation classes
##################################

class pbcoreInstantiation():
    def __init__(self, instantiationType=None):
        self.instantiationAssetType = instantiationType
        # For example: "Physical Asset" instantiationAssetType

        self.instantiationIdentifier = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationIdentifier/
        # Use ONLY Element objects

        self.instantiationDate = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDate/
        # For example: "UTC 2014-10-24 21:37:34"

        self.instantiationDimensions = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDimensions/
        # For example: "" TODO: Give example instantiationDimensions

        self.instantiationPhysical = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationPhysical/
        # For example: "Film: 16mm"

        self.instantiationDigital = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDigital/
        # Use ONLY Element objects

        self.instantiationStandard = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationStandard/
        # For example: "Blackmagic v210 YUV"

        self.instantiationLocation = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationLocation/
        # For example: "California State Railroad Museum Library"

        self.instantiationMediaType = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationMediaType/
        # For example: "Moving Image"

        self.instantiationGenerations = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationGenerations/
        # For example: "Unknown"

        self.instantiationFileSize = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationFileSize/
        # Use ONLY Element objects

        self.instantiationTimeStart = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationTimeStart/
        # For example: "00:00:00"

        self.instantiationDuration = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDuration/
        # For example: "00:10:52"

        self.instantiationDataRate = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationDataRate/
        # For example: "" TODO: Give example instantiationDataRate

        self.instantiationColors = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationColors/
        # For example: "Color"

        self.instantiationTracks = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationTracks/
        # For example: "Silent"

        self.instantiationChannelConfiguration = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationChannelConfiguration/
        # For example: "No Audio"

        self.instantiationLanguage = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationLanguage/
        # For example: "" TODO: Give example instantiationLanguage

        self.instantiationAlternativeModes = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationAlternativeModes/
        # For example: "" TODO: Give example instantiationAlternativeModes

        self.instantiationEssenceTrack = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationEssenceTrack/

        self.instantiationRelation = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationRelation/

        self.instantiationAnnotation = []
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationAnnotation/

        self.instantiationPart = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationPart/
        # For example: "" TODO: Give example instantiationPart

        self.instantiationExtension = None
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationExtension/
        # For example: "" TODO: Give example instantiationExtension

    def getInstantiationIdentifier(self):
        return self.instantiationIdentifier

    def setInstantiationIdentifier(self, newInstantiationIdentifier):
        # TODO: Create Docstring for setInstantiationIdentifier
        # Must be an Element object!
        checkIfElement(newInstantiationIdentifier)
        self.instantiationIdentifier = newInstantiationIdentifier

    def getInstantiationDate(self):
        return self.instantiationDate

    def setInstantiationDate(self, newInstantiationDate):
        # TODO: Create Docstring for setInstantiationDate
        self.instantiationDate = newInstantiationDate

    def getInstantiationDimensions(self):
        return self.instantiationDimensions

    def setInstantiationDimensions(self, newInstantiationDimensions):
        # TODO: Create Docstring for setInstantiationDimensions
        self.instantiationDimensions = newInstantiationDimensions

    def getInstantiationPhysical(self):
        return self.instantiationPhysical

    def setInstantiationPhysical(self, newInstantiationPhysical):
        # TODO: Create Docstring for setInstantiationPhysical
        self.instantiationPhysical = newInstantiationPhysical

    def getInstantiationDigital(self):
        return self.instantiationDigital

    def setInstantiationDigital(self, newInstantiationDigital):
        # TODO: Create Docstring for setInstantiationDigital
        # Must be an Element object!
        checkIfElement(newInstantiationDigital)
        self.instantiationDigital = newInstantiationDigital

    def getInstantiationStandard(self):
        return self.instantiationStandard

    def setInstantiationStandard(self, newInstantiationStandard):
        # TODO: Create Docstring for setInstantiationStandard

        self.instantiationStandard = newInstantiationStandard

    def getInstantiationLocation(self):
        return self.instantiationLocation

    def setInstantiationLocation(self, newInstantiationLocation):
        # TODO: Create Docstring for setInstantiationLocation

        self.instantiationLocation = newInstantiationLocation

    def getInstantiationMediaType(self):
        return self.instantiationMediaType

    def setInstantiationMediaType(self, newInstantiationMediaType):
        # TODO: Create Docstring for setInstantiationMediaType

        self.instantiationMediaType = newInstantiationMediaType

    def getInstantiationGenerations(self):
        return self.instantiationGenerations

    def setInstantiationGenerations(self, newInstantiationGenerations):
        # TODO: Create Docstring for setInstantiationGenerations

        self.instantiationGenerations = newInstantiationGenerations

    def getInstantiationFileSize(self):
        return self.instantiationFileSize

    def setInstantiationFileSize(self, newInstantiationFileSize):
        # TODO: Create Docstring for setInstantiationFileSize

        # Must be an Element object!
        checkIfElement(newInstantiationFileSize)
        self.instantiationFileSize = newInstantiationFileSize

    def getInstantiationTimeStart(self):
        return self.instantiationTimeStart

    def setInstantiationTimeStart(self, newInstantiationTimeStart):
        # TODO: Create Docstring for setInstantiationTimeStart

        # Must be an Element object!
        checkIfElement(newInstantiationTimeStart)
        self.instantiationTimeStart = newInstantiationTimeStart

    def getInstantiationDuration(self):
        return self.instantiationDuration

    def setInstantiationDuration(self, newInstantiationDuration):
        # TODO: Create Docstring for setInstantiationDuration

        self.instantiationDuration = newInstantiationDuration

    def getInstantiationDataRate(self):
        return self.instantiationDataRate

    def setInstantiationDataRate(self, newInstantiationDataRate):
        # TODO: Create Docstring for setInstantiationDataRate

        self.instantiationDataRate = newInstantiationDataRate

    def getInstantiationColors(self):
        return self.instantiationColors

    def setInstantiationColors(self, newInstantiationColors):
        # TODO: Create Docstring for setInstantiationColors

        self.instantiationColors = newInstantiationColors

    def getInstantiationTracks(self):
        return self.instantiationTracks

    def setInstantiationTracks(self, newInstantiationTracks):
        # TODO: Create Docstring for setInstantiationTracks

        self.instantiationTracks = newInstantiationTracks

    def getInstantiationChannelConfiguration(self):
        return self.instantiationChannelConfiguration

    def setInstantiationChannelConfiguration(self, newInstantiationChannelConfiguration):
        # TODO: Create Docstring for setInstantiationChannelConfiguration

        self.instantiationChannelConfiguration = newInstantiationChannelConfiguration

    def getInstantiationLanguage(self):
        return self.instantiationLanguage

    def setInstantiationLanguage(self, newInstantiationLanguage):
        # TODO: Create Docstring for setInstantiationLanguage

        self.instantiationLanguage = newInstantiationLanguage

    def getInstantiationAlternativeModes(self):
        return self.instantiationAlternativeModes

    def setInstantiationAlternativeModes(self, newInstantiationAlternativeModes):
        # TODO: Create Docstring for setInstantiationAlternativeModes


        self.instantiationAlternativeModes = newInstantiationAlternativeModes

    def addInstantiationRelation(self, newinstantiationRelation):
        # TODO: Create Docstring for addInstantiationRelation
        self.instantiationRelation.append(newinstantiationRelation)

    def getInstantiationEssenceTrack(self):
        return instantiationEssenceTrack

    def addInstantiationEssenceTrack(self, newInstantiationEssenceTrack):
        # TODO: Create Docstring for addInstantiationEssenceTrack
        self.instantiationEssenceTrack.append(newInstantiationEssenceTrack)

    def getInstantiationRelation(self):
        return instantiationRelation

    def getInstantiationAnnotation(self):
        return self.instantiationAnnotation

    def addInstantiationAnnotation(self, newAnnotation):
        # TODO: Create Docstring for addInstantiationAnnotation

        self.instantiationAnnotation.append(newAnnotation)

    def getInstantiationPart(self):
        return self.instantiationPart

    def setInstantiationPart(self, newInstantiationPart):
        # TODO: Create Docstring for setInstantiationPart

        self.instantiationPart = newInstantiationPart

    def getInstantiationExtension(self):
        return self.instantiationExtension

    def setInstantiationExtension(self, newnstantiationExtension):
        # TODO: Create Docstring for setInstantiationExtension

        self.instantiationExtension = newnstantiationExtension


class instantiationEssenceTrack():
    def __init__(self):
        self.essenceTrackType = None
        # For example "Video"
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essencetracktype/

        self.essenceTrackIdentifier = None
        # For example "" TODO: add example of essenceTrackIdentifier
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackIdentifier/

        self.essenceTrackStandard = None
        # For example "" TODO: add example of essenceTrackStandard
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackStandard/

        self.essenceTrackEncoding = None
        # For example "" TODO: add example of essenceTrackEncoding
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackEncoding/

        self.essenceTrackDataRate = None
        # Use ONLY Element objects
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackDataRate/

        self.essenceTrackFrameRate = None
        # Use ONLY Element objects
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackFrameRate/

        self.essenceTrackPlaybackSpeed = None
        # Use ONLY Element objects
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackPlaybackSpeed/


        self.essenceTrackSamplingRate = None
        # Use ONLY Element objects
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackSamplingRate/

        self.essenceTrackBitDepth = None
        # For example "10"
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackBitDepth/

        self.essenceTrackFrameSize = None
        # For example "" TODO: add example of essenceTrackFrameSize
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackFrameSize/

        self.essenceTrackAspectRatio = None
        # For example "4:3"
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackAspectRatio/

        self.essenceTrackTimeStart = None
        # For example "00:00:00"
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackTimeStart/

        self.essenceTrackDuration = None
        # For example "00:10:52"
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackDuration/

        self.essenceTrackLanguage = None
        # For example "" TODO: add example of essenceTrackLanguage
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackLanguage/

        self.essenceTrackAnnotation = None
        # Use ONLY Element objects
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackAnnotation/

        self.essenceTrackExtension = None
        # For example "" TODO: add example of essenceTrackExtension
        # URI # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationessencetrack/essenceTrackExtension/


    def getEssenceTrackType(self):
        return self.essenceTrackType

    def setEssenceTrackType(self, newEssenceTrackType):
        # TODO: Create Docstring for setEssenceTrackType
        self.essenceTrackType = newEssenceTrackType

    def getEssenceTrackIdentifier(self):
        # TODO: Create Docstring for getEssenceTrackIdentifier
        return self.essenceTrackIdentifier

    def setEssenceTrackIdentifier(self, newEssenceTrackIdentifier):
        # TODO: Create Docstring for setEssenceTrackIdentifier
        self.essenceTrackIdentifier = newEssenceTrackIdentifier

    def getEssenceTrackStandard(self):
        return self.essenceTrackStandard

    def setEssenceTrackStandard(self, newEssenceTrackStandard):
        # TODO: Create Docstring for setEssenceTrackStandard
        self.essenceTrackStandard = newEssenceTrackStandard

    def getEssenceTrackEncoding(self):
        return self.essenceTrackEncoding

    def setEssenceTrackEncoding(self, newEssenceTrackEncoding):
        # TODO: Create Docstring for setEssenceTrackEncoding
        self.essenceTrackEncoding = newEssenceTrackEncoding

    def getEssenceTrackDataRate(self):
        return self.essenceTrackDataRate

    def setEssenceTrackDataRate(self, newEssenceTrackDataRate):
        # TODO: Create Docstring for setEssenceTrackDataRate
        # Must be an Element object!
        checkIfElement(newEssenceTrackDataRate)
        self.essenceTrackDataRate = newEssenceTrackDataRate

    def getEssenceTrackFrameRate(self):
        return self.essenceTrackFrameRate

    def setEssenceTrackFrameRate(self, newEssenceTrackFrameRate):
        # TODO: Create Docstring for setEssenceTrackFrameRate
        # Must be an Element object!
        checkIfElement(newEssenceTrackFrameRate)
        self.essenceTrackFrameRate = newEssenceTrackFrameRate

    def getEssenceTrackPlaybackSpeed(self):
        return self.essenceTrackPlaybackSpeed

    def setEssenceTrackPlaybackSpeed(self, newEssenceTrackPlaybackSpeed):
        # TODO: Create Docstring for setEssenceTrackPlaybackSpeed
        # Must be an Element object!
        checkIfElement(newEssenceTrackPlaybackSpeed)
        self.essenceTrackPlaybackSpeed = newEssenceTrackPlaybackSpeed

    def getEssenceTrackSamplingRate(self):
        return self.essenceTrackSamplingRate

    def setEssenceTrackSamplingRate(self, newEssenceTrackSamplingRate):
        # TODO: Create Docstring for setEssenceTrackSamplingRate
        # Must be an Element object!
        checkIfElement(newEssenceTrackSamplingRate)
        self.essenceTrackSamplingRate = newEssenceTrackSamplingRate

    def getEssenceTrackBitDepth(self):
        return self.essenceTrackBitDepth

    def setEssenceTrackBitDepth(self, newEssenceTrackBitDepth):
        # TODO: Create Docstring for setEssenceTrackBitDepth
        self.essenceTrackBitDepth = newEssenceTrackBitDepth

    def getEssenceTrackFrameSize(self):
        return self.essenceTrackFrameSize

    def setEssenceTrackFrameSize(self, newEssenceTrackFrameSize):
        # TODO: Create Docstring for setEssenceTrackFrameSize
        self.essenceTrackFrameSize = newEssenceTrackFrameSize

    def getEssenceTrackAspectRatio(self):
        return self.essenceTrackAspectRatio

    def setEssenceTrackAspectRatio(self, newEssenceTrackAspectRatio):
        self.essenceTrackAspectRatio = newEssenceTrackAspectRatio

    def getEssenceTrackTimeStart(self):
        return self.essenceTrackTimeStart

    def setEssenceTrackTimeStart(self, newEssenceTrackTimeStart):
        # TODO: Create Docstring for setEssenceTrackTimeStart
        self.essenceTrackTimeStart = newEssenceTrackTimeStart

    def getEssenceTrackDuration(self):
        return self.essenceTrackDuration

    def setEssenceTrackDuration(self, newEssenceTrackDuration):
        # TODO: Create Docstring for setEssenceTrackDuration
        self.essenceTrackDuration = newEssenceTrackDuration

    def getEssenceTrackLanguage(self):
        return self.essenceTrackLanguage

    def setEssenceTrackLanguage(self, newEssenceTrackLanguage):
        # TODO: Create Docstring for setEssenceTrackLanguage
        self.essenceTrackLanguage = newEssenceTrackLanguage

    def getEssenceTrackAnnotation(self):
        return self.essenceTrackAnnotation

    def setEssenceTrackAnnotation(self, newEssenceTrackAnnotation):
        # TODO: Create Docstring for setEssenceTrackAnnotation
        # Must be an Element object!
        checkIfElement(newEssenceTrackAnnotation)
        self.essenceTrackAnnotation = newEssenceTrackAnnotation

    def getEssenceTrackExtension(self):
        return self.essenceTrackExtension

    def setEssenceTrackExtension(self, newEssenceTrackExtension):
        # TODO: Create Docstring for setEssenceTrackExtension
        self.essenceTrackExtension = newEssenceTrackExtension


class instantiationRelation():
    def __init__(self):
        self.instantiationRelationType = None
        # For example: "" TODO: Add example of instantiationRelationType
        # Use ONLY Element objects
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationrelation/instantiationrelationtype/

        self.instantiationRelationIdentifier = None
        # For example: "" TODO: Add example of instantiationRelationIdentifier
        # Use ONLY Element objects
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreinstantiation/instantiationRelationIdentifier/


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
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/

        self.pbcorePart = None
        # For example: "" TODO: Add example of pbcorePart
        # URI: http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/

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
        # URIL http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionWrap/

        self.extensionElement = None
        # For example: "countryOfCreation"
        # URIL http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionElement/

        self.extensionValue = None
        # For example: "US"
        # URIL http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionValue/

        self.extensionAuthorityUsed = None
        # For example: "ISO 3166.1"
        # URIL http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionAuthorityUsed/

        self.extensionEmbedded = None
        # For example: "" TODO: Add example of extensionEmbedded
        # URIL http://pbcore.org/v2/elements/pbcoredescriptiondocument/pbcoreextension/extensionEmbedded/


    def addExtensionWrap(self, newExtensionWrap):
        # TODO: Create Docstring for addExtensionWrap
        self.extensionWrap.append(newExtensionWrap)

    def getExtensionWrap(self):
        return self.extensionWrap

    def setExtensionElement(self, newExtensionElement):
        # TODO: Create Docstring for setExtensionElement
        self.extensionElement = newExtensionElement

    def getExtensionElement(self):
        return self.extensionElement

    def setExtensionValue(self, newExtensionValue):
        # TODO: Create Docstring for setExtensionValue
        self.extensionValue = newExtensionValue

    def getExtensionValue(self):
        return self.extensionValue

    def setExtensionAuthorityUsed(self, newExtensionAuthorityUsed):
        # TODO: Create Docstring for setExtensionAuthorityUsed
        self.extensionAuthorityUsed = newExtensionAuthorityUsed

    def getExtensionAuthorityUsed(self):
        return self.extensionAuthorityUsed

    def setExtensionEmbedded(self, newExtensionEmbedded):
        # TODO: Create Docstring for setExtensionEmbedded
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
        # TODO: Create Docstring for addAttribute
        self.attribute[key] = value

    def deleteAttribute(self, key):
        # TODO: Create Docstring for deleteAttribute
        del self.attribute[key]

    def getTag(self):
        return self.tag

    def setTag(self, tag):
        # TODO: Create Docstring for setTag
        self.tag = tag

    def getValue(self):
        return self.getvalue()

    def setValue(self, value):
        # TODO: Create Docstring for setValue
        self.value = value


##################################
# Utility functions
##################################
def checkIfElement(objectInQuestion):
    if not isinstance(objectInQuestion, Element):
        raise TypeError