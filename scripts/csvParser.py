import sys
import logging
import argparse
from time import sleep
from os.path import isfile
from xml.dom.minidom import parseString
from xml.etree import ElementTree
from modules.PBCore.PBCore import *

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


class RemoveErrorsFilter(logging.Filter):
    def filter(self, record):
        # if record.getMessage().startswith('INFO'):
        if record.levelno < logging.WARNING:
            return record.getMessage()
        # return not record.getMessage().startswith('WARNING')


def generate_pbcore(record):
    # TODO create XML generatation code here
    XML = ""
    new_XML_file = PBCore(collectionSource=record['Institution'])  #TODO: Find out if collectionSource is the 'Institution'.
    parts = []

# pbcoreDescriptionDocument
    obj_ID = ""
    proj_ID = ""
    asset_type = ""
    main_title = ""
    add_title = ""
    ser_title = ""
    descrp = ""
    obj_ARK = ""
    inst_ARK = ""
    inst_URL = ""
    subjects = ""
    genre = ""
    genre_autority= ""



    if record['Object Identifier']:
        obj_ID = record['Object Identifier'].split(';')[0].split('_t')[0]

    if record['Project Identifier']:
        # pbcoreInstantiation.instantiationIdentifier is part of CAVPP_Part class
        proj_ID = record['Project Identifier']

    if record['Asset Type']:
        # pbcoreDescriptionDocument.pbcoreAssetType is in pbcoreDescriptionDocument()
        # pbcoreInstantiation.pbcoreAssetType is in pbcoreDescriptionDocument()
        asset_type = record['Asset Type']

    if record['Main or Supplied Title']:
        # TODO add Main or Supplied Title to pbcoreDescriptionDocument.pbcoreTitle titleType="Main" and pbcorePart.pbcoreTitle titleType="Main"
        # pbcorePart.pbcoreTitle is in pbcoreDescriptionDocument()
        main_title = record['Main or Supplied Title']

    if record['Additional Title']:
        # TODO add Additional Title to PBCore object
        add_title = record['Additional Title']

    if record['Series Title']:
        # TODO add Series Title to PBCore object
        ser_title = record['Series Title']

    if record['Description or Content Summary']:
        # TODO add Description or Content Summary to PBCore object
        descrp = record['Description or Content Summary']

    if record['Object ARK']:
        # TODO add Object ARK to PBCore object
        obj_ARK = record['Object ARK']

    if record['Institution ARK']:
        # TODO add Institution ARK to PBCore object
        inst_ARK = record['Institution ARK']

    if record['Institution URL']:
        # TODO add Institution URL to PBCore object
        inst_URL = record['Institution URL']

    if record['Genre']:
        genre = record['Genre']

    if record['Genre Authority Source']:
        genre_autority = record['Genre Authority Source']


# DO THESE V

    if record['Call Number']:
        # TODO add Call Number to pbcoreDescriptionDocument.pbcoreIdentifier and pbcoreInstantiation.instantiationIdentifier
        # pbcoreDescriptionDocument.pbcoreIdentifier is part of pbcoreDescriptionDocument class
        # pbcoreInstantiation.instantiationIdentifier is part of CAVPP_Part class

        XML += '\t<CallNumber>' + record['Call Number'] + '</CallNumber>\n'

