#!/bin/python3

import math
import os
import random
import re
import sys


# Input format = n x n matrix
#    3
#    8 1 -2
#    4 5 6
#    9 7 3
# expected answer = |(8+5+3) - (-2+5+9)| = 4

def diagonalDifference(arr):
    i = 0
    j = len(arr) - 1
    diag_sum_1 = 0
    diag_sum_2 = 0
    while i < len(arr):
        diag_sum_1 += arr[i][i]
        i += 1
    i = 0
    while j >= 0:
        diag_sum_2 += arr[i][j]
        i += 1
        j -= 1

    return abs(diag_sum_1 - diag_sum_2)


def diagonal_difference(arr):
    i = 0
    j = len(arr) - 1
    diag_sum_1 = 0
    diag_sum_2 = 0
    while i < len(arr) and j >= 0:
        diag_sum_1 += arr[i][i]
        diag_sum_2 += arr[i][j]
        i += 1
        j -= 1
    return abs(diag_sum_1 - diag_sum_2)


if __name__ == '__main__':

    n = int(input("Enter count of numbers in the matrix: ").strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input("row = ").rstrip().split())))

    result = diagonal_difference(arr)

    print(f"Diagonal difference = {result} ")
