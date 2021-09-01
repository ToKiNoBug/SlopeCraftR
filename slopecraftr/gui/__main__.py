import sys
from tkinter import Tk

from slopecraftr import constants
from slopecraftr.gui.main_window import Application
from slopecraftr.__main__ import main as scr_main


def gui_entry():
    Application(Tk()).mainloop()


def main():
    scr_main()
    print(f'<{constants.NAME}-GUI>', end='\n' * 2)
    gui_entry()


if __name__ == '__main__':
    sys.exit(main())
