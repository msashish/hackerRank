import unittest

from solutions.diagonal_difference import diagonal_difference


class TestPlusMinusProblem(unittest.TestCase):

    def test_zero_array(self):
        sample = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(diagonal_difference(sample), 0)

    def test_simple_array(self):
        sample = [[8, 1, -2], [4, 5, 6], [9, 7, 3]]
        print(len(sample))
        self.assertEqual(diagonal_difference(sample), 4)
