CSV Batch Import Script
=======================
This script takes a comma-separated values csv file and converts the information into PBCore records according to the scheme adapted by California Audio Visual Preservation Project.

Usage:
______

Simply add the csv file as an argument to the script csvParser.py::

    python csvParser.py casauhs_export.csv

Optional arguments:
+++++++++++++++++++

+----------+-------------+---------------------------------------------------------+
| Argument | Setting     | Description                                             |
+==========+=============+=========================================================+
|-d        | Debug mode. | This prints all debug messages to the screen as well the|
|          |             | log files.                                              |
+----------+-------------+---------------------------------------------------------+

Notes:
______
* This script works with comma-separated values (.csv) files only. Tab-separated values (.tsv) files are currently not supported. To use these files, convert them first into csv format.
* The csv file must not contain any unicode.
* Log files are created in a log folder.


Mapping:
________
TODO: Add the mapping information to PBCore