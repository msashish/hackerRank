#!/bin/python3

import math
import os
import random
import re
import sys

#
# Input format
#  6
#  -4 3 -9 0 4 1
# Output format
#   0.500000
#   0.333333
#   0.166667

def plusMinus(arr):
    (zero_sum, pos_sum, neg_sum) = 0, 0, 0
    for num in arr:
        if num == 0:
            zero_sum += 1
        elif num > 0:
            pos_sum += 1
        else:
            neg_sum += 1
    print("{:.6f}".format(float(pos_sum / len(arr))))
    print("{:.6f}".format(float(neg_sum / len(arr))))
    print("{:.6f}".format(float(zero_sum / len(arr))))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
