# audio_convert
CAVPP PBCore Generator script

Description
===========
Generates PBCore xml files from data exported from CONTENTdm and derivates technical metadata from any data files 
that are located in the same folder.

To Install
==========

You have two options:


Option 1: Standard
------------------

1. Open a terminal window and type:

        cd Downloads
        git clone https://github.com/cavpp/PBCore.git
        cd PBCore
        sudo python setup.py install 
        
2. Enter your computer password and the script will install along with all the dependencies.


Option 2: pip
-------------

1. Download the latest version in the dist folder to your Download folder
2. In a terminal window, type:

        cd Downloads
        sudo pip install CAVPP_Audio_Convert-0.1.1.tar.gz

3. Enter your computer password and the script will install along with all the dependencies. 

**Note:** If you have a problem that pip isn't installed, you can install it with 
 the following command.
 
        sudo easy_install pip


To Use
======

**Note:** This currently will only work with CSV and not the tab-delimited txt files that are saved directly by 
CONTENTdm. In order to use this files you must convert them first. See below instructions on how to convert the this 
file into a properly-formatted csv files.

To use with the command line:
-----------------------------
In a terminal, simply type "makepbcore" followed by a csv files containing the data from a CONTENTdm export.

    
### Example

    
    makpbcore /Volumes/CAPPS-01/Headlands/Headlands_caps_export.txt
            
  
  
To use the graphical user interface:
------------------------------------
In a terminal windows, simple type the following command::
  
    makpbcore -g

Credits
=======
Author: Henry Borchers 