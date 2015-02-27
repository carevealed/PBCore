import os
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
                          collectionTitle=record['Collection Guide Title'])


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
    parts = record['Object Identifier'].split(';')



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


    if record['Institution']:
        inst_name = record['Institution']

    if record['Institution URL']:
        inst_URL = record['Institution URL']







    descritive = pbcoreDescriptionDocument(parentObjectID=obj_ID,
                                           projectID=proj_ID,
                                           assetType=asset_type,
                                           mainTitle=main_title,
                                           addTitle=add_title,
                                           seriesTitle=ser_title,
                                           institutionName=inst_name,
                                           institutionURL=inst_URL)

    if record['Institution ARK']:
        inst_ARK = record['Institution ARK']
        descritive.add_pbcoreIdentifier(PB_Element(['source', 'CDL'], ['annotation', 'Institution ARK'], tag='pbcoreIdentifier', value=inst_ARK))

    if record['Object ARK']:
        obj_ARK = record['Object ARK']
        descritive.add_pbcoreIdentifier(PB_Element(['source', 'CDL'], ['annotation', 'Object ARK'], tag='pbcoreIdentifier', value=obj_ARK))


    if record['Description or Content Summary']:
        descriptions = record['Description or Content Summary'].split(";")
        for description in descriptions:
            descritive.add_pbcoreDescription(PB_Element(tag="pbcoreDescription", value=description.strip()))


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
                descritive.add_pbcoreSubject(PB_Element(['source', subjectTopicAuthority], ['subjectType', 'Topic'], tag="pbcoreSubject", value=subjectTopic.strip()))
            else:
                descritive.add_pbcoreSubject(PB_Element(['source', "Library of Congress Subject Headings"], ['subjectType', 'Topic'], tag="pbcoreSubject", value=subjectTopic.strip()))

    if record['Subject Entity']:
        subjectEnts = record['Subject Entity']
        subjectEntities = subjectEnts.split(';')
        subjectEntityAuthority = record['Subject Entity Authority Source']

        for subjectEntity in subjectEntities:
            if subjectEntityAuthority and subjectEntityAuthority != "":
                descritive.add_pbcoreSubject(PB_Element(['source', subjectEntityAuthority], ['subjectType', 'Entity'], tag="pbcoreSubject", value=subjectEntity.strip()))
            else:
                descritive.add_pbcoreSubject(PB_Element(['subjectType', 'Entity'], tag="pbcoreSubject", value=subjectEntity.strip()))

    if record['Spatial Coverage']:
        spatCoverages = record['Spatial Coverage']
        spatialCoverages = spatCoverages.split(';')
        for spatialCoverage in spatialCoverages:
            descritive.add_pbcoreCoverage(pbcoreCoverage(covItem=spatialCoverage, covType="Spatial"))

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
                descritive.add_pbcoreGenre(PB_Element(['source', genreAuthoity], tag="pbcoreGenre", value=genre.strip()))
            else:
                descritive.add_pbcoreGenre(PB_Element(tag="pbcoreGenre", value=genre.strip()))

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
        notes = record['Additional Descriptive Notes for Overall Work']
        descritive.add_pbcoreDescription(PB_Element(['descriptionType', 'Additional Descriptive Notes for Overall Work'], tag='pbcoreDescription', value=notes.strip()))

    if record['Transcript']:
        transcript = record['Transcript']
        descritive.add_pbcoreDescription(PB_Element(['descriptionType', 'Transcript'], tag='pbcoreDescription', value=transcript))


# Descriptive Creator: Producer,Director,Writer,Interviewer,Performer

    producers = ""
    directors = ""
    writers = ""
    interviewers = ""
    performers = ""

    if record['Producer']:
        producers = record['Producer'].split(";")
        for producer in producers:
            creator = pbcoreCreator(name=producer.strip(), role="Producer")
            descritive.add_pbcoreCreator(creator)

    if record['Director']:
        directors = record['Director'].split(";")
        for director in directors:
            creator = pbcoreCreator(name=director.strip(), role="Director")
            descritive.add_pbcoreCreator(creator)

    if record['Writer']:
        writers = record['Writer'].split(";")
        for writer in writers:
            creator = pbcoreCreator(name=writer.strip(), role="Writer")
            descritive.add_pbcoreCreator(creator)

    if record['Interviewer']:
        interviewers = record['Interviewer'].split(";")
        for interviewer in interviewers:
            creator = pbcoreCreator(name=interviewer.strip(), role="Interviewer")
            descritive.add_pbcoreCreator(creator)

    if record['Performer']:
        performers = record['Performer'].split(";")
        for performer in performers:
            creator = pbcoreCreator(name=performer.strip(), role="Performer")
            descritive.add_pbcoreCreator(creator)


