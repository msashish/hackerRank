"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

python solutions/array_rotation.py
6 3
124 9 10 0 7 6

output:
[0, 7, 6, 124, 9, 10]


"""


def rotLeft(a, d, n):
    if d == n:
        return a

    return [element for element in a[d:]] + [a[i] for i in range(d)]


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d, n)

    print(result)

