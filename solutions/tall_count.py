#!/bin/python3


# Given an array of numbers,
# Calculate count of biggest number
# 3 2 1 3
# 3 is the biggest number appearting twice hence output count is 2


def tall_count(arr):
    max_number = 0
    max_number_count = 0
    for num in arr:
        if max_number == num:
            max_number_count += 1
        elif max_number < num:
            max_number = num
            max_number_count = 1

    return max_number_count


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    print(tall_count(arr))