# Descriptive Contributor: Camera,Editor,Sound,Music,Cast,Interviewee,Speaker,Musician

    # cameras = ""
    # editors = ""
    # sounds = ""
    # musics = ""
    # cast_members = ""
    # interviewees = ""
    # speakers = ""
    # musicians = ""

    if record['Camera']:
        cameras = record['Camera'].split(';')
        for camera in cameras:
            contributor = pbcoreContributor(name=camera.strip(), role="Camera")
            descritive.add_pbcoreContributor(contributor)

    if record['Editor']:
        editors = record['Editor'].split(';')
        for editor in editors:
            contributor = pbcoreContributor(name=editor.strip(), role="Editor")
            descritive.add_pbcoreContributor(contributor)

    if record['Sound']:
        sounds = record['Sound'].split(';')
        for sound in sounds:
            contributor = pbcoreContributor(name=sound.strip(), role="Sound")
            descritive.add_pbcoreContributor(contributor)

    if record['Music']:
        musics = record['Music'].split(';')
        for music in musics:
            contributor = pbcoreContributor(name=music.strip(), role="Music")
            descritive.add_pbcoreContributor(contributor)

    if record['Cast']:
        cast_members = record['Cast'].split(';')
        for cast in cast_members:
            contributor = pbcoreContributor(name=cast.strip(), role="Cast")
            descritive.add_pbcoreContributor(contributor)

    if record['Interviewee']:
        interviewees = record['Interviewee'].split(';')
        for interviewee in interviewees:
            contributor = pbcoreContributor(name=interviewee.strip(), role="Interviewee")
            descritive.add_pbcoreContributor(contributor)

    if record['Speaker']:
        speakers = record['Speaker'].split(';')
        for speaker in speakers:
            contributor = pbcoreContributor(name=speaker.strip(), role="Speaker")
            descritive.add_pbcoreContributor(contributor)

    if record['Musician']:
        musicians = record['Musician'].split(';')
        for musician in musicians:
            contributor = pbcoreContributor(name=musician.strip(), role="Musician")
            descritive.add_pbcoreContributor(contributor)


# Descriptive Publisher: Publisher,Distributor
#     publisher = ""
#     distributor = ""

    if record['Publisher']:
        publisher = record['Publisher']
        publish = pbcorePublisher(name=publisher, role="Publisher")
        descritive.add_pbcorePublisher(publish)

    if record['Distributor']:
        distributor = record['Distributor']
        publish = pbcorePublisher(name=distributor, role="Distributor")
        descritive.add_pbcorePublisher(publish)


# Descriptive Rights
#     copyright_statement = ""
#     copyright_holder = ""
#     copyright_holder_info = ""
#     copyright_dates = []
#     copyright_notice = ""
#     institutional_rights_statement_URL = ""

    if record['Copyright Statement']:
        rights = pbcoreRightsSummary(copyright_statement=record['Copyright Statement'].strip())
        descritive.add_pbcoreRightsSummary(rights)

    if record['Copyright Holder']:
        rights = pbcoreRightsSummary(copyright_holder=record['Copyright Holder'].strip())
        descritive.add_pbcoreRightsSummary(rights)

    if record['Copyright Holder Info']:
        rights = pbcoreRightsSummary(copyright_holder_info=record['Copyright Holder Info'])
        descritive.add_pbcoreRightsSummary(rights)

    if record['Copyright Date']:
        copyright_dates = re.split('; |,|and', record['Copyright Date'])
        for copyright_date in copyright_dates:
            rights = pbcoreRightsSummary()
            rights.set_rightsSummary(PB_Element(['annotation', 'Copyright Date'], tag="rightsSummary", value=copyright_date.strip()))
            descritive.add_pbcoreRightsSummary(rights)

    if record['Copyright Notice']:
        rights = pbcoreRightsSummary()
        copyright_notice = record['Copyright Notice']
        rights.set_rightsSummary(PB_Element(['annotation', 'Copyright Notice'], tag="rightsSummary", value=copyright_notice.strip()))
        descritive.add_pbcoreRightsSummary(rights)

    if record['Institutional Rights Statement (URL)']:
        rights = pbcoreRightsSummary()
        institutional_rights_statement_URL = record['Institutional Rights Statement (URL)']
        rights.set_rightsSummary(PB_Element(['annotation', 'Institutional Rights Statement (URL)'], tag="rightsSummary", value=institutional_rights_statement_URL.strip()))
        descritive.add_pbcoreRightsSummary(rights)

