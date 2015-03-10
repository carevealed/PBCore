import os
import sys
import logging
import argparse
from ConfigParser import ConfigParser
from onesheet.VideoObject import *
from onesheet.AudioObject import *
import string
from time import sleep
from os.path import isfile
from xml.dom.minidom import parseString
from xml.etree import ElementTree
import re
from modules.PBCore.PBCore import *


LARGEFILE = 1065832230
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

def sizeofHuman(num):
        num = int(num)
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x), x
            num /= 1024.0
def build_descriptive(record):
    obj_ID = ''
    proj_ID = ''
    asset_type = ''
    main_title = ''
    add_title = ''
    ser_title = ''
    inst_name = ''
    inst_URL = ''
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

    descriptive = pbcoreDescriptionDocument(parentObjectID=obj_ID,
                                            projectID=proj_ID,
                                            assetType=asset_type,
                                            mainTitle=main_title,
                                            addTitle=add_title,
                                            seriesTitle=ser_title,
                                            institutionName=inst_name,
                                            institutionURL=inst_URL)

    if record['Institution ARK']:
        inst_ARK = record['Institution ARK']
        descriptive.add_pbcoreIdentifier(
            PB_Element(['source', 'CDL'], ['annotation', 'Institution ARK'], tag='pbcoreIdentifier', value=inst_ARK))

    if record['Object ARK']:
        obj_ARK = record['Object ARK']
        descriptive.add_pbcoreIdentifier(
            PB_Element(['source', 'CDL'], ['annotation', 'Object ARK'], tag='pbcoreIdentifier', value=obj_ARK))

    if record['Description or Content Summary']:
        description = record['Description or Content Summary']
        descriptive.add_pbcoreDescription(PB_Element(tag="pbcoreDescription", value=description.strip()))

    if record['Internet Archive URL']:
        IA_URL = record['Internet Archive URL']
        descriptive.add_pbcoreIdentifier(
            PB_Element(['source', 'CAVPP'], ['annotation', 'Internet Archive URL'], tag='pbcoreIdentifier',
                       value=IA_URL))

    if record['Subject Topic']:
        subjectTops = record['Subject Topic']
        subjectTopics = subjectTops.split(';')
        subjectTopicAuthority = record['Subject Topic Authority Source']

        for subjectTopic in subjectTopics:
            # Unless another subject authority is specified, the source will default to the LOC subject headings
            if subjectTopicAuthority and subjectTopicAuthority != "":
                descriptive.add_pbcoreSubject(
                    PB_Element(['source', subjectTopicAuthority], ['subjectType', 'Topic'], tag="pbcoreSubject",
                               value=subjectTopic.strip()))
            else:
                descriptive.add_pbcoreSubject(
                    PB_Element(['source', "Library of Congress Subject Headings"], ['subjectType', 'Topic'],
                               tag="pbcoreSubject", value=subjectTopic.strip()))

    if record['Subject Entity']:
        subjectEnts = record['Subject Entity']
        subjectEntities = subjectEnts.split(';')
        subjectEntityAuthority = record['Subject Entity Authority Source']

        for subjectEntity in subjectEntities:
            if subjectEntityAuthority and subjectEntityAuthority != "":
                descriptive.add_pbcoreSubject(
                    PB_Element(['source', subjectEntityAuthority], ['subjectType', 'Entity'], tag="pbcoreSubject",
                               value=subjectEntity.strip()))
            else:
                descriptive.add_pbcoreSubject(
                    PB_Element(['subjectType', 'Entity'], tag="pbcoreSubject", value=subjectEntity.strip()))

    if record['Spatial Coverage']:
        spatCoverages = record['Spatial Coverage']
        spatialCoverages = spatCoverages.split(';')
        for spatialCoverage in spatialCoverages:
            descriptive.add_pbcoreCoverage(pbcoreCoverage(covItem=spatialCoverage, covType="Spatial"))

    if record['Temporal Coverage']:
        tempCoverages = record['Temporal Coverage']
        temporalCoverages = tempCoverages.split(';')
        for temporalCoverage in temporalCoverages:
            descriptive.add_pbcoreCoverage(pbcoreCoverage(covItem=temporalCoverage, covType="Temporal"))

    if record['Genre']:
        genres_data = record['Genre']
        genres = genres_data.split(';')
        genreAuthoity = record['Genre Authority Source']
        for genre in genres:
            if genreAuthoity and genreAuthoity != "":
                descriptive.add_pbcoreGenre(
                    PB_Element(['source', genreAuthoity], tag="pbcoreGenre", value=genre.strip()))
            else:
                descriptive.add_pbcoreGenre(PB_Element(tag="pbcoreGenre", value=genre.strip()))

    if record['Date Created']:
        creation = record['Date Created']
        creationDates = creation.split(';')
        for creationDate in creationDates:
            descriptive.add_pbcoreAssetDate(
                PB_Element(['dateType', 'created'], tag="pbcoreAssetDate", value=creationDate.strip()))

    if record['Date Published']:
        published = record['Date Published']
        publishedDates = published.split(';')
        for publishedDate in publishedDates:
            descriptive.add_pbcoreAssetDate(
                PB_Element(['dateType', 'published'], tag="pbcoreAssetDate", value=publishedDate.strip()))

    if record['Additional Descriptive Notes for Overall Work']:
        notes = record['Additional Descriptive Notes for Overall Work']
        descriptive.add_pbcoreDescription(
            PB_Element(['descriptionType', 'Additional Descriptive Notes for Overall Work'], tag='pbcoreDescription',
                       value=notes.strip()))

    if record['Transcript']:
        transcript = record['Transcript']
        descriptive.add_pbcoreDescription(
            PB_Element(['descriptionType', 'Transcript'], tag='pbcoreDescription', value=transcript))


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
            descriptive.add_pbcoreCreator(creator)

    if record['Director']:
        directors = record['Director'].split(";")
        for director in directors:
            creator = pbcoreCreator(name=director.strip(), role="Director")
            descriptive.add_pbcoreCreator(creator)

    if record['Writer']:
        writers = record['Writer'].split(";")
        for writer in writers:
            creator = pbcoreCreator(name=writer.strip(), role="Writer")
            descriptive.add_pbcoreCreator(creator)

    if record['Interviewer']:
        interviewers = record['Interviewer'].split(";")
        for interviewer in interviewers:
            creator = pbcoreCreator(name=interviewer.strip(), role="Interviewer")
            descriptive.add_pbcoreCreator(creator)

    if record['Performer']:
        performers = record['Performer'].split(";")
        for performer in performers:
            creator = pbcoreCreator(name=performer.strip(), role="Performer")
            descriptive.add_pbcoreCreator(creator)


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
            descriptive.add_pbcoreContributor(contributor)

    if record['Editor']:
        editors = record['Editor'].split(';')
        for editor in editors:
            contributor = pbcoreContributor(name=editor.strip(), role="Editor")
            descriptive.add_pbcoreContributor(contributor)

    if record['Sound']:
        sounds = record['Sound'].split(';')
        for sound in sounds:
            contributor = pbcoreContributor(name=sound.strip(), role="Sound")
            descriptive.add_pbcoreContributor(contributor)

    if record['Music']:
        musics = record['Music'].split(';')
        for music in musics:
            contributor = pbcoreContributor(name=music.strip(), role="Music")
            descriptive.add_pbcoreContributor(contributor)

    if record['Cast']:
        cast_members = record['Cast'].split(';')
        for cast in cast_members:
            contributor = pbcoreContributor(name=cast.strip(), role="Cast")
            descriptive.add_pbcoreContributor(contributor)

    if record['Interviewee']:
        interviewees = record['Interviewee'].split(';')
        for interviewee in interviewees:
            contributor = pbcoreContributor(name=interviewee.strip(), role="Interviewee")
            descriptive.add_pbcoreContributor(contributor)

    if record['Speaker']:
        speakers = record['Speaker'].split(';')
        for speaker in speakers:
            contributor = pbcoreContributor(name=speaker.strip(), role="Speaker")
            descriptive.add_pbcoreContributor(contributor)

    if record['Musician']:
        musicians = record['Musician'].split(';')
        for musician in musicians:
            contributor = pbcoreContributor(name=musician.strip(), role="Musician")
            descriptive.add_pbcoreContributor(contributor)


        # Descriptive Publisher: Publisher,Distributor
        # publisher = ""
        #     distributor = ""

    if record['Publisher']:
        publisher = record['Publisher']
        publish = pbcorePublisher(name=publisher, role="Publisher")
        descriptive.add_pbcorePublisher(publish)

    if record['Distributor']:
        distributor = record['Distributor']
        publish = pbcorePublisher(name=distributor, role="Distributor")
        descriptive.add_pbcorePublisher(publish)


    # Descriptive Rights
    # copyright_statement = ""
    #     copyright_holder = ""
    #     copyright_holder_info = ""
    #     copyright_dates = []
    #     copyright_notice = ""
    #     institutional_rights_statement_URL = ""

    if record['Copyright Statement']:
        rights = pbcoreRightsSummary(copyright_statement=record['Copyright Statement'].strip())
        descriptive.add_pbcoreRightsSummary(rights)

    if record['Copyright Holder']:
        rights = pbcoreRightsSummary(copyright_holder=record['Copyright Holder'].strip())
        descriptive.add_pbcoreRightsSummary(rights)

    if record['Copyright Holder Info']:
        rights = pbcoreRightsSummary(copyright_holder_info=record['Copyright Holder Info'])
        descriptive.add_pbcoreRightsSummary(rights)

    if record['Copyright Date']:
        copyright_dates = re.split('; |,|and', record['Copyright Date'])
        for copyright_date in copyright_dates:
            rights = pbcoreRightsSummary()
            rights.set_rightsSummary(
                PB_Element(['annotation', 'Copyright Date'], tag="rightsSummary", value=copyright_date.strip()))
            descriptive.add_pbcoreRightsSummary(rights)

    if record['Copyright Notice']:
        rights = pbcoreRightsSummary()
        copyright_notice = record['Copyright Notice']
        rights.set_rightsSummary(
            PB_Element(['annotation', 'Copyright Notice'], tag="rightsSummary", value=copyright_notice.strip()))
        descriptive.add_pbcoreRightsSummary(rights)

    if record['Institutional Rights Statement (URL)']:
        rights = pbcoreRightsSummary()
        institutional_rights_statement_URL = record['Institutional Rights Statement (URL)']
        rights.set_rightsSummary(PB_Element(['annotation', 'Institutional Rights Statement (URL)'], tag="rightsSummary",
                                            value=institutional_rights_statement_URL.strip()))
        descriptive.add_pbcoreRightsSummary(rights)

    return descriptive


