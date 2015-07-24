#!/usr/local/bin/python
__version__ = "0.1.6"

import sys
from datetime import date

if sys.version_info >= (3, 0):
    from tkinter.filedialog import asksaveasfilename
    from queue import Queue
    from configparser import ConfigParser
    from tkinter.messagebox import showerror, askyesno
else:
    from Queue import Queue
    from ConfigParser import ConfigParser
    from tkMessageBox import showerror, askyesno
    from tkFileDialog import asksaveasfilename
__author__ = 'California Audio Visual Preservation Project'
__copyright__ = "Copyright 2015, California Audiovisual Preservation Project"
__credits__ = "Henry Borchers"
import traceback
import os
import sys
import logging
import argparse
import re
import threading
from onesheet.VideoObject import *
from onesheet.FileObject import *
from onesheet.AudioObject import *
from onesheet import OExceptions
# from PBCore.scripts.modules.PBCore.patch import trt

from time import sleep
from os.path import isfile
from xml.dom.minidom import parseString

from PBCore.scripts.modules.PBCore.PBCore import *
FILE_NAME_PATTERN = re.compile("[A-Z,a-z]+_\d+")
use_gui = True

# a series of letters that is lowercase from a through z,
# followed an underscore
# followed by a number 5 or 6 digits long,
# optionally followed another underscore
# optionally followed the letters a or b
# optionally followed an underscore and the letters t, r, or d and a number of 1 or more digits
# optionally followed another underscore and the letters a or b
# followed by a semicolon, an end-of-line character, end of word, or end of string
VALID_OBJECT_PATTERN = re.compile('([a-z]*_\d{5,6})_?[a,b]?(_(t|r|d)\d+)?(_(a|b))?(\s|;|\b|\>|\Z)')

LARGEFILE = 1065832230
import csv

