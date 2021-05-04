"""
Given a number array and 2 disjoint sets A and B.
    If a number in number array exists in set A then count +1
    If a number in number array exists in set B then count -1
    Else do not count

example:
Enter 3 array of numbers below

1 2 3 4 5 6 7 8 9 10
2 3 7 8 9 5
1 8

output:
Total present absent sum is =  4
"""


def present_absent(num_array, a, b):
    return sum((num in a) - (num in b) for num in num_array)


if __name__ == '__main__':
    print("Enter 3 array of numbers below \n")
    num_array = list(map(int, input().rstrip().split()))

    arr1 = set(map(int, input().rstrip().split()))
    arr2 = set(map(int, input().rstrip().split()))

    result = present_absent(num_array, arr1, arr2)

    print("Total present absent sum is = ", result)
