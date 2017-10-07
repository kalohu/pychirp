import unittest
import unittest.mock
import tkinter

from pychirp.pychirp import PyChirp


class MainWindowTest(unittest.TestCase):

    def setUp(self):
        pychirp = PyChirp()
        self.ui = pychirp.ui

    def test_mainwindow_close_button_is_pressed_should_appear_exit_confirm_window(self):
        self.ui.show_exit_confirm_window()
        self.assertIn('exit_confirm_window', self.ui.children)

    def test_exit_confirm_window_is_open_twice_it_should_not_open_new_window_again(self):
        self.ui.show_exit_confirm_window()
        first_window_id = self.ui.children['exit_confirm_window'].winfo_id()
        self.ui.show_exit_confirm_window()
        second_window_id = self.ui.children['exit_confirm_window'].winfo_id()
        self.assertEqual(first_window_id, second_window_id)

    def test_exit_confirm_window_is_closed_and_opened_again_the_new_window_should_have_a_new_id(self):
        self.ui.show_exit_confirm_window()
        first_window_id = self.ui.children['exit_confirm_window'].winfo_id()
        self.ui.children['exit_confirm_window'].click_cancel_button()
        self.assertNotIn('exit_confirm_window', self.ui.children)
        self.ui.show_exit_confirm_window()
        second_window_id = self.ui.children['exit_confirm_window'].winfo_id()
        self.assertNotEqual(first_window_id, second_window_id)

    @unittest.mock.patch.object(tkinter.Misc, 'focus_get', return_value='.')
    @unittest.mock.patch.object(tkinter.Misc, 'focus_set')
    def test_exit_confirm_window_is_called_twice_and_root_window_is_focused_should_set_focus_instead_of_open_new_window(self, f_set, f_get):
        self.ui.show_exit_confirm_window()
        self.assertFalse(f_set.called)
        self.ui.show_exit_confirm_window()
        self.assertTrue(f_set.called)

    @unittest.mock.patch.object(tkinter.Misc, 'focus_get', return_value='.exit_confirm_window')
    @unittest.mock.patch.object(tkinter.Misc, 'focus_set')
    def test_exit_confirm_window_is_called_twice_and_exit_confirm_window_is_focused_should_not_set_focus_on_it_again(self, f_set, f_get):
        self.ui.show_exit_confirm_window()
        self.assertFalse(f_set.called)
        self.ui.show_exit_confirm_window()
        self.assertFalse(f_set.called)

    def tearDown(self):
        self.ui.destroy()
