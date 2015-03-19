__author__ = 'California Audio Visual Preservation Project'
__copyright__ = "California Audiovisual Preservation Project. 2015"
__credits__ = ["Henry Borchers"]
__version__ = "0.0.0.1"
__license__ = 'TBD'

import csv
import os
from time import sleep
from tkFileDialog import askopenfilename
from tkMessageBox import showerror

import threading
from Tkinter import *
import ttk



class MainWindow():
    def __init__(self, master, input_file=None, settings=None):
        self.master = master
        self.settings = settings
        self.csv_status = ""
        self.item_total = IntVar()
        self.item_total.set(0)
        self.item_progress = IntVar()
        self.item_progress.set(0)

        self.part_total = IntVar()
        self.part_total.set(0)
        self.part_progress = IntVar()
        self.part_total.set(0)

        self.display_records = []
        # ---------- Menus -----------
        self.master.option_add('*tearOff', False)
        self.menu_bar = Menu(master)
        self.master.config(menu=self.menu_bar)
        self.fileMenu = Menu(self.menu_bar)
        self.settingsMenu = Menu(self.menu_bar)
        self.helpMenu = Menu(self.menu_bar)

        self.menu_bar.add_cascade(menu=self.fileMenu, label="File")
        self.menu_bar.add_cascade(menu=self.settingsMenu, label="Settings")
        self.menu_bar.add_cascade(menu=self.helpMenu, label="Help")

        self.fileMenu.add_command(label="Open...", command=self.retrieve_folder)
        self.fileMenu.entryconfig('Open...', accelerator='Ctrl + O')
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=lambda: quit())

        self.settingsMenu.add_command(label="View Settings File...", command=self.view_settings)

        self.helpMenu.add_command(label="About...",
                                  command=self.load_about_window)

        # ----------
        self.background = ttk.Frame(self.master, padding=(20,10))
        self.background.pack(fill=BOTH, expand=True)
        # ----------
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

        # ----------
        self.dataEntryFrame = ttk.Frame(self.panel,
                                        height=100,
                                        width=100,
                                        padding=(30, 15),
                                        relief=SUNKEN)
        # self.dataEntryFrame.grid(row=2, column=1)
        self.panel.add(self.dataEntryFrame, weight=4)


        self.csv_filename_label = ttk.Label(self.dataEntryFrame,
                                            text="CSV file",
                                            width=10)
        self.csv_filename_label.grid(row=2, column=0, sticky=E)
        self.csv_filename_entry = ttk.Entry(self.dataEntryFrame, width=80)
        self.csv_filename_entry.grid(row=2, column=1, columnspan=5, sticky=W+E)


        self.locateCSVButton = ttk.Button(self.dataEntryFrame,
                                          text='Browse',
                                          command=self.retrieve_folder)
        self.locateCSVButton.grid(row=2, column=6, sticky=E)

        self.startButton = ttk.Button(self.dataEntryFrame,
                                      text='Start',
                                      command=self.start)
        self.startButton.grid(row=3, column=6, sticky=E)

        self.validate_label = ttk.Label(self.dataEntryFrame, text='File Status:')
        self.validate_label.grid(row=3, column=0, sticky=W)
        self.validate_entry = ttk.Entry(self.dataEntryFrame, state=DISABLED)
        self.validate_entry.grid(row=3, column=1, sticky=W+E)
        self.validate_details_button = ttk.Button(self.dataEntryFrame, text='Details', command=self.show_details)
        self.validate_details_button.grid(row=3, column=2, sticky=W)

        # --------------------  Records  --------------------

        self.recordsFrame = ttk.Frame(self.panel,
                                               height=200,
                                               width=100,
                                               padding=(5, 5),
                                               relief=SUNKEN)

        self.panel.add(self.recordsFrame)

        # self.recordsList = Listbox(self.recordsFrame)
        self.recordsTree = ttk.Treeview(self.recordsFrame, columns=('title', 'project', 'files', 'xml_file'))
        self.recordsTree.heading('xml_file', text='Save As')
        self.recordsTree.heading('title', text='Title')
        self.recordsTree.heading('project', text='Project')
        self.recordsTree.heading('files', text='Files')
        self.recordsTree.column('#0', width=20, anchor='center')
        self.recordsTree.column('xml_file', width=150)
        self.recordsTree.column('project', width=100)
        self.recordsTree.column('title', width=250)
        self.recordsTree.pack(fill=BOTH, expand=True)

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
# ============================= status bar =============================
        self.statusBar = Label(self.master, text="test", bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)