def build_physical(new_part, record):
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
    creationDates = []
    inst_name = ""
    part = new_part
    if record['Institution']:
        inst_name = record['Institution']
    if record['Date Created']:
        creation = record['Date Created']
        creationDates = creation.split(';')
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
        physical.add_instantiationAnnotation(
            PB_Element(['annotationType', 'Additional Technical Notes for Overall'], tag="instantiationAnnotation",
                       value=note.strip()))
    if record['Cataloger Notes']:
        note = record['Cataloger Notes']
        physical.add_instantiationAnnotation(
            PB_Element(['annotationType', 'Cataloger Notes'], tag="instantiationAnnotation", value=note.strip()))

    # FIXME: add subtitles to script
    if record['Subtitles/Intertitles/Closed Captions']:
        subtitles = record['Subtitles/Intertitles/Closed Captions'].split(';')
        for subtitle in subtitles:
            physical.get_instantiationAlternativeModes()

            # instantiationPart
    if media_type.lower() == 'audio' or media_type.lower() == 'sound':
        speed = record['Running Speed']
        newInstPart = InstantiationPart(objectID=part, location=inst_name)
        newEss = InstantiationEssenceTrack(type="Audio", ips=speed, standard=track_standard)
        newInstPart.add_instantiationEssenceTrack(newEss)
        physical.add_instantiationPart(newInstPart)

    elif media_type.lower() == 'moving image':
        newEss = InstantiationEssenceTrack(objectID=part,
                                           frameRate=run_speed,
                                           aspectRatio=aspect_ratio,
                                           standard=track_standard)
        physical.add_instantiationEssenceTrack(newEss)
    # return inst_name, physical
    return physical


