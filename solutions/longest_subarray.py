"""
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

Example

    There are two subarrays meeting the criterion:  and . The maximum length subarray has  elements.

"""


def pickingNumbers(a):
    max_len = 0
    evaluated_numbers = []
    for i in range(len(a)):
        counter1 = 1
        counter2 = 1
        if a[i] not in evaluated_numbers:
            for j in range(i+1, len(a)):
                if a[i] - a[j] == 1 or a[i] == a[j]:
                    counter1 += 1
                if a[i] - a[j] == -1 or a[i] == a[j]:
                    counter2 += 1
            evaluated_numbers.append(a[i])
        max_len = max(max_len, counter1, counter2)

    return max_len


if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    print(pickingNumbers(a))