# ============================= Load the data into tree =============================
        if input_file:
            self.csv_filename_entry.insert(0, input_file)
            if self.validate(input_file):
                self.file_records = pbcore_csv.pbcoreBuilder(input_file)
                self.file_records.load_records()
                self.load_records_list(self.file_records.records)

        self.running = False

    def load_about_window(self):
        aboutRoot = Toplevel(self.master)
        aboutRoot.wm_title("About")
        aboutRoot.resizable(FALSE,FALSE)
        about = AboutWindow(aboutRoot)

    def show_details(self):
        if self.remarks:
            self.alerts(self.remarks, type=self.csv_status)

    def retrieve_folder(self):
        fileName = askopenfilename()
        if fileName != "":
            self.csv_filename_entry.delete(0, END)
            self.csv_filename_entry.insert(0, fileName)
            if self.validate(fileName):
                self.file_records = pbcore_csv.pbcoreBuilder(fileName)
                self.file_records.load_records()
                self.load_records_list(self.file_records.records)
            else:
                for i in self.recordsTree.get_children():
                    self.recordsTree.delete(i)

    def view_settings(self):
        settingsRoot = Toplevel(self.master)
        settingsRoot.wm_title("Settings")
        settings = SettingsWindow(settingsRoot, self.settings)

        # f = open(self.settings)
        # self.settingsWindow = Toplevel(self.background)
        # self.settingsWindow.title("Settings")
        # self.settingsBackgroundFrame = ttk.Frame(self.settingsWindow, padding=(5,5))
        # self.settingsBackgroundFrame.pack(fill=BOTH, expand=True)
        # self.settingsFrame = ttk.Labelframe(self.settingsBackgroundFrame, text=f.name, padding=(10,10))
        # self.settingsFrame.pack(padx=5, pady=5, fill=BOTH, expand=True)
        # self.scrollbar = Scrollbar(self.settingsFrame)
        # self.scrollbar.pack(side=RIGHT, fill=Y)
        # self.settingsText = Text(self.settingsFrame, yscrollcommand=self.scrollbar.set)
        # self.settingsText.pack(fill=BOTH, expand=True)
        # self.scrollbar.config(command=self.settingsText.yview)
        # closeButton = ttk.Button(self.settingsBackgroundFrame, text="Close", command=lambda: self.settingsWindow.destroy())
        # closeButton.pack()
        # # print f.name
        # for line in f.readlines():
        #     self.settingsText.insert(END, line)
        # f.close()
        #
        # self.settingsText.config(state=DISABLED)

    def edit_file(self):
        print "Editing: " + self.csv_filename_entry.get()
        command = "open " + self.csv_filename_entry.get()
        os.system(command)


    def alerts(self, messages, type="Error"):
        try:
            self.warningMessageWindow.destroy()
        except:
            pass
        self.warningMessageWindow = Toplevel(self.master)
        self.warningMessageWindow.title(type)
        self.warningBackgroundFrame = ttk.Frame(self.warningMessageWindow)
        self.warningBackgroundFrame.pack(fill=BOTH, expand=True)
        self.warningFrame = ttk.Frame(self.warningBackgroundFrame)
        self.warningFrame.pack(fill=BOTH, expand=True, pady=5, padx=5)
        # warningMessages = Text(warningMessageWindow)
        # warningMessages = Listbox(self.warningMessageWindow, width=75)
        warningMessages = ttk.Treeview(self.warningFrame)
        warningMessages.config(columns=('projectID', 'type', 'message'))
        warningMessages.heading('projectID', text='Project Identifier')
        warningMessages.heading('type', text='Type')
        warningMessages.heading('message', text='Message')
        warningMessages.pack(fill=BOTH, expand=True)
        self.optionsFrame = ttk.Frame(self.warningBackgroundFrame)
        self.optionsFrame.pack(fill=BOTH, expand=True, pady=5, padx=5)

        closeButton = ttk.Button(self.optionsFrame, text='Close', command=lambda: self.warningMessageWindow.destroy())
        closeButton.grid(column=0, row=0, sticky=W+E+S)

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
            warningMessages.column('#0', width=40, anchor='center')
            warningMessages.column('projectID', width=150)
            warningMessages.column('message', width=400)
            # warningMessages.set(index+1, '#0', index)
            warningMessages.set(index+1, 'projectID', remark['record'])
            warningMessages.set(index+1, 'type', remark['type'])
            warningMessages.set(index+1, 'message', warning_message)
            # warningMessages.insert(END, (str(index+1) + ") " + warning_message))

    def validate(self, in_file):
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
                # f = open(in_file, 'rU')
                # records = []
                # for item in csv.DictReader(f):
                #     records.append(item)
                # f.close()
                self.remarks = []
                # total_errors = []
                warnings, errors = testFile.check_content_valid()
                # for record in testFile.records:
                #     warnings, errors = testFile.content_valid(record)
                #     self.remarks += warnings
                self.remarks += warnings
                # for warning in total_warnings:
                #     print warning
                if self.remarks:
                    self.alerts(self.remarks, type="Warnings")
                    self.csv_status = "Warnings"
                    self.validate_entry.config(state=NORMAL)
                    self.validate_entry.delete(0,END)
                    self.validate_entry.insert(0, "Warning: Click details for more info.")
                    self.validate_entry.config(state=DISABLED)
                    self.validate_details_button.config(state=NORMAL)
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
            file_name_pattern = re.compile("[A-Z,a-z]+_\d+")
            fileName = re.search(file_name_pattern, record['Object Identifier']).group(0)
            parts = record['Object Identifier'].split(';')

            media_files = self.locate_files(root=os.path.dirname(self.csv_filename_entry.get()), fileName=fileName)
            pres, access = sep_pres_access(media_files)
            media_files = pres + access

            outIndex = record['Main or Supplied Title']
            self.recordsTree.insert('', index, outIndex, text=index+1)
            self.recordsTree.set(outIndex, 'title', record['Main or Supplied Title'])
            self.recordsTree.set(outIndex, 'project', record['Project Identifier'])
            self.recordsTree.set(outIndex, 'files', str(len(media_files)) + " Files Found")
            # fileName = fileName + "_ONLYTEST.xml"
            self.recordsTree.set(outIndex, 'xml_file', fileName + "_ONLYTEST.xml")
            # print self.recordsTree.get_children()
            # for a_index, part in enumerate(parts):
            #     inIndex = str(a_index)+outIndex
            #     self.recordsTree.insert(outIndex, a_index, inIndex)
            #     self.recordsTree.set(inIndex, 'objectID', part.strip())
            for a_index, media_file in enumerate(media_files):
                inIndex = str(a_index)+outIndex
                self.recordsTree.insert(outIndex, a_index, inIndex)
                self.recordsTree.set(inIndex, 'files', os.path.basename(media_file.strip()))
                # print a_index
                # self.recordsTree.set(index+1, 'object', part.strip())
            # self.recordsTree.insert('', index, index, text=record['Project Identifier'])
            # self.recordsTree.insert('', index, index, text=record['Project Identifier'])

    def locate_files(self, root, fileName):
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

    def get_records(self, file_name):
        f = open(file_name, 'rU')
        records = []
        for item in csv.DictReader(f):
            records.append(item)
        # self.records = csv.DictReader(f)
        f.close()
        return records


    def start(self):

        if self.running is False:
            self.display_records = []
            self.display_records = self.get_records(self.csv_filename_entry.get())
            self.set_total_progress(progress=0, total=10)

            if self.validate(self.csv_filename_entry.get()):
                savefile = pbcore_csv.pbcoreBuilder(self.csv_filename_entry.get())

                self.generate = observer(savefile)
                self.generate.daemon = True
                self.generate.start()
            self.update_progress()

            self.running = True
        else:
            self.total_progress_pbar.stop()
            self.running = False
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
class AboutWindow():
    def __init__(self, master):
        self.master = master
        self.master.resizable(width=None, height=None)
        self.background = ttk.Frame(self.master, width=20, padding=10)
        self.background.pack(fill=BOTH, expand=True)

# ----------------- Title
        self.titleFrame = ttk.Frame(self.background, width=20, padding=10, relief=RIDGE)
        self.titleFrame.pack()
        self.titleLabel = ttk.Label(self.titleFrame, text="CAVPP PBCore Builder")
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
        self.closeButton.pack()

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
        self.records.join()
        self._record_total = self.records.job_total
        self._md5_progress = self.records.calculation_percent
        self._part_progress = self.records.parts_progress
        self._part_total = self.records.parts_total
        self._record_progress = self.records.job_progress


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


if __name__ == '__main__':
    sys.stderr.write("Not a standalone program. Please run pbcore-csv.py -g to run the GUI")
    # # print()
    # # TODO: Delete when done testing -------#-|
    # root = Tk()                             # |
    # ini_file = "/Users/lpsdesk/PycharmProjects/PBcore/settings/pbcore-csv-settings.ini"
    # root.wm_title('PBCore Generator')       # |
    # root.resizable(FALSE,FALSE)             # |
    # app = SettingsWindow(root, ini_file)    # | <== This can go when done testing --<
    # root.mainloop()                         # |
    # --------------------------------------#-|
else:
    import pbcore_csv