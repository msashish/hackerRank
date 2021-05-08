#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def compare(a, b):
    a += 'z'
    b += 'z'

    for _ in range(len(a) + len(b) - 2):
        if a < b:
            yield a[0]
            a = a[1:]
        else:
            yield b[0]
            b = b[1:]


def morganAndString(a, b):
    return ''.join(compare(a, b))


def morganAndString1(a, b):
    jack = [a[i] for i in range(len(a))]
    daniel = [b[i] for i in range(len(b))]
    output = ''
    return compare_cards(jack, daniel, output)


def compare_cards(a, b, output):
    if len(a) == 0 and len(b) == 0:
        return output
    elif len(a) == 0 and len(b) != 0:
        output += b[0]
        return compare_cards(a, b[1:], output)
    elif len(b) == 0 and len(a) != 0:
        output += a[0]
        return compare_cards(a[1:], b, output)
    elif a[0] == b[0] or a[0] < b[0]:
        output += a[0]
        return compare_cards(a[1:], b, output)
    else:
        output += b[0]
        return compare_cards(a, b[1:], output)



if __name__ == '__main__':

    a = input()

    b = input()

    print(morganAndString(a, b))
