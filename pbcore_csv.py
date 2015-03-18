import os
import sys
import logging
import argparse
from ConfigParser import ConfigParser
import threading
from onesheet.VideoObject import *
from onesheet.AudioObject import *
import gui.pbcore_csv_gui
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
class pbcoreBuilder(threading.Thread):

    def __init__(self, input_file, verbose=False):
        threading.Thread.__init__(self)
        self._running = False
        self._source = input_file
        self._job_total = 0
        self._job_progress = 0
        self._parts_total = 0
        self._parts_progress = 0
        self._calculation_percent = 0
        self._records = []
        self._xmlFiles = []
        # self.number_of_records = 0
        self._new_records = []
        self._overwritten_records = []
        self.verbose = verbose
        self.log = ""  # TODO add loging feature

    @property
    def isRunning(self):
        return self._running

    @property
    def number_of_records(self):
        return len(self._new_records) + len(self._overwritten_records)
    @property
    def new_records(self):
        return self._new_records
    @property
    def overwritten_records(self):
        return self._overwritten_records

    @property
    def job_total(self):
        return self._job_total

    @property
    def job_progress(self):
        return self._job_progress

    @property
    def parts_total(self):
        return self._parts_total

    @property
    def parts_progress(self):
        return self._parts_progress

    @property
    def calculation_percent(self):
        return self._calculation_percent

    @property
    def records(self):
        return self._records

    @property
    def xml_files(self):
        return self._xmlFiles

    @property
    def source(self):
        return self._source

    def sizeofHuman(self, num):
            num = int(num)
            for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
                if num < 1024.0:
                    return "%3.1f %s" % (num, x), x
                num /= 1024.0
    def _samplerate_cleanup(self, data):

        data = str(data/float(1000))
        # print data
        return data.rstrip('.0')
    def build_descriptive(self, record):
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
            proj_ID = record['Project Identifier']

        if record['Asset Type']:
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

        if record['Publisher']:
            publisher = record['Publisher']
            publish = pbcorePublisher(name=publisher, role="Publisher")
            descriptive.add_pbcorePublisher(publish)

        if record['Distributor']:
            distributor = record['Distributor']
            publish = pbcorePublisher(name=distributor, role="Distributor")
            descriptive.add_pbcorePublisher(publish)


        # Descriptive Rights

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


    def build_physical(self, new_part, record):
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


    def build_preservation_master(self, record, preservation_file_set):

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
                file_size, file_units = self.sizeofHuman(f.file_size)
                new_mast_part.set_instantiationFileSize(PB_Element(['unitsOfMeasure',file_units],
                                                                   tag="instantiationFileSize",
                                                                   value=str(file_size)))
                new_mast_part.add_instantiationIdentifier(PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                                     ['annotation', 'File Name'],
                                                                     tag="instantiationIdentifier",
                                                                     value=os.path.basename(master_part)))
                if not args.nochecksum and SETTINGS.getboolean('CHECKSUM','CalculateChecksums') is True:
                    if self.verbose:
                        print("\t"),
                        print "Part " + str(self._parts_progress) + " of " + str(self._parts_total) + ": ",
                        logger.info("Calculating MD5 checksum for " + f.file_name + ".")
                        if f.file_size > LARGEFILE:
                            print "\tNote: " + f.file_name + " is " + f.file_size_human + " and might take some times to calculate."
                        md5 = f.calculate_MD5(progress=True)
                    else:
                        f.calculate_MD5(threaded=True)
                        while f.isMD5Calculating:
                            self._calculation_percent = f.calulation_progresss
                            sleep(.1)
                        md5 = f.MD5_hash
                    new_mast_part.add_instantiationIdentifier(PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                                         ['version', 'MD5'],
                                                                         ['annotation', 'checksum'],
                                                                         tag="instantiationIdentifier",
                                                                         value=md5))
                    sleep(.5)
                newfile = InstantiationEssenceTrack(type="Audio")
                newfile.set_essenceTrackBitDepth(PB_Element(tag="essenceTrackBitDepth",
                                                            value=str(f.audioBitDepth)))
                newfile.set_essenceTrackSamplingRate(PB_Element(["unitsOfMeasure", "kHz"],
                                                                tag="essenceTrackSamplingRate",
                                                                value=self._samplerate_cleanup(f.audioSampleRate)))
                datarate = f.audioBitRateH.split(" ")
                newfile.set_essenceTrackDataRate(PB_Element(['unitsOfMeasure', datarate[1]],
                                                                tag="essenceTrackDataRate",
                                                                value=datarate[0]))
                if f.file_extension.lower() == '.wav':
                    pres_master.set_instantiationDigital(PB_Element(['source', 'PRONOM Technical Registry'],
                                                                    tag='instantiationDigital',
                                                                    value='audio/x-wav'))  # This is really ugly code I don't know a better way
                    newfile.set_essenceTrackEncoding(PB_Element(tag='essenceTrackEncoding', value='WAV'))

                audio_codec = f.audioCodec + ": " + f.audioCodecLongName
                pres_master.set_instantiationStandard(PB_Element(tag='instantiationStandard',
                                                                 value=audio_codec))

                new_mast_part.add_instantiationEssenceTrack(newfile)

                self._parts_progress += 1
                pres_master.add_instantiationPart(new_mast_part)

            pass

        # ============================================================ #
        # ======================= Moving Image ======================= #
        # ============================================================ #
        elif media_type.lower() == 'moving image':
            f = VideoObject(preservation_file_set[0])
            pres_master.set_instantiationMediaType(PB_Element(tag='instantiationMediaType', value='Moving Image'))
            video_codec = str(f.videoCodec + ": " + f.videoCodecLongName)
            pres_master.set_instantiationStandard(PB_Element(tag='instantiationStandard', value=video_codec))
            pres_master.add_instantiationIdentifier(PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                               ['annotation', 'File Name'],
                                                               tag="instantiationIdentifier",
                                                               value=os.path.basename(preservation_file_set[0])))

            file_size, file_units = self.sizeofHuman(f.file_size)
            pres_master.set_instantiationFileSize(PB_Element(['unitsOfMeasure', file_units],
                                                             tag="instantiationFileSize",
                                                             value=str(file_size)))

            if not args.nochecksum and SETTINGS.getboolean('CHECKSUM', 'CalculateChecksums') is True:
                if self.verbose:
                    print("\t"),
                    print "Part " + str(self._parts_progress) + " of " + str(self._parts_total) + ": ",
                    logger.info("Calculating MD5 checksum for " + f.file_name + ".")
                    if f.file_size > LARGEFILE:
                        print "\tNote: This file is " + f.file_size_human + " and might take some times to calculate."
                    md5 = f.calculate_MD5(progress=True)
                else:
                    f.calculate_MD5(threaded=True)
                    while f.isMD5Calculating:
                        self._calculation_percent = f._calculation_progress
                        sleep(.1)
                    md5 = f.MD5_hash
                pres_master.add_instantiationIdentifier(PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                                   ['version', 'MD5'],
                                                                   ['annotation', 'checksum'],
                                                                   tag="instantiationIdentifier",
                                                                   value=md5))
                sleep(.5)

            # ---------- Video essence track ----------
            newfile = InstantiationEssenceTrack(type='Video',
                                                frameRate=str(f.videoFrameRate),
                                                duration=f.totalRunningTimeSMPTE,
                                                aspectRatio=str(f.videoAspectRatio))
            datarate = f.videoBitRateH.split(" ")
            newfile.set_essenceTrackDataRate(PB_Element(['unitsOfMeasure', datarate[1]],
                                                        tag="essenceTrackDataRate",
                                                        value=datarate[0]))
            newfile.set_essenceTrackBitDepth(PB_Element(tag='essenceTrackBitDepth', value=f.videoColorDepth))
            colorspace = f.videoColorSpace
            if colorspace:
                newfile.add_essenceTrackAnnotation(PB_Element(['annotationType', 'Color Space'],
                                                              tag="essenceTrackAnnotation",
                                                              value=colorspace))
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
            audio_codec = f.audioCodec + ": " + f.audioCodecLongName
            newfile.set_essenceTrackStandard(PB_Element(tag='essenceTrackStandard',
                                                        value=audio_codec))
            datarate = f.audioBitRateH.split(" ")
            newfile.set_essenceTrackDataRate(PB_Element(['unitsOfMeasure', datarate[1]],
                                                                tag="essenceTrackDataRate",
                                                                value=datarate[0]))
            self._parts_progress += 1
            pres_master.add_instantiationEssenceTrack(newfile)

            pass


        if record['Quality Control Notes']:
            note = record['Quality Control Notes']
            pres_master.add_instantiationAnnotation(
                PB_Element(['annotationType', 'CAVPP Quality Control/Partner Quality Control'],
                           tag="instantiationAnnotation",
                           value=note.strip()))
        return pres_master

    def build_access_copy(self, record, access_files_sets):
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



                    size, units = self.sizeofHuman(f.file_size)
                    newAudioFile.set_instantiationFileSize(PB_Element(['unitsOfMeasure', units],
                                                                      tag="instantiationFileSize",
                                                                      value=size))
                    if not args.nochecksum and SETTINGS.getboolean('CHECKSUM','CalculateChecksums') is True:
                        if self.verbose:
                            print("\t"),
                            print "Part " + str(self._parts_progress) + " of " + str(self._parts_total) + ": ",
                            logger.info("Calculating MD5 checksum for " + f.file_name + ".")
                            if f.file_size > LARGEFILE:
                                print "\tNote: This file is " + f.file_size_human + " and might take some times to calculate."
                            md5 = f.calculate_MD5(progress=True)
                        else:
                            f.calculate_MD5(threaded=True)
                            while f.isMD5Calculating:
                                self._calculation_percent = f.calulation_progresss
                                sleep(.1)
                            md5 = f.MD5_hash
                        newAudioFile.add_instantiationIdentifier(
                            PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                       ['version', 'MD5'],
                                       ['annotation', 'checksum'],
                                       tag="instantiationIdentifier",
                                       value=md5))
                        sleep(.5)
                    if f.audioChannels == 1:
                        access_copy.set_instantiationTracks(PB_Element(tag="instantiationTracks", value='Sound'))
                        access_copy.set_instantiationChannelConfiguration(PB_Element(tag="instantiationChannelConfiguration",
                                                                                     value='Mono'))
                    elif f.audioChannels == 2:
                        access_copy.set_instantiationTracks(PB_Element(tag="instantiationTracks", value='Sound'))
                        access_copy.set_instantiationChannelConfiguration(PB_Element(tag="instantiationChannelConfiguration",
                                                                                     value='Stereo'))
                    newEssTrack = InstantiationEssenceTrack(type="Audio", bitDepth=f.audioBitDepth)
                    newEssTrack.set_essenceTrackSamplingRate(PB_Element(["unitsOfMeasure", "kHz"],
                                                                        tag="essenceTrackSamplingRate",
                                                                        value=self._samplerate_cleanup(f.audioSampleRate)))
                    if f.file_extension.lower() == '.mp3':
                        newEssTrack.set_essenceTrackEncoding(PB_Element(tag='essenceTrackEncoding', value='MP3'))
                    datarate = f.audioBitRateH.split(" ")
                    newEssTrack.set_essenceTrackDataRate(PB_Element(['unitsOfMeasure', datarate[1]],
                                                                    tag="essenceTrackDataRate",
                                                                    value=datarate[0]))
                    newAudioFile.add_instantiationEssenceTrack(newEssTrack)
                    access_copy.add_instantiationPart(newAudioFile)
                    self._parts_progress += 1

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
                video_codec = str(f.videoCodec + ": " + f.videoCodecLongName)
                access_copy.set_instantiationStandard(PB_Element(tag='instantiationStandard', value=video_codec))
                size, units = self.sizeofHuman(f.file_size)
                access_copy.set_instantiationFileSize(PB_Element(['unitsOfMeasure', units],
                                                                 tag="instantiationFileSize",
                                                                 value=size))
                if not args.nochecksum and SETTINGS.getboolean('CHECKSUM', 'CalculateChecksums') is True:
                    if self.verbose:
                        print("\t"),
                        print "Part " + str(self._parts_progress) + " of " + str(self._parts_total) + ": ",
                        logger.info("Calculating MD5 checksum for " + f.file_name + ".")
                        if f.file_size > LARGEFILE:
                            print "\tNote: This file is " + f.file_size_human + " and might take some times to calculate."
                        md5 = f.calculate_MD5(progress=True)
                    else:
                        f.calculate_MD5(threaded=True)
                        while f.isMD5Calculating:
                            self._calculation_percent = f.calulation_progresss
                            sleep(.1)
                        md5 = f.MD5_hash
                    access_copy.add_instantiationIdentifier(
                        PB_Element(['source', SETTINGS.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                   ['version', 'MD5'],
                                   ['annotation', 'checksum'],
                                   tag="instantiationIdentifier",
                                   value=md5))
                    sleep(.5)
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
                datarate = f.videoBitRateH.split(" ")
                newEssTrack.set_essenceTrackDataRate(PB_Element(['unitsOfMeasure', datarate[1]],
                                                        tag="essenceTrackDataRate",
                                                        value=datarate[0]))
                newEssTrack.set_essenceTrackBitDepth(PB_Element(tag='essenceTrackBitDepth', value=f.videoColorDepth))
                colorspace = f.videoColorSpace
                if colorspace:
                    newEssTrack.add_essenceTrackAnnotation(PB_Element(['annotationType', 'Color Space'],
                                                                      tag="essenceTrackAnnotation",
                                                                      value=colorspace))
                newEssTrack.add_essenceTrackAnnotation(PB_Element(['annotationType', 'Frame Size Vertical'],
                                                                  tag="essenceTrackAnnotation",
                                                                  value=f.videoResolutionHeight))
                newEssTrack.add_essenceTrackAnnotation(PB_Element(['annotationType', 'Frame Size Horizontal'],
                                                                  tag="essenceTrackAnnotation",
                                                                  value=f.videoResolutionWidth))
                access_copy.add_instantiationEssenceTrack(newEssTrack)

                # ------------------ Audio track ------------------
                audio_codec = f.audioCodec + ": " + f.audioCodecLongName
                newEssTrack = InstantiationEssenceTrack(type='Audio',
                                                        standard=audio_codec,
                                                        samplingRate=f.audioSampleRate/1000)
                datarate = f.audioBitRateH.split(" ")
                newEssTrack.set_essenceTrackDataRate(PB_Element(['unitsOfMeasure', datarate[1]],
                                                                tag="essenceTrackDataRate",
                                                                value=datarate[0]))
                bitdepth = f.audioBitDepth
                if bitdepth == 32:
                    bitdepth = "32-Bit Float"
                newEssTrack.set_essenceTrackBitDepth(PB_Element(tag='essenceTrackBitDepth', value=bitdepth))
                access_copy.add_instantiationEssenceTrack(newEssTrack)
                self._parts_progress += 1
        return access_copy

    def generate_pbcore(self, record, files=None, verbose=False):
        self._running = True
        XML = ""
        new_XML_file = PBCore(collectionSource=record['Institution'],
                              collectionTitle=record['Collection Guide Title'])
        if files:
            preservation_file_sets, access_files_sets = self.sep_pres_access(files)
        else:
            file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
            fileName = re.search(file_name_pattern, record['Object Identifier']).group(0)
            newfiles = self.locate_files(os.path.abspath(self.source), fileName)
            preservation_file_sets, access_files_sets = self.sep_pres_access(newfiles)
        self._parts_total = len(preservation_file_sets) + len(access_files_sets)
        preservation_file_sets = self.group_sides(preservation_file_sets)
        access_files_sets = self.group_sides(access_files_sets)

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


        descriptive = self.build_descriptive(record)
        # PARTS
        call_numbers = ""
        if record['Call Number']:
            call_numbers = record['Call Number'].split(';')

    # =================
    # AUDIO ONLY
    # =================


        if record['Media Type'].lower() == 'audio' or record['Media Type'].lower() == 'sound':
        # PBcore Parts
            self._parts_progress = 1
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
                physical = self.build_physical(part, record)
                newPart.add_pbcoreInstantiation(physical)

        # -----------------------------------------------------
        #           Preservation Master
        # -----------------------------------------------------
                if files:
                    # self._parts_progress = 1
                    if preservation_file_sets:
                        for preservation_file_set in preservation_file_sets:
                            # print preservation_file_set
                            pres_master = self.build_preservation_master(record, preservation_file_set)
                            newPart.add_pbcoreInstantiation(pres_master)


        # -----------------------------------------------------
        #           access copy
        # -----------------------------------------------------
                    access_copy = self.build_access_copy(record, access_files_sets)
                    newPart.add_pbcoreInstantiation(access_copy)

            descriptive.add_pbcore_part(newPart)

    # =================
    # Moving Image ONLY
    # =================

        elif record['Media Type'].lower() == 'moving image':
            # print "moving image"
            self._parts_progress = 1
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
                physical = self.build_physical(part, record)
                newPart.add_pbcoreInstantiation(physical)
                # descriptive.add_pbcore_part(newPart)
        # -----------------------------------------------------
        #           Preservation Master
        # -----------------------------------------------------
        #     print preservation_file_sets[index]
        #         for preservation_file_set in preservation_file_sets:
        #             # print preservation_file_set
                if files:
                    pres_master = self.build_preservation_master(record, preservation_file_sets[index])
                    newPart.add_pbcoreInstantiation(pres_master)
        # -----------------------------------------------------
        #           access copy
        # -----------------------------------------------------
        #         print access_files_sets[index][0]
                    access_copy = self.build_access_copy(record, access_files_sets[index])
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
        self._running = False
        return new_XML_file.xmlString()



    def build_all_records(self):
        file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
        self._job_total = len(self._records)

        self._job_progress = 0
        for record in self._records:
            fileName = re.search(file_name_pattern, record['Object Identifier']).group(0)
            file_output_name = fileName + "_ONLYTEST.xml"
            if self.verbose:
                logger.info("Producing PBCore XML for " + fileName + ".")
            if isfile(file_output_name):
                # logger.warning(file_output_name + " already exists. Overwriting.")
                self._overwritten_records.append(file_output_name)
            else:
                self._new_records.append(file_output_name)
            digital_files = self.locate_files(self.source, fileName)
            xmlFile = dict()
            xmlFile['name'] = file_output_name
            xmlFile['data'] = self.generate_pbcore(record, digital_files)
            self._xmlFiles.append(xmlFile)
            self._job_progress += 1


    def validate_col_titles(self):
        test_file = open(self.source, 'rU')
        mismatched = []
        valid = True
        for index, heading in enumerate(csv.reader(test_file).next()):
            if heading != officialList[index]:
                valid = False
                mismatched.append("CSV title mismatch. At column "
                                  + str(index + 1)
                                  + ", recived: ["
                                  + heading
                                  + "]. Expected: ["
                                  + officialList[index]
                                  + "]")
        test_file.close()
        return valid, mismatched


    def valid_date(self, date):
        date_re = '(19||20)\d\d-(0[1-9]|1[012])-(0[1-9]|[1|2][0-9]|3[0-1])'
        if re.match(date_re, date):
            return True
        else:
            return False
        pass

    def is_valid_file(self, testfile):
        if os.path.splitext(testfile)[1] != ".csv":
            message = str(testfile + " is not a csv file.")
            # logger.critical(testfile + " is not a csv file.")

            return False, message
        else:
            if isfile(testfile):  # checks if the file passed in is a real file):
                try:

                    f = open(testfile, 'rU')
                    f.close()
                    return True, ""
                except IOError:
                    message = "Unable to open " + testfile
                    return False, ""
            else:
                message = str("Cannot locate " + testfile + ".")
                return False, message

    def is_valid_csv(self):
        try:
            f = open(self.source, 'rU')
            csv.Sniffer().sniff(f.read(1024))
            csv.DictReader(f)
            f.close()
            return True
        except ValueError:
            return False
        except csv.Error:
            return False


    def check_content_valid(self):
        warnings = []
        errors = []
        # Validate all dates
        f = open(self.source, "rU")
        # test_record = csv.DictReader(f)
        test_records = []
        for record in csv.DictReader(f):
            test_records.append(record)
        f.close()

        check_list = []
        for test_record in test_records:
            check_list.append(["Date Created", test_record["Date Created"]])
            check_list.append(["Date Published", test_record["Date Published"]])

            for item in check_list:
                # print item
                warning = dict()
                if item[1] != "":
                    if not self.valid_date(item[1]):
                        warning['record'] = test_record['Project Identifier']
                        warning['received'] = item[1]
                        warning['location'] = item[0]
                        warning['type'] = 'Incorrect Date Format'
                        warning['message'] = 'Expected YYYY-MM-DD.'
                        # warnings.append("\""
                        #                 + item[1]
                        #                 + "\" in the \'"
                        #                 + item[0]
                        #                 + "\' column is not in the correct date format. Expected YYYY-MM-DD.")
                        warnings.append(warning)
            warning = dict()
            # check that there is a description
            if test_record['Description or Content Summary'] == '':
                warning['record'] = test_record['Project Identifier']
                warning['received'] = "No data"
                warning['location'] = "Description or Content Summary"
                warning['type'] = 'Missing Required Data'
                warning['message'] = 'This is a required field for PBCore to validate.'
                warnings.append(warning)
            #     warnings.append("Missing required \"Description or Content Summary\" field")

            # for index, error in enumerate(errors):
            # errors[index] = "["+ input_record["Object Identifier"] + "] " + errors[index]
            # for warning in warnings:
            #     print warning['record'] + ": Recieved \"" + warning['received'] + "\" at " + warning['location'] + ". " + warning['message']

        return warnings, errors


    def locate_files(self, root, fileName):
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




    def group_sides(self, digital_files):
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


    def sep_pres_access(self, digital_files):
        preservation = []
        access = []
        # part = []
        for file in digital_files:
            if "_prsv" in file and ".md5" not in file:
                preservation.append(file)

            elif "_access" in file and ".md5" not in file:
                access.append(file)
        return preservation, access

    def load_records(self):

        f = open(self.source, 'rU')
        records = csv.DictReader(f)
        for record in records:
            self._records.append(record)
        f.close()
        self._job_total = len(self._records)

    def check_files_exist(self):
        file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
        files_not_found = []
        warnings = []
        self.load_records()
        for record in self._records:
            fileName = re.search(file_name_pattern, record['Object Identifier']).group(0)
            # logging.debug("Locating possible files for: " + fileName)
            digital_files = self.locate_files(self.source, fileName)
            if digital_files:
                # logger.debug("Files located for: " + fileName)
                preservation_files, access_files = self.sep_pres_access(digital_files)
                if not preservation_files:
                    warning = dict()
                    warning['record'] = record['Project Identifier']
                    warning['type'] = 'Missing Files'
                    warning['message'] = "Unable to locate any preservation master files."
                    # warnings.append("No preservation files found for " + fileName)
                    warnings.append(warning)
                if not access_files:
                    warning = dict()
                    warning['record'] = record['Project Identifier']
                    warning['type'] = 'Missing Files'
                    warning['message'] = "Unable to locate any access files."
                    warnings.append(warning)
                    # warnings.append("No access files found for " + fileName)
            else:
                files_not_found.append(fileName)

        if files_not_found:
            for file_not_found in files_not_found:
                warning = dict()
                warning['record'] = file_not_found
                warning['type'] = 'Missing Files'
                warning['message'] = "Unable to locate any files."
                warnings.append(warning)

                # message = "[" + file_not_found + "] Could not find files that match this record."
                # # logger.warning(message)
                # warnings.append(message)
                # print "quiting"
                # quit()
                pass
        return warnings

    def run(self):
        # print "starting thread"
        self._running = True
        # while self._running:
        #     parts = str(self._parts_progress) + " : " + str(self._parts_total)
        #     total = str(self._job_progress) + " : " + str(self._job_total)
        #     print(parts, total)
        #     sleep(1)
        # pass
        self.build_all_records()
        self._running = False


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


def proceed(message, warnings=None):
        key = ""
        print ""
        while True:

            if warnings:
                print "\tWarnings:"
                print "\n\t**************************************************************\n"
                for index, warning in enumerate(warnings):
                    # print warning
                    # print str(index + 1) + ")\t" + warning + "\n"
                    warning_message = str(index + 1) + ")\t"
                    # print warning['record']
                    if 'record' in warning:
                        warning_message += warning['record']

                    if 'received' in warning:
                        warning_message += (": Received \"" + warning['received'] + "\"")

                    if 'location' in warning:
                        warning_message += (" at [" + warning['location'] + "].")
                    else:
                        warning_message += "."
                    if 'message' in warning:
                        warning_message += warning['message']

                    print warning_message
                    # print str(index + 1) + ")\t" +warning['record'] + ": Recieved \"" + warning['received'] + "\" at " + warning['location'] + ". " + warning['message']
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

    logger.debug("Opening file:" + args.csv)
    record_file = pbcoreBuilder(args.csv, verbose=True)
    valid, error_message = record_file.is_valid_file(args.csv)
    if valid:
        logger.debug(args.csv + " successfully opened.")
        pass
    else:
        print "FAILED"
        logger.critical(error_message)
        print "Quiting"
        quit()

    logger.debug("Validating file is a csv.")
    if record_file.is_valid_csv():
        logger.debug(args.csv + " successfully validated as a CSV.")
    else:
        logger.critical("Error, cannot load file as a CSV.")
        print "FAILED"
        print "Quitting."
        quit()

    logger.debug("Validating files column titles.")
    valid, errors = record_file.validate_col_titles()
    if valid:
        logger.debug(args.csv + " has valid columns.")
    else:
        sys.stdout.flush()
        for error in errors:
            logger.critical(error)
        quit()


    # ---------- Validate data in CSV file ----------
    total_warnings = []
    total_errors = []

    logger.debug("Validating data in CSV.")
    warnings, errors = record_file.check_content_valid()
    total_warnings += warnings
    total_errors += errors
    # for warning in warnings:

    # for record in records:
    #     data_warnings, data_errors = record_file.check_content_valid(record)
    #     total_warnings += data_warnings
    #     total_errors += data_errors
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
    total_warnings += record_file.check_files_exist()



        # ---------- Check if XML file already exists. ----------

    file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
    for record in record_file.records:
        fileName = re.search(file_name_pattern, record['Object Identifier']).group(0)
        file_output_name = fileName + "_ONLYTEST.xml"
        if isfile(file_output_name):
            warning = dict()
            warning['record'] = file_output_name
            warning['message'] = "File already exists. Do you wish to overwrite it?"
            total_warnings.append(warning)

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
    # record_file.build_all_records()
    # print record_file.overwritten_records
    file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
    number_of_records = 0
    number_of_new_records = 0
    number_of_rewritten_records = 0

    # for record in record_file.records:
    #     print record
    files_created = []
    for record in record_file.records:
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
        digital_files = record_file.locate_files(args.csv, fileName)
        # I'm sending this into miniDOM because I can't get etree to print a pretty XML
        if digital_files:
            buf = parseString(record_file.generate_pbcore(record, digital_files))
        else:
            buf = parseString(record_file.generate_pbcore(record))
        output_file = open(file_output_name, 'w')
        output_file.write(buf.toprettyxml(encoding='utf-8'))
        output_file.close()
        logger.info("Saved XML PBCore metadata record: " + file_output_name)
        number_of_records += 1
        files_created.append(file_output_name)
        print("")
        sys.stdout.flush()





    # for xml_file in record_file.xml_files:
    #     print xml_file['name']
    #     file_output_name = xml_file['name']
    #     output_file = open(file_output_name, 'w')
    #     # print xml_file['data']
    #     dom_buffer = parseString(xml_file['data'])
    #     output_file.write(dom_buffer.toprettyxml(encoding='utf-8'))
    #     output_file.close()
    #     logger.info("Saved XML PBCore metadata record: " + file_output_name)

    logger.debug("Closing CSV file:")
    # f.close()
    # files_created = []
    # files_created += record_file.new_records
    # files_created += record_file.overwritten_records

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
parser.add_argument("csv", help="Source CSV file", nargs='?', default="", type=str)
parser.add_argument("-d", "--debug", help="Debug mode. Writes all messages to debug log.", action='store_true')
parser.add_argument("-nc", "--nochecksum", help="Bypasses md5 checksum generation for files.", action='store_true')
parser.add_argument("-np", "--noprogress", help="hides the percentage completed of the md5 checksum calculation.", action='store_true')
parser.add_argument("-g", "--gui", help="EXPERIMENTAL: Loads the gui interface.", action='store_true')
# TODO: add argument that lets you create pbcore without the files present
args = parser.parse_args()



if __name__ == '__main__':
    if args.csv == "" and not args.gui:
        parser.print_help()
    elif args.csv == "" and args.gui:
        print("Loading graphical user interface")
        # print os.path.abspath(settingsFileName)
        gui.pbcore_csv_gui.start_gui(settings=os.path.abspath(settingsFileName))
    elif args.csv != "" and args.gui:
        print("Loading graphical user interface with: "+args.csv)
        gui.pbcore_csv_gui.start_gui(settings=os.path.abspath(settingsFileName), csvfile=args.csv)
    else:
        main()