import sys
import logging
import argparse
import string
from time import sleep
from os.path import isfile
from xml.dom.minidom import parseString
from xml.etree import ElementTree
import re
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
    XML = ""
    new_XML_file = PBCore(collectionSource=record['Institution'],
                          collectionTitle=record['Collection Guide Title'])  #TODO: Find out if collectionSource is the 'Institution'.


# pbcoreDescriptionDocument
    obj_ID = ""
    proj_ID = ""
    asset_type = ""
    main_title = ""
    add_title = ""
    ser_title = ""
    descrp = ""
    obj_ARK = ""
    inst_name = ""
    inst_ARK = ""
    inst_URL = ""
    creationDates = []
    subjectTops = ""
    genre = ""
    genre_autority= ""
    IA_URL= ""
    QC_notes_list = ""
    transcript = ""



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
        main_title = record['Main or Supplied Title']

    if record['Additional Title']:
        add_title = record['Additional Title']

    if record['Series Title']:
        ser_title = record['Series Title']

    if record['Description or Content Summary']:
        descrp = record['Description or Content Summary']

    if record['Object ARK']:
        obj_ARK = record['Object ARK']

    if record['Institution']:
        inst_name = record['Institution']

    if record['Institution ARK']:
        inst_ARK = record['Institution ARK']

    if record['Institution URL']:
        inst_URL = record['Institution URL']







    descritive = pbcoreDescriptionDocument(parentObjectID=obj_ID,
                                           projectID=proj_ID,
                                           assetType=asset_type,
                                           mainTitle=main_title,
                                           addTitle=add_title,
                                           seriesTitle=ser_title,
                                           description=descrp,
                                           objectARK=obj_ARK,
                                           institutionName=inst_name,
                                           institutionARK=inst_ARK,
                                           institutionURL=inst_URL,)


    if record['Internet Archive URL']:
        IA_URL = record['Internet Archive URL']
        descritive.add_pbcoreIdentifier(PB_Element(['source', 'CAVPP'], ['annotation', 'Internet Archive URL'], tag='pbcoreIdentifier', value=IA_URL))

    if record['Subject Topic']:
        subjectTops = record['Subject Topic']
        subjectTopics = subjectTops.split(';')
        subjectTopicAuthority = record['Subject Topic Authority Source']

        for subjectTopic in subjectTopics:
            # Unless another subject authority is specified, the source will default to the LOC subject headings
            if subjectTopicAuthority and subjectTopicAuthority != "":
                descritive.add_pbcoreSubject(PB_Element(['source', subjectTopicAuthority], tag="pbcoreSubject", value=subjectTopic))
            else:
                descritive.add_pbcoreSubject(PB_Element(['source', "Library of Congress Subject Headings"], tag="pbcoreSubject", value=subjectTopic))

    if record['Subject Entity']:
        subjectEnts = record['Subject Entity']
        subjectEntities = subjectEnts.split(';')
        subjectEntityAuthority = record['Subject Entity Authority Source']

        for subjectEntity in subjectEntities:
            if subjectEntityAuthority and subjectEntityAuthority != "":
                descritive.add_pbcoreSubject(PB_Element(['source', subjectEntityAuthority], tag="pbcoreSubject", value=subjectEntity))
            else:
                descritive.add_pbcoreSubject(PB_Element(tag="pbcoreSubject", value=subjectEntity))

    if record['Spatial Coverage']:
        spatCoverages = record['Spatial Coverage']
        spatialCoverages = spatCoverages.split(';')
        for spatialCoverage in spatialCoverages:
            descritive.add_pbcoreCoverage(pbcoreCoverage(covItem=spatialCoverage, covType="Spacial"))


    if record['Temporal Coverage']:
        tempCoverages = record['Temporal Coverage']
        temporalCoverages = tempCoverages.split(';')
        for temporalCoverage in temporalCoverages:
            descritive.add_pbcoreCoverage(pbcoreCoverage(covItem=temporalCoverage, covType="Temporal"))


    if record['Genre']:
        genres_data = record['Genre']
        genres = genres_data.split(';')
        genreAuthoity = record['Genre Authority Source']
        for genre in genres:
            if genreAuthoity and genreAuthoity != "":
                descritive.add_pbcoreGenre(PB_Element(['source', genreAuthoity], tag="pbcoreGenre", value=genre))
            else:
                descritive.add_pbcoreGenre(PB_Element(tag="pbcoreGenre", value=genre))


    if record['Date Created']:
        creation = record['Date Created']
        creationDates = creation.split(';')
        for creationDate in creationDates:
            descritive.add_pbcoreAssetDate(PB_Element(['dateType', 'created'], tag="pbcoreAssetDate", value=creationDate.strip()))

    if record['Date Published']:
        published = record['Date Published']
        publishedDates = published.split(';')
        for publishedDate in publishedDates:
            descritive.add_pbcoreAssetDate(PB_Element(['dateType', 'published'], tag="pbcoreAssetDate", value=publishedDate.strip()))

    if record['Additional Descriptive Notes for Overall Work']:
        add_desc_notes = record['Additional Descriptive Notes for Overall Work'].split(';')
        for note in add_desc_notes:
            descritive.add_pbcoreDescription(PB_Element(['descriptionType', 'Additional Descriptive Notes for Overall Work'], tag='pbcoreDescription', value=note.strip()))
        # TODO add Additional Descriptive Notes for Overall Work to PBCore object
        # goes with pbCoreDescription

    if record['Transcript']:
        # TODO add Transcript to PBCore object
        transcript = record['Transcript']
        descritive.add_pbcoreDescription(PB_Element(['descriptionType', 'Transcript'], tag='pbcoreDescription', value=transcript))



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
    copyright_holder = ""
    copyright_holder_info = ""
    copyright_dates = []
    copyright_notice = ""
    institutional_rights_statement_URL = ""
    rights = pbcoreRightsSummary()

    if record['Copyright Statement']:
        copyright_statement = record['Copyright Statement']
        rights.add_rightsSummary(PB_Element(['annotation', 'Copyright Statement'], tag="rightsSummary", value=copyright_statement.strip()))


    if record['Copyright Holder']:
        copyright_holder = record['Copyright Holder']
        rights.add_rightsSummary(PB_Element(['annotation', 'Copyright Holder'], tag="rightsSummary", value=copyright_holder.strip()))

    if record['Copyright Holder Info']:
        copyright_holder_info = record['Copyright Holder Info']
        rights.add_rightsSummary(PB_Element(['annotation', 'Copyright Holder Info'], tag="rightsSummary", value=copyright_holder_info.strip()))

    if record['Copyright Date']:
        copyright_dates = re.split('; |,|and', record['Copyright Date'])
        for copyright_date in copyright_dates:
            rights.add_rightsSummary(PB_Element(['annotation', 'Copyright Date'], tag="rightsSummary", value=copyright_date.strip()))

    if record['Copyright Notice']:
        copyright_notice = record['Copyright Notice']
        rights.add_rightsSummary(PB_Element(['annotation', 'Copyright Notice'], tag="rightsSummary", value=copyright_notice.strip()))

    if record['Institutional Rights Statement (URL)']:
        institutional_rights_statement_URL = record['Institutional Rights Statement (URL)']
        rights.add_rightsSummary(PB_Element(['annotation', 'Institutional Rights Statement (URL)'], tag="rightsSummary", value=institutional_rights_statement_URL.strip()))



    descritive.add_pbcoreRightsSummary(rights)



