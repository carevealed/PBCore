from collections import OrderedDict
from platform import system
import tkFileDialog
import tkMessageBox
import webbrowser

__author__ = 'California Audio Visual Preservation Project'
__copyright__ = "California Audiovisual Preservation Project. 2015"
__credits__ = ["Henry Borchers"]
__version__ = "0.1"
__license__ = 'GPL'

import csv
import os
from time import sleep
from tkFileDialog import askopenfilename
from tkMessageBox import showerror

import threading
from Tkinter import *
import ttk

FILE_NAME_PATTERN = re.compile("[A-Z,a-z]+_\d+")

# DEFAULT_PATH = None

class MainWindow():
    def __init__(self, master, input_file=None, settings=None):
        if input_file:
            self.default_path = os.path.dirname(input_file)
        else:
            self.default_path = None
        self.master = master
        self.settings = settings
        self.updated = False
        self.csv_status = ""
        self.item_total = IntVar()
        self.item_total.set(0)
        self.item_progress = IntVar()
        self.item_progress.set(0)
        self.records_edited = False

        self.part_total = IntVar()
        self.part_total.set(0)
        self.part_progress = IntVar()
        self.part_total.set(0)

        self.display_records = []
        # -------------------- Menus --------------------
        self.master.option_add('*tearOff', False)
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)
        self.fileMenu = Menu(self.menu_bar)
        self.recordMenu = Menu(self.menu_bar)
        self.settingsMenu = Menu(self.menu_bar)
        self.helpMenu = Menu(self.menu_bar)

        self.menu_bar.add_cascade(menu=self.fileMenu, label="File")
        self.menu_bar.add_cascade(menu=self.recordMenu, label="Record")
        self.menu_bar.add_cascade(menu=self.settingsMenu, label="Settings")
        self.menu_bar.add_cascade(menu=self.helpMenu, label="Help")

        self.recordMenu.add_command(label="Change Export Name...")
        self.recordMenu.add_command(label="More Info...")


        self.fileMenu.add_command(label="Open...", command=self.load_csv)
        self.fileMenu.entryconfig('Open...', accelerator='Ctrl + O')
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=lambda: quit())

        self.settingsMenu.add_command(label="View Settings File...", command=self.view_settings)

        self.helpMenu.add_command(label="PBCore Website",
                                  command=lambda: webbrowser.open_new("http://pbcore.org/"))
        self.helpMenu.add_separator()
        self.helpMenu.add_command(label="CAVPP Website",
                                  command=lambda: webbrowser.open_new("http://calpreservation.org/projects/audiovisual-preservation/"))
        self.helpMenu.add_command(label="Github Source",
                                  command=lambda: webbrowser.open_new("https://github.com/cavpp/PBCore"))
        self.helpMenu.add_separator()
        self.helpMenu.add_command(label="About...",
                                  command=self.load_about_window)


        # -------------------- Background --------------------
        self.background = ttk.Frame(self.master, padding=(20,10))
        self.background.pack(fill=BOTH, expand=True)

        # -------------------- Title --------------------
        self.titleFrame = ttk.Frame(self.background,
                                    height=100,
                                    width=200,
                                    padding=(30, 15))
                                    # relief=GROOVE)
        self.titleFrame.pack(fill=BOTH)
        self.titleLabel = ttk.Label(self.titleFrame,
                                    text="CAVPP PBCore Generator",
                                    font=('TkDefaultFont', 30, 'bold')).pack()


        self.allInfoFrame = ttk.Frame(self.background)
        self.allInfoFrame.pack(fill=BOTH, expand=True)


        self.panel = ttk.Panedwindow(self.allInfoFrame, orient=VERTICAL)
        self.panel.pack(fill=BOTH, expand=True)
        # self.panel.grid(row=2, column=0, sticky=W+E+S+N)
        #
        # self.testButton = ttk.Button(self.background, text='test', command=self.test)
        # self.testButton.pack()


        # -------------------- Input Information --------------------
        self.dataEntryFrame = ttk.Frame(self.panel,
                                        height=100,
                                        width=100,
                                        padding=(30, 15),
                                        relief=SUNKEN)
        # self.dataEntryFrame.grid(row=2, column=1)
        self.panel.add(self.dataEntryFrame, weight=0)

        self.csv_filename_label = ttk.Label(self.dataEntryFrame,
                                            text="CSV file",
                                            width=10)
        self.csv_filename_label.grid(row=2, column=0, sticky=E)
        self.csv_filename_entry = ttk.Entry(self.dataEntryFrame, width=80)
        self.csv_filename_entry.grid(row=2, column=1, columnspan=5, sticky=W+E)

        self.locateCSVButton = ttk.Button(self.dataEntryFrame,
                                          text='Browse',
                                          command=self.load_csv)
        self.locateCSVButton.grid(row=2, column=6, sticky=W+E)



        self.save_csvButton = ttk.Button(self.dataEntryFrame,
                                      text='Save',
                                      command=self.save_csv)
        # self.set_record_edited(False)
        self.set_record_edited(True)
        self.save_csvButton.grid(row=3, column=6, sticky=W+E)

        self.validate_label = ttk.Label(self.dataEntryFrame, text='File Status:')
        self.validate_label.grid(row=3, column=0, sticky=W)
        self.validate_entry = ttk.Entry(self.dataEntryFrame, state=DISABLED)
        self.validate_entry.grid(row=3, column=1, sticky=W+E)
        self.validate_details_button = ttk.Button(self.dataEntryFrame, text='Details', command=self.show_details)
        self.validate_details_button.grid(row=3, column=2, sticky=W)

        # -------------------- Records --------------------
        self.recordsFrame = ttk.Frame(self.panel,
                                               height=200,
                                               width=100,
                                               padding=(5, 5),
                                               relief=SUNKEN)

        self.panel.add(self.recordsFrame, weight=10)

        # self.recordsList = Listbox(self.recordsFrame)
        self.recordsTree = ttk.Treeview(self.recordsFrame, columns=('title', 'project', 'files', 'xml_file'))
        self.recordsTree.heading('xml_file', text='Save As')
        self.recordsTree.heading('title', text='Title')
        self.recordsTree.heading('project', text='Project')
        self.recordsTree.heading('files', text='Files')
        self.recordsTree.column('#0', width=30, stretch=NO)
        self.recordsTree.column('project', minwidth=100, width=100, stretch=NO)
        self.recordsTree.column('files', minwidth=100, width=100, stretch=NO)
        self.recordsTree.column('title', minwidth=200,width=250, stretch=NO)
        self.recordsTree.column('xml_file', width=300)
        self.recordsTree.pack(fill=BOTH, expand=True)

        if system() == 'Darwin':
            self.recordsTree.bind("<Button-2>", self._popup)
        else:
            self.recordsTree.bind("<Button-3>", self._popup)
        self.recordsTree.bind("<Double-Button-1>", lambda e: self.view_item_details(self.recordsTree.selection()))

        # --------------------  Feedback  --------------------
        self.feedbackFrame = ttk.Frame(self.panel,
                                       height=200,
                                       width=100,
                                       padding=(30, 15),
                                       relief=SUNKEN)
        # self.feedbackFrame.grid(row=3, column=1, sticky=W)
        self.panel.add(self.feedbackFrame)
        self.total_progress_label = ttk.Label(self.feedbackFrame, text="Total:")
        self.total_progress_label.grid(row=0, column=0, sticky=E)
        self.total_progress_value_label = ttk.Label(self.feedbackFrame, text="(0/0)")
        self.total_progress_value_label.grid(row=0, column=1, sticky=E)
        self.total_progress_pbar = ttk.Progressbar(self.feedbackFrame, orient=HORIZONTAL, length=500, mode='determinate',value=self.item_progress.get(), maximum=self.item_total.get())
        self.total_progress_pbar.grid(row=0, column=2, sticky=W)

        self.part_progress_label = ttk.Label(self.feedbackFrame, text="Part:")
        self.part_progress_label.grid(row=1, column=0, sticky=E)
        self.part_progress_value_label = ttk.Label(self.feedbackFrame, text="(0/0)")
        self.part_progress_value_label.grid(row=1, column=1, sticky=E)
        self.part_progress_pbar = ttk.Progressbar(self.feedbackFrame, orient=HORIZONTAL, length=500, mode='determinate', value=self.part_progress.get(), maximum=self.part_total.get())
        self.part_progress_pbar.grid(row=1, column=2, sticky=W)

        self.calculation_progress_label = ttk.Label(self.feedbackFrame, text="Calculation:")
        self.calculation_progress_label.grid(row=2, column=0, sticky=E)
        self.calculation_progress_value_label = ttk.Label(self.feedbackFrame, text="0%")
        self.calculation_progress_value_label.grid(row=2, column=1, sticky=E)
        self.calculation_progress_pbar = ttk.Progressbar(self.feedbackFrame, orient=HORIZONTAL, length=500, maximum=100, mode='determinate')
        self.calculation_progress_pbar.grid(row=2, column=2, sticky=W)

    # --------------------  status bar --------------------
        self.startFrame = ttk.Frame(self.background)
        self.startFrame.pack()
        self.startButton = ttk.Button(self.startFrame,
                                      text='Start',
                                      command=self.start)
        self.startButton.config(state="disabled")
        self.startButton.pack()

    # --------------------  status bar --------------------
        self.statusBar = Label(self.master, text="", bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)

     # -------------------- Context Menu --------------------

        self.propertyMenu = Menu(self.recordsTree, tearoff=0)
        self.propertyMenu.add_command(label="Change Export Name...", command=lambda: self.change_export(self.recordsTree.selection()))
        self.propertyMenu.add_command(label="Edit...", command=lambda: self.view_item_details(self.recordsTree.selection()))


