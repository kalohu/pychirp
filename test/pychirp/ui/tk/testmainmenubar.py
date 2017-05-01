import unittest

from pychirp.pychirp import PyChirp

class MainWindowTest(unittest.TestCase):

    def setUp(self):
        pychirp = PyChirp()
        self.ui = pychirp.ui

    def test_main_menubar_exists(self):
        self.assertIn('main_menubar', self.ui.children.keys())

    def test_click_on_file_menu_exit_menuitem_program_should_exit(self):
        result = self.ui.children['main_menubar'].children['main_menubar_menus'].children['file_menu'].invoke('Exit')
        self.assertEqual(result, 'Bye.')

    def tearDown(self):
        self.ui.destroy()
