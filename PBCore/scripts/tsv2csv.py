import codecs
import os
import string
from time import sleep
import unicodedata

__author__ = 'California Audio Visual Preservation Project'
__module__ = 'TSV to CSV File Converter'
__date__ = '2015'
__credits__ = ['Henry Borchers']

import csv
import sys

def banner():
    print(__author__)
    print(__module__)
    print(__date__)
    for credit in __credits__:
        print credit
    print("")



def main():
    banner()
    if len(sys.argv) > 2 or len(sys.argv) < 1:
        sys.stderr("Error: expected only one CSV file as an argument.")

    newname = os.path.splitext(sys.argv[1])[0] + ".csv"
    print "Saving a new csv files as: " + newname

    # import codecs
    # test = codecs.open(sys.argv[1], encoding='utf-8')
    # for line in test:
    #     print line
    # test.close()
    # quit()
    with open(newname, 'w') as output_file:
        with codecs.open(sys.argv[1], 'r', 'UTF-8') as input_file:
            cleanstring = input_file.read()
            cleanstring = cleanstring.encode('UTF-8', errors='ignore')
            cleanFile = csv.StringIO(cleanstring)
            #
            tsv_file = csv.reader(cleanFile, dialect=csv.excel_tab)
            a = csv.writer(output_file)


            for n in tsv_file:
                a.writerow(n)
                print n
                print "n"

                # print len(unicode(line))
                # print len(unicode(line))


    # input_file.seek(0)


    # a.writerows(tsv_file)
    # input_file.close()
    # output_file.close()



if __name__ == "__main__":
    main()