# ============================= Load the data into tree =============================
        if input_file:
            self.csv_filename_entry.insert(0, input_file)
            if self.validate_file(input_file):
                self.file_records = pbcore_csv.pbcoreBuilder(input_file)
                self.file_records.load_records()
                self.load_records_list(self.file_records.records)

        self.running = False

        if input_file:
            self.startButton.config(state=NORMAL)
    def _popup(self, event):
        # self.propertyMenu.post()
        if self.recordsTree.selection():
            # print "gotcha", self.recordsTree.selection()
            self.propertyMenu.post(event.x_root, event.y_root)


    def view_item_details(self, record):
        item_record = record[0]
        project_id = self.recordsTree.set(item_record)['project']
        xml = self.recordsTree.set(item_record)['xml_file']

        # print(project_id)
        itemsRoot = Toplevel(self.master)
        itemsRoot.wm_title("Details: " + project_id)
        view_record = self.file_records.get_record(project_id)
        # print view_record
        item = RecordDetailsWindow(itemsRoot, view_record, path=os.path.dirname(self.file_records.source), xml=xml)
        # print self.recordsTree.set(item_record)['xml_file']
        itemsRoot.wait_window()
        if item.shouldUpdate:
            # print self.recordsTree.set(item_record)['xml_file']
            self.recordsTree.set(item_record, column="xml_file", value=item.xml_file)

            self.file_records.update_record(project_id, item.newRecord)
            self.update_status_bar("Updated record: " + project_id)
            self.set_record_edited(True)

            self.load_records_list(self.file_records.records)
            warnings, errors = self.validate_records(self.file_records)
            self.update_messages(warnings)



    def change_export(self, record):
        # print "Changing Name of " + record[0]
        f = tkFileDialog.asksaveasfilename(defaultextension=".xml",
                                           initialdir=os.path.dirname(self.recordsTree.set(record[0], column="xml_file")),
                                           initialfile=os.path.basename(self.recordsTree.set(record[0], column="xml_file")),
                                           filetypes=[("XML", "*.xml")])
        if f:
            # print "changing to " + f
            self.recordsTree.set(record[0], column="xml_file", value=f)

    def load_about_window(self):
        aboutRoot = Toplevel(self.master)
        aboutRoot.wm_title("About")
        aboutRoot.resizable(FALSE,FALSE)
        about = AboutWindow(aboutRoot)

    def show_details(self):
        if self.remarks:
            self.alerts(self.remarks)

    def load_csv(self):
        fileName = askopenfilename(filetypes=[("CSV", "*.csv")])
        if fileName != "":
            self.default_path = os.path.dirname(fileName)
            self.csv_filename_entry.delete(0, END)
            self.csv_filename_entry.insert(0, fileName)
            if self.validate_file(fileName):
                self.file_records = pbcore_csv.pbcoreBuilder(fileName)
                self.file_records.load_records()
                self.load_records_list(self.file_records.records)

            else:
                for i in self.recordsTree.get_children():
                    self.recordsTree.delete(i)
            self.records_edited = False
            self.startButton.config(state=NORMAL)
        else:
            self.startButton.config(state=DISABLED)


    def view_settings(self):
        settingsRoot = Toplevel(self.master)
        # settingsRoot.wm_title("Settings")
        settings = SettingsWindow(settingsRoot, self.settings)
        settingsRoot.wait_window()

    def alerts(self, messages, alert_type="Error"):
        try:
            self.alertRoot.destroy()
        except:
            pass
        self.alertRoot = Toplevel(self.master)
        self.alertRoot.wm_title(alert_type)
        alerts = AlertWindow(self.alertRoot, messages, self.csv_filename_entry.get())
        # alertRoot.wait_window()


    def validate_records(self, records):
        warnings, errors = records.check_content_valid()
        return warnings, errors

    def update_messages(self, messages):
        self.remarks = []
        self.remarks += messages
        if self.remarks:
            self.alerts(self.remarks, alert_type="Warnings")
            self.csv_status = "Warnings"
            self.validate_entry.config(state=NORMAL)
            self.validate_entry.delete(0,END)
            self.validate_entry.insert(0, "Warning: Click details for more info.")
            self.validate_entry.config(state=DISABLED)
            self.validate_details_button.config(state=NORMAL)


    def validate_file(self, in_file):
        if os.path.isfile(in_file):

            testFile = pbcore_csv.pbcoreBuilder(in_file)
            if testFile.is_valid_csv():

                valid, messages = testFile.validate_col_titles()

                if valid:
                    self.validate_entry.config(state=NORMAL)
                    self.validate_entry.delete(0,END)
                    self.validate_entry.insert(0, "Valid")
                    self.csv_status = "Valid"
                    self.startButton.config(state=NORMAL)
                    self.validate_details_button.config(state=DISABLED)
                    self.validate_entry.config(state=DISABLED)
                else:
                    self.validate_entry.config(state=NORMAL)
                    self.validate_entry.delete(0,END)
                    self.validate_entry.insert(0, "Error: CSV file not valid.")
                    self.validate_entry.config(state=DISABLED)
                    self.startButton.config(state=DISABLED)
                    return False


                warnings, errors = self.validate_records(testFile)

                self.update_messages(warnings)
                return True

                # for error in total_errors:
                #     print error

            else:
                self.validate_entry.config(state=NORMAL)
                self.validate_entry.delete(0,END)
                errorMessage = "Not Valid CSV file"
                self.validate_entry.insert(0, errorMessage)
                self.csv_status = "Errors"
                self.startButton.config(state=DISABLED)
                self.validate_details_button.config(state=NORMAL)
                self.validate_entry.config(state=DISABLED)
                self.alerts(self.remarks, type="Error")
                showerror('Error', errorMessage)

                # self.warningMessageWindow.lift(self.master)
                return False

        else:
            self.validate_entry.config(state=NORMAL)
            self.validate_entry.delete(0,END)
            self.validate_entry.insert(0, "File Not Found")
            self.validate_entry.config(state=DISABLED)
            return False

    def load_records_list(self, records):
        # self.recordsList.delete(0, END)
        for i in self.recordsTree.get_children():
            self.recordsTree.delete(i)
        for index, record in enumerate(records):

            fileName = re.search(FILE_NAME_PATTERN, record['Object Identifier']).group(0)
            parts = record['Object Identifier'].split(';')

            media_files = locate_files(root=os.path.dirname(self.csv_filename_entry.get()), fileName=fileName)
            pres, access = sep_pres_access(media_files)
            media_files = pres + access

            outIndex = record['Main or Supplied Title']
            self.recordsTree.insert('', index, outIndex, text=index+1)
            self.recordsTree.set(outIndex, 'title', record['Main or Supplied Title'])
            self.recordsTree.set(outIndex, 'project', record['Project Identifier'])
            self.recordsTree.set(outIndex, 'files', str(len(media_files)) + " Files Found")

            self.recordsTree.set(outIndex, 'xml_file', (fileName + "_PBCore.xml"))

            if self.default_path:
                xml_file_name = os.path.join(self.default_path, (fileName + "_PBCore.xml"))
            else:
                xml_file_name = (fileName + "_PBCore.xml")
            self.recordsTree.set(outIndex, 'xml_file', xml_file_name)

            # for a_index, media_file in enumerate(media_files):
            #     inIndex = str(a_index)+outIndex
            #     self.recordsTree.insert(outIndex, a_index, inIndex)
            #     self.recordsTree.set(inIndex, 'files', os.path.basename(media_file.strip()))


    def get_records(self, file_name):
        f = open(file_name, 'rU')
        records = []
        for item in csv.DictReader(f):
            records.append(item)
        # self.records = csv.DictReader(f)
        f.close()
        return records

    def save_csv(self):
        if tkMessageBox.askokcancel("Are You Sure?", "Are you sure you want to save changes to " + os.path.basename(self.csv_filename_entry.get()) + "?"):
            self.file_records.save_csv(self.csv_filename_entry.get())
    def start(self):

        if self.running is False:
            self.display_records = []
            self.display_records = self.get_records(self.csv_filename_entry.get())
            self.set_total_progress(progress=0, total=10)

            # if self.validate_file(self.csv_filename_entry.get()):
            xml_content = pbcore_csv.pbcoreBuilder(self.csv_filename_entry.get())
            xml_content.load_records()
            for record in self.recordsTree.get_children():
                output = self.recordsTree.set(record)
                savefile = os.path.dirname(self.csv_filename_entry.get())
                savefile = os.path.join(savefile, output['xml_file'])

                foo = xml_content.get_record(output['project'])
                xml_content.add_job(foo, savefile)
            self.generate = observer(xml_content)
            self.generate.daemon = True
            self.generate.start()
            self.update_progress()

            self.running = True
        else:
            self.total_progress_pbar.stop()
            self.running = False
    def update_status_bar(self, message):
        self.statusBar.config(text=message)

    def update_progress(self):
            # print str(self.generate.item_progress) + "/" + str(self.generate.record_total)
        record_total = self.generate.record_total
        record_progress = self.generate.record_progress
        part_total = self.generate.part_total
        part_progress = self.generate.part_progress
        calulation_percent = self.generate.calulation_progress

        self.set_total_progress(record_progress, record_total)
        self.set_part_progress(part_progress, part_total)
        self.set_calculation_progress(self.generate.calulation_progress)
        self.set_calculation_progress(calulation_percent)
        self.update_status_bar(self.generate.status)
        # parts = str(part_progress) + " : " + str(part_total)
        # total = str(record_progress) + " : " + str(record_total)
        # print(parts, total)
        if self.generate.is_alive():
            self.master.after(100, self.update_progress)
        else:
        # self.master.after(200)
            self.generate.join()
            # print self.generate.calulation_progress
            self.set_total_progress(record_progress, record_total)
            self.set_part_progress(part_progress, part_total)
            self.set_calculation_progress(self.generate.calulation_progress)
            self.set_calculation_progress(calulation_percent)

    def test(self):
        # foo = pbcore_csv.pbcoreBuilder(self.csv_filename_entry.get())
        # foo.load_records()
        # # print foo.source
        # for record in self.recordsTree.get_children():
        #     print(self.recordsTree.set(record))
        # # foo.get_record("adfa")
        # for test in self.file_records.records:
        test_record = {'Date Created': '6/26/58', 'Object ARK': 'ark:/13030/c8m61n3r', 'Timecode Content Begins': '', 'Media Type': 'Sound', 'Interviewee': '', 'Series Title': '', 'Temporal Coverage': '', 'Writer': '', 'Institution URL': 'http://www.cityofsacramento.org/ccl/history/', 'Project Identifier': 'cavpp002554', 'Quality Control Notes': 'Vendor Tech Notes:  Clicks and Pops on Tape; very little content on side b. seems to be an outtake with  fluctuating volume. Speed: 33 1/3 RPM. Direction: Outside In    CAVPP QC Notes:  a: *psrv file includes markers with annotations on the waveform in Wavelab. Is this from MP QC? Crackle, pops and clicks.  b: Crackle, pops and clicks. Distorted in last 20 seconds. *Duplicate segment do not keep. Remove _a from name. Re-embed.    ', 'Silent or Sound': 'Sound', 'Camera': '', 'Music': '', 'Editor': '', 'Track Standard': '', 'CONTENTdm number': '57', 'Subtitles/Intertitles/Closed Captions': '', 'Distributor': '', 'Date modified': '1/28/15', 'Subject Topic Authority Source': '', 'Aspect Ratio': '', 'Total Number of Reels or Tapes': '1 disc of 1', 'Copyright Holder Info': '', 'Running Speed': '', 'Subject Entity Authority Source': '', 'Additional Technical Notes for Overall Work': '', 'Musician': '', 'Main or Supplied Title': 'Max and Buddy Baer Interview with Regis Philbin', 'Internet Archive URL': 'https://archive.org/details/casacsh_000048', 'Relationship Type': '', 'Director': '', 'Copyright Statement': 'Copyright status unknown. This work may be protected by the U.S. Copyright Law (Title 17, U.S.C.). In addition, its reproduction may be restricted by terms of gift or purchase agreements, donor restrictions, privacy and publicity rights, licensing and trademarks. This work is accessible for purposes of education and research. Transmission or reproduction of works protected by copyright beyond that allowed by fair use requires the written permission of the copyright owners. Works not in the public domain cannot be commercially exploited without permission of the copyright owner. Responsibility for any use rests exclusively with the user. Center for Sacramento History attempted to find rights owners without success but is eager to hear from them so that we may obtain permission, if needed. Upon request to csh@cityofsacramento.org, digitized works can be removed from public view if there are rights issues that need to be resolved.', 'Genre': '', 'Cataloger Notes': '', 'Collection Guide URL': '', 'Interviewer': '', 'Description or Content Summary': 'An interview on a 78 rpm record of the Baer brothers - heavyweight boxers (Max being a former world champion) and Sacramento residents with a young Regis Philbin of KSON radio in San Diego.', 'Institution': 'Center for Sacramento History', 'Stock Manufacturer': '', 'Sound': '', 'Publisher': '', 'Asset Type': 'Media Object', 'Object Identifier': 'casacsh_000048', 'Copyright Date': '', 'Copyright Holder': '', 'Language': '', 'Color and/or Black and White': '', 'Institution ARK': 'ark:/13030/tf7779p65f', 'CONTENTdm file name': 'http://archive.org/details/', 'OCLC number': '', 'Why the recording is significant to California/local history': 'An interview on a 78 rpm record of the Baer brothers - heavyweight boxers (Max being a former world champion) and Sacramento residents with a young Regis Philbin of KSON radio in San Diego.', 'Subject Entity': '', 'Gauge and Format': '[LP Record]', 'Additional Descriptive Notes for Overall Work': '', 'Genre Authority Source': '', 'Date Published': '', 'Country of Creation': 'US', 'Project Note': 'California Audiovisual Preservation Project (CAVPP)', 'Institutional Rights Statement (URL)': '', 'Spatial Coverage': '', 'Copyright Notice': '', 'Subject Topic': '', 'Performer': '', 'Relationship': '', 'Producer': '', 'Cast': '', 'Generation': 'Copy', 'Transcript': '', 'Channel Configuration': '', 'Date created': '3/17/14', 'Reference URL': 'http://cdm15972.contentdm.oclc.org:80/cdm/ref/collection/p15972coll52/id/57', 'Call Number': '2000/189', 'Base Thickness': '', 'Base Type': '', 'Additional Title': '', 'CONTENTdm file path': 'http://archive.org/details/', 'Duration': '', 'Speaker': '', 'Collection Guide Title': ''}
        self.file_records.update_record("cavpp002554", test_record)

    def set_total_progress(self, progress, total=None):
        if total:
            self.item_total.set(total)
            # print progress
        self.item_progress.set(progress)

        self.total_progress_value_label.config(text="(" + str(progress) + "/" + str(self.item_total.get()) + ")")
        self.total_progress_pbar.config(maximum=total, value=progress)

    def set_part_progress(self, progress, total=None):
        if total:
            self.part_total.set(total)
        self.part_progress.set(progress)
        # print self.part_total.get()
        self.part_progress_value_label.config(text="(" + str(progress) + "/" + str(self.part_total.get()) + ")")
        self.part_progress_pbar.config(maximum=total, value=progress)

    def set_calculation_progress(self, percent):
        self.calculation_progress_value_label.config(text = (str(percent)+'%'))
        self.calculation_progress_pbar.config(value=percent)

    def set_record_edited(self, value):
        if not isinstance(value, bool):
            raise ValueError("Expected boolean. Recieved: " + str(type(value)))
        self.records_edited = value
        if value:
            self.save_csvButton.config(state=NORMAL)
        else:
            self.save_csvButton.config(state=DISABLED)

        pass


