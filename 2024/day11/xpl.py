from functools import cache


def parse_cnt(cnt):
    return [int(n) for n in cnt.split(' ')]


@cache
def count(num, depth):
    if depth == 0:
        return 1
    if num == 0:
        return count(1, depth - 1)
    elif (len(str(num)) % 2) == 0:
        sn = str(num)
        return count(int(sn[:len(sn) // 2]), depth - 1) + count(int(sn[len(sn) // 2:]), depth - 1)
    else:
        return count(num * 2024, depth - 1)


def task1(cnt):
    stones = parse_cnt(cnt)
    print(sum(count(stone, 25) for stone in stones))


def task2(cnt):
    stones = parse_cnt(cnt)
    print(sum(count(stone, 75) for stone in stones))
