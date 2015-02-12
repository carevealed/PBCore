import sys
from time import sleep

__author__ = 'lpsdesk'
import csv

officialList = ['Internet Archive URL',
                'Object Identifier',
                'Call Number',
                'Project Identifier',
                'Project Note',
                'Institution',
                'Asset Type',
                'Media Type',
                'Generation',
                'Main or Supplied Title',
                'Additional Title',
                'Series Title',
                'Description or Content Summary',
                'Why the recording is significant to California/local history',
                'Producer',
                'Director',
                'Writer',
                'Interviewer',
                'Performer',
                'Country of Creation',
                'Date Created',
                'Date Published',
                'Copyright Statement',
                'Gauge and Format',
                'Total Number of Reels or Tapes',
                'Duration',
                'Silent or Sound',
                'Color and/or Black and White',
                'Camera',
                'Editor',
                'Sound',
                'Music',
                'Cast',
                'Interviewee',
                'Speaker',
                'Musician',
                'Publisher',
                'Distributor',
                'Language',
                'Subject Topic',
                'Subject Topic Authority Source',
                'Subject Entity',
                'Subject Entity Authority Source',
                'Genre',
                'Genre Authority Source',
                'Spatial Coverage',
                'Temporal Coverage',
                'Collection Guide Title',
                'Collection Guide URL',
                'Relationship',
                'Relationship Type',
                'Aspect Ratio',
                'Running Speed',
                'Timecode Content Begins',
                'Track Standard',
                'Channel Configuration',
                'Subtitles/Intertitles/Closed Captions',
                'Stock Manufacturer',
                'Base Type',
                'Base Thickness',
                'Copyright Holder',
                'Copyright Holder Info',
                'Copyright Date',
                'Copyright Notice',
                'Institutional Rights Statement (URL)',
                'Object ARK',
                'Institution ARK',
                'Institution URL',
                'Quality Control Notes',
                'Additional Descriptive Notes for Overall Work',
                'Additional Technical Notes for Overall Work',
                'Transcript',
                'Cataloger Notes',
                'OCLC number',
                'Date created',
                'Date modified',
                'Reference URL',
                'CONTENTdm number',
                'CONTENTdm file name',
                'CONTENTdm file path']