# PARTS
    call_numbers = ""
    if record['Call Number']:
        call_numbers = record['Call Number'].split(';')

# PBcore Parts
    for part in parts:
        newPart = CAVPP_Part(objectID=part.strip(),
                             mainTitle=main_title.strip(),
                             description=descrp.strip())
        for call_number in call_numbers:
            newPart.add_pbcoreIdentifier(PB_Element(['source', inst_name], ['annotation', 'Call Number'], tag='pbcoreIdentifier', value=call_number.strip()))
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
        aspect_ratio = ""
        track_standard = ""
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
            aspect_ratio = record['Aspect Ratio']

        if record['Track Standard']:
            track_standard = record['Track Standard']

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
                                       baseType=base_type,
                                       baseThickness=bass_thickness,
                                       stockManufacture=stock,
                                       location=inst_name)

        for date in creationDates:
            physical.add_instantiationDate(PB_Element(tag='instantiationDate', value=date))

        if record['Additional Technical Notes for Overall Work']:
            note = record['Additional Technical Notes for Overall Work']
            physical.add_instantiationAnnotation(PB_Element(['annotationType', 'Additional Technical Notes for Overall'], tag="instantiationAnnotation", value=note.strip()))

        if record['Cataloger Notes']:
            note = record['Cataloger Notes']
            physical.add_instantiationAnnotation(PB_Element(['annotationType', 'Cataloger Notes'], tag="instantiationAnnotation", value=note.strip()))

        # FIXME: add subtitles to script
        if record['Subtitles/Intertitles/Closed Captions']:
            subtitles = record['Subtitles/Intertitles/Closed Captions'].split(';')
            for subtitle in subtitles:
                physical.get_instantiationAlternativeModes()

# instantiationPart
        if media_type.lower() == 'audio' or media_type.lower() == 'sound':
            speed = record['Running Speed']
            newInstPart = InstantiationPart(objectID=part)
            newEss = InstantiationEssenceTrack(objectID=part, type="Audio", ips=speed, standard=track_standard)
            newInstPart.add_instantiationEssenceTrack(newEss)
            physical.add_instantiationPart(newInstPart)

        elif media_type.lower() == 'moving image':
            newEss = InstantiationEssenceTrack(objectID=part, frameRate=run_speed, aspectRatio=aspect_ratio, standard=track_standard)
            physical.add_instantiationEssenceTrack(newEss)


        newPart.add_pbcoreInstantiation(physical)

# <!--Preservation Master-->
        pres_master = pbcoreInstantiation(type="Preservation Master",
                                          location="CAVPP",
                                          objectID=(part.strip()+"_prsv"))
        if record['Quality Control Notes']:
            note = record['Quality Control Notes']
            pres_master.add_instantiationAnnotation(PB_Element(['annotationType', 'CAVPP Quality Control/Partner Quality Control'], tag="instantiationAnnotation", value=note.strip()))

        newPart.add_pbcoreInstantiation(pres_master)

# access copy
        access_copy = pbcoreInstantiation(type="Access Copy",
                                          location="CAVPP",
                                          objectID=(part.strip()+"_access"))
        newPart.add_pbcoreInstantiation(access_copy)

        descritive.add_pbcore_part(newPart)

# Extension
    if record['Country of Creation']:
        exten = pbcoreExtension(exElement="countryOfCreation",
                                exValue=record['Country of Creation'],
                                exAuthority="ISO 3166.1")
        descritive.add_pbcore_extension(exten)

    if record['Project Note']:
        if record['Project Note'] == 'California Audiovisual Preservation Project (CAVPP)':
            exten = pbcoreExtension(exElement="projectNote",
                                    exValue='California Audiovisual Preservation Project',
                                    exAuthority='CAVPP')
        else:  # I don't know if this will be anything other than "California Audiovisual Preservation Project"
            exten = pbcoreExtension(exElement="projectNote",
                                    exValue=record['Project Note'])
        descritive.add_pbcore_extension(exten)