def build_preservation_master(record, preservation_file_set):

# for preservation_file_set in preservation_file_sets:
    lang = ''
    media_type = ''
    obj_ID = ''
    if record['Object Identifier']:
        obj_ID = record['Object Identifier'].split(';')[0].split('_t')[0]

    if record['Language']:
        lang = record['Language']

    if record['Media Type']:
        media_type = record['Media Type']
    pres_master = pbcoreInstantiation(type="Preservation Master",
                                      location=SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource'),
                                      generations="Preservation Master",
                                      language=lang)

    # ============================================================ #
    # ======================== Audio only ======================== #
    # ============================================================ #
    if media_type.lower() == 'audio' or media_type.lower() == 'sound':
        pres_master.add_instantiationIdentifier(PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                           tag="instantiationIdentifier",
                                                           value=obj_ID+"_prsv"))
        pres_master.set_instantiationMediaType(PB_Element(tag='instantiationMediaType',
                                                          value='Sound'))
        pres_master.add_instantiationRelation(InstantiationRelation(derived_from=obj_ID))
        for master_part in preservation_file_set:
            f = AudioObject(master_part)
            new_mast_part = InstantiationPart(location=SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource'), duration=f.totalRunningTimeSMPTE)
            file_size, file_units = sizeofHuman(f.file_size)
            new_mast_part.set_instantiationFileSize(PB_Element(['unitsOfMeasure',file_units],
                                                               tag="instantiationFileSize",
                                                               value=str(file_size)))
            new_mast_part.add_instantiationIdentifier(PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                                 ['annotation', 'File Name'],
                                                                 tag="instantiationIdentifier",
                                                                 value=os.path.basename(master_part)))
            if not args.nochecksum and SETTINGS.getboolean('CHECKSUM','CalculateChecksums') is True:
                print("\t"),
                logger.info("Calculating MD5 checksum for " + f.file_name + ".")
                if f.file_size > LARGEFILE:
                    print "\tNote: " + f.file_name + " is " + f.file_size_human + " and might take some times to calculate."

                if args.noprogress or SETTINGS.getboolean('CHECKSUM','DisplayProgress') is False:
                    md5 = f.calculate_MD5()
                else:
                    md5 = f.calculate_MD5(progress=True)
                new_mast_part.add_instantiationIdentifier(PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                                     ['version', 'MD5'],
                                                                     ['annotation', 'checksum'],
                                                                     tag="instantiationIdentifier",
                                                                     value=md5))
            newfile = InstantiationEssenceTrack(type="Audio")
            newfile.set_essenceTrackBitDepth(PB_Element(tag="essenceTrackBitDepth",
                                                        value=str(f.audioBitDepth)))
            newfile.set_essenceTrackSamplingRate(PB_Element(["unitsOfMeasure", "kHz"],
                                                            tag="essenceTrackSamplingRate",
                                                            value=str(f.audioSampleRate/1000)))
            if f.file_extension.lower() == '.wav':
                pres_master.set_instantiationDigital(PB_Element(['source', 'PRONOM Technical Registry'],
                                                                tag='instantiationDigital',
                                                                value='audio/x-wav'))  # This is really ugly code I don't know a better way
                if f.audioCodec == 'PCM 24-bit':
                    pres_master.set_instantiationStandard(PB_Element(tag='instantiationStandard',
                                                                     value='Linear PCM Audio')) # This is really ugly code I don't know a better way

                newfile.set_essenceTrackEncoding(PB_Element(tag='essenceTrackEncoding', value='WAV'))
            new_mast_part.add_instantiationEssenceTrack(newfile)

            pres_master.add_instantiationPart(new_mast_part)
        # f = AudioObject(preservation_file_set)0
        #
        pass

    # ============================================================ #
    # ======================= Moving Image ======================= #
    # ============================================================ #
    elif media_type.lower() == 'moving image':
        f = VideoObject(preservation_file_set[0])
        pres_master.set_instantiationMediaType(PB_Element(tag='instantiationMediaType', value='Moving Image'))
        pres_master.add_instantiationIdentifier(PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                           ['annotation', 'File Name'],
                                                           tag="instantiationIdentifier",
                                                           value=os.path.basename(preservation_file_set[0])))

        file_size, file_units = sizeofHuman(f.file_size)
        pres_master.set_instantiationFileSize(PB_Element(['unitsOfMeasure', file_units],
                                                         tag="instantiationFileSize",
                                                         value=str(file_size)))

        if not args.nochecksum and SETTINGS.getboolean('CHECKSUM','CalculateChecksums') is True:
            print("\t"),
            logger.info("Calculating MD5 checksum for " + f.file_name + ".")
            if f.file_size > LARGEFILE:
                print "\tNote: This file is " + f.file_size_human + " and might take some times to calculate."

            if args.noprogress or SETTINGS.getboolean('CHECKSUM','DisplayProgress') is False:
                md5 = f.calculate_MD5()
            else:
                md5 = f.calculate_MD5(progress=True)
            pres_master.add_instantiationIdentifier(PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                               ['version', 'MD5'],
                                                               ['annotation', 'checksum'],
                                                               tag="instantiationIdentifier",
                                                               value=md5))

        # ---------- Video essence track ----------
        newfile = InstantiationEssenceTrack(type='Video',
                                            frameRate=str(f.videoFrameRate),
                                            duration=f.totalRunningTimeSMPTE,
                                            aspectRatio=str(f.videoAspectRatio))
        newfile.add_essenceTrackAnnotation(PB_Element(['annotationType', 'Frame Size Vertical'],
                                                      tag="essenceTrackAnnotation",
                                                      value=f.videoResolutionHeight))
        newfile.add_essenceTrackAnnotation(PB_Element(['annotationType', 'Frame Size Horizontal'],
                                                      tag="essenceTrackAnnotation",
                                                      value=f.videoResolutionWidth))
        pres_master.add_instantiationEssenceTrack(newfile)

        # ---------- Audio essence track ----------

        newfile = InstantiationEssenceTrack(type='Audio',
                                            samplingRate=f.audioSampleRate/1000,
                                            bitDepth=f.audioBitDepth)

        pres_master.add_instantiationEssenceTrack(newfile)

        pass


    if record['Quality Control Notes']:
        note = record['Quality Control Notes']
        pres_master.add_instantiationAnnotation(
            PB_Element(['annotationType', 'CAVPP Quality Control/Partner Quality Control'],
                       tag="instantiationAnnotation",
                       value=note.strip()))
    return pres_master

