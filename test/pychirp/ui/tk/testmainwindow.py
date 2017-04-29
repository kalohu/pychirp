import unittest

from pychirp.pychirp import PyChirp

class MainWindowTest(unittest.TestCase):

    def setUp(self):
        pychirp = PyChirp()
        self.ui = pychirp.ui

    def test_mainwindow_exists(self):
        self.assertIn('main_window', self.ui.children.keys())

    def tearDown(self):
        self.ui.destroy()
