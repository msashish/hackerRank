#!/bin/python3

#
# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.


def timeConversion(s):
    time = list(s[0: 8].split(":"))
    form = s[8: 10]
    new_time = time
    if form == "PM" and int(time[0]) < 12:
        new_time[0] = str(int(time[0]) + 12)
    if form == "AM" and int(time[0]) == 12:
        new_time[0] = "00"
    return ":".join(new_time)


if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