def build_access_copy(record, access_files_sets):
    lang = ''
    obj_ID = ''
    if record['Language']:
        lang = record['Language']
    if record['Object Identifier']:
        obj_ID = record['Object Identifier'].split(';')[0].split('_t')[0]

    media_type = ''
    if record['Media Type']:
        media_type = record['Media Type']

    for access_files in access_files_sets:
        # print access_files_sets
        access_copy = pbcoreInstantiation(type="Access Copy",
                                          location=SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource'),
                                          language=lang,
                                          generations="Access Copy")

    # ============================================================ #
    # =========================== Audio ========================== #
    # ============================================================ #
        if media_type.lower() == 'audio' or media_type.lower() == 'sound':
            access_copy.add_instantiationIdentifier(
                PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                           tag="instantiationIdentifier",
                           value=obj_ID+"_access"))
            access_copy.add_instantiationRelation(InstantiationRelation(derived_from=obj_ID+"_prsv"))
            for access_file in access_files:
                f = AudioObject(access_file)
                newAudioFile = InstantiationPart(objectID=f.file_name,
                                                 location=SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource'),
                                                 duration=f.totalRunningTimeSMPTE)
                size, units = sizeofHuman(f.file_size)
                newAudioFile.set_instantiationFileSize(PB_Element(['unitsOfMeasure', units],
                                                                  tag="instantiationFileSize",
                                                                  value=size))
                if not args.nochecksum and SETTINGS.getboolean('CHECKSUM','CalculateChecksums') is True:
                    print("\t"),
                    logger.info("Calculating MD5 checksum for " + f.file_name + ".")
                    if f.file_size > LARGEFILE:
                        print "\tNote: This file is " + f.file_size_human + " and might take some times to calculate."
                    if args.noprogress or SETTINGS.getboolean('CHECKSUM','DisplayProgress') is False:
                        md5 = f.calculate_MD5()
                    else:
                        md5 = f.calculate_MD5(progress=True)
                    newAudioFile.add_instantiationIdentifier(
                        PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                   ['version', 'MD5'],
                                   ['annotation', 'checksum'],
                                   tag="instantiationIdentifier",
                                   value=md5))
                if f.audioChannels == 1:
                    access_copy.set_instantiationTracks(PB_Element(tag="instantiationTracks", value='Sound'))
                    access_copy.set_instantiationChannelConfiguration(PB_Element(tag="instantiationChannelConfiguration",
                                                                                 value='Mono'))
                elif f.audioChannels == 2:
                    access_copy.set_instantiationTracks(PB_Element(tag="instantiationTracks", value='Sound'))
                    access_copy.set_instantiationChannelConfiguration(PB_Element(tag="instantiationChannelConfiguration",
                                                                                 value='Stereo'))
                newEssTrack = InstantiationEssenceTrack(type="Audio", bitDepth=f.audioBitDepth)
                if f.file_extension.lower() == '.mp3':
                    newEssTrack.set_essenceTrackEncoding(PB_Element(tag='essenceTrackEncoding', value='MP3'))
                newAudioFile.add_instantiationEssenceTrack(newEssTrack)
                access_copy.add_instantiationPart(newAudioFile)

    # ============================================================ #
    # ======================= Moving Image ======================= #
    # ============================================================ #
        elif media_type.lower() == 'moving image':
            f = VideoObject(access_files)
            # print "audio", f.file_name
            access_copy.add_instantiationIdentifier(PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                               ['annotation', 'File Name'],
                                                               tag="instantiationIdentifier",
                                                               value=f.file_name))
            access_copy.set_instantiationMediaType(PB_Element(tag='instantiationMediaType', value='Moving Image'))
            access_copy.set_instantiationDuration(PB_Element(tag="instantiationDuration",
                                                             value=f.totalRunningTimeSMPTE))
            size, units = sizeofHuman(f.file_size)
            access_copy.set_instantiationFileSize(PB_Element(['unitsOfMeasure', units],
                                                             tag="instantiationFileSize",
                                                             value=size))
            if not args.nochecksum and SETTINGS.getboolean('CHECKSUM','CalculateChecksums') is True:
                print("\t"),
                logger.info("Calculating MD5 checksum for " + f.file_name + ".")
                if f.file_size > LARGEFILE:
                    print "\tNote: This file is " + f.file_size_human + " and might take some times to calculate."
                if args.noprogress or SETTINGS.getboolean('CHECKSUM','DisplayProgress') is False:
                    md5 = f.calculate_MD5()
                else:
                    md5 = f.calculate_MD5(progress=True)
                access_copy.add_instantiationIdentifier(
                    PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                               ['version', 'MD5'],
                               ['annotation', 'checksum'],
                               tag="instantiationIdentifier",
                               value=md5))
            if f.audioChannels == 1:
                access_copy.set_instantiationTracks(PB_Element(tag="instantiationTracks", value='Sound'))
                access_copy.set_instantiationChannelConfiguration(PB_Element(tag="instantiationChannelConfiguration",
                                                                             value='Mono'))
            elif f.audioChannels == 2:
                access_copy.set_instantiationTracks(PB_Element(tag="instantiationTracks", value='Sound'))
                access_copy.set_instantiationChannelConfiguration(PB_Element(tag="instantiationChannelConfiguration",
                                                                             value='Stereo'))

            # ------------------ video track ------------------
            newEssTrack = InstantiationEssenceTrack(type='Video',
                                                    frameRate=("%.2f" % f.videoFrameRate),
                                                    aspectRatio=str(f.videoAspectRatio),
                                                    duration=f.totalRunningTimeSMPTE)
            newEssTrack.add_essenceTrackAnnotation(PB_Element(['annotationType', 'Frame Size Vertical'],
                                                              tag="essenceTrackAnnotation",
                                                              value=f.videoResolutionHeight))
            newEssTrack.add_essenceTrackAnnotation(PB_Element(['annotationType', 'Frame Size Horizontal'],
                                                              tag="essenceTrackAnnotation",
                                                              value=f.videoResolutionWidth))
            access_copy.add_instantiationEssenceTrack(newEssTrack)

            # ------------------ Audio track ------------------
            newEssTrack = InstantiationEssenceTrack(type='Audio',
                                                    standard=f.audioCodec,
                                                    samplingRate=f.audioSampleRate/1000)

            access_copy.add_instantiationEssenceTrack(newEssTrack)
    return access_copy