# DO THESE ^




    descritive = pbcoreDescriptionDocument(parentObjectID=obj_ID,
                                           projectID=proj_ID,
                                           assetType=asset_type,
                                           mainTitle=main_title,
                                           addTitle=add_title,
                                           seriesTitle=ser_title,
                                           description=descrp,
                                           objectARK=obj_ARK,
                                           genre=genre,
                                           genreAutority=genre_autority,
                                           institutionARK=inst_ARK,
                                           institutionURL=inst_URL,)

    if record['Subject Topic']:
        # TODO add Subject Topic to PBCore object
        subjects = record['Subject Topic']
        subjectTopics = subjects.split(';')
        for subjectTopic in subjectTopics:
            descritive.add_pbcoreSubject(PB_Element(tag="pbcoreSubject", value=subjectTopic))

    if record['Date Created']:
        creation = record['Date Created']
        creationDates = creation.split(';')
        for creationDate in creationDates:
            descritive.add_pbcoreAssetDate(PB_Element(['dateType', 'created'], tag="pbcoreAssetDate", value=creationDate))

    if record['Date Published']:
        # TODO add Date Published to PBCore object
        published = record['Date Published']
        publishedDates = published.split(';')
        for publishedDate in publishedDates:
            descritive.add_pbcoreAssetDate(PB_Element(['dateType', 'published'], tag="pbcoreAssetDate", value=publishedDate))


    # FIXME: Figure the subject authority, subject entity, Subject Entity Authority Source work in PBCORe
    if record['Subject Topic Authority Source']:
        # TODO add Subject Topic Authority Source to PBCore object
        XML += '\t<SubjectTopicAuthoritySource>' + record['Subject Topic Authority Source'] + '</SubjectTopicAuthoritySource>\n'
        # descritive.add_pbcoreS
    if record['Subject Entity']:
        # TODO add Subject Entity to PBCore object
        XML += '\t<SubjectEntity>' + record['Subject Entity'] + '</SubjectEntity>\n'

    if record['Subject Entity Authority Source']:
        # TODO add Subject Entity Authority Source to PBCore object
        XML += '\t<SubjectEntityAuthoritySource>' + record['Subject Entity Authority Source'] + '</SubjectEntityAuthoritySource>\n'


# Descriptive Creator: Producer,Director,Writer,Interviewer,Performer

    producer = ""
    director = ""
    writer = ""
    interviewer = ""
    performer = ""

    if record['Producer']:
        producer = record['Producer']
        creator = pbcoreCreator(name=producer, role="Producer")
        descritive.add_pbcoreCreator(creator)

    if record['Director']:
        director = record['Director']
        creator = pbcoreCreator(name=director, role="Director")
        descritive.add_pbcoreCreator(creator)

    if record['Writer']:
        writer = record['Writer']
        creator = pbcoreCreator(name=writer, role="Writer")
        descritive.add_pbcoreCreator(creator)

    if record['Interviewer']:
        interviewer = record['Interviewer']
        creator = pbcoreCreator(name=interviewer, role="Interviewer")
        descritive.add_pbcoreCreator(creator)

    if record['Performer']:
        performer = record['Performer']
        creator = pbcoreCreator(name=performer, role="Performer")
        descritive.add_pbcoreCreator(creator)


# Descriptive Contributor: Camera,Editor,Sound,Music,Cast,Interviewee,Speaker,Musician

    camera = ""
    editor = ""
    sound = ""
    music = ""
    cast = ""
    interviewee = ""
    speaker = ""
    musician = ""

    if record['Camera']:
        camera = record['Camera']
        contributor = pbcoreContributor(name=camera, role="Camera")
        descritive.add_pbcoreContributor(contributor)

    if record['Editor']:
        editor = record['Editor']
        contributor = pbcoreContributor(name=editor, role="Editor")
        descritive.add_pbcoreContributor(contributor)

    if record['Sound']:
        sound = record['Sound']
        contributor = pbcoreContributor(name=sound, role="Sound")
        descritive.add_pbcoreContributor(contributor)

    if record['Music']:
        music = record['Music']
        contributor = pbcoreContributor(name=music, role="Music")
        descritive.add_pbcoreContributor(contributor)

    if record['Cast']:
        cast = record['Cast']
        contributor = pbcoreContributor(name=cast, role="Cast")
        descritive.add_pbcoreContributor(contributor)

    if record['Interviewee']:
        interviewee = record['Interviewee']
        contributor = pbcoreContributor(name=interviewee, role="Interviewee")
        descritive.add_pbcoreContributor(contributor)

    if record['Speaker']:
        speaker = record['Speaker']
        contributor = pbcoreContributor(name=speaker, role="Speaker")
        descritive.add_pbcoreContributor(contributor)

    if record['Musician']:
        musician = record['Musician']
        contributor = pbcoreContributor(name=musician, role="Musician")
        descritive.add_pbcoreContributor(contributor)


