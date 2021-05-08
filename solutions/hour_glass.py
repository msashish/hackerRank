#
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#

def hourglassSum(arr):

    # matrix = [ [ 0 for i in range(n) ] for j in range(m) ]
    max_hour_glass_sum = -63
    for sj in range(4):
        print("------------ next set ------------ ")
        for si in range(4):
            print("next")
            ri = 1
            hour_glass_sum = 0
            for i in range(si, si+3):
                ci = 1
                for j in range(sj, sj+3):
                    if (ri == 1 or ri == 3) or (ri == 2 and ci == 2):
                            hour_glass_sum += arr[i][j]
                    ci += 1
                ri += 1
            max_hour_glass_sum = max(max_hour_glass_sum, hour_glass_sum)
    return max_hour_glass_sum


def hourglassSumAlt(arr):
    sum = []

    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            sum.append(
                arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] +
                arr[i + 2][j + 2])

    return max(sum)

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
