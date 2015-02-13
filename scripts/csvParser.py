import sys
import logging
import argparse
from time import sleep
from os.path import isfile

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
    XML = str()
    rootTag = "XML"
    XML += "<" + rootTag + ">\n"

    if record['Object Identifier']:
        # TODO add Object Identifier to pbcoreDescriptionDocument.pbcoreIdentifier and pbcoreInstantiation.instantiationIdentifier
        # pbcoreDescriptionDocument.pbcoreIdentifier is part of pbcoreDescriptionDocument class
        # pbcoreInstantiation.instantiationIdentifier is part of CAVPP_Part class
        objectIDs = record['Object Identifier'].split(';')
        for objectID in objectIDs:
            XML += '\t<ObjectIdentifier>' + objectID.lstrip() + '</ObjectIdentifier>\n'

    if record['Internet Archive URL']:
        # TODO add Internet Archive URL to PBCore object
        # TODO: Find out where Internet Archive URL maps to in PBCore
        XML += '\t<InternetArchiveURL>' + record['Internet Archive URL'] + '</InternetArchiveURL>\n'

    if record['Call Number']:
        # TODO add Call Number to pbcoreDescriptionDocument.pbcoreIdentifier and pbcoreInstantiation.instantiationIdentifier
        # pbcoreDescriptionDocument.pbcoreIdentifier is part of pbcoreDescriptionDocument class
        # pbcoreInstantiation.instantiationIdentifier is part of CAVPP_Part class

        XML += '\t<CallNumber>' + record['Call Number'] + '</CallNumber>\n'

    if record['Project Identifier']:
        # TODO add Project Identifier to pbcoreDescriptionDocument.pbcoreIdentifier
        # pbcoreInstantiation.instantiationIdentifier is part of CAVPP_Part class

        XML += '\t<ProjectIdentifier>' + record['Project Identifier'] + '</ProjectIdentifier>\n'

    if record['Project Note']:
        # TODO add Project Note to PBCore object
        # TODO: Find out where Project Note maps to in PBCore
        XML += '\t<ProjectNote>' + record['Project Note'] + '</ProjectNote>\n'

    if record['Institution']:
        # TODO add Institution to PBCore object
        # TODO: Find out where Institution maps to in PBCore
        XML += '\t<Institution>' + record['Institution'] + '</Institution>\n'

    if record['Asset Type']:
        # TODO add Asset Type to pbcoreDescriptionDocument.pbcoreAssetType
        # pbcoreDescriptionDocument.pbcoreAssetType is in pbcoreDescriptionDocument()
        # pbcoreInstantiation.pbcoreAssetType is in pbcoreDescriptionDocument()
        XML += '\t<AssetType>' + record['Asset Type'] + '</AssetType>\n'

    if record['Media Type']:
        # TODO add Media Type to pbcoreInstantiation.instantiationMediaType
        # pbcoreInstantiation.instantiationMediaType is in pbcoreInstantiation()
        XML += '\t<MediaType>' + record['Media Type'] + '</MediaType>\n'

    if record['Generation']:
        # TODO add Generation to pbcoreInstantiation.instantiationGenerations
        # pbcoreInstantiation.instantiationGenerations is in pbcoreInstantiation()
        XML += '\t<Generation>' + record['Generation'] + '</Generation>\n'

    if record['Main or Supplied Title']:
        # TODO add Main or Supplied Title to pbcoreDescriptionDocument.pbcoreTitle titleType="Main" and pbcorePart.pbcoreTitle titleType="Main"
        # pbcorePart.pbcoreTitle is in pbcoreDescriptionDocument()

        XML += '\t<MainOrSuppliedTitle>' + record['Main or Supplied Title'] + '</MainOrSuppliedTitle>\n'

    if record['Additional Title']:
        # TODO add Additional Title to PBCore object
        XML += '\t<AdditionalTitle>' + record['Additional Title'] + '</AdditionalTitle>\n'

    if record['Series Title']:
        # TODO add Series Title to PBCore object
        XML += '\t<SeriesTitle>' + record['Series Title'] + '</SeriesTitle>\n'

    if record['Description or Content Summary']:
        # TODO add Description or Content Summary to PBCore object
        XML += '\t<DescriptionOrContentSummary>' + record['Description or Content Summary'] + '</DescriptionOrContentSummary>\n'

    if record['Why the recording is significant to California/local history']:
        # TODO add Why the recording is significant to California/local history to PBCore object
        XML += '\t<WhyTheRecordingIsSignificantToCaliforniaLocalHistory>' + record['Why the recording is significant to California/local history'] + '</WhyTheRecordingIsSignificantToCaliforniaLocalHistory>\n'

    if record['Producer']:
        # TODO add Producer to PBCore object
        XML += '\t<Producer>' + record['Producer'] + '</Producer>\n'

    if record['Director']:
        # TODO add Director to PBCore object
        XML += '\t<Director>' + record['Director'] + '</Director>\n'

    if record['Writer']:
        # TODO add Writer to PBCore object
        XML += '\t<Writer>' + record['Writer'] + '</Writer>\n'

    if record['Interviewer']:
        # TODO add Interviewer to PBCore object
        XML += '\t<Interviewer>' + record['Interviewer'] + '</Interviewer>\n'

    if record['Performer']:
        # TODO add Performer to PBCore object
        XML += '\t<Performer>' + record['Performer'] + '</Performer>\n'

    if record['Country of Creation']:
        # TODO add Country of Creation to PBCore object
        XML += '\t<CountryOfCreation>' + record['Country of Creation'] + '</CountryOfCreation>\n'

    if record['Date Created']:
        # TODO add Date Created to PBCore object
        creationDates = record['Date Created'].split(';')
        for creationDate in creationDates:
            XML += '\t<DateCreated>' + creationDate.lstrip() + '</DateCreated>\n'

    if record['Date Published']:
        # TODO add Date Published to PBCore object
        XML += '\t<DatePublished>' + record['Date Published'] + '</DatePublished>\n'

    if record['Copyright Statement']:
        # TODO add Copyright Statement to PBCore object
        XML += '\t<CopyrightStatement>' + record['Copyright Statement'] + '</CopyrightStatement>\n'

    if record['Gauge and Format']:
        # TODO add Gauge and Format to PBCore object
        XML += '\t<GaugeAndFormat>' + record['Gauge and Format'] + '</GaugeAndFormat>\n'

    if record['Total Number of Reels or Tapes']:
        # TODO add Total Number of Reels or Tapes to PBCore object
        XML += '\t<TotalNumberOfReelsOrTapes>' + record['Total Number of Reels or Tapes'] + '</TotalNumberOfReelsOrTapes>\n'

    if record['Duration']:
        # TODO add Duration to PBCore object
        XML += '\t<Duration>' + record['Duration'] + '</Duration>\n'

    if record['Silent or Sound']:
        # TODO add Silent or Sound to PBCore object
        XML += '\t<SilentOrSound>' + record['Silent or Sound'] + '</SilentOrSound>\n'

    if record['Color and/or Black and White']:
        # TODO add Color and/or Black and White to PBCore object
        XML += '\t<ColorAndOrBlackAndWhite>' + record['Color and/or Black and White'] + '</ColorAndOrBlackAndWhite>\n'

    if record['Camera']:
        # TODO add Camera to PBCore object
        XML += '\t<Camera>' + record['Camera'] + '</Camera>\n'

    if record['Editor']:
        # TODO add Editor to PBCore object
        XML += '\t<Editor>' + record['Editor'] + '</Editor>\n'

    if record['Sound']:
        # TODO add Sound to PBCore object
        XML += '\t<Sound>' + record['Sound'] + '</Sound>\n'

    if record['Music']:
        # TODO add Music to PBCore object
        XML += '\t<Music>' + record['Music'] + '</Music>\n'

    if record['Cast']:
        # TODO add Cast to PBCore object
        XML += '\t<Cast>' + record['Cast'] + '</Cast>\n'

    if record['Interviewee']:
        # TODO add Interviewee to PBCore object
        XML += '\t<Interviewee>' + record['Interviewee'] + '</Interviewee>\n'

    if record['Speaker']:
        # TODO add Speaker to PBCore object
        XML += '\t<Speaker>' + record['Speaker'] + '</Speaker>\n'

    if record['Musician']:
        # TODO add Musician to PBCore object
        XML += '\t<Musician>' + record['Musician'] + '</Musician>\n'

    if record['Publisher']:
        # TODO add Publisher to PBCore object
        XML += '\t<Publisher>' + record['Publisher'] + '</Publisher>\n'

    if record['Distributor']:
        # TODO add Distributor to PBCore object
        XML += '\t<Distributor>' + record['Distributor'] + '</Distributor>\n'

    if record['Language']:
        # TODO add Language to PBCore object
        XML += '\t<Language>' + record['Language'] + '</Language>\n'

    if record['Subject Topic']:
        # TODO add Subject Topic to PBCore object
        subjectTopics = record['Subject Topic'].split(';')
        for subjectTopic in subjectTopics:
            XML += '\t<SubjectTopic>' + subjectTopic.lstrip() + '</SubjectTopic>\n'

    if record['Subject Topic Authority Source']:
        # TODO add Subject Topic Authority Source to PBCore object
        XML += '\t<SubjectTopicAuthoritySource>' + record['Subject Topic Authority Source'] + '</SubjectTopicAuthoritySource>\n'

    if record['Subject Entity']:
        # TODO add Subject Entity to PBCore object
        XML += '\t<SubjectEntity>' + record['Subject Entity'] + '</SubjectEntity>\n'

    if record['Subject Entity Authority Source']:
        # TODO add Subject Entity Authority Source to PBCore object
        XML += '\t<SubjectEntityAuthoritySource>' + record['Subject Entity Authority Source'] + '</SubjectEntityAuthoritySource>\n'

    if record['Genre']:
        # TODO add Genre to PBCore object
        XML += '\t<Genre>' + record['Genre'] + '</Genre>\n'

    if record['Genre Authority Source']:
        # TODO add Genre Authority Source to PBCore object
        XML += '\t<GenreAuthoritySource>' + record['Genre Authority Source'] + '</GenreAuthoritySource>\n'

    if record['Spatial Coverage']:
        # TODO add Spatial Coverage to PBCore object
        XML += '\t<SpatialCoverage>' + record['Spatial Coverage'] + '</SpatialCoverage>\n'

    if record['Temporal Coverage']:
        # TODO add Temporal Coverage to PBCore object
        XML += '\t<TemporalCoverage>' + record['Temporal Coverage'] + '</TemporalCoverage>\n'

    if record['Collection Guide Title']:
        # TODO add Collection Guide Title to PBCore object
        XML += '\t<CollectionGuideTitle>' + record['Collection Guide Title'] + '</CollectionGuideTitle>\n'

    if record['Collection Guide URL']:
        # TODO add Collection Guide URL to PBCore object
        XML += '\t<CollectionGuideURL>' + record['Collection Guide URL'] + '</CollectionGuideURL>\n'

    if record['Relationship']:
        # TODO add Relationship to PBCore object
        XML += '\t<Relationship>' + record['Relationship'] + '</Relationship>\n'

    if record['Relationship Type']:
        # TODO add Relationship Type to PBCore object
        XML += '\t<RelationshipType>' + record['Relationship Type'] + '</RelationshipType>\n'

    if record['Aspect Ratio']:
        # TODO add Aspect Ratio to PBCore object
        XML += '\t<AspectRatio>' + record['Aspect Ratio'] + '</AspectRatio>\n'

    if record['Running Speed']:
        # TODO add Running Speed to PBCore object
        XML += '\t<RunningSpeed>' + record['Running Speed'] + '</RunningSpeed>\n'

    if record['Timecode Content Begins']:
        # TODO add Timecode Content Begins to PBCore object
        XML += '\t<TimecodeContentBegins>' + record['Timecode Content Begins'] + '</TimecodeContentBegins>\n'

    if record['Track Standard']:
        # TODO add Track Standard to PBCore object
        XML += '\t<TrackStandard>' + record['Track Standard'] + '</TrackStandard>\n'

    if record['Channel Configuration']:
        # TODO add Channel Configuration to PBCore object
        XML += '\t<ChannelConfiguration>' + record['Channel Configuration'] + '</ChannelConfiguration>\n'

    if record['Subtitles/Intertitles/Closed Captions']:
        # TODO add Subtitles/Intertitles/Closed Captions to PBCore object
        XML += '\t<SubtitlesIntertitlesClosedCaptions>' + record['Subtitles/Intertitles/Closed Captions'] + '</SubtitlesIntertitlesClosedCaptions>\n'

    if record['Stock Manufacturer']:
        # TODO add Stock Manufacturer to PBCore object
        XML += '\t<StockManufacturer>' + record['Stock Manufacturer'] + '</StockManufacturer>\n'

    if record['Base Type']:
        # TODO add Base Type to PBCore object
        XML += '\t<BaseType>' + record['Base Type'] + '</BaseType>\n'

    if record['Base Thickness']:
        # TODO add Base Thickness to PBCore object
        XML += '\t<BaseThickness>' + record['Base Thickness'] + '</BaseThickness>\n'

    if record['Copyright Holder']:
        # TODO add Copyright Holder to PBCore object
        XML += '\t<CopyrightHolder>' + record['Copyright Holder'] + '</CopyrightHolder>\n'

    if record['Copyright Holder Info']:
        # TODO add Copyright Holder Info to PBCore object
        XML += '\t<CopyrightHolderInfo>' + record['Copyright Holder Info'] + '</CopyrightHolderInfo>\n'

    if record['Copyright Date']:
        # TODO add Copyright Date to PBCore object
        copyrightdates = record['Copyright Date'].split(';')
        for copyrightdate in copyrightdates:
            XML += '\t<CopyrightDate>' + copyrightdate.lstrip() + '</CopyrightDate>\n'

    if record['Copyright Notice']:
        # TODO add Copyright Notice to PBCore object
        XML += '\t<CopyrightNotice>' + record['Copyright Notice'] + '</CopyrightNotice>\n'

    if record['Institutional Rights Statement (URL)']:
        # TODO add Institutional Rights Statement (URL) to PBCore object
        XML += '\t<InstitutionalRightsStatementURL>' + record['Institutional Rights Statement (URL)'] + '</InstitutionalRightsStatementURL>\n'

    if record['Object ARK']:
        # TODO add Object ARK to PBCore object
        XML += '\t<ObjectARK>' + record['Object ARK'] + '</ObjectARK>\n'

    if record['Institution ARK']:
        # TODO add Institution ARK to PBCore object
        XML += '\t<InstitutionARK>' + record['Institution ARK'] + '</InstitutionARK>\n'

    if record['Institution URL']:
        # TODO add Institution URL to PBCore object
        XML += '\t<InstitutionURL>' + record['Institution URL'] + '</InstitutionURL>\n'

    if record['Quality Control Notes']:
        # TODO add Quality Control Notes to PBCore object
        QCNotes = record['Quality Control Notes'].split(';')
        for QCNote in QCNotes:
            XML += '\t<QualityControlNotes>' + QCNote.lstrip() + '</QualityControlNotes>\n'

    if record['Additional Descriptive Notes for Overall Work']:
        # TODO add Additional Descriptive Notes for Overall Work to PBCore object
        XML += '\t<AdditionalDescriptiveNotesForOverallWork>' + record['Additional Descriptive Notes for Overall Work'] + '</AdditionalDescriptiveNotesForOverallWork>\n'

    if record['Additional Technical Notes for Overall Work']:
        # TODO add Additional Technical Notes for Overall Work to PBCore object
        XML += '\t<AdditionalTechnicalNotesForOverallWork>' + record['Additional Technical Notes for Overall Work'] + '</AdditionalTechnicalNotesForOverallWork>\n'

    if record['Transcript']:
        # TODO add Transcript to PBCore object
        XML += '\t<Transcript>' + record['Transcript'] + '</Transcript>\n'

    if record['Cataloger Notes']:
        # TODO add Cataloger Notes to PBCore object
        XML += '\t<CatalogerNotes>' + record['Cataloger Notes'] + '</CatalogerNotes>\n'

    if record['OCLC number']:
        # TODO add OCLC number to PBCore object
        XML += '\t<OCLCnumber>' + record['OCLC number'] + '</OCLCnumber>\n'

    if record['Date modified']:
        # TODO add Date modified to PBCore object
        XML += '\t<Datemodified>' + record['Date modified'] + '</Datemodified>\n'

    if record['Reference URL']:
        # TODO add Reference URL to PBCore object
        XML += '\t<ReferenceURL>' + record['Reference URL'] + '</ReferenceURL>\n'

    if record['CONTENTdm number']:
        # TODO add CONTENTdm number to PBCore object
        XML += '\t<CONTENTdmNumber>' + record['CONTENTdm number'] + '</CONTENTdmNumber>\n'

    if record['CONTENTdm file name']:
        # TODO add CONTENTdm file name to PBCore object
        XML += '\t<CONTENTdmFileName>' + record['CONTENTdm file name'] + '</CONTENTdmFileName>\n'

    if record['CONTENTdm file path']:
        # TODO add CONTENTdm file path to PBCore object
        XML += '\t<CONTENTdmFilePath>' + record['CONTENTdm file path'] + '</CONTENTdmFilePath>\n'

    XML += "</" + rootTag + ">\n"
    return XML


