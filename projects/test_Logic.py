import unittest

from projects.Logic import Logic


class TestLogic(unittest.TestCase):

    def test_logics(self):
        Logics = Logic()
        self.assertEqual(13000, Logics.logics(50))

    def test_logics_2(self):
        Logics = Logic()
        self.assertRaises(ValueError, lambda: Logics.logics(-5))

    def test_logics_3(self):
        Logics = Logic()
        self.assertRaises(ValueError, lambda: Logics.logics(105))
