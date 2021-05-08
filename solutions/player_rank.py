#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    ranks = []

    for score in player:
        i = 0
        dense_i = 1
        prev_score = sys.maxsize

        while i < len(ranked) and score < ranked[i]:

            if prev_score > ranked[i]:
                prev_score = ranked[i]
                dense_i += 1
            i += 1

        ranks.append(dense_i)

    return ranks


def climb_optimal(ranked, player):
    ranks = []
    i = len(ranked) - 1
    prev_score = 0
    dense_i = len(set(ranked)) + 1

    for score in player:

        while i >= 0 and score >= ranked[i]:

            if ranked[i] > prev_score:
                prev_score = ranked[i]
                dense_i -= 1

            i -= 1

        if i < 0:
            dense_i = 1

        ranks.append(dense_i)

    return ranks


if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climb_optimal(ranked, player)

    print(result)
