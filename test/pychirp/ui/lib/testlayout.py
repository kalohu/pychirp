import unittest

from pychirp.ui.lib.layout import Layout


class LayoutTest(unittest.TestCase):

    def setUp(self):
        self.layout = Layout()

    def test_child_size_is_smaller_than_parent_size_child_should_be_in_the_middle_of_the_parent(self):
        child_x, child_y = self.layout.calculate_child_position({'x': 100, 'y': 150, 'width': 300, 'height': 200},
                                                                {'width': 200, 'height': 80})
        self.assertEqual(child_x, 150)
        self.assertEqual(child_y, 210)

    def test_child_size_is_equal_to_parent_size_child_should_be_at_left_bottom_of_parent_location(self):
        child_x, child_y = self.layout.calculate_child_position({'x': 100, 'y': 150, 'width': 300, 'height': 200},
                                                                {'width': 300, 'height': 200})
        self.assertEqual(child_x, 120)
        self.assertEqual(child_y, 170)

    def test_child_size_is_greater_than_parent_size_child_should_be_at_left_bottom_of_parent_location(self):
        child_x, child_y = self.layout.calculate_child_position({'x': 100, 'y': 150, 'width': 300, 'height': 200},
                                                                {'width': 400, 'height': 300})
        self.assertEqual(child_x, 120)
        self.assertEqual(child_y, 170)
