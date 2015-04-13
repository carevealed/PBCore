# CAVPP PBCore Tools

Description
===========
Generates PBCore xml files from data exported from CONTENTdm and derives technical metadata from any data files 
that are located in the same folder.

To Install
==========

You have a few options. You most likely want to use the first one as it is the easiest. 


Option 1: Install binary (Wheel)
--------------------------------

1. Download the latest version from the releases section of the project's Github page https://github.com/cavpp/PBCore/releases and save it to your Downloads folder.
2. Open a terminal and type:
    
        cd Downloads
        sudo pip install CAVPP_PBCore_Tools-0.1.2-py2.py3-none-any.whl

#### Notes: 


The actual name of the file will change with each version.

If you have a problem that pip isn't installed, you can install it with the following command.
 
        sudo easy_install pip


Option 2: pip
-------------

1. Download the latest version (or eariler) in the dist folder to your Download folder
2. In a terminal window, type:

        cd Downloads
        sudo pip install CAVPP PBCore Tools-0.1.tar.gz

3. Enter your computer password and the script will install along with all the dependencies. 



Option 3: From source using Setuptools
--------------------------------------

1. Open a terminal window and type:

        cd Downloads
        git clone https://github.com/cavpp/PBCore.git
        cd PBCore
        sudo python setup.py install 
        
2. Enter your computer password and the script will install along with all the dependencies.

To Use
======

**Note:** This currently will only work with CSV and not the tab-delimited txt files that are saved directly by 
CONTENTdm. In order to use this files you must convert them first. See below instructions on how to convert the this 
file into a properly-formatted csv files.

To use with the command line:
-----------------------------
In a terminal, simply type "makepbcore" followed by a csv files containing the data from a CONTENTdm export.

    
### Example

    
    makepbcore /Volumes/CAPPS-01/Headlands/Headlands_caps_export.txt
            
  
  
To use the graphical user interface:
------------------------------------
In a terminal windows, simple type the following command::
  
    makepbcore -g
    
    
To convert ContentDM tab-delimited files to CSV files:
------------------------------------------------------
In a terminal window, type "tsv2csv" and the file name.

### Example

    tsv2csv /Volumes/CAPPS-01/Headlands/Headlands_caps_export.txt

Credits
=======
Author: Henry Borchers 