# PARTS
    call_number = ""
    if record['Call Number']:
        # pbcoreDescriptionDocument.pbcoreIdentifier is part of pbcoreDescriptionDocument class
        # pbcoreInstantiation.instantiationIdentifier is part of CAVPP_Part class
        call_number = record['Call Number']
    # TODO add Call Number to pbcoreDescriptionDocument.pbcoreIdentifier and pbcoreInstantiation.instantiationIdentifier

# PBcore Parts
    for part in record['Object Identifier'].split(';'):
        newPart = CAVPP_Part(objectID=part.strip(),
                             callNumber=call_number.strip(),
                             mainTitle=main_title.strip(),
                             description=descrp.strip())

        # physical
        physical_asset = ""
        media_type = ""
        generation = ""
        timecode_begins = ""
        durton = ""
        chan_config = ""
        lang = ""
        track_standard = ""
        total_number = ""
        stock = ""
        base_type = ""
        bass_thickness = ""
        cataloger_notes = ""
        speed = ""
        sound = ""
        color = ""
        aspect = ""
        run_speed = ""

        if record['Gauge and Format']:
            physical_asset = record['Gauge and Format']

        if record['Media Type']:
            media_type = record['Media Type']

        if record['Generation']:
            generation = record['Generation']

        if record['Timecode Content Begins']:
            timecode_begins = record['Timecode Content Begins']

        if record['Duration']:
            durton = record['Duration']

        if record['Channel Configuration']:
            chan_config = record['Channel Configuration']

        if record['Language']:
            lang = record['Language']

        if record['Track Standard']:
            track_standard = record['Track Standard']

        if record['Total Number of Reels or Tapes']:
            total_number = record['Total Number of Reels or Tapes']

        if record['Stock Manufacturer']:
            stock = record['Stock Manufacturer']

        if record['Base Type']:
            base_type = record['Base Type']

        if record['Base Thickness']:
            bass_thickness = record['Base Thickness']

        if record['Silent or Sound']:
            sound = record['Silent or Sound']

        if record['Color and/or Black and White']:
            color = record['Color and/or Black and White']


        if record['Aspect Ratio']:
            aspect = record['Aspect Ratio']

        if record['Running Speed']:
            run_speed = record['Running Speed']



        physical = pbcoreInstantiation(type="Physical Asset",
                                       objectID=part.strip(),
                                       extent=total_number,
                                       physical=physical_asset,
                                       mediaType=media_type,
                                       generations=generation,
                                       tracks=sound,
                                       colors=color,
                                       timeStart=timecode_begins,
                                       duration=durton,
                                       channelConfiguration=chan_config,
                                       language=lang,
                                       baseType=stock,
                                       stockManufacture=base_type,
                                       baseThickness=bass_thickness)

        for date in creationDates:
            physical.add_instantiationDate(PB_Element(tag='instantiationDate', value=date))



        if record['Additional Technical Notes for Overall Work']:
            tech_notes = record['Additional Technical Notes for Overall Work'].split(";")
            for note in tech_notes:
                physical.add_instantiationAnnotation(PB_Element(['annotation', 'Additional Technical Notes for Overall'], tag="instantiationAnnotation", value=note.strip()))

        if record['Cataloger Notes']:
            cataloger_notes = record['Cataloger Notes'].split(';')
            for note in cataloger_notes:
                physical.add_instantiationAnnotation(PB_Element(['annotation', 'Cataloger Notes'], tag="instantiationAnnotation", value=note.strip()))

