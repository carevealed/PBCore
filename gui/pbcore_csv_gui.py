from platform import system
import tkFileDialog

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

FILE_NAME_PATTERN = re.compile("[A-Z,a-z]+_\d+")

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
        # -------------------- Menus --------------------
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
        self.locateCSVButton.grid(row=2, column=0, sticky=E)

        self.startButton = ttk.Button(self.dataEntryFrame,
                                      text='Start',
                                      command=self.start)
        self.startButton.grid(row=3, column=0, sticky=E)

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

        if system() == 'Darwin':
            self.recordsTree.bind("<Button-2>", self._popup)
        else:
            self.recordsTree.bind("<Button-3>", self._popup)

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
        self.statusBar = Label(self.master, text="", bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)

     # -------------------- Context Menu --------------------

        self.propertyMenu = Menu(self.recordsTree, tearoff=0)
        self.propertyMenu.add_command(label="Change Export Name", command=lambda: self.change_export(self.recordsTree.selection()))
        self.propertyMenu.add_command(label="More Info", command=lambda: self.view_item_details(self.recordsTree.selection()))


# ============================= Load the data into tree =============================
        if input_file:
            self.csv_filename_entry.insert(0, input_file)
            if self.validate(input_file):
                self.file_records = pbcore_csv.pbcoreBuilder(input_file)
                self.file_records.load_records()
                self.load_records_list(self.file_records.records)

        self.running = False
    def _popup(self, event):
        # self.propertyMenu.post()
        if self.recordsTree.selection():
            print "gotcha", self.recordsTree.selection()
            self.propertyMenu.post(event.x_root, event.y_root)

    def view_item_details(self, record):
        item = record[0]
        project_id = self.recordsTree.set(item)['project']
        print(project_id)
        itemsRoot = Toplevel(self.master)
        itemsRoot.wm_title("Details: " + project_id)
        item = RecordDetailsWindow(itemsRoot, self.csv_filename_entry.get(), project_id)


    def change_export(self, record):
        print "Changing Name of " + record[0]
        f = tkFileDialog.asksaveasfilename(defaultextension=".xml")
        if f:
            print "changing to " + f
            self.recordsTree.set(record[0], column="xml_file", value=f)

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

            fileName = re.search(FILE_NAME_PATTERN, record['Object Identifier']).group(0)
            parts = record['Object Identifier'].split(';')

            media_files = self.locate_files(root=os.path.dirname(self.csv_filename_entry.get()), fileName=fileName)
            pres, access = sep_pres_access(media_files)
            media_files = pres + access

            outIndex = record['Main or Supplied Title']
            self.recordsTree.insert('', index, outIndex, text=index+1)
            self.recordsTree.set(outIndex, 'title', record['Main or Supplied Title'])
            self.recordsTree.set(outIndex, 'project', record['Project Identifier'])
            self.recordsTree.set(outIndex, 'files', str(len(media_files)) + " Files Found")

            self.recordsTree.set(outIndex, 'xml_file', fileName + "_ONLYTEST.xml")

            # for a_index, media_file in enumerate(media_files):
            #     inIndex = str(a_index)+outIndex
            #     self.recordsTree.insert(outIndex, a_index, inIndex)
            #     self.recordsTree.set(inIndex, 'files', os.path.basename(media_file.strip()))

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
        self.statusBar.config(text=self.generate.status)
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
        foo = pbcore_csv.pbcoreBuilder(self.csv_filename_entry.get())
        foo.load_records()
        # print foo.source
        for record in self.recordsTree.get_children():
            print(self.recordsTree.set(record))
        # foo.get_record("adfa")
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
    def __init__(self, master, csv, projectID):
        self.style = ttk.Style()
        self.style.configure('labels.TLabel', wraplength=150)
        self.style.configure('labels.TEntry', width=300)
        self.master = master
        # print "new records details: " + projectID + " in " + csv
        data = pbcore_csv.pbcoreBuilder(csv)
        data.load_records()
        self.properties = data.get_record(projectID)

        # ------------ background --------------
        self.background = ttk.Frame(self.master, padding=(10,10))
        self.background.pack(fill=BOTH, expand=True)

        # ------------ Title --------------
        self.titleFrame = ttk.Frame(self.background, padding=(10,10), relief=RIDGE)
        self.titleFrame.pack(pady=20)
        self.label = ttk.Label(self.titleFrame, text="Details")
        self.label.pack()

        # ------------ data --------------

        # self.dataOuterFrame = ttk.Frame(self.background, padding=(10,10))
        self.dataOuterFrame = ttk.LabelFrame(self.background, text="Record Data")
        self.dataOuterFrame.pack(fill=BOTH, expand=True)

        self.vscrollbar = Scrollbar(self.dataOuterFrame, orient=VERTICAL)
        self.vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.canvas=Canvas(self.dataOuterFrame, yscrollcommand=self.vscrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
        self.vscrollbar.config(command=self.canvas.yview)

        self.dataFrame = interior = Frame(self.canvas)
        self.dataFrame.pack()
        interior_id = self.canvas.create_window(0, 0, window=interior,
                                           anchor=NW)
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
        self.Date_Created_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Date Created:")
        self.Date_Created_Label.grid(row=0, column=0, sticky=N+E)


        self.Date_Created_Entry = ttk.Entry(self.dataFrame)
        self.Date_Created_Entry.grid(row=0, column=1, columnspan=2, sticky=NE+W)

        self.Object_ARK_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Object_ARK:")
        self.Object_ARK_Label.grid(row=1, column=0, sticky=N+E)

        self.Object_ARK_Entry = ttk.Entry(self.dataFrame)
        self.Object_ARK_Entry.grid(row=1, column=1, columnspan=2, sticky=N+E+W)

        self.Timecode_Content_Begins_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Timecode Content Begins:")
        self.Timecode_Content_Begins_Label.grid(row=2, column=0, sticky=N+E)

        self.Timecode_Content_Begins_Entry = ttk.Entry(self.dataFrame)
        self.Timecode_Content_Begins_Entry.grid(row=2, column=1, columnspan=2, sticky=N+E+W)

        self.Media_Type_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Media Type:")
        self.Media_Type_Label.grid(row=3, column=0, sticky=N+E)

        self.Media_Type_Entry = ttk.Entry(self.dataFrame)
        self.Media_Type_Entry.grid(row=3, column=1, columnspan=2, sticky=N+E+W)

        self.Interviewee_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Interviewee:")
        self.Interviewee_Label.grid(row=4, column=0, sticky=N+E)

        self.Interviewee_Entry = ttk.Entry(self.dataFrame)
        self.Interviewee_Entry.grid(row=4, column=1, columnspan=2, sticky=N+E+W)

        self.Series_Title_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Series Title:")
        self.Series_Title_Label.grid(row=5, column=0, sticky=N+E)

        self.Series_Title_Entry = ttk.Entry(self.dataFrame)
        self.Series_Title_Entry.grid(row=5, column=1, columnspan=2, sticky=N+E+W)

        self.Temporal_Coverage_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Temporal Coverage:")
        self.Temporal_Coverage_Label.grid(row=6, column=0, sticky=N+E)

        self.Temporal_Coverage_Entry = ttk.Entry(self.dataFrame)
        self.Temporal_Coverage_Entry.grid(row=6, column=1, columnspan=2, sticky=N+E+W)

        self.Writer_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Writer:")
        self.Writer_Label.grid(row=7, column=0, sticky=N+E)

        self.Writer_Entry = ttk.Entry(self.dataFrame)
        self.Writer_Entry.grid(row=7, column=1, columnspan=2, sticky=N+W+E)

        self.Institution_URL_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Institution URL:")
        self.Institution_URL_Label.grid(row=8, column=0, sticky=N+E)

        self.Institution_URL_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Institution_URL_Entry.grid(row=8, column=1, columnspan=2, sticky=N+E+W)

        self.Project_Identifier_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Project Identifier:")
        self.Project_Identifier_Label.grid(row=9, column=0, sticky=N+E)

        self.Project_Identifier_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Project_Identifier_Entry.grid(row=9, column=1, columnspan=2, sticky=N+S+E+W)

        self.Quality_Control_Notes_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Quality Control Notes:")
        self.Quality_Control_Notes_Label.grid(row=10, column=0, sticky=N+E)

        self.Quality_Control_Notes_Entry = Text(self.dataFrame, width=40, height=10, wrap=WORD)
        self.Quality_Control_Notes_Entry.grid(row=10, column=1, columnspan=2, rowspan=5, sticky=N+E+W)

        self.Silent_or_Sound_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Silent or Sound:")
        self.Silent_or_Sound_Label.grid(row=15, column=0, sticky=N+E)

        self.Silent_or_Sound_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Silent_or_Sound_Entry.grid(row=15, column=1, columnspan=2, sticky=N+S+E+W)

        self.Camera_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Camera:")
        self.Camera_Label.grid(row=16, column=0, sticky=N+E)

        self.Camera_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Camera_Entry.grid(row=16, column=1, columnspan=2, sticky=N+S+E+W)

        self.Music_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Music:")
        self.Music_Label.grid(row=17, column=0, sticky=N+E)

        self.Music_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Music_Entry.grid(row=17, column=1, columnspan=2, sticky=N+S+E+W)

        self.Editor_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Editor:")
        self.Editor_Label.grid(row=18, column=0, sticky=N+E)

        self.Editor_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Editor_Entry.grid(row=18, column=1, columnspan=2, sticky=N+S+E+W)

        self.Track_Standard_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Track Standard:")
        self.Track_Standard_Label.grid(row=19, column=0, sticky=N+E)

        self.Track_Standard_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Track_Standard_Entry.grid(row=19, column=1, columnspan=2, sticky=N+E+W)

        self.CONTENTdm_number_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="CONTENTdm number:")
        self.CONTENTdm_number_Label.grid(row=20, column=0, sticky=N+E)

        self.CONTENTdm_number_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.CONTENTdm_number_Entry.grid(row=20, column=1, columnspan=2, sticky=N+E+W)

        self.Subtitles_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Subtitles:")
        self.Subtitles_Label.grid(row=19, column=0, sticky=N+E)

        self.Subtitles_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Subtitles_Entry.grid(row=19, column=1, columnspan=2, sticky=N+S+E+W)

        self.Distributor_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Distributor:")
        self.Distributor_Label.grid(row=20, column=0, sticky=N+E)

        self.Distributor_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Distributor_Entry.grid(row=20, column=1, columnspan=2, sticky=N+E+W)

        self.Date_modified_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Date modified:")
        self.Date_modified_Label.grid(row=19, column=0, sticky=N+E)

        self.Date_modified_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Date_modified_Entry.grid(row=19, column=1, columnspan=2, sticky=N+S+E+W)

        self.Subject_Topic_Authority_Source_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Subject Topic Authority Source:")
        self.Subject_Topic_Authority_Source_Label.grid(row=20, column=0, sticky=N+E)

        self.Subject_Topic_Authority_Source_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Subject_Topic_Authority_Source_Entry.grid(row=20, column=1, columnspan=2, sticky=N+S+E+W)

        self.Aspect_Ratio_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Aspect Ratio:")
        self.Aspect_Ratio_Label.grid(row=21, column=0, sticky=N+E)

        self.Aspect_Ratio_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Aspect_Ratio_Entry.grid(row=21, column=1, columnspan=2, sticky=N+E+W)

        self.Total_Number_of_Reels_or_Tapes_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Total Number of Reels or Tapes:")
        self.Total_Number_of_Reels_or_Tapes_Label.grid(row=22, column=0, sticky=N+E)

        self.Total_Number_of_Reels_or_Tapes_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Total_Number_of_Reels_or_Tapes_Entry.grid(row=22, column=1, columnspan=2, sticky=N+S+E+W)

        self.Copyright_Holder_Info_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Copyright Holder Info:")
        self.Copyright_Holder_Info_Label.grid(row=23, column=0, sticky=N+E)

        self.Copyright_Holder_Info_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Copyright_Holder_Info_Entry.grid(row=23, column=1, columnspan=2, sticky=N+S+E+W)

        self.Running_Speed_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Running Speed")
        self.Running_Speed_Label.grid(row=24, column=0, sticky=N+E)

        self.Running_Speed_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Running_Speed_Entry.grid(row=24, column=1, columnspan=2, sticky=N+S+E+W)

        self.Subject_Entity_Authority_Source_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Subject Entity Authority Source:")
        self.Subject_Entity_Authority_Source_Label.grid(row=25, column=0, sticky=N+E)

        self.Subject_Entity_Authority_Source_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Subject_Entity_Authority_Source_Entry.grid(row=25, column=1, columnspan=2, sticky=N+S+E+W)

        self.Additional_Technical_Notes_for_Overall_Work_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Additional Technical Notes for Overall Work:")
        self.Additional_Technical_Notes_for_Overall_Work_Label.grid(row=26, column=0, sticky=N+E)

        # self.Additional_Technical_Notes_for_Overall_Work_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Additional_Technical_Notes_for_Overall_Work_Entry = Text(self.dataFrame, width=40, height=10, wrap=WORD)
        self.Additional_Technical_Notes_for_Overall_Work_Entry.grid(row=26, column=1, columnspan=2, sticky=N+S+E+W)

        self.Musician_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Musician")
        self.Musician_Label.grid(row=27, column=0, sticky=N+E)

        self.Musician_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Musician_Entry.grid(row=27, column=1, columnspan=2, sticky=N+S+E+W)

        self.Main_or_Supplied_Title_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Main or Supplied Title:")
        self.Main_or_Supplied_Title_Label.grid(row=28, column=0, sticky=N+E)

        self.Main_or_Supplied_Title_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Main_or_Supplied_Title_Entry.grid(row=28, column=1, columnspan=2, sticky=N+S+E+W)

        self.Internet_Archive_URL_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Internet Archive URL:")
        self.Internet_Archive_URL_Label.grid(row=29, column=0, sticky=N+E)

        self.Internet_Archive_URL_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Internet_Archive_URL_Entry.grid(row=29, column=1, columnspan=2, sticky=N+S+E+W)

        # ------------ columns 3 + 4 ----------
        #
        self.Relationship_Type_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Relationship Type:")
        self.Relationship_Type_Label.grid(row=30, column=0, stick=S+E)
        self.Relationship_Type_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Relationship_Type_Entry.grid(row=30, column=1, columnspan=2, sticky=N+S+E+W)

        self.Director_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Director:")
        self.Director_Label.grid(row=31, column=0, stick=S+E)
        self.Director_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Director_Entry.grid(row=31, column=1, columnspan=2, sticky=N+S+E+W)

        self.Copyright_Statement_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Copyright Statement:")
        self.Copyright_Statement_Label.grid(row=32, column=0, stick=S+E)
        self.Copyright_Statement_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Copyright_Statement_Entry.grid(row=32, column=1, columnspan=2, sticky=N+S+E+W)

        self.Genre_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Genre")
        self.Genre_Label.grid(row=33, column=0, stick=S+E)
        self.Genre_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Genre_Entry.grid(row=33, column=1, columnspan=2, sticky=N+S+E+W)

        self.Cataloger_Notes_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Cataloger Notes:")
        self.Cataloger_Notes_Label.grid(row=34, column=0, stick=S+E)
        self.Cataloger_Notes_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Cataloger_Notes_Entry.grid(row=34, column=1, columnspan=2, sticky=N+S+E+W)

        self.Collection_Guide_URL_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Collection Guide URL:")
        self.Collection_Guide_URL_Label.grid(row=35, column=0, stick=S+E)
        self.Collection_Guide_URL_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Collection_Guide_URL_Entry.grid(row=35, column=1, columnspan=2, sticky=N+S+E+W)

        self.Interviewer_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Interviewer:")
        self.Interviewer_Label.grid(row=36, column=0, stick=S+E)
        self.Interviewer_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Interviewer_Entry.grid(row=36, column=1, columnspan=2, sticky=N+S+E+W)

        self.Description_or_Content_Summary_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Description or Content Summary:")
        self.Description_or_Content_Summary_Label.grid(row=37, column=0, stick=N+E)
        # self.Description_or_Content_Summary_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Description_or_Content_Summary_Entry = Text(self.dataFrame, width=40, height=6, wrap=WORD)
        self.Description_or_Content_Summary_Entry.grid(row=37, column=1, columnspan=2, rowspan=3, sticky=N+E+W)

        self.Institution_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Institution:")
        self.Institution_Label.grid(row=40, column=0, stick=N+E)
        self.Institution_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Institution_Entry.grid(row=40, column=1, sticky=N+E+W)

        self.Stock_Manufacturer_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Stock Manufacturer:")
        self.Stock_Manufacturer_Label.grid(row=41, column=0, stick=N+E)
        self.Stock_Manufacturer_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Stock_Manufacturer_Entry.grid(row=41, column=1, columnspan=2, sticky=N+E+W)

        self.Sound_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Sound:")
        self.Sound_Label.grid(row=42, column=0, stick=N+E)
        self.Sound_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Sound_Entry.grid(row=42, column=1, columnspan=2, sticky=N+E+W)

        self.Publisher_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Publisher:")
        self.Publisher_Label.grid(row=43, column=0, stick=S+E)
        self.Publisher_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Publisher_Entry.grid(row=43, column=1, columnspan=2, sticky=N+S+E+W)

        self.Asset_Type_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Asset Type:")
        self.Asset_Type_Label.grid(row=46, column=0, stick=S+E)
        self.Asset_Type_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Asset_Type_Entry.grid(row=46, column=1, columnspan=2, sticky=N+S+E+W)

        self.Object_Identifier_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Object Identifier:")
        self.Object_Identifier_Label.grid(row=43, column=0, stick=N+E)
        self.Object_Identifier_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Object_Identifier_Entry.grid(row=43, column=1, columnspan=2, sticky=N+E+W)

        self.Copyright_Date_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Copyright Date:")
        self.Copyright_Date_Label.grid(row=44, column=0, stick=S+E)
        self.Copyright_Date_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Copyright_Date_Entry.grid(row=44, column=1, columnspan=2, sticky=N+S+E+W)

        self.Copyright_Holder_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Copyright Holder:")
        self.Copyright_Holder_Label.grid(row=45, column=0, stick=S+E)
        self.Copyright_Holder_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Copyright_Holder_Entry.grid(row=45, column=1, columnspan=2, sticky=N+S+E+W)

        self.Language_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Language")
        self.Language_Label.grid(row=46, column=0, stick=S+E)
        self.Language_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Language_Entry.grid(row=46, column=1, columnspan=2, sticky=N+S+E+W)

        self.Color_and_or_Black_and_White_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Color and or Black and White:")
        self.Color_and_or_Black_and_White_Label.grid(row=47, column=0, stick=S+E)
        self.Color_and_or_Black_and_White_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Color_and_or_Black_and_White_Entry.grid(row=47, column=1, columnspan=2, sticky=N+S+E+W)

        self.Institution_ARK_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Institution ARK:")
        self.Institution_ARK_Label.grid(row=48, column=0, stick=S+E)
        self.Institution_ARK_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Institution_ARK_Entry.grid(row=48, column=1, columnspan=2, sticky=N+S+E+W)

        self.CONTENTdm_file_name_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="CONTENTdm file name:")
        self.CONTENTdm_file_name_Label.grid(row=49, column=0, stick=S+E)
        self.CONTENTdm_file_name_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.CONTENTdm_file_name_Entry.grid(row=49, column=1, columnspan=2, sticky=N+S+E+W)

        self.OCLC_number_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="OCLC number:")
        self.OCLC_number_Label.grid(row=50, column=0, stick=S+E)
        self.OCLC_number_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.OCLC_number_Entry.grid(row=50, column=1, columnspan=2, sticky=N+S+E+W)

        self.Why_the_recording_is_significant_to_California_local_history_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Why the recording is significant to California local history:")
        self.Why_the_recording_is_significant_to_California_local_history_Label.grid(row=51, column=0, stick=N+E)
        self.Why_the_recording_is_significant_to_California_local_history_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Why_the_recording_is_significant_to_California_local_history_Entry = Text(self.dataFrame, width=40, height=10, wrap=WORD)
        self.Why_the_recording_is_significant_to_California_local_history_Entry.grid(row=51, column=1, columnspan=2, rowspan=5, sticky=N+S+E+W)

        self.Subject_Entity_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Subject_Entity:")
        self.Subject_Entity_Label.grid(row=52, column=0, stick=S+E)
        self.Subject_Entity_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Subject_Entity_Entry.grid(row=52, column=1, columnspan=2, sticky=N+S+E+W)

        self.Gauge_and_Format_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Gauge and Format:")
        self.Gauge_and_Format_Label.grid(row=53, column=0, stick=S+E)
        self.Gauge_and_Format_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Gauge_and_Format_Entry.grid(row=53, column=1, columnspan=2, sticky=N+S+E+W)

        self.Additional_Descriptive_Notes_for_Overall_Work_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Additional Descriptive Notes for Overall Work:")
        self.Additional_Descriptive_Notes_for_Overall_Work_Label.grid(row=54, column=0, stick=S+E)
        self.Additional_Descriptive_Notes_for_Overall_Work_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Additional_Descriptive_Notes_for_Overall_Work_Entry.grid(row=54, column=1, columnspan=2, rowspan=2, sticky=N+S+E+W)

        self.Genre_Authority_Source_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Genre Authority Source:")
        self.Genre_Authority_Source_Label.grid(row=55, column=0, stick=S+E)
        self.Genre_Authority_Source_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Genre_Authority_Source_Entry.grid(row=55, column=1, columnspan=2, sticky=N+S+E+W)

        self.Date_Published_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Date Published:")
        self.Date_Published_Label.grid(row=56, column=0, stick=S+E)
        self.Date_Published_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Date_Published_Entry.grid(row=56, column=1, columnspan=2, sticky=N+S+E+W)

        self.Country_of_Creation_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Country of Creation:")
        self.Country_of_Creation_Label.grid(row=57, column=0, stick=S+E)
        self.Country_of_Creation_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Country_of_Creation_Entry.grid(row=57, column=1, columnspan=2, sticky=N+S+E+W)

        self.Project_Note_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Project Note:")
        self.Project_Note_Label.grid(row=58, column=0, stick=S+E)
        self.Project_Note_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Project_Note_Entry.grid(row=58, column=1, columnspan=2, sticky=N+S+E+W)

        self.Institutional_Rights_Statement_URL_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Institutional Rights Statement URL:")
        self.Institutional_Rights_Statement_URL_Label.grid(row=59, column=0, stick=S+E)
        self.Institutional_Rights_Statement_URL_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Institutional_Rights_Statement_URL_Entry.grid(row=59, column=1, columnspan=2, sticky=N+S+E+W)
        #
        # # ------ columns 4+5 ------
        self.Spatial_Coverage_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Spatial Coverage:")
        self.Spatial_Coverage_Label.grid(row=60, column=0, sticky=S+E)
        self.Spatial_Coverage_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Spatial_Coverage_Entry.grid(row=60, column=1, columnspan=2, sticky=N+S+E+W)

        self.Copyright_Notice_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Copyright Notice:")
        self.Copyright_Notice_Label.grid(row=61, column=0, sticky=S+E)
        self.Copyright_Notice_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Copyright_Notice_Entry.grid(row=61, column=1, columnspan=2, sticky=N+S+E+W)

        self.Subject_Topic_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Subject Topic:")
        self.Subject_Topic_Label.grid(row=62, column=0, sticky=S+E)
        self.Subject_Topic_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Subject_Topic_Entry.grid(row=62, column=1, columnspan=2, sticky=N+S+E+W)

        self.Performer_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Performer:")
        self.Performer_Label.grid(row=63, column=0, sticky=S+E)
        self.Performer_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Performer_Entry.grid(row=63, column=1, columnspan=2, sticky=N+S+E+W)

        self.Relationship_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Relationship:")
        self.Relationship_Label.grid(row=64, column=0, sticky=S+E)
        self.Relationship_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Relationship_Entry.grid(row=64, column=1, columnspan=2, sticky=N+S+E+W)

        self.Producer_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Producer:")
        self.Producer_Label.grid(row=65, column=0, sticky=S+E)
        self.Producer_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Producer_Entry.grid(row=65, column=1, columnspan=2, sticky=N+S+E+W)

        self.Cast_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Cast:")
        self.Cast_Label.grid(row=66, column=0, sticky=S+E)
        self.Cast_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Cast_Entry.grid(row=66, column=1, columnspan=2, sticky=N+S+E+W)

        self.Generation_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Generation:")
        self.Generation_Label.grid(row=67, column=0, sticky=N+E)
        self.Generation_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Generation_Entry.grid(row=67, column=1, columnspan=2, sticky=N+E+W)

        self.Transcript_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Transcript:")
        self.Transcript_Label.grid(row=68, column=0, sticky=S+E)
        self.Transcript_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Transcript_Entry.grid(row=68, column=1, columnspan=2, sticky=N+S+E+W)

        self.Channel_Configuration_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Channel Configuration:")
        self.Channel_Configuration_Label.grid(row=69, column=0, sticky=S+E)
        self.Channel_Configuration_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Channel_Configuration_Entry.grid(row=69, column=1, columnspan=2, sticky=N+S+E+W)

        self.Date_created_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Date created:")
        self.Date_created_Label.grid(row=70, column=0, sticky=N+E)
        self.Date_created_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Date_created_Entry.grid(row=70, column=1, columnspan=2, sticky=N+E+W)

        self.Reference_URL_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Reference URL:")
        self.Reference_URL_Label.grid(row=71, column=0, sticky=S+E)
        self.Reference_URL_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Reference_URL_Entry.grid(row=71, column=1, columnspan=2, sticky=N+S+E+W)

        self.Call_Number_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Call Number:")
        self.Call_Number_Label.grid(row=72, column=0, sticky=S+E)
        self.Call_Number_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Call_Number_Entry.grid(row=72, column=1, columnspan=2, sticky=N+S+E+W)

        self.Base_Thickness_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Base Thickness:")
        self.Base_Thickness_Label.grid(row=73, column=0, sticky=S+E)
        self.Base_Thickness_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Base_Thickness_Entry.grid(row=73, column=1, columnspan=2, sticky=N+S+E+W)

        self.Base_Type_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Base Type:")
        self.Base_Type_Label.grid(row=74, column=0, sticky=S+E)
        self.Base_Type_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Base_Type_Entry.grid(row=74, column=1, columnspan=2, sticky=N+S+E+W)

        self.Additional_Title_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Additional Title:")
        self.Additional_Title_Label.grid(row=75, column=0, sticky=S+E)
        self.Additional_Title_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Additional_Title_Entry.grid(row=75, column=1, columnspan=2, sticky=N+S+E+W)

        self.CONTENTdm_file_path_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="CONTENTdm file path:")
        self.CONTENTdm_file_path_Label.grid(row=76, column=0, sticky=S+E)
        self.CONTENTdm_file_path_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.CONTENTdm_file_path_Entry.grid(row=76, column=1, columnspan=2, sticky=N+S+E+W)

        self.Duration_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Duration:")
        self.Duration_Label.grid(row=77, column=0, sticky=S+E)
        self.Duration_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Duration_Entry.grid(row=77, column=1, columnspan=2, sticky=N+S+E+W)

        self.Speaker_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Speaker:")
        self.Speaker_Label.grid(row=78, column=0, sticky=S+E)
        self.Speaker_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Speaker_Entry.grid(row=78, column=1, columnspan=2, sticky=N+S+E+W)

        self.Collection_Guide_Title_Label = ttk.Label(self.dataFrame, style='labels.TLabel', text="Collection Guide Title:")
        self.Collection_Guide_Title_Label.grid(row=79, column=0, sticky=S+E)
        self.Collection_Guide_Title_Entry = ttk.Entry(self.dataFrame, style='labels.TEntry')
        self.Collection_Guide_Title_Entry.grid(row=79, column=1, columnspan=2, sticky=N+S+E+W)
        #
         # ------------ files  --------------

        # self.dataOuterFrame = ttk.Frame(self.background, padding=(10,10))
        self.associated_files_Frame = ttk.LabelFrame(self.background, text="Associated Files")
        self.associated_files_Frame.pack(fill=BOTH, expand=True)
        self.associated_files_Tree = ttk.Treeview(self.associated_files_Frame)
        self.associated_files_Tree.pack(fill=BOTH, expand=True)

        
        # ------------ Options --------------
        self.optionsFrame = ttk.LabelFrame(self.background)
        self.optionsFrame.pack(fill=X, expand=True)

        self.closeButton = ttk.Button(self.optionsFrame, text="Close", command=lambda: self.master.destroy())
        # self.closeButton.grid(column=0, row=0, sticky=W+S)
        self.closeButton.pack()

        self.loadrecord()

    def loadrecord(self):
        print("loading record")
        # for index, proper in enumerate(self.properties):
        #     print proper
        self.Date_Created_Entry.insert(0,self.properties['Date Created'])
        self.Object_ARK_Entry.insert(0, self.properties['Object ARK'])
        self.Timecode_Content_Begins_Entry.insert(0,self.properties['Timecode Content Begins'])
        self.Media_Type_Entry.insert(0, self.properties['Media Type'])
        self.Interviewee_Entry.insert(0, self.properties['Interviewee'])
        self.Series_Title_Entry.insert(0, self.properties['Series Title'])
        self.Temporal_Coverage_Entry.insert(0, self.properties['Temporal Coverage'])
        self.Writer_Entry.insert(0, self.properties['Writer'])
        self.Institution_URL_Entry.insert(0, self.properties['Institution URL'])
        self.Project_Identifier_Entry.insert(0, self.properties['Project Identifier'])
        self.Quality_Control_Notes_Entry.insert('1.0', self.properties['Quality Control Notes'])
        self.Silent_or_Sound_Entry.insert(0, self.properties['Silent or Sound'])
        self.Camera_Entry.insert(0, self.properties['Camera'])
        self.Music_Entry.insert(0, self.properties['Music'])
        self.Editor_Entry.insert(0, self.properties['Editor'])
        self.Track_Standard_Entry.insert(0, self.properties['Track Standard'])
        self.CONTENTdm_number_Entry.insert(0, self.properties['CONTENTdm number'])
        self.Subtitles_Entry.insert(0, self.properties['Subtitles/Intertitles/Closed Captions'])
        self.Distributor_Entry.insert(0, self.properties['Distributor'])
        self.Date_modified_Entry.insert(0, self.properties['Date modified'])
        self.Subject_Topic_Authority_Source_Entry.insert(0, self.properties['Subject Topic Authority Source'])
        self.Aspect_Ratio_Entry.insert(0, self.properties['Aspect Ratio'])
        self.Total_Number_of_Reels_or_Tapes_Entry.insert(0, self.properties['Total Number of Reels or Tapes'])
        self.Copyright_Holder_Info_Entry.insert(0, self.properties['Copyright Holder Info'])
        self.Running_Speed_Entry.insert(0, self.properties['Running Speed'])
        self.Subject_Entity_Authority_Source_Entry.insert(0, self.properties['Subject Entity Authority Source'])
        self.Additional_Technical_Notes_for_Overall_Work_Entry.insert('1.0', self.properties['Additional Technical Notes for Overall Work'])
        self.Musician_Entry.insert(0, self.properties['Musician'])
        self.Main_or_Supplied_Title_Entry.insert(0, self.properties['Main or Supplied Title'])
        self.Internet_Archive_URL_Entry.insert(0, self.properties['Internet Archive URL'])
        self.Relationship_Type_Entry.insert(0, self.properties['Relationship Type'])
        self.Director_Entry.insert(0, self.properties['Director'])
        self.Copyright_Statement_Entry.insert(0, self.properties['Copyright Statement'])
        self.Genre_Entry.insert(0, self.properties['Genre'])
        self.Cataloger_Notes_Entry.insert(0, self.properties['Cataloger Notes'])
        self.Collection_Guide_URL_Entry.insert(0, self.properties['Collection Guide URL'])
        self.Interviewer_Entry.insert(0, self.properties['Interviewer'])
        self.Description_or_Content_Summary_Entry.insert('1.0', self.properties['Description or Content Summary'])
        self.Institution_Entry.insert(0, self.properties['Institution'])
        self.Stock_Manufacturer_Entry.insert(0, self.properties['Stock Manufacturer'])
        self.Sound_Entry.insert(0, self.properties['Sound'])
        self.Publisher_Entry.insert(0, self.properties['Publisher'])
        self.Asset_Type_Entry.insert(0, self.properties['Asset Type'])
        self.Object_Identifier_Entry.insert(0, self.properties['Object Identifier'])
        self.Copyright_Date_Entry.insert(0, self.properties['Copyright Date'])
        self.Copyright_Holder_Entry.insert(0, self.properties['Copyright Holder'])
        self.Language_Entry.insert(0, self.properties['Language'])
        self.Color_and_or_Black_and_White_Entry.insert(0, self.properties['Color and/or Black and White'])
        self.Institution_ARK_Entry.insert(0, self.properties['Institution ARK'])
        self.CONTENTdm_file_name_Entry.insert(0, self.properties['CONTENTdm file name'])
        self.OCLC_number_Entry.insert(0, self.properties['OCLC number'])
        self.Why_the_recording_is_significant_to_California_local_history_Entry.insert('1.0', self.properties['Why the recording is significant to California/local history'])
        self.Subject_Topic_Authority_Source_Entry.insert(0, self.properties['Subject Entity'])
        self.Gauge_and_Format_Entry.insert(0, self.properties['Gauge and Format'])
        self.Additional_Descriptive_Notes_for_Overall_Work_Entry.insert(0, self.properties['Additional Descriptive Notes for Overall Work'])
        self.Genre_Authority_Source_Entry.insert(0, self.properties['Genre Authority Source'])
        self.Date_Published_Entry.insert(0, self.properties['Date Published'])
        self.Country_of_Creation_Entry.insert(0, self.properties['Country of Creation'])
        self.Project_Note_Entry.insert(0, self.properties['Project Note'])
        self.Institutional_Rights_Statement_URL_Entry.insert(0, self.properties['Institutional Rights Statement (URL)'])
        self.Spatial_Coverage_Entry.insert(0, self.properties['Spatial Coverage'])
        self.Copyright_Notice_Entry.insert(0, self.properties['Copyright Notice'])
        self.Subject_Topic_Entry.insert(0, self.properties['Subject Topic'])
        self.Performer_Entry.insert(0, self.properties['Performer'])
        self.Relationship_Entry.insert(0, self.properties['Relationship'])
        self.Producer_Entry.insert(0, self.properties['Producer'])
        self.Cast_Entry.insert(0, self.properties['Cast'])
        self.Generation_Entry.insert(0, self.properties['Generation'])
        self.Transcript_Entry.insert(0, self.properties['Transcript'])
        self.Channel_Configuration_Entry.insert(0, self.properties['Channel Configuration'])
        self.Date_created_Entry.insert(0, self.properties['Date created'])
        self.Reference_URL_Entry.insert(0, self.properties['Reference URL'])
        self.Call_Number_Entry.insert(0, self.properties['Call Number'])
        self.Base_Thickness_Entry.insert(0, self.properties['Base Thickness'])
        self.Base_Type_Entry.insert(0, self.properties['Base Type'])
        self.Additional_Title_Entry.insert(0, self.properties['Additional Title'])
        self.CONTENTdm_file_path_Entry.insert(0, self.properties['CONTENTdm file path'])
        self.Duration_Entry.insert(0, self.properties['Duration'])
        self.Speaker_Entry.insert(0, self.properties['Speaker'])
        self.Collection_Guide_Title_Entry.insert(0, self.properties['Collection Guide Title'])





if __name__ == '__main__':
    from pbcore_csv import pbcoreBuilder
    sys.stderr.write("Not a standalone program. Please run pbcore-csv.py -g to run the GUI")
    # # print()
    # # TODO: Delete when done testing -------#-|
    root = Tk()                             # |
    ini_file = "/Users/lpsdesk/PycharmProjects/PBcore/settings/pbcore-csv-settings.ini"
    root.wm_title('Details')       # |
    # root.resizable(FALSE,FALSE)             # |
    app = RecordDetailsWindow(root, "/Users/lpsdesk/PycharmProjects/PBcore/sample_records/casacsh_000048_export.csv", "cavpp002554")    # | <== This can go when done testing --<
    root.mainloop()                         # |
    # --------------------------------------#-|
else:
    import pbcore_csv