class AboutWindow():
    def __init__(self, master):
        self.master = master
        self.master.resizable(width=None, height=None)
        self.background = ttk.Frame(self.master, width=20, padding=10)
        self.background.pack(fill=BOTH, expand=True)

# ----------------- Title
        self.titleFrame = ttk.Frame(self.background, width=20, padding=10, relief=RIDGE)
        self.titleFrame.pack()
        # print os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images/CAVPPcolor.gif')
        self.logo = PhotoImage(file=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images/CAVPPcolor.gif'))
        self.titleLabel = ttk.Label(self.titleFrame, text="CAVPP PBCore Builder", image=self.logo, compound=TOP)
        self.titleLabel.pack()
        self.versionLabel = ttk.Label(self.titleFrame, text="Version: " + __version__)
        self.versionLabel.pack()

# ----------------- More info
        self.moreInfoframe = ttk.Labelframe(self.background, text="Info")
        self.moreInfoframe.pack(fill=BOTH, expand=True)

        self.copyrightTitleLabel = ttk.Label(self.moreInfoframe, text="Copyright:")
        self.copyrightTitleLabel.grid(column=0, row=0, sticky=W+N)
        self.copyrightDataLabel = ttk.Label(self.moreInfoframe, text=__copyright__)
        self.copyrightDataLabel.grid(column=1, row=0, sticky=W)

        self.LicenseTitleLabel = ttk.Label(self.moreInfoframe, text="License:")
        self.LicenseTitleLabel.grid(column=0, row=1, sticky=W+N)
        self.LicenseDataLabel = ttk.Label(self.moreInfoframe, text=__license__)
        self.LicenseDataLabel.grid(column=1, row=1, sticky=W)

        self.creditsTitleLabel = ttk.Label(self.moreInfoframe, text="Credits:")
        self.creditsTitleLabel.grid(column=0, row=2, sticky=W+N)
        names = ""
        for credit in __credits__:
            names = names + credit + "\n"
        self.creditsdataLabel = ttk.Label(self.moreInfoframe, text=names)
        self.creditsdataLabel.grid(column=1, row=2, sticky=W)

        self.closeButton = ttk.Button(self.background, text="Close", command=lambda: self.master.destroy())
        self.closeButton.pack(side=BOTTOM)





class SettingsWindow():
    def __init__(self, master, settingFile):
        f = open(settingFile)
        self.master = master
        self.master.resizable(False, False)
        self.master.title("Settings")
        # --------
        self.settingsBackgroundFrame = ttk.Frame(self.master, padding=(5,5))
        self.settingsBackgroundFrame.pack(fill=BOTH, expand=True)

        # --------
        self.settingsFrame = ttk.Labelframe(self.settingsBackgroundFrame, text=settingFile, padding=(10,10))
        self.settingsFrame.pack(padx=5, pady=5, fill=BOTH, expand=True)
        self.scrollbar = Scrollbar(self.settingsFrame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.settingsText = Text(self.settingsFrame, yscrollcommand=self.scrollbar.set)
        self.settingsText.pack(fill=BOTH, expand=True)
        self.scrollbar.config(command=self.settingsText.yview)
        closeButton = ttk.Button(self.settingsBackgroundFrame, text="Close", command=lambda: self.master.destroy())
        closeButton.pack()

        for line in f.readlines():
            self.settingsText.insert(END, line)
        f.close()

        self.settingsText.config(state=DISABLED)

class observer(threading.Thread):
    def __init__(self, records):
        threading.Thread.__init__(self)
        if not isinstance(records, pbcore_csv.pbcoreBuilder):
            raise TypeError
        self.records = records
        self.records.load_records()
        self._record_progress = 0
        self._record_total = self.records.job_total
        self._isRunning = False
        self._part_progress = 0
        self._part_total = 0
        self._md5_progress = 0
        self._status = ''

    def run(self):
        self._isRunning = True
        self.records.daemon = True
        self.records.start()
        # self.records.build_all_records()
        while self.records.isAlive():
            sleep(.1)
            self._md5_progress = self.records.calculation_percent
            self._part_progress = self.records.parts_progress
            self._part_total = self.records.parts_total
            self._record_progress = self.records.job_progress
            self._status = self.records.working_file + ": " + self.records.working_status
        self.records.join()
        self._record_total = self.records.job_total
        self._md5_progress = self.records.calculation_percent
        self._part_progress = self.records.parts_progress
        self._part_total = self.records.parts_total
        self._record_progress = self.records.job_progress
        self._status = "Done"


        sleep(1)

        # print "\ndone"
        # for index, record in enumerate(self.records.records):
        #     print "Record: " + str(index)
        #     print self.records.source
        #     temp = self.records.generate_pbcore(record)
        #     self._record_progress = index + 1
        #     # for p_index, part in enumerate(self.records.records):
        #     #     print p_index
        #     # temp = self.records.generate_pbcore(record)
        #     # print "parts" + str(self.records.parts_total)
        #     # for part_index in range(1, self.records.parts_total):
        #     #     print "part" + part_index
        #     #     sleep(.01)
        #     #     self._part_progress = part_index + 1
        #     # for i in range(0, 100, 1):
        #     #     # print i
        #     #     self._md5_progress = i
        #     #     sleep(.01)
        #     # sleep(.25)
        # self._isRunning = False

    @property
    def status(self):
        return self._status

    @property
    def isRunning(self):
        return self._isRunning

    @property
    def record_progress(self):
        return self._record_progress

    @property
    def record_total(self):
        return self._record_total

    @property
    def part_progress(self):
        return self._part_progress

    @property
    def part_total(self):
        return self._part_total

    @property
    def calulation_progress(self):
        # print self._md5_progress
        return self._md5_progress

def locate_files(root, fileName):


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

def sep_pres_access(digital_files):
        preservation = []
        access = []
        # part = []
        for file in digital_files:
            if "_prsv" in file and ".md5" not in file:
                preservation.append(file)

            elif "_access" in file and ".md5" not in file:
                access.append(file)
        return preservation, access

def start_gui(settings, csvfile=None):
    root = Tk()
    root.wm_title('PBCore Generator')
    # global settingsFile
    # # if settings:
    # # settingsFile = settings
    # self.settings = settings
    if csvfile:
        app = MainWindow(root, input_file=csvfile, settings=settings)
    else:
        app = MainWindow(root)
    # root.option_add('*tearOff', False)
    root.mainloop()

class RecordDetailsWindow():
    #TODO Make a singleton
    def __init__(self, master, record, path=None,xml=None):
        if not isinstance(record, OrderedDict):
            raise TypeError("Expected OrderedDict. Recieved " + str(type(record)))
        self.xml = xml
        self.csv = csv
        # self.project_id = projectID
        self.filepath = path
        self.current_record = record
        self.style = ttk.Style()
        self.style.configure('labels.TLabel', wraplength=200)
        self.style.configure('labels.TEntry', width=350)
        self.master = master
        self.shouldUpdate = False
        self.updated = False
        self.newRecord = OrderedDict()
        # print "new records details: " + projectID + " in " + csv
        # data = pbcore_csv.pbcoreBuilder(self.csv)
        # data.load_records()
        # self.properties = data.get_record(projectID)
        self._init_date_created = self.current_record['Date Created']
        self._init_object_ark = self.current_record['Object ARK']
        self._init_timecode_content_begins = self.current_record['Timecode Content Begins']
        self._init_media_type = self.current_record['Media Type']
        self._init_interviewee = self.current_record['Interviewee']
        self._init_series_title = self.current_record['Series Title']
        self._init_temporal_coverage = self.current_record['Temporal Coverage']
        self._init_writer = self.current_record['Writer']
        self._init_institution_URL = self.current_record['Institution URL']
        self._init_project_identifier = self.current_record['Project Identifier']
        self._init_quality_control_notes = self.current_record['Quality Control Notes']
        self._init_silent_or_sound = self.current_record['Silent or Sound']
        self._init_camera = self.current_record['Camera']
        self._init_music = self.current_record['Music']
        self._init_editor = self.current_record['Editor']
        self._init_track_standard = self.current_record['Track Standard']
        self._init_contentdm_number = self.current_record['CONTENTdm number']
        self._init_subtitles = self.current_record['Subtitles/Intertitles/Closed Captions']
        self._init_distributor = self.current_record['Distributor']
        self._init_date_modified = self.current_record['Date modified']
        self._init_subject_topic_authority_source = self.current_record['Subject Topic Authority Source']
        self._init_aspect_ratio = self.current_record['Aspect Ratio']
        self._init_total_number_of_reels_or_tapes = self.current_record['Total Number of Reels or Tapes']
        self._init_copyright_holder_info = self.current_record['Copyright Holder Info']
        self._init_running_speed = self.current_record['Running Speed']
        self._init_subject_entity_authority_source = self.current_record['Subject Entity Authority Source']
        self._init_additional_technical_notes_for_overall_work = self.current_record['Additional Technical Notes for Overall Work']
        self._init_musician = self.current_record['Musician']
        self._init_main_or_supplied_title = self.current_record['Main or Supplied Title']
        self._init_internet_archive_url = self.current_record['Internet Archive URL']
        self._init_relationship_type = self.current_record['Relationship Type']
        self._init_director = self.current_record['Director']
        self._init_copyright_statement = self.current_record['Copyright Statement']
        self._init_genre = self.current_record['Genre']
        self._init_cataloger_notes = self.current_record['Cataloger Notes']
        self._init_collection_guide_url = self.current_record['Collection Guide URL']
        self._init_interviewer = self.current_record['Interviewer']
        self._init_description_or_content_summary = self.current_record['Description or Content Summary']
        self._init_institution = self.current_record['Institution']
        self._init_stock_manufacturer = self.current_record['Stock Manufacturer']
        self._init_sound = self.current_record['Sound']
        self._init_publisher = self.current_record['Publisher']
        self._init_asset_type = self.current_record['Asset Type']
        self._init_object_identifier = self.current_record['Object Identifier']
        self._init_copyright_date = self.current_record['Copyright Date']
        self._init_copyright_holder = self.current_record['Copyright Holder']
        self._init_language = self.current_record['Language']
        self._init_color_and_or_black_and_white = self.current_record['Color and/or Black and White']
        self._init_institution_ark = self.current_record['Institution ARK']
        self._init_contentdm_file_name = self.current_record['CONTENTdm file name']
        self._init_OCLC_number = self.current_record['OCLC number']
        self._init_why_significant_CA = self.current_record['Why the recording is significant to California/local history']
        self._initial_subject_entity = self.current_record['Subject Entity']
        self._init_gauge_and_format = self.current_record['Gauge and Format']
        self._init_addit_descrpt_nts_overall_wrk = self.current_record['Additional Descriptive Notes for Overall Work']
        self._init_genre_authority_source = self.current_record['Genre Authority Source']
        self._init_date_published = self.current_record['Date Published']
        self._init_country_of_creation = self.current_record['Country of Creation']
        self._init_project_note = self.current_record['Project Note']
        self._init_institutional_rights_statement_URL = self.current_record['Institutional Rights Statement (URL)']
        self._init_spatial_coverage = self.current_record['Spatial Coverage']
        self._init_copyright_notice = self.current_record['Copyright Notice']
        self._init_subject_topic = self.current_record['Subject Topic']
        self._init_performer = self.current_record['Performer']
        self._init_relationship = self.current_record['Relationship']
        self._init_producer = self.current_record['Producer']
        self._init_cast = self.current_record['Cast']
        self._init_generation = self.current_record['Generation']
        self._init_transcript = self.current_record['Transcript']
        self._init_channel_configuration = self.current_record['Channel Configuration']
        self._init_date_created1 = self.current_record['Date created']
        self._init_reference_url = self.current_record['Reference URL']
        self._init_call_number = self.current_record['Call Number']
        self._init_base_thickness = self.current_record['Base Thickness']
        self._init_base_type = self.current_record['Base Type']
        self._init_additional_title = self.current_record['Additional Title']
        self._init_contentdm_file_path = self.current_record['CONTENTdm file path']
        self._init_duration = self.current_record['Duration']
        self._init_speaker = self.current_record['Speaker']
        self._init_collection_guide_title = self.current_record['Collection Guide Title']

        # ------------ background --------------
        self.background = ttk.Frame(self.master, padding=(10,10))
        self.background.pack(fill=BOTH, expand=True)

        # ------------ Title --------------
        self.titleFrame = ttk.Frame(self.background, padding=(10,10), relief=RIDGE)
        self.titleFrame.pack(pady=20)
        self.label = ttk.Label(self.titleFrame, text="Details")
        self.label.pack()
        # ------------ XML file --------------
        self.xmlFrame = ttk.Frame(self.background, padding=(10,10))
        self.xmlFrame.pack(fill=X)
        self.xmlFrame.grid_columnconfigure(0, weight=0)
        self.xmlFrame.grid_columnconfigure(1, weight=1)
        self.xmlFrame.grid_columnconfigure(2, weight=0)


        self.xmlLabel = ttk.Label(self.xmlFrame, text="Save XML record as:")
        self.xmlLabel.grid(column=0, row=0, sticky=W)

        self._xmlEntry = ttk.Entry(self.xmlFrame)
        self._xmlEntry.grid(column=1, row=0, sticky=W+E)

        if xml:
            self._xmlEntry.insert(0, xml)
            self._init_xml = xml
        else:
            self.xml = ""
        self.xmlSaveAsButton = ttk.Button(self.xmlFrame, text="Save As", command=self.save_as)
        self.xmlSaveAsButton.grid(column=2, row=0, sticky=E)
        # ------------- panel -------------

        self.panel = ttk.PanedWindow(self.background, orient=VERTICAL)
        self.panel.pack(fill=BOTH, expand=True)


        # ------------ data --------------

        # self.dataOuterFrame = ttk.Frame(self.background, padding=(10,10))
        self.dataOuterFrame = ttk.Frame(self.background, relief=SUNKEN, padding=(2,2))
        # self.dataOuterFrame.pack(fill=BOTH, expand=True)
        self.panel.add(self.dataOuterFrame, weight=4)
        self.vscrollbar = Scrollbar(self.dataOuterFrame, orient=VERTICAL)
        self.vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.canvas=Canvas(self.dataOuterFrame, yscrollcommand=self.vscrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
        self.vscrollbar.config(command=self.canvas.yview)

        # self.dataFrame = Frame(self.canvas)
        self.dataFrame = interior = ttk.Frame(self.canvas)
        # self.dataFrame.pack()
        interior_id = self.canvas.create_window(0, 0, window=interior, anchor=NW)
        def _configure_interior(event):
                # update the scrollbars to match the size of the inner frame
                size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
                self.canvas.config(scrollregion="0 0 %s %s" % size)
                if interior.winfo_reqwidth() != self.canvas.winfo_width():
                    # update the canvas's width to fit the inner frame
                    self.canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != self.canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                self.canvas.itemconfigure(interior_id, width=self.canvas.winfo_width())
        self.canvas.bind('<Configure>', _configure_canvas)
        # self.dataFrame.pack(fill=BOTH, expand=True)
        # for i in range(20):
        #     self.testButton = ttk.Button(self.dataFrame, text="Sfdaa")
        #     self.testButton.pack()

        # properties = data.get_record(projectID)
        self.dataFrame.grid_columnconfigure(0, weight=0)
        self.dataFrame.grid_columnconfigure(1, weight=1)



        #     label.grid(column=column, row=row, sticky=E)
        #     entry.grid(column=column+1, row=row, sticky=E)
        # ---------Column 0+1+3 -------
        self._internet_archive_URL_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Internet Archive URL:")
        self._internet_archive_URL_label.grid(row=0, column=0, sticky=N+W)
        self._internet_archive_URL_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._internet_archive_URL_entry.grid(row=0, column=1, columnspan=2, sticky=N+E+W)

        self._object_identifier_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Object Identifier:")
        self._object_identifier_label.grid(row=1, column=0, stick=N+W)
        self._object_identifier_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._object_identifier_entry.grid(row=1, column=1, columnspan=2, sticky=N+E+W)

        self._call_number_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Call Number:")
        self._call_number_label.grid(row=2, column=0, sticky=N+W)
        self._call_number_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._call_number_entry.grid(row=2, column=1, columnspan=2, sticky=N+E+W)

        self._project_identifier_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Project Identifier:")
        self._project_identifier_label.grid(row=3, column=0, sticky=N+W)
        self._project_identifier_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._project_identifier_entry.grid(row=3, column=1, columnspan=2, sticky=N+E+W)

        self._project_note_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Project Note:")
        self._project_note_label.grid(row=4, column=0, stick=N+W)
        self._project_note_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._project_note_entry.grid(row=4, column=1, columnspan=2, sticky=N+E+W)

        self._institution_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Institution:")
        self._institution_label.grid(row=5, column=0, stick=N+W)
        self._institution_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._institution_entry.grid(row=5, column=1, sticky=N+E+W)

        self._asset_type_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Asset Type:")
        self._asset_type_label.grid(row=6, column=0, stick=N+W)
        self._asset_type_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._asset_type_entry.grid(row=6, column=1, columnspan=2, sticky=N+E+W)

        self._media_type_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Media Type:")
        self._media_type_label.grid(row=7, column=0, sticky=N+W)
        self._media_type_entry = ttk.Entry(self.dataFrame)
        self._media_type_entry.grid(row=7, column=1, columnspan=2, sticky=N+E+W)

        self._generation_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Generation:")
        self._generation_label.grid(row=8, column=0, sticky=N+W)
        self._generation_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._generation_entry.grid(row=8, column=1, columnspan=2, sticky=N+E+W)

        self._main_or_supplied_title_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Main or Supplied Title:")
        self._main_or_supplied_title_label.grid(row=9, column=0, sticky=N+W)
        self._main_or_supplied_title_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._main_or_supplied_title_entry.grid(row=9, column=1, columnspan=2, sticky=N+E+W)

        self._additional_title_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Additional Title:")
        self._additional_title_label.grid(row=10, column=0, sticky=N+W)
        self._additional_title_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._additional_title_entry.grid(row=10, column=1, columnspan=2, sticky=N+E+W)

        self._series_title_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Series Title:")
        self._series_title_label.grid(row=11, column=0, sticky=N+W)
        self._series_title_entry = ttk.Entry(self.dataFrame)
        self._series_title_entry.grid(row=11, column=1, columnspan=2, sticky=N+E+W)

        self._description_or_content_summary_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Description or Content Summary:")
        self._description_or_content_summary_label.grid(row=12, column=0, stick=N+W)
        self._description_or_content_summary_entry = Text(self.dataFrame, width=40, height=6, wrap=WORD)
        self._description_or_content_summary_entry.grid(row=12, column=1, columnspan=2, rowspan=3, sticky=N+E+W)

        self._why_the_recording_is_significant_to_california_local_history_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Why the recording is significant to California local history:")
        self._why_the_recording_is_significant_to_california_local_history_label.grid(row=16, column=0, stick=N+W)
        self._why_significant_CA_entry = Text(self.dataFrame, width=40, height=10, wrap=WORD)
        self._why_significant_CA_entry.grid(row=16, column=1, columnspan=2, rowspan=5, sticky=N+E+W)

        self._producer_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Producer:")
        self._producer_label.grid(row=21, column=0, sticky=N+W)
        self._producer_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._producer_entry.grid(row=21, column=1, columnspan=2, sticky=N+E+W)

        self._director_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Director:")
        self._director_label.grid(row=22, column=0, stick=N+W)
        self._director_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._director_entry.grid(row=22, column=1, columnspan=2, sticky=N+E+W)

        self._writer_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Writer:")
        self._writer_label.grid(row=23, column=0, sticky=N+W)
        self._writer_entry = ttk.Entry(self.dataFrame)
        self._writer_entry.grid(row=23, column=1, columnspan=2, sticky=N+E+W)

        self._interviewer_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Interviewer:")
        self._interviewer_label.grid(row=24, column=0, stick=N+W)
        self._interviewer_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._interviewer_entry.grid(row=24, column=1, columnspan=2, sticky=N+E+W)

        self._performer_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Performer:")
        self._performer_label.grid(row=25, column=0, sticky=N+W)
        self._performer_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._performer_entry.grid(row=25, column=1, columnspan=2, sticky=N+E+W)

        self._country_of_creation_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Country of Creation:")
        self._country_of_creation_label.grid(row=26, column=0, stick=N+W)
        self._country_of_creation_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._country_of_creation_entry.grid(row=26, column=1, columnspan=2, sticky=N+E+W)

        self._date_created_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Date Created:")
        self._date_created_label.grid(row=27, column=0, sticky=N+W)
        self._date_created_entry = ttk.Entry(self.dataFrame)
        self._date_created_entry.grid(row=27, column=1, columnspan=2, sticky=N+E+W)

        self._date_published_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Date Published:")
        self._date_published_label.grid(row=28, column=0, stick=N+W)
        self._date_published_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._date_published_entry.grid(row=28, column=1, columnspan=2, sticky=N+E+W)

        self._copyright_statement_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Copyright Statement:")
        self._copyright_statement_label.grid(row=29, column=0, stick=N+W)
        self._copyright_statement_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._copyright_statement_entry.grid(row=29, column=1, columnspan=2, sticky=N+E+W)

        self._gauge_and_format_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Gauge and Format:")
        self._gauge_and_format_label.grid(row=30, column=0, stick=N+W)
        self._gauge_and_format_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._gauge_and_format_entry.grid(row=30, column=1, columnspan=2, sticky=N+E+W)

        self._total_number_of_reels_or_tapes_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Total Number of Reels or Tapes:")
        self._total_number_of_reels_or_tapes_label.grid(row=31, column=0, sticky=N+W)
        self._total_number_of_reels_or_tapes_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._total_number_of_reels_or_tapes_entry.grid(row=31, column=1, columnspan=2, sticky=N+E+W)

        self._duration_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Duration:")
        self._duration_label.grid(row=32, column=0, sticky=N+W)
        self._duration_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._duration_entry.grid(row=32, column=1, columnspan=2, sticky=N+E+W)

        self._silent_or_sound_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Silent or Sound:")
        self._silent_or_sound_label.grid(row=33, column=0, sticky=N+W)
        self._silent_or_sound_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._silent_or_sound_entry.grid(row=33, column=1, columnspan=2, sticky=N+E+W)

        self._color_and_or_black_and_white_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Color and or Black and White:")
        self._color_and_or_black_and_white_label.grid(row=34, column=0, stick=N+W)
        self._color_and_or_black_and_white_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._color_and_or_black_and_white_entry.grid(row=34, column=1, columnspan=2, sticky=N+E+W)

        self._camera_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Camera:")
        self._camera_label.grid(row=35, column=0, sticky=N+W)
        self._camera_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._camera_entry.grid(row=35, column=1, columnspan=2, sticky=N+E+W)

        self._editor_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Editor:")
        self._editor_label.grid(row=36, column=0, sticky=N+W)
        self._editor_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._editor_entry.grid(row=36, column=1, columnspan=2, sticky=N+E+W)

        self._sound_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Sound:")
        self._sound_label.grid(row=37, column=0, stick=N+W)
        self._sound_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._sound_entry.grid(row=37, column=1, columnspan=2, sticky=N+E+W)

        self._music_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Music:")
        self._music_label.grid(row=38, column=0, sticky=N+W)
        self._music_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._music_entry.grid(row=38, column=1, columnspan=2, sticky=N+E+W)

        self._cast_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Cast:")
        self._cast_label.grid(row=39, column=0, sticky=N+W)
        self._cast_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._cast_entry.grid(row=39, column=1, columnspan=2, sticky=N+E+W)

        self._interviewee_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Interviewee:")
        self._interviewee_label.grid(row=40, column=0, sticky=N+W)
        self._interviewee_entry = ttk.Entry(self.dataFrame)
        self._interviewee_entry.grid(row=40, column=1, columnspan=2, sticky=N+E+W)

        self._speaker_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Speaker:")
        self._speaker_label.grid(row=41, column=0, sticky=N+W)
        self._speaker_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._speaker_entry.grid(row=41, column=1, columnspan=2, sticky=N+E+W)

        self._musician_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Musician")
        self._musician_label.grid(row=42, column=0, sticky=N+W)
        self._musician_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._musician_entry.grid(row=42, column=1, columnspan=2, sticky=N+E+W)

        self._publisher_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Publisher:")
        self._publisher_label.grid(row=43, column=0, stick=N+W)
        self._publisher_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._publisher_entry.grid(row=43, column=1, columnspan=2, sticky=N+E+W)

        self._distributor_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Distributor:")
        self._distributor_label.grid(row=44, column=0, sticky=N+W)
        self._distributor_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._distributor_entry.grid(row=44, column=1, columnspan=2, sticky=N+E+W)

        self._language_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Language")
        self._language_label.grid(row=45, column=0, stick=N+W)
        self._language_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._language_entry.grid(row=45, column=1, columnspan=2, sticky=N+E+W)

        self._subject_topic_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Subject Topic:")
        self._subject_topic_label.grid(row=46, column=0, sticky=N+W)
        self._subject_topic_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._subject_topic_entry.grid(row=46, column=1, columnspan=2, sticky=N+E+W)

        self._subject_topic_authority_source_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Subject Topic Authority Source:")
        self._subject_topic_authority_source_label.grid(row=47, column=0, sticky=N+W)
        self._subject_topic_authority_source_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._subject_topic_authority_source_entry.grid(row=47, column=1, columnspan=2, sticky=N+E+W)

        self._subject_entity_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Subject_Entity:")
        self._subject_entity_label.grid(row=48, column=0, stick=N+W)
        self._subject_entity_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._subject_entity_entry.grid(row=48, column=1, columnspan=2, sticky=N+E+W)

        self._subject_entity_authority_source_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Subject Entity Authority Source:")
        self._subject_entity_authority_source_label.grid(row=49, column=0, sticky=N+W)
        self._subject_entity_authority_source_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._subject_entity_authority_source_entry.grid(row=49, column=1, columnspan=2, sticky=N+E+W)

        self._genre_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Genre")
        self._genre_label.grid(row=50, column=0, stick=N+W)
        self._genre_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._genre_entry.grid(row=50, column=1, columnspan=2, sticky=N+E+W)

        self._genre_authority_source_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Genre Authority Source:")
        self._genre_authority_source_label.grid(row=51, column=0, stick=N+W)
        self._genre_authority_source_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._genre_authority_source_entry.grid(row=51, column=1, columnspan=2, sticky=N+E+W)

        self._spatial_coverage_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Spatial Coverage:")
        self._spatial_coverage_label.grid(row=52, column=0, sticky=N+W)
        self._spatial_coverage_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._spatial_coverage_entry.grid(row=52, column=1, columnspan=2, sticky=N+E+W)

        self._temporal_coverage_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Temporal Coverage:")
        self._temporal_coverage_label.grid(row=53, column=0, sticky=N+W)
        self._temporal_coverage_entry = ttk.Entry(self.dataFrame)
        self._temporal_coverage_entry.grid(row=53, column=1, columnspan=2, sticky=N+E+W)

        self._collection_guide_title_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Collection Guide Title:")
        self._collection_guide_title_label.grid(row=54, column=0, sticky=N+W)
        self._collection_guide_title_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._collection_guide_title_entry.grid(row=54, column=1, columnspan=2, sticky=N+E+W)

        self._collection_guide_url_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Collection Guide URL:")
        self._collection_guide_url_label.grid(row=55, column=0, stick=N+W)
        self._collection_guide_url_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._collection_guide_url_entry.grid(row=55, column=1, columnspan=2, sticky=N+S+E+W)

        self._relationship_type_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Relationship Type:")
        self._relationship_type_label.grid(row=56, column=0, stick=N+W)
        self._relationship_type_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._relationship_type_entry.grid(row=56, column=1, columnspan=2, sticky=N+E+W)

        self._relationship_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Relationship:")
        self._relationship_label.grid(row=57, column=0, sticky=N+W)
        self._relationship_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._relationship_entry.grid(row=57, column=1, columnspan=2, sticky=N+E+W)

        self._aspect_ratio_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Aspect Ratio:")
        self._aspect_ratio_label.grid(row=58, column=0, sticky=N+W)
        self._aspect_ratio_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._aspect_ratio_entry.grid(row=58, column=1, columnspan=2, sticky=N+E+W)

        self._running_speed_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Running Speed")
        self._running_speed_label.grid(row=59, column=0, sticky=N+W)
        self._running_speed_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._running_speed_entry.grid(row=59, column=1, columnspan=2, sticky=N+E+W)

        self._timecode_content_begins_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Timecode Content Begins:")
        self._timecode_content_begins_label.grid(row=60, column=0, sticky=N+W)
        self._timecode_content_begins_entry = ttk.Entry(self.dataFrame)
        self._timecode_content_begins_entry.grid(row=60, column=1, columnspan=2, sticky=N+E+W)

        self._track_standard_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Track Standard:")
        self._track_standard_label.grid(row=61, column=0, sticky=N+W)
        self._track_standard_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._track_standard_entry.grid(row=61, column=1, columnspan=2, sticky=N+E+W)

        self._channel_configuration_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Channel Configuration:")
        self._channel_configuration_label.grid(row=62, column=0, sticky=N+W)
        self._channel_configuration_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._channel_configuration_entry.grid(row=62, column=1, columnspan=2, sticky=N+E+W)

        self._subtitles_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Subtitles:")
        self._subtitles_label.grid(row=63, column=0, sticky=N+W)
        self._subtitles_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._subtitles_entry.grid(row=63, column=1, columnspan=2, sticky=N+E+W)

        self._stock_manufacturer_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Stock Manufacturer:")
        self._stock_manufacturer_label.grid(row=64, column=0, stick=N+W)
        self._stock_manufacturer_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._stock_manufacturer_entry.grid(row=64, column=1, columnspan=2, sticky=N+E+W)

        self._base_type_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Base Type:")
        self._base_type_label.grid(row=65, column=0, sticky=N+W)
        self._base_type_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._base_type_entry.grid(row=65, column=1, columnspan=2, sticky=N+E+W)

        self._base_thickness_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Base Thickness:")
        self._base_thickness_label.grid(row=66, column=0, sticky=N+W)
        self._base_thickness_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._base_thickness_entry.grid(row=66, column=1, columnspan=2, sticky=N+E+W)

        self._copyright_holder_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Copyright Holder:")
        self._copyright_holder_label.grid(row=67, column=0, stick=N+W)
        self._copyright_holder_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._copyright_holder_entry.grid(row=67, column=1, columnspan=2, sticky=N+E+W)

        self._copyright_holder_info_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Copyright Holder Info:")
        self._copyright_holder_info_label.grid(row=68, column=0, sticky=N+W)
        self._copyright_holder_info_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._copyright_holder_info_entry.grid(row=68, column=1, columnspan=2, sticky=N+E+W)

        self._copyright_date_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Copyright Date:")
        self._copyright_date_label.grid(row=69, column=0, stick=N+W)
        self._copyright_date_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._copyright_date_entry.grid(row=69, column=1, columnspan=2, sticky=N+E+W)

        self._copyright_notice_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Copyright Notice:")
        self._copyright_notice_label.grid(row=70, column=0, sticky=N+W)
        self._copyright_notice_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._copyright_notice_entry.grid(row=70, column=1, columnspan=2, sticky=N+E+W)

        self._institutional_rights_statement_url_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Institutional Rights Statement URL:")
        self._institutional_rights_statement_url_label.grid(row=71, column=0, stick=N+W)
        self._institutional_rights_statement_URL_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._institutional_rights_statement_URL_entry.grid(row=71, column=1, columnspan=2, sticky=N+E+W)

        self._object_ark_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Object_ARK:")
        self._object_ark_label.grid(row=72, column=0, sticky=N+W)
        self._object_ark_entry = ttk.Entry(self.dataFrame)
        self._object_ark_entry.grid(row=72, column=1, columnspan=2, sticky=N+E+W)

        self._institution_ark_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Institution ARK:")
        self._institution_ark_label.grid(row=73, column=0, stick=N+W)
        self._institution_ark_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._institution_ark_entry.grid(row=73, column=1, columnspan=2, sticky=N+E+W)

        self._institution_URL_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Institution URL:")
        self._institution_URL_label.grid(row=74, column=0, sticky=N+W)
        self._institution_URL_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._institution_URL_entry.grid(row=74, column=1, columnspan=2, sticky=N+E+W)

        self._quality_control_notes_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Quality Control Notes:")
        self._quality_control_notes_label.grid(row=75, column=0, sticky=N+W)
        self._quality_control_notes_entry = Text(self.dataFrame, width=40, height=10, wrap=WORD)
        self._quality_control_notes_entry.grid(row=75, column=1, columnspan=2, rowspan=5, sticky=N+E+W)

        self._additional_descriptive_notes_for_overall_work_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Additional Descriptive Notes for Overall Work:")
        self._additional_descriptive_notes_for_overall_work_label.grid(row=80, column=0, stick=N+W)
        self._additional_descrpt_nts_overall_wrk_entry = Text(self.dataFrame, width=40, height=10, wrap=WORD)
        # self.Additional_Descriptive_Notes_for_Overall_Work_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._additional_descrpt_nts_overall_wrk_entry.grid(row=80, column=1, columnspan=2, rowspan=2, sticky=N+E+W)

        self._additional_technical_notes_for_overall_work_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Additional Technical Notes for Overall Work:")
        self._additional_technical_notes_for_overall_work_label.grid(row=82, column=0, sticky=N+W)
        self._additional_technical_notes_for_overall_work_entry = Text(self.dataFrame, width=40, height=10, wrap=WORD)
        self._additional_technical_notes_for_overall_work_entry.grid(row=82, column=1, columnspan=2, sticky=N+E+W)

        self._transcript_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Transcript:")
        self._transcript_label.grid(row=83, column=0, sticky=N+W)
        self._transcript_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._transcript_entry.grid(row=83, column=1, columnspan=2, sticky=N+E+W)

        self._cataloger_notes_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Cataloger Notes:")
        self._cataloger_notes_label.grid(row=84, column=0, stick=N+W)
        self._cataloger_notes_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._cataloger_notes_entry.grid(row=84, column=1, columnspan=2, sticky=N+E+W)

        self._OCLC_number_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="OCLC number:")
        self._OCLC_number_label.grid(row=85, column=0, stick=N+W)
        self._OCLC_number_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._OCLC_number_entry.grid(row=85, column=1, columnspan=2, sticky=N+E+W)

        self._date_created1_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Date created:")
        self._date_created1_label.grid(row=86, column=0, sticky=N+W)
        self._date_created1_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._date_created1_entry.grid(row=86, column=1, columnspan=2, sticky=N+E+W)

        self._date_modified_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Date modified:")
        self._date_modified_label.grid(row=87, column=0, sticky=N+W)
        self._date_modified_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._date_modified_entry.grid(row=87, column=1, columnspan=2, sticky=N+E+W)

        self.reference_URL_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Reference URL:")
        self.reference_URL_label.grid(row=88, column=0, sticky=N+W)
        self._reference_URL_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._reference_URL_entry.grid(row=88, column=1, columnspan=2, sticky=N+E+W)

        self._CONTENTdm_number_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="CONTENTdm number:")
        self._CONTENTdm_number_label.grid(row=89, column=0, sticky=N+W)
        self._CONTENTdm_number_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._CONTENTdm_number_entry.grid(row=89, column=1, columnspan=2, sticky=N+E+W)

        self._CONTENTdm_file_name_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="CONTENTdm file name:")
        self._CONTENTdm_file_name_label.grid(row=90, column=0, stick=N+W)
        self._CONTENTdm_file_name_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._CONTENTdm_file_name_entry.grid(row=90, column=1, columnspan=2, sticky=N+E+W)

        self._CONTENTdm_file_path_label = ttk.Label(self.dataFrame, style='labels.TLabel', text="CONTENTdm file path:")
        self._CONTENTdm_file_path_label.grid(row=91, column=0, sticky=N+W)
        self._CONTENTdm_file_path_entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self._CONTENTdm_file_path_entry.grid(row=91, column=1, columnspan=2, sticky=N+E+W)

        # ++++++++++++++++++++++
        # ++++++++++++++++++++++
        # ++++++++++++++++++++++


        #
         # ------------ files  --------------

        # self.dataOuterFrame = ttk.Frame(self.background, padding=(10,10))
        self.associated_files_Frame = ttk.LabelFrame(self.background, text="Associated Files")
        # self.associated_files_Frame.pack(fill=BOTH, expand=True)
        self.panel.add(self.associated_files_Frame, weight=1)
        self.associated_files_Tree = ttk.Treeview(self.associated_files_Frame, height=5, columns=('file', 'type', 'size'))
        self.associated_files_Tree.heading('file', text='File')
        self.associated_files_Tree.heading('type', text='Type')
        self.associated_files_Tree.heading('size', text='Size')
        self.associated_files_Tree['show'] = 'headings'

        self.associated_files_Tree.pack(fill=BOTH, expand=True)
        self.associated_files_Tree.column('#0', width=0, stretch=NO, anchor='center')
        self.associated_files_Tree.column('file', width=250, stretch=NO, anchor=W)
        self.associated_files_Tree.column('type', width=100, stretch=NO, anchor=W)
        self.associated_files_Tree.column('size', width=50, anchor=W)
        # self.associated_files_Tree.config
        self.load_associated_files()

        # ------------ Options --------------
        self.optionsFrame = ttk.LabelFrame(self.background)
        self.optionsFrame.pack(fill=X)
        # self.panel.add(self.optionsFrame)
        self.CancelButton = ttk.Button(self.optionsFrame, text="Cancel", command=lambda: self.master.destroy())
        # self.closeButton.grid(column=0, row=0, sticky=W+S)
        self.CancelButton.grid(column=0, row=0, sticky=E)
        self.okayButton = ttk.Button(self.optionsFrame, text="OK", command=self.applyChanges)
        self.okayButton.grid(column=1, row=0)

        self.loadrecord()

    def applyChanges(self):
        # self.updated = True
        changes = self._get_changes()
        if changes:
            self.updated = True

            if len(changes) < 5:
                message = "Are you sure you want to make the following changes?"
                for change in changes:
                    message += ("\n" + change[0] + ": " + change[1] +"\n")
            else:
                message = "There are "+ str(len(changes))+" changes with this record. " \
                                                          "\nAre you sure you want to change them?\n\n"
            ask = tkMessageBox.askokcancel("Are You Sure?", message)
            if ask:
                self.shouldUpdate = True


                self.xml_file = self._xmlEntry.get()

                self.newRecord.update({'Date Created': self._date_created_entry.get()})
                self.newRecord.update({'Object ARK': self._object_ark_entry.get()})
                self.newRecord.update({'Timecode Content Begins': self._timecode_content_begins_entry.get()})
                self.newRecord.update({'Media Type': self._media_type_entry.get()})
                self.newRecord.update({'Interviewee': self._interviewee_entry.get()})
                self.newRecord.update({'Series Title': self._series_title_entry.get()})
                self.newRecord.update({'Temporal Coverage': self._temporal_coverage_entry.get()})
                self.newRecord.update({'Writer': self._writer_entry.get()})
                self.newRecord.update({'Institution URL': self._institution_URL_entry.get()})
                self.newRecord.update({'Project Identifier': self._project_identifier_entry.get()})
                self.newRecord.update({'Quality Control Notes': str(self._quality_control_notes_entry.get("0.0", END).replace('\n', ''))})
                self.newRecord.update({'Silent or Sound': self._silent_or_sound_entry.get()})
                self.newRecord.update({'Camera': self._camera_entry.get()})
                self.newRecord.update({'Music': self._music_entry.get()})
                self.newRecord.update({'Editor': self._editor_entry.get()})
                self.newRecord.update({'Track Standard': self._track_standard_entry.get()})
                self.newRecord.update({'CONTENTdm number': self._CONTENTdm_number_entry.get()})
                self.newRecord.update({'Subtitles/Intertitles/Closed Captions': self._subtitles_entry.get()})
                self.newRecord.update({'Distributor': self._distributor_entry.get()})
                self.newRecord.update({'Date modified': self._date_modified_entry.get()})
                self.newRecord.update({'Subject Topic Authority Source': self._subject_topic_authority_source_entry.get()})
                self.newRecord.update({'Aspect Ratio': self._aspect_ratio_entry.get()})
                self.newRecord.update({'Total Number of Reels or Tapes': self._total_number_of_reels_or_tapes_entry.get()})
                self.newRecord.update({'Copyright Holder Info': self._copyright_holder_info_entry.get()})
                self.newRecord.update({'Running Speed': self._running_speed_entry.get()})
                self.newRecord.update({'Subject Entity Authority Source': self._subject_entity_authority_source_entry.get()})
                self.newRecord.update({'Additional Technical Notes for Overall Work': str(self._additional_technical_notes_for_overall_work_entry.get("0.0", END).replace('\n', ''))})
                self.newRecord.update({'Musician': self._musician_entry.get()})
                self.newRecord.update({'Main or Supplied Title': self._main_or_supplied_title_entry.get()})
                self.newRecord.update({'Internet Archive URL': self._internet_archive_URL_entry.get()})
                self.newRecord.update({'Relationship Type': self._relationship_type_entry.get()})
                self.newRecord.update({'Director': self._director_entry.get()})
                self.newRecord.update({'Copyright Statement': self._copyright_statement_entry.get()})
                self.newRecord.update({'Genre': self._genre_entry.get()})
                self.newRecord.update({'Cataloger Notes': self._cataloger_notes_entry.get()})
                self.newRecord.update({'Collection Guide URL': self._collection_guide_url_entry.get()})
                self.newRecord.update({'Interviewer': self._interviewer_entry.get()})
                self.newRecord.update({'Description or Content Summary': str(self._description_or_content_summary_entry.get("0.0", END).replace('\n', ''))})
                self.newRecord.update({'Institution': self._institution_entry.get()})
                self.newRecord.update({'Stock Manufacturer': self._stock_manufacturer_entry.get()})
                self.newRecord.update({'Sound': self._sound_entry.get()})
                self.newRecord.update({'Publisher': self._publisher_entry.get()})
                self.newRecord.update({'Asset Type': self._asset_type_entry.get()})
                self.newRecord.update({'Object Identifier': self._object_identifier_entry.get()})
                self.newRecord.update({'Copyright Date': self._copyright_date_entry.get()})
                self.newRecord.update({'Copyright Holder': self._copyright_holder_entry.get()})
                self.newRecord.update({'Language': self._language_entry.get()})
                self.newRecord.update({'Color and/or Black and White': self._color_and_or_black_and_white_entry.get()})
                self.newRecord.update({'Institution ARK': self._institution_ark_entry.get()})
                self.newRecord.update({'CONTENTdm file name': self._CONTENTdm_file_name_entry.get()})
                self.newRecord.update({'OCLC number': self._OCLC_number_entry.get()})
                self.newRecord.update({'Why the recording is significant to California/local history': str(self._why_significant_CA_entry.get("0.0", END).replace('\n', ''))})
                self.newRecord.update({'Subject Entity': self._subject_entity_entry.get()})
                self.newRecord.update({'Gauge and Format': self._gauge_and_format_entry.get()})
                self.newRecord.update({'Additional Descriptive Notes for Overall Work': str(self._additional_descrpt_nts_overall_wrk_entry.get("0.0", END).replace('\n', ''))})
                self.newRecord.update({'Genre Authority Source': self._genre_authority_source_entry.get()})
                self.newRecord.update({'Date Published': self._date_published_entry.get()})
                self.newRecord.update({'Country of Creation': self._country_of_creation_entry.get()})
                self.newRecord.update({'Project Note': self._project_note_entry.get()})
                self.newRecord.update({'Institutional Rights Statement (URL)': self._institutional_rights_statement_URL_entry.get()})
                self.newRecord.update({'Spatial Coverage': self._spatial_coverage_entry.get()})
                self.newRecord.update({'Copyright Notice': self._copyright_notice_entry.get()})
                self.newRecord.update({'Subject Topic':self._subject_topic_entry.get()})
                self.newRecord.update({'Performer': self._performer_entry.get()})
                self.newRecord.update({'Relationship': self._relationship_entry.get()})
                self.newRecord.update({'Producer': self._producer_entry.get()})
                self.newRecord.update({'Cast': self._cast_entry.get()})
                self.newRecord.update({'Generation': self._generation_entry.get()})
                self.newRecord.update({'Transcript': self._transcript_entry.get()})
                self.newRecord.update({'Channel Configuration': self._channel_configuration_entry.get()})
                self.newRecord.update({'Date created': self._date_created1_entry.get()})
                self.newRecord.update({'Reference URL': self._reference_URL_entry.get()})
                self.newRecord.update({'Call Number': self._call_number_entry.get()})
                self.newRecord.update({'Base Thickness': self._base_thickness_entry.get()})
                self.newRecord.update({'Base Type': self._base_type_entry.get()})
                self.newRecord.update({'Additional Title': self._additional_title_entry.get()})
                self.newRecord.update({'CONTENTdm file path': self._CONTENTdm_file_path_entry.get()})
                self.newRecord.update({'Duration': self._duration_entry.get()})
                self.newRecord.update({'Speaker': self._speaker_entry.get()})
                self.newRecord.update({'Collection Guide Title': self._collection_guide_title_entry.get()})

                # print "done"



                self.master.destroy()
        else:
            self.master.destroy()



    def load_associated_files(self):
        # print "loading associated files"
        root = os.path.dirname(self.filepath)
        # print root
        fileName = re.search(FILE_NAME_PATTERN, self.current_record['Object Identifier']).group(0)
        # print fileName
        files = locate_files(root, fileName)
        prsv, access = pbcore_csv.sep_pres_access(files)

        for index, file in enumerate(prsv):
            # self.associated_files_Tree
            self.associated_files_Tree.insert('', index, file)
            self.associated_files_Tree.set(file, 'file', os.path.basename(file))
            self.associated_files_Tree.set(file, 'type', "Preservation Master")
            self.associated_files_Tree.set(file, 'size', str(os.path.getsize(file)/1048576) + " MB")
        for index, file in enumerate(access):
            # self.associated_files_Tree
            self.associated_files_Tree.insert('', index, file)
            self.associated_files_Tree.set(file, 'file', os.path.basename(file))
            self.associated_files_Tree.set(file, 'type', "Access Copy")
            self.associated_files_Tree.set(file, 'size', str(os.path.getsize(file)/1048576) + " MB")
        # print locate_files()

    def save_as(self):
        save_file = tkFileDialog.asksaveasfilename(defaultextension=".xml",
                                                   initialdir=os.path.dirname(self._xmlEntry.get()),
                                                   initialfile=os.path.basename(self._xmlEntry.get()),
                                                   filetypes=[("XML", "*.xml")])
        if save_file:
            self._xmlEntry.delete(0, END)
            self._xmlEntry.insert(0,save_file)
    def loadrecord(self):
        # print("loading record")
        # for index, proper in enumerate(self.properties):
        
        
        
        #     print proper
        self._date_created_entry.insert(0, self._init_date_created)
        self._object_ark_entry.insert(0, self._init_object_ark)
        self._timecode_content_begins_entry.insert(0, self._init_timecode_content_begins)
        self._media_type_entry.insert(0, self._init_media_type)
        self._interviewee_entry.insert(0, self._init_interviewee)
        self._series_title_entry.insert(0, self._init_series_title)
        self._temporal_coverage_entry.insert(0, self._init_temporal_coverage)
        self._writer_entry.insert(0, self._init_writer)
        self._institution_URL_entry.insert(0, self._init_institution_URL)
        self._project_identifier_entry.insert(0, self._init_project_identifier)
        self._project_identifier_entry.config(state='disabled')
        self._quality_control_notes_entry.insert('1.0', self._init_quality_control_notes)
        self._silent_or_sound_entry.insert(0, self._init_silent_or_sound)
        self._camera_entry.insert(0, self._init_camera)
        self._music_entry.insert(0, self._init_music)
        self._editor_entry.insert(0, self._init_editor)
        self._track_standard_entry.insert(0, self._init_track_standard)
        self._CONTENTdm_number_entry.insert(0, self._init_contentdm_number)
        self._subtitles_entry.insert(0, self._init_subtitles)
        self._distributor_entry.insert(0, self._init_distributor)
        self._date_modified_entry.insert(0, self._init_date_modified)
        self._subject_topic_authority_source_entry.insert(0, self._init_subject_topic_authority_source)
        self._aspect_ratio_entry.insert(0, self._init_aspect_ratio)
        self._total_number_of_reels_or_tapes_entry.insert(0, self._init_total_number_of_reels_or_tapes)
        self._copyright_holder_info_entry.insert(0, self._init_copyright_holder_info)
        self._running_speed_entry.insert(0, self._init_running_speed)
        self._subject_entity_authority_source_entry.insert(0, self._init_subject_entity_authority_source)
        self._additional_technical_notes_for_overall_work_entry.insert('1.0', self._init_additional_technical_notes_for_overall_work)
        self._musician_entry.insert(0, self._init_musician)
        self._main_or_supplied_title_entry.insert(0, self._init_main_or_supplied_title)
        self._internet_archive_URL_entry.insert(0, self._init_internet_archive_url)
        self._relationship_type_entry.insert(0, self._init_relationship_type)
        self._director_entry.insert(0, self._init_director)
        self._copyright_statement_entry.insert(0, self._init_copyright_statement)
        self._genre_entry.insert(0, self._init_genre)
        self._cataloger_notes_entry.insert(0, self._init_cataloger_notes)
        self._collection_guide_url_entry.insert(0, self._init_collection_guide_url)
        self._interviewer_entry.insert(0, self._init_interviewer)
        self._description_or_content_summary_entry.insert('1.0', self._init_description_or_content_summary)
        self._institution_entry.insert(0, self._init_institution)
        self._stock_manufacturer_entry.insert(0, self._init_stock_manufacturer)
        self._sound_entry.insert(0, self._init_sound)
        self._publisher_entry.insert(0, self._init_publisher)
        self._asset_type_entry.insert(0, self._init_asset_type)
        self._object_identifier_entry.insert(0, self._init_object_identifier)
        self._copyright_date_entry.insert(0, self._init_copyright_date)
        self._copyright_holder_entry.insert(0, self._init_copyright_holder)
        self._language_entry.insert(0, self._init_language)
        self._color_and_or_black_and_white_entry.insert(0, self._init_color_and_or_black_and_white)
        self._institution_ark_entry.insert(0, self._init_institution_ark)
        self._CONTENTdm_file_name_entry.insert(0, self._init_contentdm_file_name)
        self._OCLC_number_entry.insert(0, self._init_OCLC_number)
        self._why_significant_CA_entry.insert('1.0', self._init_why_significant_CA)
        # self._subject_topic_authority_source_entry.insert(0, self._init_subject_topic_authority_source)
        self._gauge_and_format_entry.insert(0, self._init_gauge_and_format)
        self._additional_descrpt_nts_overall_wrk_entry.insert('1.0', self._init_addit_descrpt_nts_overall_wrk)
        self._genre_authority_source_entry.insert(0, self._init_genre_authority_source)
        self._date_published_entry.insert(0, self._init_date_published)
        self._country_of_creation_entry.insert(0, self._init_country_of_creation)
        self._project_note_entry.insert(0, self._init_project_note)
        self._institutional_rights_statement_URL_entry.insert(0, self._init_institutional_rights_statement_URL)
        self._spatial_coverage_entry.insert(0, self._init_spatial_coverage)
        self._copyright_notice_entry.insert(0, self._init_copyright_notice)
        self._subject_topic_entry.insert(0, self._init_subject_topic)
        self._performer_entry.insert(0, self._init_performer)
        self._relationship_entry.insert(0, self._init_relationship)
        self._producer_entry.insert(0, self._init_producer)
        self._cast_entry.insert(0, self._init_cast)
        self._generation_entry.insert(0, self._init_generation)
        self._transcript_entry.insert(0, self._init_transcript)
        self._channel_configuration_entry.insert(0, self._init_channel_configuration)
        self._date_created1_entry.insert(0, self._init_date_created1)
        self._reference_URL_entry.insert(0, self._init_reference_url)
        self._call_number_entry.insert(0, self._init_call_number)
        self._base_thickness_entry.insert(0, self._init_base_thickness)
        self._base_type_entry.insert(0, self._init_base_type)
        self._additional_title_entry.insert(0, self._init_additional_title)
        self._CONTENTdm_file_path_entry.insert(0, self._init_contentdm_file_path)
        self._duration_entry.insert(0, self._init_duration)
        self._speaker_entry.insert(0, self._init_speaker)
        self._collection_guide_title_entry.insert(0, self._init_collection_guide_title)

    def _get_changes(self):
        changes = []

        if self._xmlEntry.get().strip() != self._init_xml:
            changes.append(('Save new xml as', self._xmlEntry.get()))

        if self._additional_descrpt_nts_overall_wrk_entry.get('0.0', END).replace('\n', '') != self._init_addit_descrpt_nts_overall_wrk:
            changes.append(('Additional Descriptive Notes Overall Work', self._additional_descrpt_nts_overall_wrk_entry.get('0.0', END).replace('\n', '')))

        if self._additional_technical_notes_for_overall_work_entry.get('0.0', END).replace('\n', '') != self._init_additional_technical_notes_for_overall_work:
            changes.append(('Additional Technical Notes For Overall Work', self._additional_technical_notes_for_overall_work_entry.get('0.0', END).replace('\n', '')))

        if self._additional_title_entry.get() != self._init_additional_title:
            changes.append(('Additional Title', self._additional_title_entry.get()))

        if self._aspect_ratio_entry.get() != self._init_aspect_ratio:
            changes.append(('Aspect Ratio', self._aspect_ratio_entry.get()))

        if self._asset_type_entry.get() != self._init_asset_type:
            changes.append(('Asset Type', self._asset_type_entry.get()))

        if self._base_thickness_entry.get() != self._init_base_thickness:
            changes.append(('Base Thickness', self._base_thickness_entry.get()))

        if self._base_type_entry.get() != self._init_base_type:
            changes.append(('Base type', self._base_type_entry.get()))

        if self._call_number_entry.get() != self._init_call_number:
            changes.append(('Call Number', self._call_number_entry.get()))

        if self._camera_entry.get() != self._init_camera:
            changes.append(('camera', self._camera_entry.get()))

        if self._cast_entry.get() != self._init_cast:
            changes.append(('cast', self._cast_entry.get()))

        if self._cataloger_notes_entry.get() != self._init_cataloger_notes:
            changes.append(('Cataloger Notes', self._cataloger_notes_entry.get()))

        if self._channel_configuration_entry.get() != self._init_channel_configuration:
            changes.append(('Channel Configuration', self._channel_configuration_entry.get()))

        if self._collection_guide_title_entry.get() != self._init_collection_guide_title:
            changes.append(('Collection Guide Title', self._collection_guide_title_entry.get()))

        if self._collection_guide_url_entry.get() != self._init_collection_guide_url:
            changes.append(('Collection Guide URL', self._collection_guide_url_entry.get()))

        if self._color_and_or_black_and_white_entry.get() != self._init_color_and_or_black_and_white:
            changes.append(('Color and/or Black and White', self._color_and_or_black_and_white_entry.get()))

        if self._CONTENTdm_file_name_entry.get() != self._init_contentdm_file_name:
            changes.append(('CONTENTdm File Name', self._CONTENTdm_file_name_entry.get()))

        if self._CONTENTdm_file_path_entry.get() != self._init_contentdm_file_path:
            changes.append(('CONTENTdm File Path', self._CONTENTdm_file_path_entry.get()))

        if self._CONTENTdm_number_entry.get() != self._init_contentdm_number:
            changes.append(('CONTENTdm Number', self._CONTENTdm_number_entry.get()))

        if self._copyright_date_entry.get() != self._init_copyright_date:
            changes.append(('Copyright Date', self._copyright_date_entry.get()))

        if self._copyright_holder_entry.get() != self._init_copyright_holder:
            changes.append(('Copyright Holder', self._copyright_holder_entry.get()))

        if self._copyright_holder_info_entry.get() != self._init_copyright_holder_info:
            changes.append(('Copyright Holder Info', self._copyright_holder_info_entry.get()))

        if self._copyright_notice_entry.get() != self._init_copyright_notice:
            changes.append(('Copyright Notice', self._copyright_notice_entry.get()))

        if self._copyright_statement_entry.get() != self._init_copyright_statement:
            changes.append(('Copyright Statement', self._copyright_statement_entry.get()))

        if self._country_of_creation_entry.get() != self._init_country_of_creation:
            changes.append(('Country of Creation', self._country_of_creation_entry.get()))

        if self._date_created_entry.get() != self._init_date_created:
            changes.append(('Date Created', self._date_created_entry.get()))

        if self._date_created1_entry.get() != self._init_date_created1:
            changes.append(('Date Created', self._date_created1_entry.get()))

        if self._date_modified_entry.get() != self._init_date_modified:
            changes.append(('Date Modified', self._date_modified_entry.get()))

        if self._date_published_entry.get() != self._init_date_published:
            changes.append(('Date Published', self._date_published_entry.get()))

        if self._description_or_content_summary_entry.get('0.0', END).replace('\n', '') != self._init_description_or_content_summary:
            changes.append(('Description or Content Summary', self._description_or_content_summary_entry.get('0.0', END).replace('\n', '')))

        if self._director_entry.get() != self._init_director:
            changes.append(('Director', self._director_entry.get()))

        if self._distributor_entry.get() != self._init_distributor:
            changes.append(('Distributor', self._distributor_entry.get()))

        if self._duration_entry.get() != self._init_duration:
            changes.append(('Duration', self._duration_entry.get()))

        if self._editor_entry.get() != self._init_editor:
            changes.append(('Editor', self._editor_entry.get()))

        if self._gauge_and_format_entry.get() != self._init_gauge_and_format:
            changes.append(('Gauge and Format', self._gauge_and_format_entry.get()))

        if self._generation_entry.get() != self._init_generation:
            changes.append(('Generation', self._generation_entry.get()))

        if self._genre_entry.get() != self._init_genre:
            changes.append(('Genre', self._genre_entry.get))

        if self._genre_authority_source_entry.get() != self._init_genre_authority_source:
            changes.append(('Genre Authority Source', self._genre_authority_source_entry.get()))

        if self._institutional_rights_statement_URL_entry.get() != self._init_institutional_rights_statement_URL:
            changes.append(('Institutional Rights Statement URL', self._institutional_rights_statement_URL_entry.get()))

        if self._interviewer_entry.get() != self._init_interviewer:
            changes.append(('Interviewer', self._interviewer_entry.get()))

        if self._institution_entry.get() != self._init_institution:
            changes.append(('Institution', self._institution_entry.get()))

        if self._institution_ark_entry.get() != self._init_institution_ark:
            changes.append(('Institution ARK', self._institution_ark_entry.get()))

        if self._institution_URL_entry.get() != self._init_institution_URL:
            changes.append(('Institution URL', self._institution_URL_entry.get()))

        if self._internet_archive_URL_entry.get() != self._init_internet_archive_url:
            changes.append(('Internet Archive URL', self._internet_archive_URL_entry.get()))

        if self._interviewee_entry.get() != self._init_interviewee:
            changes.append(('Interviewee', self._interviewee_entry.get()))

        if self._language_entry.get() != self._init_language:
            changes.append(('Language', self._language_entry.get()))

        if self._main_or_supplied_title_entry.get() != self._init_main_or_supplied_title:
            changes.append(('Main or Supplied Title', self._main_or_supplied_title_entry.get()))

        if self._media_type_entry.get() != self._init_media_type:
            changes.append(('Media Type', self._media_type_entry.get()))

        if self._music_entry.get() != self._init_music:
            changes.append(('Music', self._music_entry.get()))

        if self._musician_entry.get() != self._init_musician:
            changes.append(('Musician', self._musician_entry.get()))

        if self._object_ark_entry.get() != self._init_object_ark:
            changes.append(('Object ARK', self._object_ark_entry.get()))

        if self._object_identifier_entry.get() != self._init_object_identifier:
            changes.append(('Object Identifier', self._object_identifier_entry.get()))

        if self._OCLC_number_entry.get() != self._init_OCLC_number:
            changes.append(('OCLC Number', self._OCLC_number_entry.get()))

        if self._performer_entry.get() != self._init_performer:
            changes.append(('Performer', self._performer_entry.get()))

        if self._producer_entry.get() != self._init_producer:
            changes.append(('Producer', self._producer_entry.get()))

        if self._project_identifier_entry.get() != self._init_project_identifier:
            changes.append(('Project Identifier', self._project_identifier_entry.get()))

        if self._project_note_entry.get() != self._init_project_note:
            changes.append(('Project Note', self._project_note_entry.get()))

        if self._publisher_entry.get() != self._init_publisher:
            changes.append(('Publisher', self._publisher_entry.get()))

        if self._quality_control_notes_entry.get('0.0', END).replace('\n', '') != self._init_quality_control_notes:
            changes.append(('Quality Control Notes', self._quality_control_notes_entry.get('0.0', END).replace('\n', '')))

        if self._reference_URL_entry.get() != self._init_reference_url:
            changes.append(('Reference URL', self._reference_URL_entry.get()))

        if self._relationship_entry.get() != self._init_relationship:
            changes.append(('Relationship', self._relationship_entry.get()))

        if self._relationship_type_entry.get() != self._init_relationship_type:
            changes.append(('Relationship Type', self._relationship_type_entry.get()))

        if self._running_speed_entry.get() != self._init_running_speed:
            changes.append(('Running Speed', self._running_speed_entry.get()))

        if self._series_title_entry.get() != self._init_series_title:
            changes.append(('Series Title', self._series_title_entry.get()))

        if self._silent_or_sound_entry.get() != self._init_silent_or_sound:
            changes.append(('Silent or Sound', self._silent_or_sound_entry.get()))

        if self._sound_entry.get() != self._init_sound:
            changes.append(('Sound', self._sound_entry.get()))

        if self._spatial_coverage_entry.get() != self._init_spatial_coverage:
            changes.append(('Spatial Coverage', self._spatial_coverage_entry.get()))

        if self._speaker_entry.get() != self._init_speaker:
            changes.append(('Speaker', self._speaker_entry.get()))

        if self._stock_manufacturer_entry.get() != self._init_stock_manufacturer:
            changes.append(('Stock Manufacturer', self._stock_manufacturer_entry.get()))

        if self._subject_entity_entry.get() != self._initial_subject_entity:
            changes.append(('Subject_Entity', self._subject_entity_entry.get()))

        if self._subject_entity_authority_source_entry.get() != self._init_subject_entity_authority_source:
            changes.append(('Subject Entity Authority Source', self._subject_entity_authority_source_entry.get()))

        if self._subject_topic_entry.get() != self._init_subject_topic:
            changes.append(('Subject Topic', self._subject_topic_entry.get()))

        if self._subject_topic_authority_source_entry.get() != self._init_subject_topic_authority_source:
            changes.append(('Subject Topic Authority Source', self._subject_topic_authority_source_entry.get()))

        if self._subtitles_entry.get() != self._init_subtitles:
            changes.append(('Subtitles', self._subtitles_entry.get()))

        if self._temporal_coverage_entry.get() != self._init_temporal_coverage:
            changes.append(('Temporal Coverage', self._temporal_coverage_entry.get()))

        if self._timecode_content_begins_entry.get() != self._init_timecode_content_begins:
            changes.append(('Timecode Content Begins', self._timecode_content_begins_entry.get()))

        if self._total_number_of_reels_or_tapes_entry.get() != self._init_total_number_of_reels_or_tapes:
            changes.append(('Total Number of Reels or Tapes', self._total_number_of_reels_or_tapes_entry.get()))

        if self._track_standard_entry.get() != self._init_track_standard:
            changes.append(('Track Standard', self._track_standard_entry.get()))

        if self._transcript_entry.get() != self._init_transcript:
            changes.append(('Transcript', self._transcript_entry.get()))

        if self._why_significant_CA_entry.get('0.0', END).replace('\n', '') != self._init_why_significant_CA:
            changes.append(('Why the recording is significant to California/local history', self._why_significant_CA_entry.get('0.0', END).replace('\n', '')))

        if self._writer_entry.get() != self._init_writer:
            changes.append(('Writer', self._writer_entry.get()))

        return changes
        pass


