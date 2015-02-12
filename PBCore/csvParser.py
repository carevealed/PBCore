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
    print "<XML>"
    print '\t<Project Identifier>' + record['Project Identifier'] + '</Project Identifier> '
    objectIDs = record['Object Identifier'].split(';')
    for objectID in objectIDs:
        print '\t<Object Identifier>' + objectID.lstrip() + '</Object Identifier> '
    print '\t<Internet Archive URL>' + record['Internet Archive URL'] + '</Internet Archive URL> '
    print '\t<Call Number>' + record['Call Number'] + '</Call Number> '

    if record['Call Number']:
        print '\t<Call Number>' + record['Call Number'] + '</Call Number>'

    if record['Project Identifier']:
        print '\t<Project Identifier>' + record['Project Identifier'] + '</Project Identifier>'

    if record['Project Note']:
        print '\t<Project Note>' + record['Project Note'] + '</Project Note>'

    if record['Institution']:
        print '\t<Institution>' + record['Institution'] + '</Institution>'

    if record['Asset Type']:
        print '\t<Asset Type>' + record['Asset Type'] + '</Asset Type>'

    if record['Media Type']:
        print '\t<Media Type>' + record['Media Type'] + '</Media Type>'

    if record['Generation']:
        print '\t<Generation>' + record['Generation'] + '</Generation>'

    if record['Main or Supplied Title']:
        print '\t<Main or Supplied Title>' + record['Main or Supplied Title'] + '</Main or Supplied Title>'

    if record['Additional Title']:
        print '\t<Additional Title>' + record['Additional Title'] + '</Additional Title>'

    if record['Series Title']:
        print '\t<Series Title>' + record['Series Title'] + '</Series Title>'

    if record['Description or Content Summary']:
        print '\t<Description or Content Summary>' + record['Description or Content Summary'] + '</Description or Content Summary>'

    if record['Why the recording is significant to California/local history']:
        print '\t<Why the recording is significant to California/local history>' + record['Why the recording is significant to California/local history'] + '</Why the recording is significant to California/local history>'

    if record['Producer']:
        print '\t<Producer>' + record['Producer'] + '</Producer>'

    if record['Director']:
        print '\t<Director>' + record['Director'] + '</Director>'

    if record['Writer']:
        print '\t<Writer>' + record['Writer'] + '</Writer>'

    if record['Interviewer']:
        print '\t<Interviewer>' + record['Interviewer'] + '</Interviewer>'

    if record['Performer']:
        print '\t<Performer>' + record['Performer'] + '</Performer>'

    if record['Country of Creation']:
        print '\t<Country of Creation>' + record['Country of Creation'] + '</Country of Creation>'

    if record['Date Created']:
        creationDates = record['Date Created'].split(';')
        for creationDate in creationDates:
            print '\t<Date Created>' + creationDate.lstrip() + '</Date Created>'

    if record['Date Published']:
        print '\t<Date Published>' + record['Date Published'] + '</Date Published>'

    if record['Copyright Statement']:
        print '\t<Copyright Statement>' + record['Copyright Statement'] + '</Copyright Statement>'

    if record['Gauge and Format']:
        print '\t<Gauge and Format>' + record['Gauge and Format'] + '</Gauge and Format>'

    if record['Total Number of Reels or Tapes']:
        print '\t<Total Number of Reels or Tapes>' + record['Total Number of Reels or Tapes'] + '</Total Number of Reels or Tapes>'

    if record['Duration']:
        print '\t<Duration>' + record['Duration'] + '</Duration>'

    if record['Silent or Sound']:
        print '\t<Silent or Sound>' + record['Silent or Sound'] + '</Silent or Sound>'

    if record['Color and/or Black and White']:
        print '\t<Color and/or Black and White>' + record['Color and/or Black and White'] + '</Color and/or Black and White>'

    if record['Camera']:
        print '\t<Camera>' + record['Camera'] + '</Camera>'

    if record['Editor']:
        print '\t<Editor>' + record['Editor'] + '</Editor>'

    if record['Sound']:
        print '\t<Sound>' + record['Sound'] + '</Sound>'

    if record['Music']:
        print '\t<Music>' + record['Music'] + '</Music>'

    if record['Cast']:
        print '\t<Cast>' + record['Cast'] + '</Cast>'

    if record['Interviewee']:
        print '\t<Interviewee>' + record['Interviewee'] + '</Interviewee>'

    if record['Speaker']:
        print '\t<Speaker>' + record['Speaker'] + '</Speaker>'

    if record['Musician']:
        print '\t<Musician>' + record['Musician'] + '</Musician>'

    if record['Publisher']:
        print '\t<Publisher>' + record['Publisher'] + '</Publisher>'

    if record['Distributor']:
        print '\t<Distributor>' + record['Distributor'] + '</Distributor>'

    if record['Language']:
        print '\t<Language>' + record['Language'] + '</Language>'

    if record['Subject Topic']:
        subjectTopics = record['Subject Topic'].split(';')
        for subjectTopic in subjectTopics:
            print '\t<Subject Topic>' + subjectTopic.lstrip() + '</Subject Topic>'

    if record['Subject Topic Authority Source']:
        print '\t<Subject Topic Authority Source>' + record['Subject Topic Authority Source'] + '</Subject Topic Authority Source>'

    if record['Subject Entity']:
        print '\t<Subject Entity>' + record['Subject Entity'] + '</Subject Entity>'

    if record['Subject Entity Authority Source']:
        print '\t<Subject Entity Authority Source>' + record['Subject Entity Authority Source'] + '</Subject Entity Authority Source>'

    if record['Genre']:
        print '\t<Genre>' + record['Genre'] + '</Genre>'

    if record['Genre Authority Source']:
        print '\t<Genre Authority Source>' + record['Genre Authority Source'] + '</Genre Authority Source>'

    if record['Spatial Coverage']:
        print '\t<Spatial Coverage>' + record['Spatial Coverage'] + '</Spatial Coverage>'

    if record['Temporal Coverage']:
        print '\t<Temporal Coverage>' + record['Temporal Coverage'] + '</Temporal Coverage>'

    if record['Collection Guide Title']:
        print '\t<Collection Guide Title>' + record['Collection Guide Title'] + '</Collection Guide Title>'

    if record['Collection Guide URL']:
        print '\t<Collection Guide URL>' + record['Collection Guide URL'] + '</Collection Guide URL>'

    if record['Relationship']:
        print '\t<Relationship>' + record['Relationship'] + '</Relationship>'

    if record['Relationship Type']:
        print '\t<Relationship Type>' + record['Relationship Type'] + '</Relationship Type>'

    if record['Aspect Ratio']:
        print '\t<Aspect Ratio>' + record['Aspect Ratio'] + '</Aspect Ratio>'

    if record['Running Speed']:
        print '\t<Running Speed>' + record['Running Speed'] + '</Running Speed>'

    if record['Timecode Content Begins']:
        print '\t<Timecode Content Begins>' + record['Timecode Content Begins'] + '</Timecode Content Begins>'

    if record['Track Standard']:
        print '\t<Track Standard>' + record['Track Standard'] + '</Track Standard>'

    if record['Channel Configuration']:
        print '\t<Channel Configuration>' + record['Channel Configuration'] + '</Channel Configuration>'

    if record['Subtitles/Intertitles/Closed Captions']:
        print '\t<Subtitles/Intertitles/Closed Captions>' + record['Subtitles/Intertitles/Closed Captions'] + '</Subtitles/Intertitles/Closed Captions>'

    if record['Stock Manufacturer']:
        print '\t<Stock Manufacturer>' + record['Stock Manufacturer'] + '</Stock Manufacturer>'

    if record['Base Type']:
        print '\t<Base Type>' + record['Base Type'] + '</Base Type>'

    if record['Base Thickness']:
        print '\t<Base Thickness>' + record['Base Thickness'] + '</Base Thickness>'

    if record['Copyright Holder']:
        print '\t<Copyright Holder>' + record['Copyright Holder'] + '</Copyright Holder>'

    if record['Copyright Holder Info']:
        print '\t<Copyright Holder Info>' + record['Copyright Holder Info'] + '</Copyright Holder Info>'

    if record['Copyright Date']:
        copyrightdates = record['Copyright Date'].split(';')
        for copyrightdate in copyrightdates:
            print '\t<Copyright Date>' + copyrightdate.lstrip() + '</Copyright Date>'

    if record['Copyright Notice']:
        print '\t<Copyright Notice>' + record['Copyright Notice'] + '</Copyright Notice>'

    if record['Institutional Rights Statement (URL)']:
        print '\t<Institutional Rights Statement (URL)>' + record['Institutional Rights Statement (URL)'] + '</Institutional Rights Statement (URL)>'

    if record['Object ARK']:
        print '\t<Object ARK>' + record['Object ARK'] + '</Object ARK>'

    if record['Institution ARK']:
        print '\t<Institution ARK>' + record['Institution ARK'] + '</Institution ARK>'

    if record['Institution URL']:
        print '\t<Institution URL>' + record['Institution URL'] + '</Institution URL>'

    if record['Quality Control Notes']:
        QCNotes = record['Quality Control Notes'].split(';')
        for QCNote in QCNotes:
            print '\t<Quality Control Notes>' + QCNote.lstrip() + '</Quality Control Notes>'

    if record['Additional Descriptive Notes for Overall Work']:
        print '\t<Additional Descriptive Notes for Overall Work>' + record['Additional Descriptive Notes for Overall Work'] + '</Additional Descriptive Notes for Overall Work>'

    if record['Additional Technical Notes for Overall Work']:
        print '\t<Additional Technical Notes for Overall Work>' + record['Additional Technical Notes for Overall Work'] + '</Additional Technical Notes for Overall Work>'

    if record['Transcript']:
        print '\t<Transcript>' + record['Transcript'] + '</Transcript>'

    if record['Cataloger Notes']:
        print '\t<Cataloger Notes>' + record['Cataloger Notes'] + '</Cataloger Notes>'

    if record['OCLC number']:
        print '\t<OCLC number>' + record['OCLC number'] + '</OCLC number>'

    if record['Date modified']:
        print '\t<Date modified>' + record['Date modified'] + '</Date modified>'

    if record['Reference URL']:
        print '\t<Reference URL>' + record['Reference URL'] + '</Reference URL>'

    if record['CONTENTdm number']:
        print '\t<CONTENTdm number>' + record['CONTENTdm number'] + '</CONTENTdm number>'

    if record['CONTENTdm file name']:
        print '\t<CONTENTdm file name>' + record['CONTENTdm file name'] + '</CONTENTdm file name>'

    if record['CONTENTdm file path']:
        print '\t<CONTENTdm file path>' + record['CONTENTdm file path'] + '</CONTENTdm file path>'

    print "</XML>"


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

    print "Validating columns headers:",
    for index, heading in enumerate(csv.reader(f).next()):

        # print(index, heading, officialList[index])
        if heading != officialList[index]:
            print "FAILED"
            raise ValueError("Expected " + officialList[index] + " received " + heading)
    print "VALID"
    f.seek(0)

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