def generate_pbcore(record, files=None):
    XML = ""
    new_XML_file = PBCore(collectionSource=record['Institution'],
                          collectionTitle=record['Collection Guide Title'])

    preservation_file_sets, access_files_sets = sep_pres_access(files)
    preservation_file_sets = group_sides(preservation_file_sets)
    access_files_sets = group_sides(access_files_sets)

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
    genre_autority = ""
    IA_URL = ""
    QC_notes_list = ""
    transcript = ""
    parts = record['Object Identifier'].split(';')

    # preservation, access = sep_pres_access()

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


    descriptive = build_descriptive(record)
    # PARTS
    call_numbers = ""
    if record['Call Number']:
        call_numbers = record['Call Number'].split(';')

# =================
# AUDIO ONLY
# =================


    if record['Media Type'].lower() == 'audio' or record['Media Type'].lower() == 'sound':
    # PBcore Parts
        for part in parts:
            newPart = CAVPP_Part(objectID=part.strip(),
                                 mainTitle=main_title.strip(),
                                 description=record['Description or Content Summary'])
            for call_number in call_numbers:
                newPart.add_pbcoreIdentifier(
                    PB_Element(['source', inst_name], ['annotation', 'Call Number'], tag='pbcoreIdentifier',
                               value=call_number.strip()))

    # -----------------------------------------------------
    #           physical
    # -----------------------------------------------------
            physical = build_physical(part, record)
            newPart.add_pbcoreInstantiation(physical)

    # -----------------------------------------------------
    #           Preservation Master
    # -----------------------------------------------------
            for preservation_file_set in preservation_file_sets:
                # print preservation_file_set
                pres_master = build_preservation_master(record, preservation_file_set)
                newPart.add_pbcoreInstantiation(pres_master)


    # -----------------------------------------------------
    #           access copy
    # -----------------------------------------------------
            access_copy = build_access_copy(record, access_files_sets)
            newPart.add_pbcoreInstantiation(access_copy)
        descriptive.add_pbcore_part(newPart)

