import sys
import ctypes
import tkinter as tk
from tkinter import ttk

from slopecraftr import constants
from slopecraftr.__main__ import main as scr_main


def gui_entry():
    (shcore := ctypes.windll.shcore).SetProcessDpiAwareness(1)
    (root := tk.Tk()).tk.call('tk', 'scaling', shcore.GetScaleFactorForDevice(0) / 75)
    root.title(f'{constants.NAME} v{constants.VERSION}')
    root.geometry('810x514')

    ttk.Label(root, text='114514\n1919810').pack()
    ttk.Button(root, text='0v0!', command=root.destroy).pack()
    root.mainloop()


def main():
    scr_main()
    print(f'<{constants.NAME}-GUI>', end='\n' * 2)
    gui_entry()


if __name__ == '__main__':
    sys.exit(main())
