import unittest

from solutions import grading


class TestGradingProblem(unittest.TestCase):

    def test_mixed(self):
        grades = [73, 67, 38, 33]
        self.assertEqual(grading.gradingStudents(grades), [75, 67, 40, 33])

    def test_no_rounding(self):
        grades = [71, 55, 42, 33]
        self.assertEqual(grading.gradingStudents(grades), [71, 55, 42, 33])

    def test_boundary_conditions(self):
        grades = [0, 0, 0, 0]
        self.assertEqual(grading.gradingStudents(grades), [0, 0, 0, 0])

    def test_nagative_grade(self):
        grades = [-2, -1, -2, 1]
        self.assertEqual(grading.gradingStudents(grades), [-2, -1, -2, 1])
