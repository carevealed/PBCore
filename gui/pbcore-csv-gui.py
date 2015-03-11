from tkFileDialog import askopenfilename

__author__ = 'lpsdesk'

from Tkinter import *
import ttk

class MainWindow():
    def __init__(self, master):
        self.background = ttk.Frame(master, padding=(30,15))
        self.background.pack(fill=BOTH, expand=True)
        # ----------
        self.titleFrame = ttk.Frame(self.background,
                                    height=100,
                                    width=200,
                                    padding=(30, 15),
                                    relief=GROOVE)
        # self.titleFrame.grid(row=0, column=0, columnspan=3, sticky=W+E)
        self.titleFrame.pack(fill=BOTH)
        self.titleLabel = ttk.Label(self.titleFrame,
                                    text="CAVPP PBCore Generator",
                                    font=('TkDefaultFont', 30, 'bold')).pack()
        # ----------

        self.settingsButton = ttk.Button(self.background, text="Settings", command=self.open_settings)
        self.settingsButton.pack()

        self.allInfoFrame = ttk.Frame(self.background)
        self.allInfoFrame.pack(fill=BOTH, expand=True)


        self.panel = ttk.Panedwindow(self.allInfoFrame, orient=VERTICAL)
        self.panel.pack(fill=BOTH, expand=True)
        # self.panel.grid(row=2, column=0, sticky=W+E+S+N)

        # ----------
        self.dataEntryFrame = ttk.Frame(self.panel, height=100, width=100, padding=(30, 15), relief=SUNKEN)
        # self.dataEntryFrame.grid(row=2, column=1)
        self.panel.add(self.dataEntryFrame, weight=4)


        self.csv_filename_label = ttk.Label(self.dataEntryFrame, text="CSV file", width=10)
        self.csv_filename_label.grid(row=2, column=0, sticky=E)
        self.csv_filename_entry = ttk.Entry(self.dataEntryFrame, width=80)
        self.csv_filename_entry.grid(row=2, column=1, sticky=W+E)

        self.locateCSVButton = ttk.Button(self.dataEntryFrame, text='Browse', command=self.retreve_folder)
        self.locateCSVButton.grid(row=2, column=3, sticky=E)

        self.startButton = ttk.Button(self.dataEntryFrame, text='Start', command=self.start)
        self.startButton.grid(row=3, column=3)

        # ----------
        self.feedbackFrame = ttk.Frame(self.panel, height=200, width=100, padding=(30, 15), relief=SUNKEN)
        # self.feedbackFrame.grid(row=3, column=1, sticky=W)
        self.panel.add(self.feedbackFrame)
        self.total_progress_label = ttk.Label(self.feedbackFrame, text="Total Progress:")
        self.total_progress_label.grid(row=0, column=0, sticky=E)
        self.total_progress_value_label = ttk.Label(self.feedbackFrame, text="(0/0)")
        self.total_progress_value_label.grid(row=0, column=1, sticky=E)
        self.total_progress_pbar = ttk.Progressbar(self.feedbackFrame, orient=HORIZONTAL, length=500, mode='indeterminate')
        self.total_progress_pbar.grid(row=0, column=2, sticky=W)

        self.item_progress_label = ttk.Label(self.feedbackFrame, text="Record Progress:")
        self.item_progress_label.grid(row=1, column=0, sticky=E)
        self.item_progress_value_label = ttk.Label(self.feedbackFrame, text="(0/0)")
        self.item_progress_value_label.grid(row=1, column=1, sticky=E)
        self.item_progress_pbar = ttk.Progressbar(self.feedbackFrame, orient=HORIZONTAL, length=500, mode='indeterminate')
        self.item_progress_pbar.grid(row=1, column=2, sticky=W)

        self.calculation_progress_label = ttk.Label(self.feedbackFrame, text="Calculation Progress:")
        self.calculation_progress_label.grid(row=2, column=0, sticky=E)
        self.calculation_progress_value_label = ttk.Label(self.feedbackFrame, text="0%")
        self.calculation_progress_value_label.grid(row=2, column=1, sticky=E)
        self.calculation_progress_pbar = ttk.Progressbar(self.feedbackFrame, orient=HORIZONTAL, length=500, mode='indeterminate')
        self.calculation_progress_pbar.grid(row=2, column=2, sticky=W)


        self.running = False


    def retreve_folder(self):
        fileName = askopenfilename()
        self.csv_filename_entry.delete(0, END)
        self.csv_filename_entry.insert(0, fileName)

    def open_settings(self):
        self.settingsWindow = Toplevel(self.background)
        self.settingsWindow.title("Settings")


    def start(self):
        if self.running is False:
            self.total_progress_pbar.start()
            self.running = True
        else:
            self.total_progress_pbar.stop()
            self.running = False

class SettingsWindow():
    def __init__(self, master):
        pass


def main():
    root = Tk()
    root.wm_title('PBCore Generator')
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()