# =================
# Moving Image ONLY
# =================

    elif record['Media Type'].lower() == 'moving image':
        # print "moving image"
        for index, part in enumerate(parts):
            newPart = CAVPP_Part(objectID=part.strip(),
                                 mainTitle=main_title.strip(),
                                 description=record['Description or Content Summary'])
            for call_number in call_numbers:
                newPart.add_pbcoreIdentifier(
                    PB_Element(['source', inst_name], ['annotation', 'Call Number'], tag='pbcoreIdentifier',
                               value=call_number.strip()))
    # -----------------------------------------------------
    #           physical
    # -----------------------------------------------------
            physical = build_physical(part, record)
            newPart.add_pbcoreInstantiation(physical)
            # descriptive.add_pbcore_part(newPart)
    # -----------------------------------------------------
    #           Preservation Master
    # -----------------------------------------------------
    #     print preservation_file_sets[index]
    #         for preservation_file_set in preservation_file_sets:
    #             # print preservation_file_set
            pres_master = build_preservation_master(record, preservation_file_sets[index])
            newPart.add_pbcoreInstantiation(pres_master)
    # -----------------------------------------------------
    #           access copy
    # -----------------------------------------------------
    #         print access_files_sets[index][0]
            access_copy = build_access_copy(record, access_files_sets[index])
            newPart.add_pbcoreInstantiation(access_copy)
            descriptive.add_pbcore_part(newPart)

    # Extension
    if record['Country of Creation']:
        exten = pbcoreExtension(exElement="countryOfCreation",
                                exValue=record['Country of Creation'],
                                exAuthority=SETTINGS.get('EXTRA', 'DefaultCountryAuthority'))
        descriptive.add_pbcore_extension(exten)

    if record['Project Note']:
        if record['Project Note'] == 'California Audiovisual Preservation Project (CAVPP)':
            exten = pbcoreExtension(exElement="projectNote",
                                    exValue='California Audiovisual Preservation Project',
                                    exAuthority='CAVPP')
        else:  # I don't know if this will be anything other than "California Audiovisual Preservation Project"
            exten = pbcoreExtension(exElement="projectNote",
                                    exValue=record['Project Note'])
        descriptive.add_pbcore_extension(exten)
    elif SETTINGS.getboolean('EXTRA','UseDefaultProjectNote'):
        exten = pbcoreExtension(exElement="projectNote",
                                exValue=SETTINGS.get('EXTRA', 'DefaultProjectNote'),
                                exAuthority=SETTINGS.get('EXTRA', 'DefaultProjectNoteAuthority'))
        descriptive.add_pbcore_extension(exten)

    if len(parts) > 1:
        for part in record['Object Identifier'].split(';'):
            newRelation = pbcoreRelation(reID=part.strip(), reType="Has Part")
            descriptive.add_pbcoreRelation(newRelation)

    new_XML_file.set_IntellectualContent(descriptive)

    return new_XML_file.xmlString()


def validate_col_titles(f):
    mismatched = []
    valid = True
    for index, heading in enumerate(csv.reader(f).next()):
        if heading != officialList[index]:
            valid = False
            mismatched.append("CSV title mismatch. At column "
                              + str(index + 1)
                              + ", recived: ["
                              + heading
                              + "]. Expected: ["
                              + officialList[index]
                              + "]")

    f.seek(0)
    return valid, mismatched


def valid_date(date):
    date_re = '(19||20)\d\d-(0[1-9]|1[012])-(0[1-9]|[1|2][0-9]|3[0-1])'
    if re.match(date_re, date):
        return True
    else:
        return False
    pass