def generate_pbcore(record):
    # TODO create XML generatation code here
    print "<FromCSV>"

    if record['Object Identifier']:
        # TODO add Object Identifier to pbcoreDescriptionDocument.pbcoreIdentifier and pbcoreInstantiation.instantiationIdentifier
        # pbcoreDescriptionDocument.pbcoreIdentifier is part of pbcoreDescriptionDocument class
        # pbcoreInstantiation.instantiationIdentifier is part of CAVPP_Part class
        objectIDs = record['Object Identifier'].split(';')
        for objectID in objectIDs:
            print '\t<ObjectIdentifier>' + objectID.lstrip() + '</ObjectIdentifier> '

    if record['Internet Archive URL']:
        # TODO add Internet Archive URL to PBCore object
        # TODO: Find out where Internet Archive URL maps to in PBCore
        print '\t<InternetArchiveURL>' + record['Internet Archive URL'] + '</InternetArchiveURL> '

    if record['Call Number']:
        # TODO add Call Number to pbcoreDescriptionDocument.pbcoreIdentifier and pbcoreInstantiation.instantiationIdentifier
        # pbcoreDescriptionDocument.pbcoreIdentifier is part of pbcoreDescriptionDocument class
        # pbcoreInstantiation.instantiationIdentifier is part of CAVPP_Part class

        print '\t<CallNumber>' + record['Call Number'] + '</CallNumber>'

    if record['Project Identifier']:
        # TODO add Project Identifier to pbcoreDescriptionDocument.pbcoreIdentifier
        # pbcoreInstantiation.instantiationIdentifier is part of CAVPP_Part class

        print '\t<ProjectIdentifier>' + record['Project Identifier'] + '</ProjectIdentifier>'

    if record['Project Note']:
        # TODO add Project Note to PBCore object
        # TODO: Find out where Project Note maps to in PBCore
        print '\t<ProjectNote>' + record['Project Note'] + '</ProjectNote>'

    if record['Institution']:
        # TODO add Institution to PBCore object
        # TODO: Find out where Institution maps to in PBCore
        print '\t<Institution>' + record['Institution'] + '</Institution>'

    if record['Asset Type']:
        # TODO add Asset Type to pbcoreDescriptionDocument.pbcoreAssetType
        # pbcoreDescriptionDocument.pbcoreAssetType is in pbcoreDescriptionDocument()
        # pbcoreInstantiation.pbcoreAssetType is in pbcoreDescriptionDocument()
        print '\t<AssetType>' + record['Asset Type'] + '</AssetType>'

    if record['Media Type']:
        # TODO add Media Type to pbcoreInstantiation.instantiationMediaType
        # pbcoreInstantiation.instantiationMediaType is in pbcoreInstantiation()
        print '\t<MediaType>' + record['Media Type'] + '</MediaType>'

    if record['Generation']:
        # TODO add Generation to pbcoreInstantiation.instantiationGenerations
        # pbcoreInstantiation.instantiationGenerations is in pbcoreInstantiation()
        print '\t<Generation>' + record['Generation'] + '</Generation>'

    if record['Main or Supplied Title']:
        # TODO add Main or Supplied Title to pbcoreDescriptionDocument.pbcoreTitle titleType="Main" and pbcorePart.pbcoreTitle titleType="Main"
        # pbcorePart.pbcoreTitle is in pbcoreDescriptionDocument()

        print '\t<MainOrSuppliedTitle>' + record['Main or Supplied Title'] + '</MainOrSuppliedTitle>'

    if record['Additional Title']:
        # TODO add Additional Title to PBCore object
        print '\t<AdditionalTitle>' + record['Additional Title'] + '</AdditionalTitle>'

    if record['Series Title']:
        # TODO add Series Title to PBCore object
        print '\t<SeriesTitle>' + record['Series Title'] + '</SeriesTitle>'

    if record['Description or Content Summary']:
        # TODO add Description or Content Summary to PBCore object
        print '\t<DescriptionOrContentSummary>' + record['Description or Content Summary'] + '</DescriptionOrContentSummary>'

    if record['Why the recording is significant to California/local history']:
        # TODO add Why the recording is significant to California/local history to PBCore object
        print '\t<WhyTheRecordingIsSignificantToCaliforniaLocalHistory>' + record['Why the recording is significant to California/local history'] + '</WhyTheRecordingIsSignificantToCaliforniaLocalHistory>'

    if record['Producer']:
        # TODO add Producer to PBCore object
        print '\t<Producer>' + record['Producer'] + '</Producer>'

    if record['Director']:
        # TODO add Director to PBCore object
        print '\t<Director>' + record['Director'] + '</Director>'

    if record['Writer']:
        # TODO add Writer to PBCore object
        print '\t<Writer>' + record['Writer'] + '</Writer>'

    if record['Interviewer']:
        # TODO add Interviewer to PBCore object
        print '\t<Interviewer>' + record['Interviewer'] + '</Interviewer>'

    if record['Performer']:
        # TODO add Performer to PBCore object
        print '\t<Performer>' + record['Performer'] + '</Performer>'

    if record['Country of Creation']:
        # TODO add Country of Creation to PBCore object
        print '\t<CountryOfCreation>' + record['Country of Creation'] + '</CountryOfCreation>'

    if record['Date Created']:
        # TODO add Date Created to PBCore object
        creationDates = record['Date Created'].split(';')
        for creationDate in creationDates:
            print '\t<DateCreated>' + creationDate.lstrip() + '</DateCreated>'

    if record['Date Published']:
        # TODO add Date Published to PBCore object
        print '\t<DatePublished>' + record['Date Published'] + '</DatePublished>'

    if record['Copyright Statement']:
        # TODO add Copyright Statement to PBCore object
        print '\t<CopyrightStatement>' + record['Copyright Statement'] + '</CopyrightStatement>'

    if record['Gauge and Format']:
        # TODO add Gauge and Format to PBCore object
        print '\t<GaugeAndFormat>' + record['Gauge and Format'] + '</GaugeAndFormat>'

    if record['Total Number of Reels or Tapes']:
        # TODO add Total Number of Reels or Tapes to PBCore object
        print '\t<TotalNumberOfReelsOrTapes>' + record['Total Number of Reels or Tapes'] + '</TotalNumberOfReelsOrTapes>'

    if record['Duration']:
        # TODO add Duration to PBCore object
        print '\t<Duration>' + record['Duration'] + '</Duration>'

    if record['Silent or Sound']:
        # TODO add Silent or Sound to PBCore object
        print '\t<SilentOrSound>' + record['Silent or Sound'] + '</SilentOrSound>'

    if record['Color and/or Black and White']:
        # TODO add Color and/or Black and White to PBCore object
        print '\t<ColorAndOrBlackAndWhite>' + record['Color and/or Black and White'] + '</ColorAndOrBlackAndWhite>'

    if record['Camera']:
        # TODO add Camera to PBCore object
        print '\t<Camera>' + record['Camera'] + '</Camera>'

    if record['Editor']:
        # TODO add Editor to PBCore object
        print '\t<Editor>' + record['Editor'] + '</Editor>'

    if record['Sound']:
        # TODO add Sound to PBCore object
        print '\t<Sound>' + record['Sound'] + '</Sound>'

    if record['Music']:
        # TODO add Music to PBCore object
        print '\t<Music>' + record['Music'] + '</Music>'

    if record['Cast']:
        # TODO add Cast to PBCore object
        print '\t<Cast>' + record['Cast'] + '</Cast>'

    if record['Interviewee']:
        # TODO add Interviewee to PBCore object
        print '\t<Interviewee>' + record['Interviewee'] + '</Interviewee>'

    if record['Speaker']:
        # TODO add Speaker to PBCore object
        print '\t<Speaker>' + record['Speaker'] + '</Speaker>'

    if record['Musician']:
        # TODO add Musician to PBCore object
        print '\t<Musician>' + record['Musician'] + '</Musician>'

    if record['Publisher']:
        # TODO add Publisher to PBCore object
        print '\t<Publisher>' + record['Publisher'] + '</Publisher>'

    if record['Distributor']:
        # TODO add Distributor to PBCore object
        print '\t<Distributor>' + record['Distributor'] + '</Distributor>'

    if record['Language']:
        # TODO add Language to PBCore object
        print '\t<Language>' + record['Language'] + '</Language>'

    if record['Subject Topic']:
        # TODO add Subject Topic to PBCore object
        subjectTopics = record['Subject Topic'].split(';')
        for subjectTopic in subjectTopics:
            print '\t<SubjectTopic>' + subjectTopic.lstrip() + '</SubjectTopic>'

    if record['Subject Topic Authority Source']:
        # TODO add Subject Topic Authority Source to PBCore object
        print '\t<SubjectTopicAuthoritySource>' + record['Subject Topic Authority Source'] + '</SubjectTopicAuthoritySource>'

    if record['Subject Entity']:
        # TODO add Subject Entity to PBCore object
        print '\t<SubjectEntity>' + record['Subject Entity'] + '</SubjectEntity>'

    if record['Subject Entity Authority Source']:
        # TODO add Subject Entity Authority Source to PBCore object
        print '\t<SubjectEntityAuthoritySource>' + record['Subject Entity Authority Source'] + '</SubjectEntityAuthoritySource>'

    if record['Genre']:
        # TODO add Genre to PBCore object
        print '\t<Genre>' + record['Genre'] + '</Genre>'

    if record['Genre Authority Source']:
        # TODO add Genre Authority Source to PBCore object
        print '\t<GenreAuthoritySource>' + record['Genre Authority Source'] + '</GenreAuthoritySource>'

    if record['Spatial Coverage']:
        # TODO add Spatial Coverage to PBCore object
        print '\t<SpatialCoverage>' + record['Spatial Coverage'] + '</SpatialCoverage>'

    if record['Temporal Coverage']:
        # TODO add Temporal Coverage to PBCore object
        print '\t<TemporalCoverage>' + record['Temporal Coverage'] + '</TemporalCoverage>'

    if record['Collection Guide Title']:
        # TODO add Collection Guide Title to PBCore object
        print '\t<CollectionGuideTitle>' + record['Collection Guide Title'] + '</CollectionGuideTitle>'

    if record['Collection Guide URL']:
        # TODO add Collection Guide URL to PBCore object
        print '\t<CollectionGuideURL>' + record['Collection Guide URL'] + '</CollectionGuideURL>'

    if record['Relationship']:
        # TODO add Relationship to PBCore object
        print '\t<Relationship>' + record['Relationship'] + '</Relationship>'

    if record['Relationship Type']:
        # TODO add Relationship Type to PBCore object
        print '\t<RelationshipType>' + record['Relationship Type'] + '</RelationshipType>'

    if record['Aspect Ratio']:
        # TODO add Aspect Ratio to PBCore object
        print '\t<AspectRatio>' + record['Aspect Ratio'] + '</AspectRatio>'

    if record['Running Speed']:
        # TODO add Running Speed to PBCore object
        print '\t<RunningSpeed>' + record['Running Speed'] + '</RunningSpeed>'

    if record['Timecode Content Begins']:
        # TODO add Timecode Content Begins to PBCore object
        print '\t<TimecodeContentBegins>' + record['Timecode Content Begins'] + '</TimecodeContentBegins>'

    if record['Track Standard']:
        # TODO add Track Standard to PBCore object
        print '\t<TrackStandard>' + record['Track Standard'] + '</TrackStandard>'

    if record['Channel Configuration']:
        # TODO add Channel Configuration to PBCore object
        print '\t<ChannelConfiguration>' + record['Channel Configuration'] + '</ChannelConfiguration>'

    if record['Subtitles/Intertitles/Closed Captions']:
        # TODO add Subtitles/Intertitles/Closed Captions to PBCore object
        print '\t<SubtitlesIntertitlesClosedCaptions>' + record['Subtitles/Intertitles/Closed Captions'] + '</SubtitlesIntertitlesClosedCaptions>'

    if record['Stock Manufacturer']:
        # TODO add Stock Manufacturer to PBCore object
        print '\t<StockManufacturer>' + record['Stock Manufacturer'] + '</StockManufacturer>'

    if record['Base Type']:
        # TODO add Base Type to PBCore object
        print '\t<BaseType>' + record['Base Type'] + '</BaseType>'

    if record['Base Thickness']:
        # TODO add Base Thickness to PBCore object
        print '\t<BaseThickness>' + record['Base Thickness'] + '</BaseThickness>'

    if record['Copyright Holder']:
        # TODO add Copyright Holder to PBCore object
        print '\t<CopyrightHolder>' + record['Copyright Holder'] + '</CopyrightHolder>'

    if record['Copyright Holder Info']:
        # TODO add Copyright Holder Info to PBCore object
        print '\t<CopyrightHolderInfo>' + record['Copyright Holder Info'] + '</CopyrightHolderInfo>'

    if record['Copyright Date']:
        # TODO add Copyright Date to PBCore object
        copyrightdates = record['Copyright Date'].split(';')
        for copyrightdate in copyrightdates:
            print '\t<CopyrightDate>' + copyrightdate.lstrip() + '</CopyrightDate>'

    if record['Copyright Notice']:
        # TODO add Copyright Notice to PBCore object
        print '\t<CopyrightNotice>' + record['Copyright Notice'] + '</CopyrightNotice>'

    if record['Institutional Rights Statement (URL)']:
        # TODO add Institutional Rights Statement (URL) to PBCore object
        print '\t<InstitutionalRightsStatementURL>' + record['Institutional Rights Statement (URL)'] + '</InstitutionalRightsStatementURL>'

    if record['Object ARK']:
        # TODO add Object ARK to PBCore object
        print '\t<ObjectARK>' + record['Object ARK'] + '</ObjectARK>'

    if record['Institution ARK']:
        # TODO add Institution ARK to PBCore object
        print '\t<InstitutionARK>' + record['Institution ARK'] + '</InstitutionARK>'

    if record['Institution URL']:
        # TODO add Institution URL to PBCore object
        print '\t<InstitutionURL>' + record['Institution URL'] + '</InstitutionURL>'

    if record['Quality Control Notes']:
        # TODO add Quality Control Notes to PBCore object
        QCNotes = record['Quality Control Notes'].split(';')
        for QCNote in QCNotes:
            print '\t<QualityControlNotes>' + QCNote.lstrip() + '</QualityControlNotes>'

    if record['Additional Descriptive Notes for Overall Work']:
        # TODO add Additional Descriptive Notes for Overall Work to PBCore object
        print '\t<AdditionalDescriptiveNotesForOverallWork>' + record['Additional Descriptive Notes for Overall Work'] + '</AdditionalDescriptiveNotesForOverallWork>'

    if record['Additional Technical Notes for Overall Work']:
        # TODO add Additional Technical Notes for Overall Work to PBCore object
        print '\t<AdditionalTechnicalNotesForOverallWork>' + record['Additional Technical Notes for Overall Work'] + '</AdditionalTechnicalNotesForOverallWork>'

    if record['Transcript']:
        # TODO add Transcript to PBCore object
        print '\t<Transcript>' + record['Transcript'] + '</Transcript>'

    if record['Cataloger Notes']:
        # TODO add Cataloger Notes to PBCore object
        print '\t<CatalogerNotes>' + record['Cataloger Notes'] + '</CatalogerNotes>'

    if record['OCLC number']:
        # TODO add OCLC number to PBCore object
        print '\t<OCLCnumber>' + record['OCLC number'] + '</OCLCnumber>'

    if record['Date modified']:
        # TODO add Date modified to PBCore object
        print '\t<Datemodified>' + record['Date modified'] + '</Datemodified>'

    if record['Reference URL']:
        # TODO add Reference URL to PBCore object
        print '\t<ReferenceURL>' + record['Reference URL'] + '</ReferenceURL>'

    if record['CONTENTdm number']:
        # TODO add CONTENTdm number to PBCore object
        print '\t<CONTENTdmNumber>' + record['CONTENTdm number'] + '</CONTENTdmNumber>'

    if record['CONTENTdm file name']:
        # TODO add CONTENTdm file name to PBCore object
        print '\t<CONTENTdmFileName>' + record['CONTENTdm file name'] + '</CONTENTdmFileName>'

    if record['CONTENTdm file path']:
        # TODO add CONTENTdm file path to PBCore object
        print '\t<CONTENTdmFilePath>' + record['CONTENTdm file path'] + '</CONTENTdmFilePath>'

    print "</FromCSV>"


