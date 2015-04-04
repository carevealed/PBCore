import os
import string

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


    output_file = open(newname, 'w')
    input_file = open(sys.argv[1], 'r')
    a = csv.writer(output_file)
    tsv_file = csv.reader(input_file, dialect=csv.excel_tab)

    for line in tsv_file:
        print line
        print len(unicode(line))
        a.writerow(unicode(line))


    # input_file.seek(0)


    # a.writerows(tsv_file)
    # input_file.close()
    output_file.close()



if __name__ == "__main__":
    main()