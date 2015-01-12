__author__ = 'California Audiovisual Preservation Project'
# PBCore metadata

# Intellectual Content

class IntellectualContent():
    def __init__(self):

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

    def getpbcoreAssetType(self):
        return self.pbcoreAssetType

    def addpbcoreAssetType(self, key, value):
        self.pbcoreAssetType[key] = value

    def getpbcoreAssetDate(self):
        return self.pbcoreAssetDate

    def setpbcoreAssetDate(self, newpbcoreAssetDate):
        self.pbcoreAssetDate = newpbcoreAssetDate

    def getpbcoreIdentifier(self):
        return self.pbcoreIdentifier

    def addpbcoreIdentifier(self, newIdentifier):
        self.pbcoreIdentifier.append(newIdentifier)

    def getpbcoreTitle(self):
        return self.pbcoreTitle

    def addpbcoreTitle(self, newTitle):
        self.pbcoreTitle.append(newTitle)

    def getpbcoreSubject(self):
        return self.pbcoreSubject

    def setpbcoreSubject(self, newpbcoreSubject):
        self.pbcoreSubject = newpbcoreSubject

    def getpbcoreDescription(self):
        return self.pbcoreDescription

    def addpbcoreDescription(self, newDescription):
        self.pbcoreDescription.append(newDescription)

    def getpbcoreGenre(self):
        return self.pbcoreGenre

    def setpbcoreGenre(self, newpbcoreGenre):
        self.pbcoreGenre = newpbcoreGenre

    def getpbcoreRelation(self):
        return self.pbcoreRelation

    def addpbcoreRelation(self, newpbcoreRelation):
        self.pbcoreRelation.append(newpbcoreRelation)

    def getpbcoreCoverage(self):
        return self.pbcoreCoverage

    def addpbcoreCoverage(self, newpbcoreCoverage):
        self.pbcoreCoverage.append(newpbcoreCoverage)

    def getpbcoreAudienceLevel(self):
        return self.pbcoreAudienceLevel

    def setpbcoreAudienceLevel(self, newpbcoreAudienceLevel):
        self.pbcoreAudienceLevel = newpbcoreAudienceLevel

    def getpbcoreAudienceRating(self):
        return self.pbcoreAudienceRating

    def setpbcoreAudienceRating(self, newpbcoreAudienceRating):
        self.pbcoreAudienceRating = newpbcoreAudienceRating

    def getpbcoreAnnotation(self):
        return self.pbcoreAnnotation

    def setpbcoreAnnotation(self, newpbcoreAnnotation):
        self.pbcoreAnnotation = newpbcoreAnnotation

class pbcoreRelation():
    def __init__(self):
        self.pbcoreRelationType = None
        self.pbcoreRelationIdentifier = None

    def getpbcoreRelationType(self):
        return self.pbcoreRelationType

    def setpbcoreRelationType(self, newpbcoreRelationType):
        self.pbcoreRelationType = newpbcoreRelationType

    def getpbcoreRelationIdentifier(self):
        return self.pbcoreRelationIdentifier

    def setpbcoreRelationIdentifier(self, newpbcoreRelationIdentifier):
        self.pbcoreRelationIdentifier = newpbcoreRelationIdentifier


# intellectual Property classes
class IntellectualProperty():
    def __init__(self):
        self.pbcoreCreator = []
        self.pbcoreContributor = []
        self.pbcorePublisher = []
        self.pbcoreRightsSummary = []

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
        self.creatorRole = None

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
        self.contributorRole = None

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
        self.publisherRole = None

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
        self.rightsSummary = None
        self.rightsLink = None
        self.rightsEmbedded = None

    def getRightsSummary(self):
        return self.rightsSummary

    def setRightsSummary(self, newRightsSummary):
        self.rightsSummary = newRightsSummary

    def getRightsLink(self):
        return self.rightsLink

    def setRightsLink(self, newRightsLink):
        self.rightsLink = newRightsLink

    def getRightsEmbedded(self):
        return self.rightsEmbedded

    def setRightsEmbedded(self, newRightsEmbedded):
        self.rightsEmbedded = newRightsEmbedded


# instantiation classes


class pbcoreInstantiation():
    def __init__(self):
        self.instantiationIdentifier = None
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


    def getInstantiationIdentifier(self):
        return self.instantiationIdentifier

    def setInstantiationIdentifier(self, newInstantiationIdentifier):
        self.instantiationIdentifier = newInstantiationIdentifier

    def getInstantiationDate(self):
        return self.instantiationDate

    def setInstantiationDate(self, newInstantiationDate):
        self.instantiationDate = newInstantiationDate

    def getInstantiationDimensions(self):
        return self.instantiationDimensions

    def setInstantiationDimensions(self, newInstantiationDimensions):
        self.instantiationDimensions = newInstantiationDimensions

    def getInstantiationPhysical(self):
        return self.instantiationPhysical

    def setInstantiationPhysical(self, newInstantiationPhysical):
        self.instantiationPhysical = newInstantiationPhysical

    def getInstantiationDigital(self):
        return self.instantiationDigital

    def setInstantiationDigital(self, newInstantiationDigital):
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
        self.instantiationFileSize = newInstantiationFileSize

    def getInstantiationTimeStart(self):
        return self.instantiationTimeStart

    def setInstantiationTimeStart(self, newInstantiationTimeStart):
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
        self.essenceTrackDataRate = newEssenceTrackDataRate

    def getEssenceTrackFrameRate(self):
        return self.essenceTrackFrameRate

    def setEssenceTrackFrameRate(self, newEssenceTrackFrameRate):
        self.essenceTrackFrameRate = newEssenceTrackFrameRate

    def getEssenceTrackPlaybackSpeed(self):
        return self.essenceTrackPlaybackSpeed

    def setEssenceTrackPlaybackSpeed(self, newEssenceTrackPlaybackSpeed):
        self.essenceTrackPlaybackSpeed = newEssenceTrackPlaybackSpeed

    def getEssenceTrackSamplingRate(self):
        return self.essenceTrackSamplingRate

    def setEssenceTrackSamplingRate(self, newEssenceTrackSamplingRate):
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
        self.essenceTrackAnnotation = newEssenceTrackAnnotation

    def getEssenceTrackExtension(self):
        return self.essenceTrackExtension

    def setEssenceTrackExtension(self, newEssenceTrackExtension):
        self.essenceTrackExtension = newEssenceTrackExtension


class instantiationRelation():
    def __init__(self):
        self.instantiationRelationType = None
        self.instantiationRelationIdentifier = None

    def getInstantiationRelationType(self):
        return self.instantiationRelationType

    def setInstantiationRelationType(self, newInstantiationRelationType):
        self.instantiationRelationType = newInstantiationRelationType

    def getInstantiationRelationIdentifier(self):
        return self.instantiationRelationIdentifier

    def setInstantiationRelationIdentifier(self, newInstantiationRelationIdentifier):
        self.instantiationRelationIdentifier = newInstantiationRelationIdentifier


# Extensions classes
class extensions():
    def __init__(self):
        self.pbcoreExtension = []
        self.pbcorePart = None

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
        self.extensionWrap = None
        self.extensionElement = None
        self.extensionValue = None
        self.extensionAuthorityUsed = None
        self.extensionEmbedded = None

    def setExtensionWrap(self, newExtensionWrap):
        self.extensionWrap = newExtensionWrap

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


# Other classes
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