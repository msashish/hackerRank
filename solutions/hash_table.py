"""
Python Dictionary is an implementation of hash table

Given the words in the magazine and the words in the ransom note,
print Yes if we can replicate ransom note exactly using whole words from the magazine; otherwise, print No.

python solutions/hash_table.py

6 5
two times three is not four
two times two is four

Output:
No (needed 2 two )

"""


def checkMagazine(magazine, note):
    no_flag = False
    mag = dict()
    nt = dict()

    # convert magazine array into dictionary with word as key and value as count of word in magazine
    for i in magazine:
        mag[i] = mag.get(i, 0) + 1

    # convert note array into dictionary with word as key and value as count of word in note
    for i in note:
        nt[i] = nt.get(i, 0) + 1

    # compare if words in note exits in magazine with sufficient count
    for k, v in nt.items():
        if (k not in mag.keys()) or v > mag[k]:
            no_flag = True
            break
    if no_flag:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
