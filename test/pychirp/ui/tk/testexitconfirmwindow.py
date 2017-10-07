import unittest

from tkinter import Tk
from pychirp.ui.tk.exitconfirmwindow import ExitConfirmWindow


class MainWindowTest(unittest.TestCase):

    def setUp(self):
        self.tk_root = Tk()
        self.exit_confirm_window = ExitConfirmWindow(self.tk_root)

    def test_exit_confirm_window_ok_button_is_pressed_the_program_should_exit(self):
        result = self.tk_root.children['exit_confirm_window'].children['ok_button'].invoke()
        self.assertEqual(result, 'Bye.')

    def test_exit_confirm_window_cancel_button_is_pressed_the_program_should_close_the_confirm_window(self):
        result = self.tk_root.children['exit_confirm_window'].children['cancel_button'].invoke()
        self.assertEqual(result, 'None')
        self.assertNotIn('exit_confirm_window', self.tk_root.children.keys())

    def tearDown(self):
        self.tk_root.destroy()
