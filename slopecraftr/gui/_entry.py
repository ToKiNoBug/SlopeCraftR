from tkinter import Tk

from slopecraftr.core import SlopeCraftRCore
from slopecraftr.utils.translation_manager import TranslationManager
from slopecraftr.gui.main_window import Application


def entry(language: str):
    SlopeCraftRCore()
    Application(Tk()).mainloop()
