import unittest

from solutions.present_absent import present_absent


class TestPlusMinusProblem(unittest.TestCase):

    def test_mixed(self):
        num_array = [-4, 3, -9, 0, 4, 1, 2]
        seta = (-4, -3, -9, 0)
        setb = (4, 1, 2)
        output = present_absent(num_array, seta, setb)
        self.assertEqual(output, 0)

    def test_none_present(self):
        num_array = [-1, -2, -3, 0, 4, 1, 2]
        seta = ()
        setb = (4, 1, 2)
        output = present_absent(num_array, seta, setb)
        self.assertEqual(output, -3)

    def test_none_absent(self):
        num_array = [-1, -2, -3, 0, 4, 1, 2]
        seta = (4, 1, 2)
        setb = ()
        output = present_absent(num_array, seta, setb)
        self.assertEqual(output, 3)