# TODO create a function to validate CSV and makes sure all required fields are included

def validate_col_titles(f):
    print "Validating columns headers:",
    mismatched = []
    valid = True
    for index, heading in enumerate(csv.reader(f).next()):

        # print(index, heading, officialList[index])
        if heading != officialList[index]:
            valid = False
            mismatched.append("At column " + str(index) + ", recived: ["+ heading + "]. Expected: [" + officialList[index] + "]")

    f.seek(0)
    return valid, mismatched


def main():
    f = None

    try:
        print "Opening file:",
        f = open('/Users/lpsdesk/PycharmProjects/PBcore/sample_records/casauhs_export.csv', 'rU')
        print "OPEN"
    except IOError:
        print "FAILED"
        sys.stderr.write("Error, cannot find file.\n")
        print "Quitting"
        quit()

    valid, errors = validate_col_titles(f)
    if not valid:
        print "Error"
        sys.stdout.flush()
        for error in errors:
            sys.stderr.write(error + "\n")
        quit()



    try:
        print "Loading file into memory:",
        records = csv.DictReader(f)
        print "OK"
    except ValueError:
        print "FAILED"
        sys.stderr.write("Error, cannot load file as a CSV.\n")
        print "Quitting"
        quit()

    print "Generating PBCore stubs..."
    for record in records:

        print str(record['Project Identifier']) + ":"
        generate_pbcore(record)

        print "DONE\n"

    print "Closing CSV file:",
    f.close()
    print "CLOSED"
    print "Done"

if __name__ == '__main__':
    main()