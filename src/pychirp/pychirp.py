class PyChirp(object):

    def __init__(self, ui='Tk'):
        self._select_ui(ui)
        self._init_components()

    def _select_ui(self, ui):
        if ui == 'Tk':
            from pychirp.ui.tk.tkui import TkUI
            self.ui = TkUI()
        else:
            raise Exception('UI \'{0}\' does not exist'.format(ui))

    def _init_components(self):
        pass

    def run(self):  # pragma: no cover
        self.ui.show()
