"""

"""
import time


def tradefilter1(arr, filt):
    output = []
    for i in filt:
        counter = 0
        for j in arr:
            if j <= i:
                counter += 1

        output.append(counter)
    return output


def tradefilter(arr, filt):
    return list(count(arr, filt))


def count(arr, filt):
    for num in filt:
        yield sum(num >= i for i in arr)

s

if __name__ == '__main__':

    prices = list(map(int, input().rstrip().split()))
    price_filter = list(map(int, input().rstrip().split()))
    start_time = time.time()
    print(tradefilter1(prices, price_filter))
    print("old method %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(tradefilter(prices, price_filter))
    print("new method %s seconds ---" % (time.time() - start_time))

