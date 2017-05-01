import unittest

from pychirp.pychirp import PyChirp

class MainWindowTest(unittest.TestCase):

    def test_ui_name_does_not_exist_should_raise_exception(self):
        with self.assertRaises(Exception):
            pychirp = PyChirp('abc')
