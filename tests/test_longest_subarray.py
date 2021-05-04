import unittest

from solutions.longest_subarray import pickingNumbers


class TestLongSubArrayProblem(unittest.TestCase):

    def test_simple(self):
        s = [4, 6, 5, 3, 3, 1]
        self.assertEqual(pickingNumbers(s), 3)

    def test_only_one(self):
        s = [4, 6, 8, 10, 2, 12]
        self.assertEqual(pickingNumbers(s), 1)

    def test_negative_numbers(self):
        s = [4, 6, 5, 3, 3, 1, 0, -1]
        self.assertEqual(pickingNumbers(s), 3)
