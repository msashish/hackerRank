#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#


def stockmax(n, prices):
    total_profit = 0
    shares_owned = 0

    for i in range(n):
        current_price = prices[i]
        if any(value > current_price for value in prices[i+1:]):
            shares_to_buy = 1
            shares_to_sell = 0
        else:
            shares_to_buy = 0
            shares_to_sell = shares_owned

        if shares_to_buy:
            shares_owned += 1
            total_profit -= current_price

        if shares_to_sell:
            shares_owned -= shares_to_sell
            total_profit += shares_to_sell * current_price

    return total_profit


#  Optimum solution by traversing the array backwards and adding the difference to local maximum
def stockmaxopti(n, prices):

    sum_of_diff = 0
    local_max = prices[n-1]
    i = n - 2
    while i >= 0:
        if local_max > prices[i]:
            sum_of_diff += local_max - prices[i]
        elif local_max < prices[i]:
            local_max = prices[i]
        i -= 1

    return sum_of_diff


if __name__ == '__main__':

    n = int(input().strip())

    prices = list(map(int, input().rstrip().split()))

    result = stockmax(n, prices)

    print(result)