# Relationship
#     relation_type = ''
#     if record['Relationship Type']:
#         relation_type = record['Relationship Type']
#
#         newRelation = pbcoreRelation(reID=part.strip(), reType=relation_type.strip())
#         descritive.add_pbcoreRelation(newRelation)
    if len(parts) > 1:
        for part in record['Object Identifier'].split(';'):
            newRelation = pbcoreRelation(reID=part.strip(), reType="Has Part")
            descritive.add_pbcoreRelation(newRelation)


    new_XML_file.set_IntellectualContent(descritive)


    return new_XML_file.xmlString()

def validate_col_titles(f):
    mismatched = []
    valid = True
    for index, heading in enumerate(csv.reader(f).next()):
        if heading != officialList[index]:
            valid = False
            mismatched.append("CSV title mismatch. At column "
                              + str(index+1)
                              + ", recived: ["
                              + heading
                              + "]. Expected: ["
                              + officialList[index]
                              + "]")

    f.seek(0)
    return valid, mismatched


def locate_files(root, fileName):
    # search for file with fileName in it recursively
    found_directory = None
    results = []
    # check if a directory matches the file name
    for roots, dirs, files in os.walk(os.path.dirname(root)):
        for dir in dirs:
            if fileName == dir:
                found_directory = os.path.join(roots, dir)
                break
    # see of a file in that folder has a file with that name in it
    if found_directory:
        for roots, dirs, files, in os.walk(found_directory):
            for file in files:
                if fileName in file:
                    results.append(os.path.join(roots, file))
    return results

def main():
    # ----------Setting up the logs----------
    mode = "normal"
    records = []

    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="Source CSV file", type=str)
    parser.add_argument("-d", "--debug", help="Debug mode. Writes all messages to debug log.", action='store_true')
    # TODO: add argument that lets you create pbcore without the files present
    args = parser.parse_args()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if not os.path.exists('logs'):              # automatically create a logs folder if one doesn't already exist
        os.makedirs('logs')

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

    error_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')     # DATE - USERNAME - Message
    stderr_formatter = logging.Formatter('%(levelname)s - %(message)s')                             # USERNAME - Message
    stdout_formatter = logging.Formatter('%(message)s')                                             # Message

    fh.setFormatter(error_formatter)
    eh.setFormatter(stderr_formatter)
    ch.setFormatter(stdout_formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    logger.addHandler(eh)

# ----------Validation of CSV file----------

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
        for item in csv.DictReader(f): # reason: because you can only iterate over a DictReader once
            records.append(item)
    except ValueError:
        print "FAILED"
        logger.critical("Error, cannot load file as a CSV.")
        print "Quitting"
        quit()

    # ---------- Locate all files mentioned in CSV ----------

    logger.debug("Locating files")
    file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
    files_not_found = []
    for record in records:
        fileName = re.search(file_name_pattern, record['Object Identifier']).group(0)
        logging.debug("Locating possible files for: " + fileName)
        if not locate_files(args.csv, fileName):
            files_not_found.append(fileName)
        else:
            logging.debug("Files located for: " + fileName)
    if files_not_found:
        logger.error("Could not find files for the following records. Makes sure the directory containing the media objects " \
              "is located in the same directory as the csv file. ")
        for file_not_found in files_not_found:
            logging.error(file_not_found)
        print "quiting"
        quit()


    # ---------- Genereate PBCore XML Files ----------
    logging.info("Generating PBCore stubs...")
    number_of_records = 0
    number_of_new_records = 0
    number_of_rewritten_records = 0

    for record in records:
        fileName = re.search(file_name_pattern, record['Object Identifier']).group(0)
        logger.info("Producing PBCore XML for " + fileName)
        if isfile(fileName + ".xml"):
            logger.warning(str(record['Project Identifier'])+".xml is already a file, overwriting.")
            number_of_rewritten_records += 1
        else:
            number_of_new_records += 1

        # I'm sending this into miniDOM because I can't get etree to print a pretty XML
        buf = parseString(generate_pbcore(record))
        output_file = open(fileName +".xml", 'w')
        output_file.write(buf.toprettyxml(encoding='utf-8'))
        output_file.close()
        number_of_records += 1

    logger.debug("Closing CSV file:")
    f.close()
    message = "Generated " + str(number_of_records) + " records in total."
    if number_of_new_records >= 1:
        message += " New records: " + str(number_of_new_records) + "."

    if number_of_rewritten_records >= 1:
        message += " Records overwritten: " + str(number_of_rewritten_records) + "."

    logger.info(message)
    print "Done"

if __name__ == '__main__':
    main()