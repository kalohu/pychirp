from tkinter import Toplevel, Button


class ConfirmWindow(Toplevel):

    def __init__(self, master, confirm_window_prefix):
        super().__init__(master, name=confirm_window_prefix + '_confirm_window')
        self._init_confirm_window()

    def _init_confirm_window(self):
        self.title('pychirp')
        self.geometry('800x400')
        Button(self, name='ok_button', text='Ok', command=self.click_ok_button)
        Button(self, name='cancel_button', text='Cancel', command=self.click_cancel_button)

    def click_ok_button(self): # pragma: no cover
        raise Exception('Not implemented')

    def click_cancel_button(self):
        self.destroy()