# Descriptive Publisher: Publisher,Distributor
    publisher = ""
    distributor = ""

    if record['Publisher']:
        publisher = record['Publisher']
        publish = pbcorePublisher(name=publisher, role="Publisher")
        descritive.add_pbcorePublisher(publish)

    if record['Distributor']:
        distributor = record['Distributor']
        publish = pbcorePublisher(name=distributor, role="Distributor")
        descritive.add_pbcorePublisher(publish)


# Descriptive Rights
    copyright_statement = ""
    if record['Copyright Statement']:
        # TODO add Copyright Statement to PBCore object
        copyright_statement = record['Copyright Statement']

    rights = pbcoreRightsSummary(statement=copyright_statement)

    descritive.add_pbcoreRightsSummary(rights)

    new_XML_file.set_IntellectualContent(descritive)
# PARTS
    if record['Object Identifier']:
        # TODO add Object Identifier to pbcoreDescriptionDocument.pbcoreIdentifier and pbcoreInstantiation.instantiationIdentifier
        # pbcoreDescriptionDocument.pbcoreIdentifier is part of pbcoreDescriptionDocument class
        # pbcoreInstantiation.instantiationIdentifier is part of CAVPP_Part class
        if "_t" in record['Object Identifier']:
            objectIDs = record['Object Identifier'].split(';')

            for objectID in objectIDs:
                newpart = CAVPP_Part()
                pass
                # parts.append()

    if record['Media Type']:
        # TODO add Media Type to pbcoreInstantiation.instantiationMediaType
        # pbcoreInstantiation.instantiationMediaType is in pbcoreInstantiation()
        XML += '\t<MediaType>' + record['Media Type'] + '</MediaType>\n'

    if record['Generation']:
        # TODO add Generation to pbcoreInstantiation.instantiationGenerations
        # pbcoreInstantiation.instantiationGenerations is in pbcoreInstantiation()
        XML += '\t<Generation>' + record['Generation'] + '</Generation>\n'

    if record['Gauge and Format']:
        # TODO add Gauge and Format to PBCore object
        XML += '\t<GaugeAndFormat>' + record['Gauge and Format'] + '</GaugeAndFormat>\n'

    if record['Duration']:
        # TODO add Duration to PBCore object
        XML += '\t<Duration>' + record['Duration'] + '</Duration>\n'

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


# Extension
    if record['Country of Creation']:
        exten = pbcoreExtension(exElement="countryOfCreation",
                                exValue=record['Country of Creation'])
        new_XML_file.add_extensions(exten)

    if record['Project Note']:
        exten = pbcoreExtension(exElement="projectNote",
                                exValue=record['Project Note'])
        new_XML_file.add_extensions(exten)

# Relationship
    if record['Relationship']:
        # TODO add Relationship to PBCore object
        XML += '\t<Relationship>' + record['Relationship'] + '</Relationship>\n'

    if record['Relationship Type']:
        # TODO add Relationship Type to PBCore object
        XML += '\t<RelationshipType>' + record['Relationship Type'] + '</RelationshipType>\n'

# ----Unsorted



    if record['Internet Archive URL']:
        # TODO add Internet Archive URL to PBCore object
        # TODO: Find out where Internet Archive URL maps to in PBCore
        XML += '\t<InternetArchiveURL>' + record['Internet Archive URL'] + '</InternetArchiveURL>\n'



        # XML += '\t<ProjectIdentifier>' + record['Project Identifier'] + '</ProjectIdentifier>\n'



    if record['Institution']:
        # TODO add Institution to PBCore object
        # TODO: Find out where Institution maps to in PBCore
        XML += '\t<Institution>' + record['Institution'] + '</Institution>\n'










    if record['Why the recording is significant to California/local history']:
        # TODO add Why the recording is significant to California/local history to PBCore object
        XML += '\t<WhyTheRecordingIsSignificantToCaliforniaLocalHistory>' + record['Why the recording is significant to California/local history'] + '</WhyTheRecordingIsSignificantToCaliforniaLocalHistory>\n'







    if record['Total Number of Reels or Tapes']:
        # TODO add Total Number of Reels or Tapes to PBCore object
        XML += '\t<TotalNumberOfReelsOrTapes>' + record['Total Number of Reels or Tapes'] + '</TotalNumberOfReelsOrTapes>\n'



    if record['Silent or Sound']:
        # TODO add Silent or Sound to PBCore object
        XML += '\t<SilentOrSound>' + record['Silent or Sound'] + '</SilentOrSound>\n'

    if record['Color and/or Black and White']:
        # TODO add Color and/or Black and White to PBCore object
        XML += '\t<ColorAndOrBlackAndWhite>' + record['Color and/or Black and White'] + '</ColorAndOrBlackAndWhite>\n'


    if record['Language']:
        # TODO add Language to PBCore object
        XML += '\t<Language>' + record['Language'] + '</Language>\n'



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



    return new_XML_file.xmlString()
    # return ElementTree.tostring(new_XML_file.xml(), encoding='utf8', method='xml')

