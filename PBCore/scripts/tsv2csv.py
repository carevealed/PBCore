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
    print("")
    print("**************************************************")
    print(__author__)
    print(__module__)
    print(__date__)
    print("\nCredits:")
    for credit in __credits__:
        print "  " + credit
    print("**************************************************")
    print("")
    sys.stdout.flush()



def main():
    banner()
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        sys.stderr.write("Error: expected only one CSV file as an argument.\n")
        quit()

    newname = os.path.splitext(sys.argv[1])[0] + ".csv"
    print("Saving a new csv files as: " + newname)

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
                print "  " + n[3]
            print("\nDone\n")





if __name__ == "__main__":
    main()