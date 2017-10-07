from tkinter import Tk

from pychirp.ui.tk.mainwindow import MainWindow
from pychirp.ui.tk.mainmenubar import MainMenubar
from pychirp.ui.tk.exitconfirmwindow import ExitConfirmWindow


class TkUI(Tk):

    def __init__(self):
        super().__init__()
        self._set_tkui()
        self._init_components()

    def _set_tkui(self):
        self.title('pychirp')
        self.geometry('800x400')
        self.protocol('WM_DELETE_WINDOW', self.show_exit_confirm_window)

    def _init_components(self):
        MainWindow(self)
        MainMenubar(self)

    def show_exit_confirm_window(self):
        if 'exit_confirm_window' not in self.children:
            ExitConfirmWindow(self)
        else:
            if self.focus_get() != '.exit_confirm_window':
                self.children['exit_confirm_window'].focus_set()

    def show(self):  # pragma: no cover
        self.mainloop()
