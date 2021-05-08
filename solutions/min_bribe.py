"""
python solutions/min_bribe.py
2
5
2 1 5 3 4
5
2 5 1 3 4

output:
 3
 Too chaotic

"""


def minimumBribes(q, n):
    if n == 1:
        print(1)

    chaotic_flag = False
    total_bribe = 0
    i = n - 1
    while i >= 0:
        if q[i] > i+3:
            chaotic_flag = True
            break
        j = max(0, q[i] - 2)
        while j < i:
            if q[j] > q[i]:
                total_bribe += 1
            j += 1
        i -= 1

    if chaotic_flag:
        print("Too chaotic")
    else:
        print(total_bribe)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q, n)