def content_valid(input_record):
    warnings = []
    errors = []
    # Validate all dates

    check_list = []
    check_list.append(["Date Created", input_record["Date Created"]])
    check_list.append(["Date Published", input_record["Date Published"]])

    for item in check_list:
        if item[1] != "":
            if not valid_date(item[1]):
                warnings.append("\""
                                + item[1]
                                + "\" in the \'"
                                + item[0]
                                + "\' column is not in the correct date format. Expected YYYY-MM-DD.")

    # check that there is a description
    if input_record['Description or Content Summary'] == '':
        warnings.append("Missing required \"Description or Content Summary\" field")

    # for index, error in enumerate(errors):
    # errors[index] = "["+ input_record["Object Identifier"] + "] " + errors[index]

    for index, warning in enumerate(warnings):
        warnings[index] = "[" + input_record["Object Identifier"] + "] " + warnings[index]
    return warnings, errors


def locate_files(root, fileName):
    # search for file with fileName in it
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


def proceed(message, warnings=None):
    key = ""
    print ""
    while True:

        if warnings:
            print "\tWarnings:"
            print "\n\t**************************************************************\n"
            for index, warning in enumerate(warnings):
                print str(index + 1) + ")\t" + warning + "\n"
        print "\t**************************************************************"
        print("\n\t" + message)
        print "\n\tDo you wish to continue?",
        key = raw_input("[y/n]:")
        if key.lower() == "yes":
            key = 'y'
        if key.lower() == "no":
            key = 'n'
        if key.lower() != 'y' and key.lower() != 'n':
            print "Not a valid option.\n"
        else:
            break

    if key.lower() == 'y':
        return True
    if key.lower() == 'n':
        return False


def group_sides(digital_files):
    set = []
    part = []
    for file in digital_files:
        if "_a_" in file:
            part.append(file)
        elif "_b_" in file:
            part.append(file)
            set.append(part)
            part = []
        else:
            part.append(file)
            set.append(part)
            part = []
    return set

    pass


def sep_pres_access(digital_files):
    preservation = []
    access = []
    # part = []
    for file in digital_files:
        if "_prsv" in file and ".md5" not in file:
            # if "_a_" in file:
            # part.append(file)
            # elif "_b_" in file:
            #     part.append(file)
            #     # print part
            #     preservation.append(part)
            #     part = []
            # else:
            preservation.append(file)
            # part = []

        if "_access" in file and ".md5" not in file:
            access.append(file)
    return preservation, access


def report(files_created, number_of_new_records, number_of_records, number_of_rewritten_records):
    message = "\nGenerated " + str(number_of_records) + " PBCore records in total."
    if number_of_new_records >= 1:
        message += " New records: " + str(number_of_new_records) + "."
    if number_of_rewritten_records >= 1:
        message += " Records overwritten: " + str(number_of_rewritten_records) + "."
    logger.info(message)
    print("\n\tNew Records:")
    print("\t------------")
    for index, file_created in enumerate(files_created):
        print str(index + 1) + ")\t" + file_created
    print "\n"