class AlertWindow(object):
    def __init__(self, master, messages, csv):
        self.master = master

        self.csv = csv
        # try:
        #     self.master.destroy()
        # except:
        #     pass
        # self.warningMessageWindow = Toplevel(self.master)
        # self.master.title("warning")
        self.warningBackgroundFrame = ttk.Frame(self.master)
        self.warningBackgroundFrame.pack(fill=BOTH, expand=True)
        self.warningFrame = ttk.Frame(self.warningBackgroundFrame)
        self.warningFrame.pack(fill=BOTH, expand=True, pady=5, padx=5)

        warningMessages = ttk.Treeview(self.warningFrame)
        warningMessages.config(columns=('projectID', 'type', 'message'))
        warningMessages.heading('projectID', text='Project Identifier')
        warningMessages.heading('type', text='Type')
        warningMessages.heading('message', text='Message')
        warningMessages.pack(fill=BOTH, expand=True)
        self.optionsFrame = ttk.Frame(self.warningBackgroundFrame)
        self.optionsFrame.pack(fill=X, pady=5, padx=5)

        closeButton = ttk.Button(self.optionsFrame, text='Close', command=lambda: self.master.destroy())
        closeButton.grid(column=0, row=0, sticky=W+E+S)
        if system() == 'Darwin':
            editButton = ttk.Button(self.optionsFrame, text='Edit Source in Default Editor', command=self.edit_file)
            editButton.grid(column=2, row=0, sticky=W+E+S)

        for index, remark in enumerate(messages):

            warning_message = ""
            # print warning['record']
            # if 'record' in remark:
            #     warning_message += remark['record']
            if 'received' in remark:
                warning_message += ("\"" + remark['received'] + "\"")
            if 'location' in remark:
                warning_message += (" at [" + remark['location'] + "].")
            else:
                warning_message += "."
            if 'message' in remark:
                warning_message += remark['message']
            warningMessages.insert('', index, index+1, text=index+1)
            warningMessages.column('#0', width=40, anchor=W, stretch=NO)
            warningMessages.column('projectID', width=150, stretch=NO)
            warningMessages.column('type', width=150, stretch=NO)
            warningMessages.column('message', width=400)
            # warningMessages.set(index+1, '#0', index)
            warningMessages.set(index+1, 'projectID', remark['record'])
            warningMessages.set(index+1, 'type', remark['type'])
            warningMessages.set(index+1, 'message', warning_message)
            # warningMessages.insert(END, (str(index+1) + ") " + warning_message))


    def edit_file(self):
        command = "open " + self.csv
        os.system(command)
if __name__ == '__main__':
    from pbcore_csv import pbcoreBuilder
    sys.stderr.write("Not a standalone program. Please run pbcore-csv.py -g to run the GUI")
    # # print()
    # # TODO: Delete when done testing -------#-|
    # root = Tk()                             # |
    # ini_file = "/Users/lpsdesk/PycharmProjects/PBcore/settings/pbcore-csv-settings.ini"
    # root.wm_title('Details')       # |
    # root.resizable(FALSE,FALSE)             # |
    # app = RecordDetailsWindow(root, "/Users/lpsdesk/PycharmProjects/PBcore/sample_records/casacsh_000048_export.csv", "cavpp002554")    # | <== This can go when done testing --<
    # root.mainloop()                         # |
    # --------------------------------------#-|
else:
    import pbcore_csv