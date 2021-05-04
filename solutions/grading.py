#!/bin/python3

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    return [get_new_grade(grade) for grade in grades]


def get_new_grade(grade):
    if grade >= 38:
        if (grade + 1) % 5 == 0:
            return grade + 1
        elif (grade + 2) % 5 == 0:
            return grade + 2
    return grade


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