def main():
    # ----------Setting up the logs----------
    mode = "normal"
    records = []
    digital_files = []


    logger.setLevel(logging.DEBUG)
    logPath = os.path.dirname(SETTINGS.get('LOGS', 'LogFile'))
    if not os.path.exists(logPath):  # automatically create a logs folder if one doesn't already exist
        os.makedirs(logPath)
    if SETTINGS.getboolean('LOGS','UseLogs'):
        fh = logging.FileHandler(SETTINGS.get('LOGS', 'LogFile'))  # Saves all logs to this file

    eh = logging.StreamHandler(sys.stderr)  # sends any critical errors to standard error
    eh.setLevel(logging.WARNING)
    ch = logging.StreamHandler(sys.stdout)  # sends all debug info to the standard out
    ch.setLevel(logging.DEBUG)
    log_filter = RemoveErrorsFilter()
    ch.addFilter(log_filter)  # logger.addFilter(NoParsingFilter())
    if args.debug or SETTINGS.getboolean('EXTRA', 'DebugMode') is True:
        mode = 'debug'
        print "ENTERING DEBUG MODE!"
        if SETTINGS.getboolean('LOGS','UseLogs'):
            fh.setLevel(logging.DEBUG)
    else:
        if SETTINGS.getboolean('LOGS','UseLogs'):
            fh.setLevel(logging.INFO)
    if args.nochecksum or SETTINGS.getboolean('CHECKSUM','CalculateChecksums') is False:
        print "Bypassing MD5 checksum generation."

    error_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')             # DATE - USERNAME - Message
    stderr_formatter = logging.Formatter('%(levelname)s - %(message)s')     # USERNAME - Message
    stdout_formatter = logging.Formatter('%(message)s')                     # Message
    if SETTINGS.getboolean('LOGS','UseLogs'):
        fh.setFormatter(error_formatter)
        logger.addHandler(fh)
    eh.setFormatter(stderr_formatter)
    logger.addHandler(eh)
    ch.setFormatter(stdout_formatter)
    logger.addHandler(ch)

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
    logger.debug("Validating files column titles.")
    valid, errors = validate_col_titles(f)
    if not valid:
        sys.stdout.flush()
        for error in errors:
            logger.critical(error)
        quit()

    try:
        logger.debug("Loading file into memory.")
        for item in csv.DictReader(f):  # reason: because you can only iterate over a DictReader once
            records.append(item)
    except ValueError:
        print "FAILED"
        logger.critical("Error, cannot load file as a CSV.")
        print "Quitting."
        quit()
    # ---------- Validate data in CSV file ----------
    total_warnings = []
    total_errors = []

    logger.debug("Validating data in CSV.")
    for record in records:
        data_warnings, data_errors = content_valid(record)
        total_warnings += data_warnings
        total_errors += data_errors
    # if there are any errors print them out with warnings and quit
    sys.stdout.flush()
    if total_errors:
        for error in total_errors:
            print "Error found: " + error
        if total_warnings:
            for warning in total_warnings:
                print "WARNINGS: " + warning
        print "Quitting"
        quit()


    # ---------- Locate all files mentioned in CSV ----------
    preservation_files = []
    access_files = []

    logger.debug("Locating files")
    file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
    files_not_found = []
    for record in records:
        fileName = re.search(file_name_pattern, record['Object Identifier']).group(0)
        logging.debug("Locating possible files for: " + fileName)
        digital_files = locate_files(args.csv, fileName)
        if digital_files:
            logger.debug("Files located for: " + fileName)
            preservation_files, access_files = sep_pres_access(digital_files)
            if not preservation_files:
                total_warnings.append("No preservation files found for " + fileName)
            if not access_files:
                total_warnings.append("No access files found for " + fileName)
        else:
            files_not_found.append(fileName)

    if files_not_found:
        for file_not_found in files_not_found:
            message = "[" + file_not_found + "] Could not find files that match this record."
            logger.warning(message)
            total_warnings.append(message)
            # print "quiting"
            # quit()


        # ---------- Check if XML file already exists. ----------
    for record in records:
        fileName = re.search(file_name_pattern, record['Object Identifier']).group(0)
        file_output_name = fileName + "_ONLYTEST.xml"
        if isfile(file_output_name):
            total_warnings.append(file_output_name + " already exists. Do you wish to overwrite it?")

        # ---------- Report errors and warning. ----------
    sys.stdout.flush()
    if total_errors:
        for error in total_errors:
            print "Error found: " + error
        if total_warnings:
            for warning in total_warnings:
                print "Warning: " + warning
        print "Quitting"
        quit()

    if mode != 'debug':
        if total_warnings:
            key = ""
            for warning in total_warnings:
                logger.warning(warning)
            if proceed("Possible problems with the data found.", total_warnings) is False:
                logger.info("Script terminated by user.")
                print "Quitting"
                quit()
            else:
                print("\t"),
                logger.info("Warnings ignored.")


    # ---------- Genereate PBCore XML Files ----------
    print("")
    logging.info("Generating PBCore...")
    file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
    number_of_records = 0
    number_of_new_records = 0
    number_of_rewritten_records = 0

    files_created = []
    for record in records:
        print("")
        fileName = re.search(file_name_pattern, record['Object Identifier']).group(0)
        logger.info("Producing PBCore XML for " + fileName + ".")
        file_output_name = fileName + "_ONLYTEST.xml"
        if isfile(file_output_name):
            sys.stdout.write("\t")
            sys.stdout.flush()
            logger.warning(file_output_name + " already exists. Overwriting.")
            number_of_rewritten_records += 1
        else:
            number_of_new_records += 1
        digital_files = locate_files(args.csv, fileName)
        # I'm sending this into miniDOM because I can't get etree to print a pretty XML
        buf = parseString(generate_pbcore(record, digital_files))
        output_file = open(file_output_name, 'w')
        output_file.write(buf.toprettyxml(encoding='utf-8'))
        output_file.close()
        logger.info("Saved XML PBCore metadata record: " + file_output_name)
        number_of_records += 1
        files_created.append(file_output_name)
        print("")
        sys.stdout.flush()

    logger.debug("Closing CSV file:")
    f.close()

    report(files_created, number_of_new_records, number_of_records, number_of_rewritten_records)


# load settings
settingsFileName = 'settings/pbcore-csv-settings.ini'
SETTINGS = ConfigParser()
if isfile(settingsFileName):
    SETTINGS.read(settingsFileName)
else:
    sys.stderr.write('Error: cannot find ' + settingsFileName + '. Quiting')
    quit()


# settingsFile.close()

# loggers setup
logger = logging.getLogger()
parser = argparse.ArgumentParser()
parser.add_argument("csv", help="Source CSV file", type=str)
parser.add_argument("-d", "--debug", help="Debug mode. Writes all messages to debug log.", action='store_true')
parser.add_argument("-nc", "--nochecksum", help="Bypasses md5 checksum generation for files.", action='store_true')
parser.add_argument("-np", "--noprogress", help="hides the percentage completed of the md5 checksum calculation.", action='store_true')
# TODO: add argument that lets you create pbcore without the files present
args = parser.parse_args()



if __name__ == '__main__':
    main()