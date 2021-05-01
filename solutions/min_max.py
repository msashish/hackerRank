#!/bin/python3

import math
import os
import random
import re
import sys

#
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of
# the five integers. Then print the respective minimum and maximum values as a single line of two space-separated
# long integers.
# 1 3 5 7 9
# o/p =
# 16 24


def min_max(arr):
    min_sum = 999999999
    max_sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr)):
            if j != i:
                sum += arr[j]
        if sum < min_sum:
            min_sum = sum
        if sum > max_sum:
            max_sum = sum
    return [min_sum, max_sum]


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    print(min_max(arr))
