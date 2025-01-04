from collections import Counter


def task1(cnt):
    s = set(i for i in range(347312, 805916) if list(str(i)) == sorted(list(str(i))))
    print(sum(not all(y == 1 for y in Counter(list(str(x))).values()) for x in s))

def task2(cnt):
    s = set(i for i in range(347312, 805916) if list(str(i)) == sorted(list(str(i))))
    print(sum(2 in Counter(list(str(x))).values() for x in s))