"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

python solutions/array_rotation.py
6 3
124 9 10 0 7 6

output:
[0, 7, 6, 124, 9, 10]


"""


def rotLeft(input_array, rotate_by, input_array_count):
    if rotate_by == input_array_count:
        return input_array

    return [element for element in input_array[rotate_by:]] + [input_array[i] for i in range(rotate_by)]


if __name__ == '__main__':

    first_multiple_input = input("Please enter input_array_count, rotate_by with space separation \n").rstrip().split()

    input_array_count = int(first_multiple_input[0])

    rotate_by = int(first_multiple_input[1])

    input_array = list(map(int, input("Please enter input array numbers with space separation \n").rstrip().split()))

    result = rotLeft(input_array, rotate_by, input_array_count)

    print(result)