# instantiationPart
        if media_type.lower() == 'audio' or media_type.lower() == 'sound':
            speed = record['Running Speed']
            newInstPart = InstantiationPart(objectID=part)
            newEss = InstantiationEssenceTrack(objectID=part, type="Audio", ips=speed)
            newInstPart.add_instantiationEssenceTrack(newEss)
            physical.add_instantiationPart(newInstPart)

        elif media_type.lower() == 'moving image':
            newEss = InstantiationEssenceTrack(objectID=part, frameRate=run_speed)
            physical.add_instantiationEssenceTrack(newEss)


        newPart.add_pbcoreInstantiation(physical)

        # <!--Preservation Master-->
        pres_master = pbcoreInstantiation(type="Preservation Master",
                                          objectID=(part.strip()+"_prsv"))
        if record['Quality Control Notes']:
            QC_notes_list = record['Quality Control Notes'].split(";")
            for note in QC_notes_list:
                pres_master.add_instantiationAnnotation(PB_Element(['annotation', 'CAVPP Quality Control/Partner Quality Control'], tag="instantiationAnnotation", value=note.strip()))


        newPart.add_pbcoreInstantiation(pres_master)
        descritive.add_pbcore_part(newPart)

    # if record['Object Identifier']:
    #     # TODO add Object Identifier to pbcoreDescriptionDocument.pbcoreIdentifier and pbcoreInstantiation.instantiationIdentifier
    #     # pbcoreDescriptionDocument.pbcoreIdentifier is part of pbcoreDescriptionDocument class
    #     # pbcoreInstantiation.instantiationIdentifier is part of CAVPP_Part class
    #     if "_t" in record['Object Identifier']:
    #         objectIDs = record['Object Identifier'].split(';')
    #
    #         for objectID in objectIDs:
    #             newpart = CAVPP_Part()
    #             pass
    #             # parts.append()





    if record['Subtitles/Intertitles/Closed Captions']:
        # TODO add Subtitles/Intertitles/Closed Captions to PBCore object
        XML += '\t<SubtitlesIntertitlesClosedCaptions>' + record['Subtitles/Intertitles/Closed Captions'] + '</SubtitlesIntertitlesClosedCaptions>\n'









# Extension
    if record['Country of Creation']:
        exten = pbcoreExtension(exElement="countryOfCreation",
                                exValue=record['Country of Creation'])
        new_XML_file.add_extensions(exten)

    if record['Project Note']:
        if record['Project Note'] == 'California Audiovisual Preservation Project (CAVPP)':
            exten = pbcoreExtension(exElement="projectNote",
                                    exValue='California Audiovisual Preservation Project',
                                    exAuthority='CAVPP')
        else:  # I don't know if this will be anything other than "California Audiovisual Preservation Project"
            exten = pbcoreExtension(exElement="projectNote",
                                    exValue=record['Project Note'])
        new_XML_file.add_extensions(exten)

# Relationship
    relation_type = ''
    if record['Relationship Type']:
        relation_type = record['Relationship Type']

    for part in record['Object Identifier'].split(';'):
        newRelation = pbcoreRelation(reID=part.strip(), reType=relation_type.strip())
        descritive.add_pbcoreRelation(newRelation)

        # TODO add Relationship to PBCore object
        XML += '\t<Relationship>' + record['Relationship'] + '</Relationship>\n'

    if record['Relationship Type']:
        # TODO add Relationship Type to PBCore object
        XML += '\t<RelationshipType>' + record['Relationship Type'] + '</RelationshipType>\n'

    new_XML_file.set_IntellectualContent(descritive)
    return new_XML_file.xmlString()

def validate_col_titles(f):
    mismatched = []
    valid = True
    for index, heading in enumerate(csv.reader(f).next()):
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