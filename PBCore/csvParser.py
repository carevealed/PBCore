import sys

__author__ = 'lpsdesk'
import csv

def checkTitles(row):
    print "Testing rows to see if they match expected:",
    for index, title in enumerate(row):
        if title != officialList[index]:
            raise ValueError(title + " does not match up with expected heading, " + officialList[index])
    print "PASS"

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



def main():
    f = None

    try:
        print "Opening file:",
        f = open('/Users/lpsdesk/PycharmProjects/PBcore/sample_records/casauhs_export.csv', 'rU')
    except IOError:
        print "FAILED"
        sys.stderr.write("Error, cannot find file.\n")
        print "Quitting"
        quit()
    print "OPEN"

    try:
        print "Loading file as CVS:",
        csv1 = csv.DictReader(f)
    except ValueError:
        print "FAILED"
        sys.stderr.write("Error, cannot load file as a CSV.\n")
        print "Quitting"
        quit()
    print "OK"
    for row in csv1:

        # print "\t" + str(row) + ":",
        print "\t" + str(row['Project Identifier']) + ":",
        # TODO create XML generatation code here
        print "DONE"
    print "Closing the file"
    f.close()
    print "File closed"
    print "Done"



if __name__ == '__main__':
    main()