import os
import ctypes
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

from slopecraftr import constants


class Application(Frame):
    file_selector: Button
    selected_file: Label
    quit: Button

    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        if os.name == "nt":
            (shcore := ctypes.windll.shcore).SetProcessDpiAwareness(1)
            self.master.tk.call('tk', 'scaling', shcore.GetScaleFactorForDevice(0) / 75)
        self.master.title(f'{constants.NAME} v{constants.VERSION}')
        self.master.geometry('810x514')

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.file_selector = Button(self, text='Select a File', command=self.select_file)
        self.file_selector.pack(side='top')

        self.selected_file = Label(self)
        self.selected_file.pack(side='top')

        self.quit = Button(self, text='Quit', command=self.master.destroy)
        self.quit.pack(side='bottom')

    def select_file(self):
        file = filedialog.askopenfilename()
        self.selected_file['text'] = file
