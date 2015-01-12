__author__ = 'California Audiovisual Preservation Project'


# Intellectual Content

class IntellectualContent():
    def __init__(self):

        self.pbcoreAssetType = None
        self.pbcoreAssetDate = None
        self.pbcoreIdentifier = None
        self.pbcoreTitle = None
        self.pbcoreSubject = None
        self.pbcoreDescription = None
        self.pbcoreGenre = None
        self.pbcoreRelation = []
        self.pbcoreCoverage = []
        self.pbcoreAudienceLevel = None
        self.pbcoreAudienceRating = None
        self.pbcoreAnnotation = None

    def getpbcoreAssetType(self):
        return self.pbcoreAssetType

    def setpbcoreAssetType(self, newpbcoreAssetType):
        self.pbcoreAssetType = newpbcoreAssetType

    def getpbcoreAssetDate(self):
        return self.pbcoreAssetDate

    def setpbcoreAssetDate(self, newpbcoreAssetDate):
        self.pbcoreAssetDate = newpbcoreAssetDate

    def getpbcoreIdentifier(self):
        return self.pbcoreIdentifier

    def setpbcoreIdentifier(self, newpbcoreIdentifier):
        self.pbcoreIdentifier = newpbcoreIdentifier

    def getpbcoreTitle(self):
        return self.pbcoreTitle

    def setpbcoreTitle(self, newpbcoreTitle):
        self.pbcoreTitle = newpbcoreTitle

    def getpbcoreSubject(self):
        return self.pbcoreSubject

    def setpbcoreSubject(self, newpbcoreSubject):
        self.pbcoreSubject = newpbcoreSubject

    def getpbcoreDescription(self):
        return self.pbcoreDescription

    def setpbcoreDescription(self, newpbcoreDescription):
        self.pbcoreDescription = newpbcoreDescription

    def getpbcoreGenre(self):
        return self.pbcoreGenre

    def setpbcoreGenre(self, newpbcoreGenre):
        self.pbcoreGenre = newpbcoreGenre

    def getpbcoreRelation(self):
        return self.pbcoreRelation

    def setpbcoreRelation(self, newpbcoreRelation):
        self.pbcoreRelation = newpbcoreRelation

    def getpbcoreCoverage(self):
        return self.pbcoreCoverage

    def setpbcoreCoverage(self, newpbcoreCoverage):
        self.pbcoreCoverage = newpbcoreCoverage

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
        self.instantiationAnnotation = None
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

    def getInstantiationAnnotation(self):
        return self.instantiationAnnotation

    def setInstantiationAnnotation(self, newInstantiationAnnotation):
        self.instantiationAnnotation = newInstantiationAnnotation

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