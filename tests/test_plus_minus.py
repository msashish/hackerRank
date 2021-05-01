import unittest

from solutions.plus_minus import plusMinus


class TestPlusMinusProblem(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """ Runs only once for every unittest set """
        print(f"Starting PlusMinus testing")

    def test_mixed(self):
        test_1 = [-4, 3, -9, 0, 4, 1, 2]
        output = plusMinus(test_1)
        self.assertEqual(output[0], "0.571429")  # ratio of count of positive numbers
        self.assertEqual(output[1], "0.285714")  # ratio of count of negative numbers
        self.assertEqual(output[2], "0.142857")  # ratio of count of zero numbers

    def test_all_0(self):
        output = plusMinus([0, 0, 0, 0, 0, 0, 0])
        print(output)
        self.assertEqual(output[0], "0.000000")
        self.assertEqual(output[1], "0.000000")
        self.assertEqual(output[2], "1.000000")

    def test_big_neg_sum(self):
        output = plusMinus([-2, -3, -21, -100, -400, -3, 0])
        print(output)
        self.assertEqual(output[0], "0.000000")  # ratio of count of positive numbers
        self.assertEqual(output[1], "0.857143")  # ratio of count of negative numbers = 6/7
        self.assertEqual(output[2], "0.142857")  # ratio of count of zeroes = 1/7

    def test_sum_of_ratios(self):
        """ sum of ratios of count of +ve numbers, -ve numbers and zeroes should all equal 1 """
        output = plusMinus([-236, -312, -21, -100, -400, -3, 0, 123])
        self.assertEqual(float(output[0]) + float(output[1]) + float(output[2]), 1)

    @classmethod
    def tearDownClass(cls) -> None:
        pass