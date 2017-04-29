import unittest

from pychirp.pychirp import PyChirp

class MainWindowTest(unittest.TestCase):

    def test_ui_name_exists(self):
        with self.assertRaises(Exception):
            pychirp = PyChirp('abc')