def validate_col_titles(f):
    mismatched = []
    valid = True
    for index, heading in enumerate(csv.reader(f).next()):

        # print(index, heading, officialList[index])
        if heading != officialList[index]:
            valid = False
            mismatched.append("CSV title mismatch. At column " + str(index+1) + ", recived: ["+ heading + "]. Expected: [" + officialList[index] + "]")

    f.seek(0)
    return valid, mismatched


def main():
    mode = "normal"
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="Source CSV file", type=str)
    parser.add_argument("-d", "--debug", help="Debug mode. Writes all messages to debug log.", action='store_true')
    args = parser.parse_args()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('logs/debug.log')  # Saves all logs to this file
    eh = logging.StreamHandler(sys.stderr)      # sends any critical errors to standard error
    eh.setLevel(logging.WARNING)
    ch = logging.StreamHandler(sys.stdout)      # sends all debug info to the standard out
    ch.setLevel(logging.DEBUG)
    log_filter = RemoveErrorsFilter()
    ch.addFilter(log_filter)  # logger.addFilter(NoParsingFilter())
    if args.debug:
        mode = 'debug'
        print "ENTERING DEBUG MODE!"
        fh.setLevel(logging.DEBUG)
    else:
        mode = 'normal'
        fh.setLevel(logging.INFO)
        # logging.basicConfig(filename='logs/debug.log', level=logging.INFO)
    error_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')     # DATE - USERNAME - Message
    stderr_formatter = logging.Formatter('%(levelname)s - %(message)s')                             # USERNAME - Message
    stdout_formatter = logging.Formatter('%(message)s')                                             # Message

    fh.setFormatter(error_formatter)
    eh.setFormatter(stderr_formatter)
    ch.setFormatter(stdout_formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    logger.addHandler(eh)
    f = None
    if isfile(args.csv):  # checks if the file passed in is a real file):
        try:
            logger.debug("Opening file:" + args.csv)
            f = open(args.csv, 'rU')
        except IOError:
            print "FAILED"
            logger.critical("Cannot open " + args.csv + ". Quitting")
            quit()
    else:
        logger.critical("Cannot locate " + args.csv + ". Quitting")
        quit()

    logger.debug("Validating files column titles")
    valid, errors = validate_col_titles(f)
    if not valid:
        sys.stdout.flush()
        for error in errors:
            logger.critical(error)
        quit()

    try:
        logger.debug("Loading file into memory")
        records = csv.DictReader(f)
    except ValueError:
        print "FAILED"
        logger.critical("Error, cannot load file as a CSV.")
        print "Quitting"
        quit()

    logging.info("Generating PBCore stubs...")
    for record in records:
        logger.info("Producing PBCore XML for " + str(record['Project Identifier']))
        if isfile(str(record['Project Identifier'])+".xml"):
            logger.warning(str(record['Project Identifier'])+".xml is already a file, overwriting." )
        # output = generate_pbcore(record)

        # I'm sending this into because I can't get etree to print a pretty XML
        buf = parseString(generate_pbcore(record))
        output_file = open(str(record['Project Identifier'])+".xml", 'w')
        output_file.write(buf.toprettyxml(encoding='utf-8'))
        output_file.close()

    logger.debug("Closing CSV file:")
    f.close()
    print "Done"

if __name__ == '__main__':
    main()