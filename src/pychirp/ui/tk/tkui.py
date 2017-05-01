from tkinter import Tk

from pychirp.ui.tk.mainwindow import MainWindow
from pychirp.ui.tk.mainmenubar import MainMenubar


class TkUI(Tk):

    def __init__(self):
        super().__init__()
        self._set_tkui()
        self._init_components()

    def _set_tkui(self):
        self.title('pychirp')
        self.geometry('800x400')

    def _init_components(self):
        MainWindow(self)
        MainMenubar(self)

    def show(self):  # pragma: no cover
        self.mainloop()
