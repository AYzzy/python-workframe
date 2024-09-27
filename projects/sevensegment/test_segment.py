import unittest
from segment import display_segment
class TestSegment(unittest.TestCase):
    def test_segment(self):
        self.assertEqual(display_segment('10111011'))


