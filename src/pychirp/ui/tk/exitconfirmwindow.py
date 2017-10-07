from pychirp.ui.tk.confirmwindow import ConfirmWindow


class ExitConfirmWindow(ConfirmWindow):
    
    def __init__(self, master):
        super().__init__(master, 'exit')
        self.master = master

    def click_ok_button(self):
        self.master.quit()
        return 'Bye.'