def validate_col_titles(f):
    mismatched = []
    valid = True
    for index, heading in enumerate(csv.reader(f).next()):

        # print(index, heading, officialList[index])
        if heading != officialList[index]:
            valid = False
            mismatched.append("At column " + str(index+1) + ", recived: ["+ heading + "]. Expected: [" + officialList[index] + "]")

    f.seek(0)
    return valid, mismatched


def main():
    mode = "normal"
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="Source CSV file", type=str)
    parser.add_argument("-d", "--debug", help="Debug mode. Writes all messages to debug log.", action='store_true')
    args = parser.parse_args()
    
    if args.debug:
        mode = 'debug'
        print "ENTERING DEBUG MODE!"
        # logging.basicConfig(filename='logs/debug.log', level=logging.DEBUG)
        logging.basicConfig(filename='logs/debug.log', level=logging.DEBUG)
    else:
        mode = 'normal'
        logging.basicConfig(filename='logs/debug.log', level=logging.INFO)


    f = None
    if isfile(args.csv):  # checks if the file passed in is a real filegs.csv):
        try:
            logging.debug("Opening file:" + args.csv)
            f = open(args.csv, 'rU')
        except IOError:
            print "FAILED"
            logging.critical("Error, cannot open " + args.csv + ". Quitting")
            sys.stderr.write("Error, cannot open " + args.csv + ". Quitting\n")
            quit()
    else:
        logging.critical("Error, cannot locate " + args.csv + ". Quitting")
        sys.stderr.write("Error, cannot locate " + args.csv + ". Quitting\n")
        quit()

    logging.debug("Validating files column titles")
    valid, errors = validate_col_titles(f)
    if not valid:
        sys.stdout.flush()
        for error in errors:
            sys.stderr.write(error + "\n")
            logging.critical(error)
        quit()

    try:
        logging.debug("Loading file into memory")
        records = csv.DictReader(f)
    except ValueError:
        print "FAILED"
        logging.critical("Error, cannot load file as a CSV.")
        sys.stderr.write("Error, cannot load file as a CSV.\n")
        print "Quitting"
        quit()

    print "Generating PBCore stubs..."
    for record in records:

        # print str(record['Project Identifier']) + ":"
        # logging.info("Producing PBCore XML for " + str(record['Project Identifier']))
        print generate_pbcore(record)

        # print "DONE\n"

    logging.debug("Closing CSV file:")
    f.close()
    print "Done"

if __name__ == '__main__':
    main()