officialList = ['Internet Archive URL',
                'Object Identifier',
                'Call Number',
                'Project Identifier',
                'Project Note',
                'Institution',
                'Asset Type',
                'Media Type',
                'Creator',
                'Contributor',
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


def valid_object_id(data):

    results = re.findall(VALID_OBJECT_PATTERN, data)
    if len(results) > 0:
        return True
    else:
        return False


    pass


class MediaTypeException(Exception):
    def __init__(self, message):
        super(MediaTypeException, self).__init__(message)
    pass


class pbcoreBuilder(threading.Thread):
    def __init__(self, input_file, settings, verbose=False, calculate_checksums=True):
        threading.Thread.__init__(self)
        self.calculate_checksums = calculate_checksums
        self.settings = ConfigParser()

        self.settings.read(settings)
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
        self._queue = Queue()
        self._working_status = ""
        self._working_file = ""
        self.log = ""  # TODO add loging feature


    @property
    def working_status(self):
        return self._working_status

    @property
    def working_file(self):
        return self._working_file

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

    def add_job(self, record, file_name=None):
        id = re.search(FILE_NAME_PATTERN, record['Object Identifier']).group(0)
        if file_name == None:
            file_name = os.path.join(os.path.dirname(self.source), str(id + ".xml"))
        # id = job['Project Identifier']
        job = dict()
        path = os.path.dirname(self.source)
        job['dirname'] = path
        job['files'] = self.locate_files(path, id)
        job['xml'] = file_name
        job['record'] = record
        # print "id: " + str(id)
        # print "dirname: " + str(dirname)
        # files = job
        self._queue.put(job)

    def show_jobs(self):
        replacement = Queue()
        while not self._queue.empty():
            item = self._queue.get()
            dirname = item['dirname']
            files = item['files']
            xml = item['xml']
            record = item['record']
            replacement.put(item)
            print(record['Object Identifier'])
            print(dirname)
            print(xml)
            for file in files:
                print(file)
            print("")
        self._queue = replacement

    def update_record(self, project_id, new_record):
        # print "updating project " + project_id
        replacement_records = []
        # record_to_update = self.get_record(project_id)
        if self._is_valid_record(new_record):
            for record in self._records:
                # print "running"
                if record['Project Identifier'] == project_id:
                    # print "found it"
                    replacement = OrderedDict()
                    replacement.update({'Date Created': new_record['Date Created']})
                    replacement.update({'Object ARK': new_record['Object ARK']})
                    replacement.update({'Timecode Content Begins': new_record['Timecode Content Begins']})
                    replacement.update({'Media Type': new_record['Media Type']})
                    replacement.update({'Interviewee': new_record['Interviewee']})
                    replacement.update({'Series Title': new_record['Series Title']})
                    replacement.update({'Temporal Coverage': new_record['Temporal Coverage']})
                    replacement.update({'Writer': new_record['Writer']})
                    replacement.update({'Institution URL': new_record['Institution URL']})
                    replacement.update({'Project Identifier': new_record['Project Identifier']})
                    replacement.update({'Quality Control Notes': new_record['Quality Control Notes']})
                    replacement.update({'Silent or Sound': new_record['Silent or Sound']})
                    replacement.update({'Camera': new_record['Camera']})
                    replacement.update({'Music': new_record['Music']})
                    replacement.update({'Editor': new_record['Editor']})
                    replacement.update({'Track Standard': new_record['Track Standard']})
                    replacement.update({'CONTENTdm number': new_record['CONTENTdm number']})
                    replacement.update({'Subtitles/Intertitles/Closed Captions': new_record['Subtitles/Intertitles/Closed Captions']})
                    replacement.update({'Distributor': new_record['Distributor']})
                    replacement.update({'Date modified': new_record['Date modified']})
                    replacement.update({'Subject Topic Authority Source': new_record['Subject Topic Authority Source']})
                    replacement.update({'Aspect Ratio': new_record['Aspect Ratio']})
                    replacement.update({'Total Number of Reels or Tapes': new_record['Total Number of Reels or Tapes']})
                    replacement.update({'Copyright Holder Info': new_record['Copyright Holder Info']})
                    replacement.update({'Running Speed': new_record['Running Speed']})
                    replacement.update({'Subject Entity Authority Source': new_record['Subject Entity Authority Source']})
                    replacement.update({'Additional Technical Notes for Overall Work': new_record['Additional Technical Notes for Overall Work']})
                    replacement.update({'Musician': new_record['Musician']})
                    replacement.update({'Main or Supplied Title': new_record['Main or Supplied Title']})
                    replacement.update({'Internet Archive URL': new_record['Internet Archive URL']})
                    replacement.update({'Relationship Type': new_record['Relationship Type']})
                    replacement.update({'Director': new_record['Director']})
                    replacement.update({'Copyright Statement': new_record['Copyright Statement']})
                    replacement.update({'Genre': new_record['Genre']})
                    replacement.update({'Cataloger Notes': new_record['Cataloger Notes']})
                    replacement.update({'Collection Guide URL': new_record['Collection Guide URL']})
                    replacement.update({'Interviewer': new_record['Interviewer']})
                    replacement.update({'Description or Content Summary': new_record['Description or Content Summary']})
                    replacement.update({'Institution': new_record['Institution']})
                    replacement.update({'Stock Manufacturer': new_record['Stock Manufacturer']})
                    replacement.update({'Sound': new_record['Sound']})
                    replacement.update({'Publisher': new_record['Publisher']})
                    replacement.update({'Asset Type': new_record['Asset Type']})
                    replacement.update({'Object Identifier': new_record['Object Identifier']})
                    replacement.update({'Copyright Date': new_record['Copyright Date']})
                    replacement.update({'Copyright Holder': new_record['Copyright Holder']})
                    replacement.update({'Language': new_record['Language']})
                    replacement.update({'Color and/or Black and White': new_record['Color and/or Black and White']})
                    replacement.update({'Institution ARK': new_record['Institution ARK']})
                    replacement.update({'CONTENTdm file name': new_record['CONTENTdm file name']})
                    replacement.update({'OCLC number': new_record['OCLC number']})
                    replacement.update({'Why the recording is significant to California/local history': new_record['Why the recording is significant to California/local history']})
                    replacement.update({'Subject Entity': new_record['Subject Entity']})
                    replacement.update({'Gauge and Format': new_record['Gauge and Format']})
                    replacement.update({'Additional Descriptive Notes for Overall Work': new_record['Additional Descriptive Notes for Overall Work']})
                    replacement.update({'Genre Authority Source': new_record['Genre Authority Source']})
                    replacement.update({'Date Published': new_record['Date Published']})
                    replacement.update({'Country of Creation': new_record['Country of Creation']})
                    replacement.update({'Project Note': new_record['Project Note']})
                    replacement.update({'Institutional Rights Statement (URL)': new_record['Institutional Rights Statement (URL)']})
                    replacement.update({'Spatial Coverage': new_record['Spatial Coverage']})
                    replacement.update({'Copyright Notice': new_record['Copyright Notice']})
                    replacement.update({'Subject Topic': new_record['Subject Topic']})
                    replacement.update({'Performer': new_record['Performer']})
                    replacement.update({'Relationship': new_record['Relationship']})
                    replacement.update({'Producer': new_record['Producer']})
                    replacement.update({'Cast': new_record['Cast']})
                    replacement.update({'Generation': new_record['Generation']})
                    replacement.update({'Transcript': new_record['Transcript']})
                    replacement.update({'Channel Configuration': new_record['Channel Configuration']})
                    replacement.update({'Date created': new_record['Date created']})
                    replacement.update({'Reference URL': new_record['Reference URL']})
                    replacement.update({'Call Number': new_record['Call Number']})
                    replacement.update({'Base Thickness': new_record['Base Thickness']})
                    replacement.update({'Base Type': new_record['Base Type']})
                    replacement.update({'Additional Title': new_record['Additional Title']})
                    replacement.update({'CONTENTdm file path': new_record['CONTENTdm file path']})
                    replacement.update({'Duration': new_record['Duration']})
                    replacement.update({'Speaker': new_record['Speaker']})
                    replacement.update({'Collection Guide Title': new_record['Collection Guide Title']})
                    replacement_records.append(replacement)
                else:
                    # print "not"
                    replacement_records.append(record)
        else:
            # print "No"
            pass
        self._records = replacement_records



    def _build_descriptive(self, record):
        obj_ID = ''
        proj_ID = ''
        asset_type = ''
        main_title = ''
        add_title = ''
        ser_title = ''
        inst_name = ''
        inst_URL = ''

        if record['Object Identifier']:
            obj_ID = record['Object Identifier'].split(';')[0].split('_t')[0].split('_r')[0].split('_a')[0]

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
            # description = record['Description or Content Summary']
            description = record['Description or Content Summary']
            if not description == "":
                descriptive.add_pbcoreDescription(PB_Element(['annotation', 'Content Summary'], tag="pbcoreDescription", value=description.strip()))
            else:
                descriptive.add_pbcoreDescription(PB_Element(['annotation', 'Content Summary'], tag="pbcoreDescription", value=""))

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


    def _build_physical(self, new_part, record):
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
        parts = new_part
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
            for part in parts:
                newInstPart = InstantiationPart(objectID=part, location=inst_name)
                newEss = InstantiationEssenceTrack(type="Audio", ips=speed, standard=track_standard)
                newInstPart.add_instantiationEssenceTrack(newEss)
                physical.add_instantiationPart(newInstPart)
            # new_xml = minidom.parseString(physical.xmlString())
            # print new_xml.toprettyxml(encoding='utf-8')

        elif media_type.lower() == 'moving image':
            physical.add_instantiationIdentifier(PB_Element(['source', "CAVPP"], tag="instantiationIdentifier", value=parts))
            newEss = InstantiationEssenceTrack(objectID=parts,
                                               frameRate=run_speed,
                                               aspectRatio=aspect_ratio,
                                               standard=track_standard)
            physical.add_instantiationEssenceTrack(newEss)
        # return inst_name, physical
        return physical


    def _build_preservation_master(self, record, preservation_file_set):
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
                                          location=self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource'),
                                          generations="Preservation Master",
                                          language=lang)



        # ============================================================ #
        # ======================== Audio only ======================== #
        # ============================================================ #
        if media_type.lower() == 'audio' or media_type.lower() == 'sound':
            top_id = obj_ID.split("_a")[0]
            top_id = top_id.split("_b")[0]
            pres_master.add_instantiationIdentifier(PB_Element(['source', self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                               tag="instantiationIdentifier",
                                                               value=top_id+"_prsv"))
            pres_master.set_instantiationMediaType(PB_Element(tag='instantiationMediaType',
                                                              value='Sound'))
            pres_master.add_instantiationRelation(InstantiationRelation(derived_from=top_id))

            for master_part in preservation_file_set:
                if os.path.splitext(master_part)[1] == ".iso":
                    f = FileObject(master_part)
                    new_mast_part = InstantiationPart(location=self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource'))
                else:
                    f = AudioObject(master_part)
                    new_mast_part = InstantiationPart(location=self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource'), duration=f.totalRunningTimeSMPTE)
                    if f.audioCodec:
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
                        try:
                            audio_codec = f.audioCodec + ": " + f.audioCodecLongName
                        except NoDataException:
                            audio_codec = f.audioCodec

                        pres_master.set_instantiationStandard(PB_Element(tag='instantiationStandard',
                                                                         value=audio_codec))

                        new_mast_part.add_instantiationEssenceTrack(newfile)
                file_size, file_units = self.sizeofHuman(f.file_size)
                new_mast_part.set_instantiationFileSize(PB_Element(['unitsOfMeasure',file_units],
                                                                   tag="instantiationFileSize",
                                                                   value=str(file_size)))
                new_mast_part.add_instantiationIdentifier(PB_Element(['source', self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                                     ['annotation', 'File Name'],
                                                                     tag="instantiationIdentifier",
                                                                     value=os.path.basename(master_part)))

                if self.calculate_checksums is True:

                    self._working_status = "Calculating MD5 checksum for " + f.file_name + " (" + f.file_size_human + ")"
                    if self.verbose:
                        print("\t"),
                        print("Part " + str(self._parts_progress+1) + " of " + str(self._parts_total) + ": ",)
                        logger.info("Calculating MD5 checksum for " + f.file_name + ".")
                        if f.file_size > LARGEFILE:
                            print("\tNote: " + f.file_name + " is " + f.file_size_human + " and might take some times to calculate.")
                        md5 = f.calculate_MD5(progress=True)
                    else:
                        f.calculate_MD5(threaded=True)
                        while f.isMD5Calculating:
                            self._calculation_percent = f.calulation_progresss
                            sleep(.1)
                        md5 = f.MD5_hash
                    new_mast_part.add_instantiationIdentifier(PB_Element(['source', self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                                         ['version', 'MD5'],
                                                                         ['annotation', 'checksum'],
                                                                         tag="instantiationIdentifier",
                                                                         value=md5))
                    sleep(.5)


                pres_master.add_instantiationPart(new_mast_part)
                self._parts_progress += 1




        # ============================================================ #
        # ======================= Moving Image ======================= #
        # ============================================================ #
        elif media_type.lower() == 'moving image':
            if os.path.splitext(preservation_file_set[0])[1] == ".iso":
                f = FileObject(preservation_file_set[0])
            else:
                f = VideoObject(preservation_file_set[0])
                try:
                    video_codec = str(f.videoCodec + ": " + f.videoCodecLongName)
                except NoDataException:
                    video_codec = str(f.videoCodec)

                pres_master.set_instantiationStandard(PB_Element(tag='instantiationStandard', value=video_codec))

                    # ---------- Video essence track ----------
                newfile = InstantiationEssenceTrack(type='Video',
                                                    frameRate=str(f.videoFrameRate),
                                                    duration=str(f.totalRunningTimeSMPTE),
                                                    # duration=trt(preservation_file_set[0]),
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

                if f.audioCodec:
                    newfile = InstantiationEssenceTrack(type='Audio',
                                                        samplingRate=f.audioSampleRate/1000,                      # isn't working currently so...
                                                        bitDepth=f.audioBitDepth)
                    try:
                        audio_codec = f.audioCodec + ": " + f.audioCodecLongName
                    except NoDataException:
                        audio_codec = f.audioCodec

                    newfile.set_essenceTrackStandard(PB_Element(tag='essenceTrackStandard',
                                                                value=audio_codec))
                    datarate = f.audioBitRateH.split(" ")
                    newfile.set_essenceTrackDataRate(PB_Element(['unitsOfMeasure', datarate[1]],
                                                                        tag="essenceTrackDataRate",
                                                                        value=datarate[0]))
                    pres_master.add_instantiationEssenceTrack(newfile)

            pres_master.set_instantiationMediaType(PB_Element(tag='instantiationMediaType', value='Moving Image'))

            pres_master.add_instantiationIdentifier(PB_Element(['source', self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                                   ['annotation', 'File Name'],
                                                                   tag="instantiationIdentifier",
                                                                   value=os.path.basename(preservation_file_set[0])))
            file_size, file_units = self.sizeofHuman(f.file_size)
            pres_master.set_instantiationFileSize(PB_Element(['unitsOfMeasure', file_units],
                                                             tag="instantiationFileSize",
                                                             value=str(file_size)))

            if self.calculate_checksums is True:
            # if not args.nochecksum and self.settings.getboolean('CHECKSUM', 'CalculateChecksums') is True:
                self._working_status = "Calculating MD5 checksum for " + f.file_name + " (" + f.file_size_human + ")"
                if self.verbose:
                    print("\t"),
                    print("Part " + str(self._parts_progress + 1) + " of " + str(self._parts_total) + ": ",)
                    logger.info("Calculating MD5 checksum for " + f.file_name + ".")
                    if f.file_size > LARGEFILE:
                        print("\tNote: This file is " + f.file_size_human + " and might take some times to calculate.")
                    md5 = f.calculate_MD5(progress=True)
                else:
                    f.calculate_MD5(threaded=True)
                    while f.isMD5Calculating:
                        self._calculation_percent = f._calculation_progress
                        sleep(.1)
                    md5 = f.MD5_hash
                pres_master.add_instantiationIdentifier(PB_Element(['source', self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                                   ['version', 'MD5'],
                                                                   ['annotation', 'checksum'],
                                                                   tag="instantiationIdentifier",
                                                                   value=md5))
                sleep(.5)

            self._parts_progress += 1





        if record['Quality Control Notes']:
            note = record['Quality Control Notes']
            pres_master.add_instantiationAnnotation(
                PB_Element(['annotationType', 'CAVPP Quality Control/Partner Quality Control'],
                           tag="instantiationAnnotation",
                           value=note.strip()))
        return pres_master

    def _build_access_copy(self, record, access_files_sets):
        lang = ''
        obj_ID = ''
        if record['Language']:
            lang = record['Language']
        if record['Object Identifier']:
            obj_ID = record['Object Identifier'].split(';')[0].split('_t')[0]

        media_type = ''
        if record['Media Type']:
            media_type = record['Media Type']
        access_copy = pbcoreInstantiation(type="Access Copy",
                                          location=self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource'),
                                          language=lang,
                                          # objectID=obj_ID.split("_a")[0]+"_access",
                                          generations="Access Copy")


        for access_part in access_files_sets:

            # print access_files_sets


        # ============================================================ #
        # =========================== Audio ========================== #
        # ============================================================ #
            if media_type.lower() == 'audio' or media_type.lower() == 'sound':
                access_copy.add_instantiationIdentifier(
                    PB_Element(['source', self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                               tag="instantiationIdentifier",
                               value=obj_ID.split("_a")[0]+"_access"))
                access_copy.add_instantiationRelation(InstantiationRelation(derived_from=obj_ID.split("_a")[0]+"_prsv"))
                f = AudioObject(access_part)
                newAudioFile = InstantiationPart(objectID=f.file_name,
                                                 location=self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource'),
                                                 duration=f.totalRunningTimeSMPTE)
                                                 # duration=trt(access_part))



                size, units = self.sizeofHuman(f.file_size)
                newAudioFile.set_instantiationFileSize(PB_Element(['unitsOfMeasure', units],
                                                                  tag="instantiationFileSize",
                                                                  value=size))
                if self.calculate_checksums is True:
                # if not args.nochecksum and self.settings.getboolean('CHECKSUM','CalculateChecksums') is True:
                    self._working_status = "Calculating MD5 checksum for " + f.file_name + " (" + f.file_size_human + ")"
                    if self.verbose:
                        print("\t"),
                        print("Part " + str(self._parts_progress + 1) + " of " + str(self._parts_total) + ": ",)
                        logger.info("Calculating MD5 checksum for " + f.file_name + ".")
                        if f.file_size > LARGEFILE:
                            print("\tNote: This file is " + f.file_size_human + " and might take some times to calculate.")
                        md5 = f.calculate_MD5(progress=True)
                    else:
                        f.calculate_MD5(threaded=True)
                        while f.isMD5Calculating:
                            self._calculation_percent = f.calulation_progresss
                            sleep(.1)
                        md5 = f.MD5_hash
                    newAudioFile.add_instantiationIdentifier(
                        PB_Element(['source', self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
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
                f = VideoObject(access_part)
                access_copy.add_instantiationIdentifier(PB_Element(['source', self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
                                                                   ['annotation', 'File Name'],
                                                                   tag="instantiationIdentifier",
                                                                   value=f.file_name))
                access_copy.set_instantiationMediaType(PB_Element(tag='instantiationMediaType', value='Moving Image'))
                access_copy.set_instantiationDuration(PB_Element(tag="instantiationDuration",
                                                                 value=f.totalRunningTimeSMPTE))  # Not working currently
                                                                 # value=trt(access_part)))          # Used as a patch for ^^
                try:
                    video_codec = str(f.videoCodec + ": " + f.videoCodecLongName)
                except NoDataException:
                    video_codec = str(f.videoCodec)

                access_copy.set_instantiationStandard(PB_Element(tag='instantiationStandard', value=video_codec))
                size, units = self.sizeofHuman(f.file_size)
                access_copy.set_instantiationFileSize(PB_Element(['unitsOfMeasure', units],
                                                                 tag="instantiationFileSize",
                                                                 value=size))
                if self.calculate_checksums is True:
                # if not args.nochecksum and self.settings.getboolean('CHECKSUM', 'CalculateChecksums') is True:
                    self._working_status = "Calculating MD5 checksum for " + f.file_name + " (" + f.file_size_human + ")"
                    if self.verbose:
                        print("\t"),
                        print("Part " + str(self._parts_progress + 1) + " of " + str(self._parts_total) + ": ",)
                        logger.info("Calculating MD5 checksum for " + f.file_name + ".")
                        if f.file_size > LARGEFILE:
                            print("\tNote: This file is " + f.file_size_human + " and might take some times to calculate.")
                        md5 = f.calculate_MD5(progress=True)
                    else:
                        f.calculate_MD5(threaded=True)
                        while f.isMD5Calculating:
                            self._calculation_percent = f.calulation_progresss
                            sleep(.1)
                        md5 = f.MD5_hash
                    access_copy.add_instantiationIdentifier(
                        PB_Element(['source', self.settings.get('PBCOREINSTANTIATION','InstantiationIdentifierSource')],
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
                                                        duration=f.totalRunningTimeSMPTE)     # Not currently working
                                                        # duration=trt(access_part))             # Used as a patch for ^^
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
                if f.audioCodec:
                    try:
                        audio_codec = f.audioCodec + ": " + f.audioCodecLongName
                    except NoDataException:
                        audio_codec = f.audioCodec

                    newEssTrack = InstantiationEssenceTrack(type='Audio',
                                                            standard=audio_codec,
                                                            samplingRate=f.audioSampleRate/1000)          # not currently Working
                                                            # samplingRate=audio_sample_rate(access_files))   # Used as a patch for ^^
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
            else:
                raise ValueError("Media Type expected Audio, Sound, or Moving Image, recieved " + media_type)
        return access_copy

    def save_csv(self, filename):
        # print "Saving " + filename
        with open(filename, 'w') as csvfile:
            # print self._records[0].keys()

            # fieldnames = ['number 1', 'number 2']
            fieldnames = ['Internet Archive URL',
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
            writer = csv.DictWriter(csvfile, fieldnames=officialList)
            writer.writeheader()
            for record in self._records:
                writer.writerow(record)
                # writer.writerow({"number 1": "asfdasdf", "number 2": "234234324"})

            pass


    def generate_pbcore(self, record, files=None, verbose=False):
        self._running = True
        XML = ""
        new_XML_file = PBCore(collectionSource=record['Institution'],
                              collectionTitle=record['Collection Guide Title'])
        if not files:
            # file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
            fileName = re.search(FILE_NAME_PATTERN, record['Object Identifier']).group(0)
            files = self.locate_files(os.path.abspath(self.source), fileName)

        preservation_file_sets, access_files_sets = sep_pres_access(files)
        self._parts_total = len(preservation_file_sets) + len(access_files_sets)
        preservation_file_sets = group_sides(preservation_file_sets)
        access_files_sets = group_sides(access_files_sets)


        # pbcoreDescriptionDocument
        # obj_ID = ""
        # proj_ID = ""
        # asset_type = ""
        main_title = ""
        # add_title = ""
        # ser_title = ""
        # descrp = ""
        # obj_ARK = ""
        inst_name = ""
        # inst_ARK = ""
        # inst_URL = ""
        # creationDates = []
        # subjectTops = ""
        # genre = ""
        # genre_autority = ""
        # IA_URL = ""
        # QC_notes_list = ""
        # transcript = ""

        ungrouped_tapes = record['Object Identifier'].split(';')

        # preservation, access = sep_pres_access()

        # if record['Object Identifier']:
        #     obj_ID = record['Object Identifier'].split(';')[0].split('_t')[0]
        #
        # if record['Project Identifier']:
        #     # pbcoreInstantiation.instantiationIdentifier is part of CAVPP_Part class
        #     proj_ID = record['Project Identifier']
        #
        # if record['Asset Type']:
        #     # pbcoreDescriptionDocument.pbcoreAssetType is in pbcoreDescriptionDocument()
        #     # pbcoreInstantiation.pbcoreAssetType is in pbcoreDescriptionDocument()
        #     asset_type = record['Asset Type']
        #
        if record['Main or Supplied Title']:
            main_title = record['Main or Supplied Title']

        # if record['Additional Title']:
        #     add_title = record['Additional Title']
        #
        # if record['Series Title']:
        #     ser_title = record['Series Title']
        #
        if record['Institution']:
            inst_name = record['Institution']
        #
        # if record['Institution URL']:
        #     inst_URL = record['Institution URL']


        # Build descriptive
        descriptive = self._build_descriptive(record)

        # PARTS
        call_numbers = ""
        if record['Call Number']:
            call_numbers = record['Call Number'].split(';')

    # =================
    # AUDIO ONLY
    # =================
        self._parts_progress = 0

        if record['Media Type'].lower() == 'audio' or record['Media Type'].lower() == 'sound':
        # PBcore Parts


            grouped_tapes = self._group_tapes(ungrouped_tapes)
            print("Grouped tapes size: " + str(len(grouped_tapes)))
            print("preservation_file_sets size: " + str(len(preservation_file_sets)))


            for tape_sides, preservation_file_set, access_files_set in zip(grouped_tapes, preservation_file_sets, access_files_sets):
                print(tape_sides)

                ob_id = tape_sides[0]
                ob_id = ob_id.split("_a")[0]

                # create the header of the PBCorePart
                if not record['Description or Content Summary'] == "":
                    new_part = CAVPP_Part(objectID=ob_id.strip(),
                                          mainTitle=main_title.strip(),
                                          description=record['Description or Content Summary'])
                else:
                    new_part = CAVPP_Part(objectID=ob_id.strip(),
                                          mainTitle=main_title.strip(),
                                          description="")

                for call_number in call_numbers:
                    new_part.add_pbcoreIdentifier(
                        PB_Element(['source', inst_name], ['annotation', 'Call Number'], tag='pbcoreIdentifier',
                                   value=call_number.strip()))
                # descriptive.add_pbcore_part(new_physical)
        # -----------------------------------------------------
        #           physical
        # -----------------------------------------------------
        #         print str(tape) + "tape"
                physical = self._build_physical(tape_sides, record)
                physical.add_instantiationIdentifier(PB_Element(['source', 'CAVPP'], tag='instantiationIdentifier', value=ob_id))
                new_part.add_pbcoreInstantiation(physical)

            # -----------------------------------------------------
            #           Preservation Master
            # -----------------------------------------------------

                if files:
                #     print("preservation_file_sets " + str(preservation_file_sets))
                #     print("access_files_sets " + str(preservation_file_sets))
                #
                #     if preservation_file_sets:
                #     for preservation_file_set in preservation_file_sets:
                    print(preservation_file_set)
                    pres_master = self._build_preservation_master(record, preservation_file_set)
                    new_part.add_pbcoreInstantiation(pres_master)


        #
        #
        # # -----------------------------------------------------
        # #           access copy
        # # -----------------------------------------------------
        #             if access_files_sets:
        #                 for access_files_set in access_files_sets:
                    print(access_files_set)
                    access_copy = self._build_access_copy(record, access_files_set)

                    new_part.add_pbcoreInstantiation(access_copy)
#
                    descriptive.add_pbcore_part(new_part)


    # =================
    # Moving Image ONLY
    # =================

        elif record['Media Type'].lower() == 'moving image':
            # print "moving image"
            for index, tape_sides in enumerate(ungrouped_tapes):
                if not record['Description or Content Summary'] == "":
                    new_part = CAVPP_Part(objectID=tape_sides.strip(),
                                         mainTitle=main_title.strip(),
                                         description=record['Description or Content Summary'])
                else:
                    new_part = CAVPP_Part(objectID=tape_sides.strip(),
                                         mainTitle=main_title.strip(),
                                         description="")
                for call_number in call_numbers:
                    new_part.add_pbcoreIdentifier(
                        PB_Element(['source', inst_name], ['annotation', 'Call Number'], tag='pbcoreIdentifier',
                                   value=call_number.strip()))
        # -----------------------------------------------------
        #           physical
        # -----------------------------------------------------
                physical = self._build_physical(tape_sides, record)
                new_part.add_pbcoreInstantiation(physical)
                # descriptive.add_pbcore_part(newPart)

        # -----------------------------------------------------
        #           Preservation Master
        # -----------------------------------------------------
        #     print preservation_file_sets[index]
        #         for preservation_file_set in preservation_file_sets:
        #             # print preservation_file_set
                if files:
                    global use_gui
                    dir_op = options = {}
                    options['defaultextension'] = "*.log"
                    options['initialfile'] = "PBCore_error_log_" + str(date.today().toordinal())

                    try:
                        pres_master = self._build_preservation_master(record, preservation_file_sets[index])
                        new_part.add_pbcoreInstantiation(pres_master)
                    except OExceptions.FormatException as error:


                        if use_gui:
                            save_error = askyesno("One Sheet Critical Error", str(error) +
                                                  "\nDo you wish to save the error information as a file?")
                            if save_error:
                                error_file = asksaveasfilename(**dir_op)
                                if error_file:
                                    traceback.print_exc(file=open(error_file, 'a'))
                                    print("Saved Error log to " + error_file)
                            self._working_status = "critical_error"
                        print("One Sheet Format error: " + str(error))

                        return False
                    except OExceptions.NoDataException as error:
                        print("One Sheet No Data error: " + str(error))
                        if use_gui:
                            save_error = askyesno("One Sheet Critical Error", str(error) + "\nDo you wish to save the error information as a file?")
                            if save_error:
                                error_file = asksaveasfilename(**dir_op)
                                if error_file:
                                    traceback.print_exc(file=open(error_file, 'a'))
                                    print("Saved Error log to " + error_file)
                                self._working_status = "critical_error"
                        return False


        # -----------------------------------------------------
        #           access copy
        # -----------------------------------------------------
        #         print access_files_sets[index][0]
                    access_copy = self._build_access_copy(record, access_files_sets[index])
                    new_part.add_pbcoreInstantiation(access_copy)
                    descriptive.add_pbcore_part(new_part)
        else:
            raise MediaTypeException(record['Project Identifier'])

        # Extension
        if record['Country of Creation']:
            exten = pbcoreExtension(exElement="countryOfCreation",
                                    exValue=record['Country of Creation'],
                                    exAuthority=self.settings.get('EXTRA', 'DefaultCountryAuthority'))
            descriptive.add_pbcore_extension(exten)

        if record['Project Note']:
            if record['Project Note'] == 'California Audiovisual Preservation Project (CAVPP)':
                exten = pbcoreExtension(exElement="projectNote",
                                        exValue='California Audiovisual Preservation Project',
                                        exAuthority='CAVPP')
            else:  # I don't know if this will be anything other than "California Audiovisual Preservation Project"
                exten = pbcoreExtension(exElement="projectNote",
                                        exValue=record['Project Note'],
                                        exAuthority='CAPS')
            descriptive.add_pbcore_extension(exten)
        elif self.settings.getboolean('EXTRA','UseDefaultProjectNote'):
            exten = pbcoreExtension(exElement="projectNote",
                                    exValue=self.settings.get('EXTRA', 'DefaultProjectNote'),
                                    exAuthority=self.settings.get('EXTRA', 'DefaultProjectNoteAuthority'))
            descriptive.add_pbcore_extension(exten)

        if len(ungrouped_tapes) > 1:
            for tape_sides in record['Object Identifier'].split(';'):
                newRelation = pbcoreRelation(reID=tape_sides.strip(), reType="Has Part")
                descriptive.add_pbcoreRelation(newRelation)
        new_XML_file.set_IntellectualContent(descriptive)
        self._running = False
        return new_XML_file.xmlString()



    def build_all_records(self):
        raise DeprecationWarning
        # file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
        self._job_total = len(self._records)

        self._job_progress = 0
        for record in self._records:
            fileName = re.search(FILE_NAME_PATTERN, record['Object Identifier']).group(0)
            file_output_name = fileName + "_PBCore.xml"
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

## Python 3
        if sys.version_info >= (3, 0):
            for heading in csv.reader(test_file).__next__():
                if not any(heading in s for s in officialList):
                    valid = False
                    mismatched.append("CSV title missing "
                                      + heading)
                    print(heading)
## Python 2
        else:
            for heading in csv.reader(test_file).next():
                if not any(heading in s for s in officialList):
                    valid = False
                    mismatched.append("CSV title missing "
                                      + heading)
                    print(heading)
        test_file.close()
        return valid, mismatched


        pass

    def valid_date(self, date):
        date_re = '(19||20)\d\d-(0[1-9]|1[012])-(0[1-9]|[1|2][0-9]|3[0-1])'
        if re.match(date_re, date):
            return True
        else:
            return False
        pass

    def _is_valid_record(self, record):
        if not isinstance(record, OrderedDict):
            raise TypeError("Expected OrderedDict. Recieved ", type(record))
        valid = True
        if 'Date Created' not in record:
            valid = False

        if 'Object ARK' not in record:
            valid = False

        if 'Timecode Content Begins' not in record:
            valid = False

        if 'Media Type' not in record:
            valid = False

        if 'Interviewee' not in record:
            valid = False

        if 'Series Title' not in record:
            valid = False

        if 'Temporal Coverage' not in record:
            valid = False

        if 'Writer' not in record:
            valid = False

        if 'Institution URL' not in record:
            valid = False

        if 'Project Identifier' not in record:
            valid = False

        if 'Quality Control Notes' not in record:
            valid = False

        if 'Silent or Sound' not in record:
            valid = False

        if 'Camera' not in record:
            valid = False

        if 'Music' not in record:
            valid = False

        if 'Editor' not in record:
            valid = False

        if 'Track Standard' not in record:
            valid = False

        if 'CONTENTdm number' not in record:
            valid = False

        if 'Subtitles/Intertitles/Closed Captions' not in record:
            valid = False

        if 'Distributor' not in record:
            valid = False

        if 'Date modified' not in record:
            valid = False

        if 'Subject Topic Authority Source' not in record:
            valid = False

        if 'Aspect Ratio' not in record:
            valid = False

        if 'Total Number of Reels or Tapes' not in record:
            valid = False

        if 'Copyright Holder Info' not in record:
            valid = False

        if 'Running Speed' not in record:
            valid = False

        if 'Subject Entity Authority Source' not in record:
            valid = False

        if 'Additional Technical Notes for Overall Work' not in record:
            valid = False

        if 'Musician' not in record:
            valid = False

        if 'Main or Supplied Title' not in record:
            valid = False

        if 'Internet Archive URL' not in record:
            valid = False

        if 'Relationship Type' not in record:
            valid = False

        if 'Director' not in record:
            valid = False

        if 'Copyright Statement' not in record:
            valid = False

        if 'Genre' not in record:
            valid = False

        if 'Cataloger Notes' not in record:
            valid = False

        if 'Collection Guide URL' not in record:
            valid = False

        if 'Interviewer' not in record:
            valid = False

        if 'Description or Content Summary' not in record:
            valid = False

        if 'Institution' not in record:
            valid = False

        if 'Stock Manufacturer' not in record:
            valid = False

        if 'Sound' not in record:
            valid = False

        if 'Publisher' not in record:
            valid = False

        if 'Asset Type' not in record:
            valid = False

        if 'Object Identifier' not in record:
            valid = False

        if 'Copyright Date' not in record:
            valid = False

        if 'Copyright Holder' not in record:
            valid = False

        if 'Language' not in record:
            valid = False

        if 'Color and/or Black and White' not in record:
            valid = False

        if 'Institution ARK' not in record:
            valid = False

        if 'CONTENTdm file name' not in record:
            valid = False

        if 'OCLC number' not in record:
            valid = False

        if 'Why the recording is significant to California/local history' not in record:
            valid = False

        if 'Subject Entity' not in record:
            valid = False

        if 'Gauge and Format' not in record:
            valid = False

        if 'Additional Descriptive Notes for Overall Work' not in record:
            valid = False

        if 'Genre Authority Source' not in record:
            valid = False

        if 'Date Published' not in record:
            valid = False

        if 'Country of Creation' not in record:
            valid = False

        if 'Project Note' not in record:
            valid = False

        if 'Institutional Rights Statement (URL)' not in record:
            valid = False

        if 'Spatial Coverage' not in record:
            valid = False

        if 'Copyright Notice' not in record:
            valid = False

        if 'Subject Topic' not in record:
            valid = False

        if 'Performer' not in record:
            valid = False

        if 'Relationship' not in record:
            valid = False

        if 'Producer' not in record:
            valid = False

        if 'Cast' not in record:
            valid = False

        if 'Generation' not in record:
            valid = False

        if 'Transcript' not in record:
            valid = False

        if 'Channel Configuration' not in record:
            valid = False

        if 'Date created' not in record:
            valid = False

        if 'Reference URL' not in record:
            valid = False

        if 'Call Number' not in record:
            valid = False

        if 'Base Thickness' not in record:
            valid = False

        if 'Base Type' not in record:
            valid = False

        if 'Additional Title' not in record:
            valid = False

        if 'CONTENTdm file path' not in record:
            valid = False

        if 'Duration' not in record:
            valid = False

        if 'Speaker' not in record:
            valid = False

        if 'Collection Guide Title' not in record:
            valid = False

        return valid


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


    def check_content_valid(self, test_records=None):
        if test_records is None:
            if not self._records:
                self.load_records()
            test_records = self._records
        # print test_records
        warnings = []
        errors = []
        # Validate all dates

        # test_record = csv.DictReader(f)


        for test_record in test_records:
            check_date_list = []
            check_date_list.append(["Date Created", test_record["Date Created"]])
            check_date_list.append(["Date Published", test_record["Date Published"]])

            for item in check_date_list:
                # print item
                warning = dict()
                if item[1] != "":
                    if not self.valid_date(item[1]):
                        warning['record'] = test_record['Project Identifier']
                        warning['received'] = item[1]
                        warning['location'] = item[0]
                        warning['type'] = 'Incorrect Format'
                        warning['message'] = 'Expected YYYY-MM-DD.'
                        # warnings.append("\""
                        #                 + item[1]
                        #                 + "\" in the \'"
                        #                 + item[0]
                        #                 + "\' column is not in the correct date format. Expected YYYY-MM-DD.")
                        warnings.append(warning)
            # check that there is a description
            if test_record['Description or Content Summary'] == '':
                warning = dict()
                warning['record'] = test_record['Project Identifier']
                warning['received'] = "No data"
                warning['location'] = "Description or Content Summary"
                warning['type'] = 'Missing Required Data'
                warning['message'] = 'There is no data for Description or Content Summary.'
                warnings.append(warning)
            #     warnings.append("Missing required \"Description or Content Summary\" field")

            # for index, error in enumerate(errors):
            # errors[index] = "["+ input_record["Object Identifier"] + "] " + errors[index]
            # for warning in warnings:
            #     print warning['record'] + ": Recieved \"" + warning['received'] + "\" at " + warning['location'] + ". " + warning['message']

            if not valid_object_id(test_record['Object Identifier']):
                error = dict()
                error['record'] = test_record['Project Identifier']
                error['received'] = test_record['Object Identifier']
                error['location'] = "Object Identifier"
                error['type'] = 'Incorrect Format'
                error['message'] = 'Expected \'[MARC Code]_[identifier]\'.'
                errors.append(error)
        return warnings, errors


    def locate_files(self, root, fileName):
        # search for file with fileName in it

        # search for file with fileName in it
        found_directory = None
        results = []
        # check if a directory matches the file name
        # for roots, dirs, files in os.walk(root):
        if os.path.isdir(root):
            for dir in os.listdir(root):
                if not dir.startswith('.'):
                    if fileName in dir:
                        if os.path.isdir(os.path.join(root, dir)):
                            found_directory = os.path.join(root, dir)
                            break
            # see of a file in that folder has a file with that name in it
            if found_directory:
                for roots, dirs, files, in os.walk(found_directory):
                    for file in files:
                        if not file.startswith('.'):
                            if fileName in file:
                                results.append(os.path.join(roots, file))
        return results

    def load_records(self):

        f = open(self.source, 'rU', errors='ignore')
        records = csv.DictReader(f)
        self._records = []
        for record in records:
            record = OrderedDict(record)
            # Python 3
            if sys.version_info >= (3, 0):
                pass
            # Python 2
            else:
                record['Object Identifier'] = record['Object Identifier'].translate('[]')
            self._records.append(record)

        f.close()
        # self._job_total = len(self._records)


    def check_files_exist(self):
        # file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
        files_not_found = []
        warnings = []
        self.load_records()
        for record in self._records:
            fileName = re.search(FILE_NAME_PATTERN, record['Object Identifier']).group(0)
            # logging.debug("Locating possible files for: " + fileName)
            digital_files = self.locate_files(self.source, fileName)
            if digital_files:
                # logger.debug("Files located for: " + fileName)
                preservation_files, access_files = sep_pres_access(digital_files)
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

                pass
        return warnings

    def _group_tapes(self, parts, files=None):
        # print "parts: " + str(parts)
        organized = []
        multi = []
        single = []
        for part in parts:
            if "_t" in part:
                if "_a" in part:
                    raise Exception("PLEASE BRING THIS EXAMPLE TO HENRY! HE'S BEEN LOOKING FOR ONE TO FIX THIS SHORTCOMING!")
                else:
                    single = [part]
                organized.append(single)
            else:
                single = parts
                organized.append(single)
                break
        return organized




    def get_record(self, project_id):
        # print "getting project: " + str(project_id)
        for record in self._records:
            if project_id == record['Project Identifier']:
                return record


    def run(self):
        # print "starting thread"
        self._running = True
        self._job_progress = 0
        while not self._queue.empty():
            queue = self._queue.get()
            record = queue['record']
            files = queue['files']
            # print record
            self._working_file = record['Project Identifier']
            self._working_status = 'Building'
            raw_xml = self.generate_pbcore(record, files)
            if not raw_xml:
                self._running = False
                return False
            new_xml = minidom.parseString(raw_xml)
            if not new_xml:
                self._running = False
                return False
            self._working_status = "Saving: " + queue['xml']
            # print "saving xml file " + queue['xml']
            save_file = open(queue['xml'], 'w')
            if sys.version_info >= (3, 0):
                save_file.write(new_xml.toprettyxml())
            else:
                save_file.write(new_xml.toprettyxml(encoding='utf-8'))

            save_file.close()
            self._job_progress += 1
        self._working_file = ""
        self._working_status = "Done"
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
        print(str(index + 1) + ")\t" + file_created)
    print("\n")


def proceed(message, warnings=None):
        key = ""
        print ("")
        while True:

            if warnings:
                print("\tWarnings:")
                print("\n\t**************************************************************\n")
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

                    print(warning_message)
                    # print str(index + 1) + ")\t" +warning['record'] + ": Recieved \"" + warning['received'] + "\" at " + warning['location'] + ". " + warning['message']
            print("\t**************************************************************")
            print("\n\t" + message)
            print("\n\tDo you wish to continue?",)
            key = raw_input("[y/n]:")
            if key.lower() == "yes":
                key = 'y'
            if key.lower() == "no":
                key = 'n'
            if key.lower() != 'y' and key.lower() != 'n':
                print("Not a valid option.\n")
            else:
                break

        if key.lower() == 'y':
            return True
        if key.lower() == 'n':
            return False






def group_sides(digital_files):
    set = []
    part = []
    if not digital_files:
        raise Exception
    if isinstance(digital_files, list):
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
    else:
        print(digital_files)
        raise TypeError("WHY????")
    # print "Set: " + str(set)
    return set

    pass


def sep_pres_access(digital_files):
    preservation = []
    access = []
    # part = []
    for file in digital_files:
        if "_prsv" in file and ".md5" not in file:
            preservation.append(file)

        elif "_access" in file and ".md5" not in file:
            access.append(file)

    return sorted(preservation), sorted(access)


def setup_logs():
    mode = "normal"
    records = []
    digital_files = []
    logger.setLevel(logging.DEBUG)
    logPath = os.path.dirname(SETTINGS.get('LOGS', 'LogFile'))
    if not os.path.exists(logPath):  # automatically create a logs folder if one doesn't already exist
        os.makedirs(logPath)
    if SETTINGS.getboolean('LOGS', 'UseLogs'):
        fh = logging.FileHandler(SETTINGS.get('LOGS', 'LogFile'))  # Saves all logs to this file
    eh = logging.StreamHandler(sys.stderr)  # sends any critical errors to standard error
    eh.setLevel(logging.WARNING)
    ch = logging.StreamHandler(sys.stdout)  # sends all debug info to the standard out
    ch.setLevel(logging.DEBUG)
    log_filter = RemoveErrorsFilter()
    ch.addFilter(log_filter)  # logger.addFilter(NoParsingFilter())
    if args.debug or SETTINGS.getboolean('EXTRA', 'DebugMode') is True:
        mode = 'debug'
        print("ENTERING DEBUG MODE!")
        if SETTINGS.getboolean('LOGS', 'UseLogs'):
            fh.setLevel(logging.DEBUG)
    else:
        if SETTINGS.getboolean('LOGS', 'UseLogs'):
            fh.setLevel(logging.INFO)
    if args.nochecksum or SETTINGS.getboolean('CHECKSUM', 'CalculateChecksums') is False:
        print("Bypassing MD5 checksum generation.")
    error_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # DATE - USERNAME - Message
    stderr_formatter = logging.Formatter('%(levelname)s - %(message)s')  # USERNAME - Message
    stdout_formatter = logging.Formatter('%(message)s')  # Message
    if SETTINGS.getboolean('LOGS', 'UseLogs'):
        fh.setFormatter(error_formatter)
        logger.addHandler(fh)
    eh.setFormatter(stderr_formatter)
    logger.addHandler(eh)
    ch.setFormatter(stdout_formatter)
    logger.addHandler(ch)
    return mode


def Validate_csv_file():
    logger.debug("Opening file:" + args.csv)
    if args.nochecksum:
        record_file = pbcoreBuilder(args.csv, verbose=True, settings=settingsFileName, calculate_checksums=False)
    else:
        record_file = pbcoreBuilder(args.csv, verbose=True, settings=settingsFileName)
    valid, error_message = record_file.is_valid_file(args.csv)
    if valid:
        logger.debug(args.csv + " successfully opened.")
        pass
    else:
        print("FAILED")
        logger.critical(error_message)
        print("Quiting")
        quit()
    logger.debug("Validating file is a csv.")
    if record_file.is_valid_csv():
        logger.debug(args.csv + " successfully validated as a CSV.")
    else:
        logger.critical("Error, cannot load file as a CSV.")
        print("FAILED")
        print("Quitting.")
        quit()
    logger.debug("Validating files column titles.")
    valid, errors = record_file.validate_col_titles()
    if valid:
        logger.debug(args.csv + " has valid columns headers.")
    else:
        sys.stdout.flush()
        for error in errors:
            logger.critical(error)
        quit()

    logger.debug("Validating files data.")

    return record_file


def validate_csv_data(record_file):
    total_warnings = []
    total_errors = []
    logger.debug("Validating data in CSV.")
    test_records = []
    f = open(args.csv, "rU")
    for record in csv.DictReader(f):
        test_records.append(record)
    f.close()
    warnings, errors = record_file.check_content_valid(test_records)
    total_warnings += warnings
    total_errors += errors
    sys.stdout.flush()
    if total_errors:
        for error in total_errors:
            print("Error found: " + error)
        if total_warnings:
            for warning in total_warnings:
                print("WARNINGS: " + warning)
        print("Quitting")
        quit()

    return total_errors, total_warnings


def report_warnings(mode, total_errors, total_warnings):
    sys.stdout.flush()
    if total_errors:
        for error in total_errors:
            print("Error found: " + error)
        if total_warnings:
            for warning in total_warnings:
                print("Warning: " + warning)
        print("Quitting")
        quit()
    if mode != 'debug':
        if total_warnings:
            key = ""
            for warning in total_warnings:
                logger.warning(warning)
            if proceed("Possible problems with the data found.", total_warnings) is False:
                logger.info("Script terminated by user.")
                print("Quitting")
                quit()
            else:
                print("\t"),
                logger.info("Warnings ignored.")


def generate_pbcore(record_file):
    print("")
    logging.info("Generating PBCore...")
    # record_file.build_all_records()
    # print record_file.overwritten_records
    # file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
    number_of_records = 0
    number_of_new_records = 0
    number_of_rewritten_records = 0
    # for record in record_file.records:
    # print record
    files_created = []
    for record in record_file.records:
        print("")
        fileName = re.search(FILE_NAME_PATTERN, record['Object Identifier']).group(0)
        logger.info("Producing PBCore XML for " + fileName + ".")
        file_output_name = fileName + "_PBCore.xml"
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
    logger.debug("Closing CSV file:")
    # f.close()
    # files_created = []
    # files_created += record_file.new_records
    # files_created += record_file.overwritten_records
    report(files_created, number_of_new_records, number_of_records, number_of_rewritten_records)


def main():
    global settingsFileName
    # settingsFileName = os.path.join(os.path.dirname(__file__), '../settings/pbcore-csv-settings.ini')
    # settingsFileName = os.path.join(os.path.dirname(__file__),'settings/pbcore-csv-settings.ini')
    # print __file__
    settingsFileName = os.path.join(os.path.dirname(__file__),'pbcore-csv-settings.ini')

    global SETTINGS
    global logger
    global args
    global use_gui
    SETTINGS = ConfigParser()
    try:
        isfile(settingsFileName)
        f = open(settingsFileName)
        f.close()
        SETTINGS.read(settingsFileName)
    except IOError:
        sys.stderr.write('Error: Cannot find ' + settingsFileName + '. Quiting\n')
        quit()

    logger = logging.getLogger()
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="Source CSV file", nargs='?', default="", type=str)
    parser.add_argument("-d", "--debug", help="Debug mode. Writes all messages to debug log.", action='store_true')
    parser.add_argument("-nc", "--nochecksum", help="Bypasses md5 checksum generation for files.", action='store_true')
    parser.add_argument("-np", "--noprogress", help="hides the percentage completed of the md5 checksum calculation.", action='store_true')
    parser.add_argument("-g", "--gui", help="EXPERIMENTAL: Loads the graphical user interface.", action='store_true')
    # TODO: add argument that lets you create pbcore without the files present
    args = parser.parse_args()

    if args.csv == "" and not args.gui:
        parser.print_help()
    elif args.gui:
        from PBCore.scripts.pbcore_csv_gui import start_gui
        use_gui = True
        if args.csv:
            print("Loading graphical user interface with: " + args.csv)
            start_gui(settings=os.path.abspath(settingsFileName), csvfile=args.csv)
        else:
            print("Loading graphical user interface")
            # print os.path.abspath(settingsFileName)
            start_gui(settings=os.path.abspath(settingsFileName))
    # elif args.csv != "" and args.gui:

    else:
        # ----------Setting up the logs----------
        mode = setup_logs()

        # ----------Validation of CSV file----------

        record_file = Validate_csv_file()

        # ---------- Validate data in CSV file ----------
        total_errors, total_warnings = validate_csv_data(record_file)
        # ---------- Locate all files mentioned in CSV ----------
        preservation_files = []
        access_files = []

        logger.debug("Locating files")
        total_warnings += record_file.check_files_exist()
        use_gui = False



            # ---------- Check if XML file already exists. ----------

        # file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
        for record in record_file.records:
            fileName = re.search(FILE_NAME_PATTERN, record['Object Identifier']).group(0)
            file_output_name = fileName + "_PBCore.xml"
            if isfile(file_output_name):
                warning = dict()
                warning['record'] = file_output_name
                warning['message'] = "File already exists. Do you wish to overwrite it?"
                total_warnings.append(warning)

            # ---------- Report errors and warning. ----------
        report_warnings(mode, total_errors, total_warnings)
        # ---------- Genereate PBCore XML Files ----------
        generate_pbcore(record_file)






if __name__ == '__main__':

        main()